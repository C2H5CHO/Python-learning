import pygame
import config
from game_managers import GameManager
from utils.draw_text import draw_text

# 初始化pygame
pygame.init()
pygame.mixer.init() # 初始化声音
# 设置窗口大小
screen = pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ico = pygame.image.load('pictures/maz.png').convert()
pygame.display.set_icon(ico)
pygame.display.set_caption('汽车迷宫') # 改名称

bgm = pygame.mixer.music.load('sounds/bgm.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) # -1 --> 表示循环播放

# 创建一个Player对象
game_manager = GameManager(screen,1)

success_time = -1 # -1 --> 当前没有获胜
success_finish = False

# 启动
running = True
while running:
    # 循环获取事件，监听事件
    for even in pygame.event.get():
        # 判断用户是否点了关闭按钮
        if even.type == pygame.QUIT:
            running = False
        elif success_finish and even.type == pygame.KEYDOWN: # 如果已通关，则按任意键结束
            running = False

    if success_finish:
        screen.fill('black')
        draw_text(screen,'Win!!',200,config.SCREEN_WIDTH / 2,config.SCREEN_HEIGHT / 2)
    else:
        if success_time >= 0:
            if pygame.time.get_ticks() - success_time > 2000:  # 获胜后等待2s
                has_next = game_manager.next_level()
                if not has_next:
                    success_finish = True
                    continue
                success_time = -1  # 继续更新获胜时间
        # 染色
        screen.fill('black')

        if game_manager.update():
            success_time = pygame.time.get_ticks()  # 更新获胜时间

    # 更新整个页面
    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()








