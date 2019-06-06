import pytest
import allure
from Common import Assert,Request,Login,Tools

assertions = Assert.Assertions()
request = Request.Request()
pwd_normal = Tools.random_str_abc(3) + Tools.random_123(3)
url = Login.url



@allure.feature('注册/登录模块')
class Test_user():

    @allure.story('注册接口')
    def test_signup(self):
        user_sig_resp = request.post_request(url=url + 'user/signup',
                                            json = {"phone": Tools.phone_num(), "pwd":pwd_normal , "rePwd": pwd_normal,
                                                  "userName": Tools.random_str_abc(2)+Tools.random_123(1)})

        resp_json = user_sig_resp.json()
        resp_base_1 = resp_json['respBase']
        assertions.assert_in_text(resp_base_1['respDesc'],'成功')








