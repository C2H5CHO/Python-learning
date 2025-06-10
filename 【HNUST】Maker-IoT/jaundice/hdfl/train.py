import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 设置数据目录和参数
train_dir = '/archive'
batch_size = 32
img_height = 224
img_width = 224

# 创建图像数据生成器
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# 从目录中加载图像数据
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'  # 这是验证数据
)

base_model = tf.keras.applications.MobileNetV2(input_shape=(img_height, img_width, 3),
                                               include_top=False,
                                               weights='imagenet')

# 冻结预训练模型的卷积层
base_model.trainable = False

# 添加自定义的顶层
model = tf.keras.models.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=50  # 你可以根据需要调整训练轮数
)

loss, accuracy = model.evaluate(validation_generator)
print(f'Validation accuracy: {accuracy}')

# 保存模型
model.save('mobilenetv2_classifier.h5')
print("Model saved to 'mobilenetv2_image_classifier.h5'")