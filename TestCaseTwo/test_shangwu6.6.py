import pytest
import allure
from Common import Assert,Request,Login,Tools,read_excel

assertions = Assert.Assertions()
request = Request.Request()
pwd_normal = Tools.random_str_abc(3) + Tools.random_123(3)
url = Login.url

excel_list = read_excel.read_excel_list('./document/用户注册.xlsx')
ids=[]
for i in range(len(excel_list)):
    pop_excel = excel_list[i].pop()
    ids.append(pop_excel)

@allure.feature('注册/登录模块')
class Test_user():

    @allure.story('注册接口')
    @pytest.mark.parametrize('phone,pwd,rePwd,userName',excel_list,ids=ids)
    def test_signup(self,phone,pwd,rePwd,userName,msg):
        user_sig_resp = request.post_request(url=url + 'user/signup',
                                            json = {"phone": phone, "pwd":pwd , "rePwd": rePwd,
                                                  "userName": userName})

        resp_json = user_sig_resp.json()
        resp_base_1 = resp_json['respBase']
        assertions.assert_in_text(resp_base_1['respDesc'],msg)