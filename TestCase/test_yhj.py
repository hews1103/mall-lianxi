import pytest
import allure
from Common import Assert, Request, read_excel

assertions = Assert.Assertions()
request = Request.Request()

token = {}
ids = 0
ids_pop=[]

excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')

for i in range(len(excel_list)):
    pop_list = excel_list[i].pop()
    ids_pop.append(pop_list)


@allure.feature('优惠卷模块')
class Test_yhj:

    @allure.story('登陆接口')
    def test_login(self):
        login_rps = request.post_request(url='http://192.168.60.132:8080/admin/login',
                                         json={"username": "admin", "password": "123456"})
        assertions.assert_code(login_rps.status_code, 200)
        login_rps_json = login_rps.json()
        assertions.assert_in_text(login_rps_json, '成功')

        # 接口关联-登陆
        rps_json_data = login_rps_json['data']
        data_token = rps_json_data['tokenHead'] + rps_json_data['token']
        global token
        token = {'Authorization': data_token}

    @allure.story('优惠卷查询接口')
    def test_sel(self):
        sel_rps = request.get_request(url='http://192.168.60.132:8080/coupon/list',
                                      params={'pageNum': 1, 'pageSize': 10}, headers=token)
        assertions.assert_code(sel_rps.status_code, 200)
        rps_json = sel_rps.json()
        assertions.assert_in_text(rps_json['message'], '成功')

        # 接口关联-ids
        json_data = rps_json['data']
        data_list = json_data["list"]
        data_list_id = data_list[0]
        list_id = data_list_id["id"]
        global ids
        ids = list_id

    @allure.story('优惠卷删除')
    def test_del(self):
        del_rps = request.post_request(url='http://192.168.60.132:8080/coupon/delete/' + str(ids), headers=token)
        assertions.assert_code(del_rps.status_code, 200)
        rps_json = del_rps.json()
        assertions.assert_in_text(rps_json['message'], '成功')

    @allure.story('增加优惠卷')
    @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg',excel_list,ids=ids_pop)
    def test_add(self,name,amount,minPoint,publishCount,msg):
        add_rsp = request.post_request(url='http://192.168.60.132:8080/coupon/create',
                                            json={"type": 0, "name": name, "platform": 0, "amount": amount,
                                                  "perLimit": 1, "minPoint": minPoint, "startTime": '', "endTime": '',
                                                  "useType": 0, "note": '', "publishCount": publishCount,
                                                  "productRelationList": [], "productCategoryRelationList": []},
                                            headers=token)
        assertions.assert_code(add_rsp.status_code, 200)
        add_json = add_rsp.json()
        assertions.assert_in_text(add_json['message'], msg)