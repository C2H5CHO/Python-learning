import math
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,center_x,center_y,forward_angle):
        super().__init__()
        self.width = 100
        self.height = 50
        self.forward_angle = forward_angle # 在游戏坐标中，顺时针转动的角度
        self.image_source = pygame.image.load('pictures/car.png').convert() # 获取图片资源
        self.image = pygame.transform.scale(self.image_source,(self.width,self.height))
        self.image = pygame.transform.rotate(self.image,-self.forward_angle) # rotate --> 指逆时针转动的角度
        self.image.set_colorkey('black') # 把black这个颜色变成透明的
        # self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (center_x,center_y)
        self.last_time = pygame.time.get_ticks() # 返回当前的时刻,单位：ms
        self.delta_time = 0 # 返回两帧之间的间隔

        self.move_velocity_limit = 220 # 速度上限
        self.move_velocity = 0 # 当前移动速度
        self.move_acc = 600 # 加速度
        self.rotate_velocity_limit = 140 # 角加速度上限
        self.rotate_velocity = 0 # 角加速度
        self.friction = 0.9 # 摩擦力

        self.crash_sound = pygame.mixer.Sound('sounds/crash.mp3')
        self.crash_sound.set_volume(0.1)
        self.move_sound = pygame.mixer.Sound('sounds/move.mp3')
        self.move_sound.set_volume(0.3)
        self.move_voice_channel = pygame.mixer.Channel(7)

    def update_delta_time(self):
        cur_time = pygame.time.get_ticks() # 获取此时的时刻
        self.delta_time = (cur_time - self.last_time) / 1000 # 将单位从 ms 换算成 s
        self.last_time = cur_time

    def input(self): # 小车的速度
        # 按照指令运动
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.move_velocity += self.move_acc * self.delta_time
            self.move_velocity = min(self.move_velocity, self.move_velocity_limit)
            if not self.move_voice_channel.get_busy():
                self.move_voice_channel.play(self.move_sound)
        elif key_pressed[pygame.K_s]:
            self.move_velocity -= self.move_acc * self.delta_time
            self.move_velocity = max(self.move_velocity, -self.move_velocity_limit)
            if not self.move_voice_channel.get_busy():
                self.move_voice_channel.play(self.move_sound)
        else:
            self.move_velocity = int(self.move_velocity * self.friction)
            if self.move_voice_channel.get_busy():
                self.move_voice_channel.stop()
        # 设置转动符号
        sign = 1
        if self.move_velocity < 0:
            sign = -1

        if key_pressed[pygame.K_d]:
            self.rotate_velocity = self.rotate_velocity_limit * sign
        elif key_pressed[pygame.K_a]:
            self.rotate_velocity = -self.rotate_velocity_limit * sign
        else:
            self.rotate_velocity = 0 # 清空角速度

    def rotate(self,direction=1):
        self.forward_angle += self.rotate_velocity * self.delta_time * direction
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)
        self.image.set_colorkey('black')
        # 重置中心点
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def move(self,direction=1): # 小车的运动
        if direction == 1 and abs(self.move_velocity) > 50:
            self.rotate(direction) # 当车身速度不为0时，车才会转动
        vx = self.move_velocity * math.cos(math.pi * self.forward_angle / 180) * direction
        vy = self.move_velocity * math.sin(math.pi * self.forward_angle / 180) * direction
        self.rect.x += vx * self.delta_time
        self.rect.y += vy * self.delta_time
        if direction == -1 and abs(self.move_velocity) > 50:
            self.rotate(direction)

    def crash(self):
        self.crash_sound.play()
        self.move(-1) # 退回现场
        if self.move_velocity >= 0:
            self.move_velocity = min(-self.move_velocity,-100)
        else:
            self.move_velocity = max(self.move_velocity,100)
        self.rotate_velocity *= -1

    def update(self):
        self.update_delta_time()
        self.input()
        self.move()















