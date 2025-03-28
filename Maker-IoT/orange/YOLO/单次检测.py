from ultralytics import YOLO
import cv2

# 加载模型
model = YOLO('train12/weights/best.pt')

# 读取图片
image_path = '3.jpg'  # 替换为你的图片路径
image = cv2.imread(image_path)

# 确保图片被正确读取
if image is None:
    print("Error: Image not found.")
else:
    # 对图片进行推理
    results = model(image)

    # 获取标注后的图片
    annotated_image = results[0].plot()

    # 调整图像大小为640x720
    annotated_image_resized = cv2.resize(annotated_image, (640, 720))

    # 显示图片
    cv2.imshow('YOLOv11', annotated_image_resized)

    # 等待按键后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
