from ultralytics import YOLO
import cv2

# 加载两个检测模型
detect_model1 = YOLO('train6/weights/best.pt')  # 检测模型1
detect_model2 = YOLO('train12/weights/best.pt')  # 检测模型2

# 读取图片
image_path = '3.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
else:
    # ================== 第一个模型推理 ==================
    results1 = detect_model1(image)

    # 处理并显示模型1结果
    annotated_img1 = cv2.resize(results1[0].plot(), (640, 720))
    cv2.imshow('Detection Model 1', annotated_img1)

    # 打印模型1置信度
    if results1[0].boxes.conf.numel() > 0:
        print("\nModel 1 检测置信度：")
        for i, conf in enumerate(results1[0].boxes.conf):
            print(f"目标 {i + 1}: {conf.item():.2%}")
    else:
        print("\nModel 1 未检测到目标")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ================== 第二个模型推理 ==================
    results2 = detect_model2(image)

    # 处理并显示模型2结果
    annotated_img2 = cv2.resize(results2[0].plot(), (640, 720))
    cv2.imshow('Detection Model 2', annotated_img2)

    # 打印模型2置信度
    if results2[0].boxes.conf.numel() > 0:
        print("\nModel 2 检测置信度：")
        for i, conf in enumerate(results2[0].boxes.conf):
            print(f"目标 {i + 1}: {conf.item():.2%}")
    else:
        print("\nModel 2 未检测到目标")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
