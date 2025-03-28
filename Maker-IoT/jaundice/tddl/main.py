import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, classification_report, confusion_matrix

# 加载数据
data = pd.read_csv('./SaYoPillow.csv')
print(data.head(10))

# 特征选择与标签分离
features = ['rr', 'lm', 'hr','sr1']
X = data[features]
y = data['sl']

# 数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)

# 数据缩放
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 模型训练
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 模型预测与评估
y_pred = model.predict(X_test_scaled)
precision = precision_score(y_test, y_pred, average='weighted')
print(f'Precision: {precision}')
print(classification_report(y_test, y_pred))

import requests
import json

# 设置IAM服务的URL
iam_url = 'https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens'

# 设置请求头
headers = {
    "Content-Type": "application/json"
}

# 设置请求体
payload = {"auth": { "identity": {"methods": ["password"], "password": {"user": {"name": "root", "password": "Zzf666666", "domain": {"name": "cc_77d"}}}}, "scope": {"poject": {"name": "cn-north-4"}}}}


# 发送POST请求
response = requests.post(iam_url, headers=headers, data=json.dumps(payload))

# 检查响应状态码
if response.status_code == 201:
    # 如果请求成功，解析响应体中的token
    token_response = response.json()
    print(token_response)
    token_header = response.headers
    print(token_header['X-Subject-Token'])


# 要请求的URL
url = 'https://cc874402a6.st1.iotda-app.cn-north-4.myhuaweicloud.com/v5/iot/6911e244c5bd4158873ff299053f8e86/devices/673c4f942ff1872637bfd8ee_220236/shadow'
token = token_header['X-Subject-Token']
headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token
}

# 发送GET请求
response = requests.get(url, headers=headers)

l_t = {}
# 检查响应状态码
if response.status_code == 200:
    # 请求成功，处理响应数据
    print('Request was successful!')
    print('Response JSON:', response.json())
    data = response.json()
    data = data['shadow'][0]['reported']['properties']
    print(data)
    l_t['rr']=data['breath_detect_value']
    l_t['lm']=data['body_move_param']
    l_t['hr']=data['heart_detect_value']
    l_t['sr1']=data['sleep_light_hour']+data['sleep_deep_hour']
    print(l_t['rr'])
    print(l_t['lm'])
    print(l_t['hr'])
    print(l_t['sr1'])
else:
    # 请求失败，打印错误信息
    print('Request failed with status code:', response.status_code)
    print('Response Text:', response.text)

# 将字典转换为DataFrame
sample_df = pd.DataFrame([l_t])

# 使用之前训练模型时创建的Scaler来转换数据
sample_scaled = scaler.transform(sample_df)  # 使用之前拟合的scaler

# 使用训练好的模型进行预测
y_pred_sample = model.predict(sample_scaled)

# 打印预测结果
print(f'Predicted class: {y_pred_sample[0]}')

# ----------------------------------------------------------------------

# 导入所需要的库
from flask import Flask, jsonify

# 创建Flask应用
app = Flask(__name__)

# 定义数据生成方式
def generate_data():
    data = {'result':y_pred_sample[0]}
    return data

# 定义API接口
@app.route('/get_data', methods=['GET'])
def get_data():
    data = generate_data()
    return jsonify(data)

# 运行Flask应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

