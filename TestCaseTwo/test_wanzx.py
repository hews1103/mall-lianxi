import pytest
import allure
from Common import Assert,Request,Login,Tools,read_excel

assertions = Assert.Assertions()
request = Request.Request()
pwd_normal = Tools.random_str_abc(3) + Tools.random_123(3)
url = Login.url

excel_list = read_excel.read_excel_list('./document/商品分类.xlsx')
ids_list = []
for i in range(len(excel_list)):
    # 删除excel_list中每个小list的最后一个元素,并赋值给ids_pop
    ids_pop = excel_list[i].pop()
    # 将ids_pop添加到 ids_list 里面
    ids_list.append(ids_pop)

@allure.feature('注册/登录模块')
class Test_user():

    @allure.story('注册接口1')
    def test_signup1(self):
        user_sig_resp = request.post_request(url=url + 'user/signup',
                                            json = {"phone": Tools.phone_num(), "pwd":pwd_normal , "rePwd": pwd_normal,
                                                  "userName": Tools.random_str_abc(2)+Tools.random_123(1)})

        resp_json = user_sig_resp.json()

        assertions.assert_in_text(resp_json['respDesc'],'成功')

    @allure.story('注册接口2')
    @pytest.mark.parametrize('phone,pwd,rePwd,userName,numb', excel_list, ids=ids_list)
    def test_signup2(self, phone, pwd, rePwd, userName, numb):
        user_sig_resp = request.post_request(url=url + 'user/signup',
                                             json={"phone": phone, "pwd": pwd, "rePwd": rePwd,
                                                   "userName": userName})








