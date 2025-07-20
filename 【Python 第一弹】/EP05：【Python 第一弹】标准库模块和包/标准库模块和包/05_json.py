"""
json 模块
"""

# 1. Python 对象转 JSON 字符串（序列化）
import json
data = {
    "name": "张三",
    "age": 25,
    "hobbies": ["读书", "跑步"]
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

print('--'*50)

# 2. JSON 字符串转 Python 对象（反序列化）
import json
json_str = '{"name": "李四", "score": 95.5}'
# 转换为Python字典
data = json.loads(json_str)
print(data["name"])
print(type(data["score"]))

print('--'*50)

# 3. 文件读写 JSON
import json
data = {"status": "success", "result": [1, 2, 3]}
# 写入JSON文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
# 读取JSON文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print(loaded_data["result"])