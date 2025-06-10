import tensorflow as tf

# 加载保存的模型
model = tf.keras.models.load_model('mobilenetv2_classifier.h5')

# 设置图像参数
img_height = 224
img_width = 224

# 加载和预处理新图像
img_path = './888eeccb-cdb9-4a5d-ae8b-c4b69ffe781c.jpg'
img = tf.keras.preprocessing.image.load_img(img_path, target_size=(img_height, img_width))
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) / 255.0

# 进行预测
prediction = model.predict(img_array)
print(f'Prediction: {prediction[0][0]}')

# 根据概率值判断类别
if prediction[0][0] > 0.5:
    print("The image is classified as class normal.")
else:
    print("The image is classified as class jaundice.")

# ----------------------------------------------------------------------
"""
# 导入所需要的库
from flask import Flask, jsonify

# 创建Flask应用
app = Flask(__name__)

# 定义数据生成方式
def generate_data():
    data = {'result':prediction[0][0]}
    return data

# 定义API接口
@app.route('./get_data', methods=['GET'])
def get_data():
    data = generate_data()
    return jsonify(data)

# 运行Flask应用
if __name__ == '__main__':
    app.run()
"""
