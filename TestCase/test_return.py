import pytest
import allure
from Common import Assert, Request, Login,read_excel

assertions = Assert.Assertions()
request = Request.Request()
token = Login.Login().get_token()
url = Login.url

ids = 0
ids_pop = []

excel_list = read_excel.read_excel_list('./document/退货.xlsx')
for i in range(len(excel_list)):
    pop = excel_list[i].pop()
    ids_pop.append(pop)


@allure.feature('退货模块')
class Test_return:

    # @allure.story('登陆接口')
    # def test_login(self):
    #     login_rps = request.post_request(url='http://192.168.60.132:8080/admin/login',
    #                                      json={"username": "admin", "password": "123456"})
    #     assertions.assert_code(login_rps.status_code, 200)
    #     login_rps_json = login_rps.json()
    #     assertions.assert_in_text(login_rps_json, '成功')
    #
    #     # 接口关联-登陆
    #     rps_json_data = login_rps_json['data']
    #     data_token = rps_json_data['tokenHead'] + rps_json_data['token']
    #     global token
    #     token = {'Authorization': data_token}

    @allure.story('退货查询')
    def test_sel(self):
        sel_rps = request.get_request(url=url+'returnReason/list',
                                          params={'pageNum': 1, 'pageSize': 5}, headers=token)
        assertions.assert_code(sel_rps.status_code, 200)
        sel_rps_json = sel_rps.json()
        assertions.assert_in_text(sel_rps_json, '成功')

        rps_data = sel_rps_json['data']
        rps_data_list = rps_data['list']
        data_list = rps_data_list[0]
        global ids
        ids = data_list['id']

    @allure.story('删除第一条退货')
    def tesst_del(self):
        del_rsp = request.get_request(url=url+'returnReason/list',
                                          params={'pageNum': 1, 'pageSize': 5})

        assertions.assert_code(del_rsp.status_code, 200)
        del_rsp_json = del_rsp.json()
        assertions.assert_in_text(del_rsp_json, '成功')

    @allure.story('新增退货')
    @pytest.mark.parametrize('name,sort,status,msg',excel_list,ids=ids_pop)
    def test_add(self,name,sort,status,msg):
        add_rsp = request.post_request(url=url+'returnReason/create',
                                            json={"name": "wu物流问题", "sort": 0, "status": 1, "createTime": ''})

        assertions.assert_code(add_rsp.status_code, 200)
        add_rsp_json = add_rsp.json()
        assertions.assert_in_text(add_rsp_json, msg)
