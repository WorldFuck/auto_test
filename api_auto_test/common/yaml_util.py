import os
import yaml


# 读取
def read_yaml():
    with open(r"C:\Users\今晚打老虎\Desktop\pythonProject\data_tokens.yaml", mode="r", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


# 写入
def write_yaml(data):
    with open(r"C:\Users\今晚打老虎\Desktop\pythonProject\data_tokens.yaml", mode="a", encoding="utf-8") as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


# 清除
def clean_yaml():
    with open(r"C:\Users\今晚打老虎\Desktop\pythonProject\data_tokens.yaml", mode="w") as f:
        f.truncate()


# 读取用例
def read_case(yaml_path):
    with open(os.getcwd() + r"\%s" % yaml_path, mode="r", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    yaml_path = "login.yaml"
    print(os.getcwd() + r"\%s" % yaml_path)
