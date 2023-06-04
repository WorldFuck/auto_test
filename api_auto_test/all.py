import os
import pytest as pytest


if __name__ == '__main__':
    pytest.main()
    #os.system("allure generate ./temp -o ./report --clean")     # 生成allure报告的方法，allure generate 是固定语法，./temp
    # 表示json临时报告 ，-o表示新报告输出的路径，./report表示输出的目标路径，--clean表示清除路径原来的文件



