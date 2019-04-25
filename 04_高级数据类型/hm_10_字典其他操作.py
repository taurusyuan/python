xiaoming_dict = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75
}
print(len(xiaoming_dict))

temp_dict = {
    "age": 20,
    "height": 1.85,
    "weight": 77
}

xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
xiaoming_dict.pop('age')
print(xiaoming_dict)