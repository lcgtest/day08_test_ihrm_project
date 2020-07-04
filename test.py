dict1 ={
    "case_name": "登录成功",
    "jsonData": {
        "mobile": "13800000002",
        "password": "123456"
    },
    "http_code": 200,
    "success": True,
    "code": 10000,
    "message": "操作成功"
}

print("dict1.values()", dict1.values())
print("dict1.keys()", dict1.keys())
# 继续分析：
# 由于parameterized，需要一个潜逃元组数据(())，所以我们需要把数据转化为嵌套元组形式
print("tuple(dict1.values())", tuple(dict1.values()))
print("tuple(dict1.values())", tuple(dict1.keys()))