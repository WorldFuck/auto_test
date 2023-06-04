import re

import pytest
import requests

from common.yaml_util import write_yaml, read_yaml, clean_yaml, read_case


class Test_login:
    import pytest
    import requests

    class TestLogin:
        access_token = None

        @pytest.mark.parametrize("username, password",
                                 [("1510025045@qq.com", "7c4a8d09ca3762af61e59520943dc26494f8941b")])
        def test_login(self, username, password):
            login_url = "https://accounts.easub.com/api/cas/login"
            payload = {
                "username": username,
                "password": password
            }
            response = requests.post(login_url, json=payload)
            response.raise_for_status()

            data = response.json()
            self.__class__.access_token = data.get("access_token")

            print("Login Response:")
            print(data)

        def test_get_personal_page(self):
            personal_page_url = "https://www.weirongmei.com/api/v2/user/customer/config"
            headers = {
                "Authorization": f"Bearer {self.__class__.access_token}"
            }
            response = requests.get(personal_page_url, headers=headers)
            response.raise_for_status()

            data = response.json()

            print("Personal Page Response:")
            print(data)

            assert response.status_code == 200
            # 可以进一步验证服务器返回的其他数据



if __name__ == '__main__':
    pytest.main()
