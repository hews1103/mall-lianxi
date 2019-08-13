import allure
from Common import Request,Assert
url='http://192.168.2.39:8280'

request = Request.Request()
assertions = Assert.Assertions()

@allure.feature("仓库信息")
class Test_gyl:
    @allure.story("查看仓库信息")
    def test_cxckxx(self):
        get_reps= request.get_request(url=url + '/warehouseInfo/findBylikeName',
                                      params={'cwhname':'保税仓-杭州心怡仓'})
        assertions.assert_code(get_reps.status_code,200)
        reps_json = get_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'],"响应成功")

    @allure.story("多条件分页检索")
    def test_dtjjs(self):
        get_reps = request.get_request(url=url + '/warehouseInfo/getPage',
                                       params={'page': 1, 'rows': 5})
        assertions.assert_code(get_reps.status_code,200)
        reps_json = get_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'],'响应成功')

    @allure.story("联想搜索")
    def test_lxss1(self):
        get_reps = request.get_request(url=url + '/warehouseInfo/searchWarehouseInfo',
                                       params={'keys':'cwhname' , 'vague': '保税仓'})
        assertions.assert_code(get_reps.status_code,200)
        reps_json = get_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'],'响应成功')

    @allure.story("根据id查询仓库详情")
    def test_ckxq(self):
        get_reps = request.get_request(url=url + '/warehouseInfo/selById',
                                       params={'id': 116})
        assertions.assert_code(get_reps.status_code, 200)
        reps_json = get_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'], '响应成功')

    @allure.story("仓库类型下拉框查询")
    def test_ckxlcx(self):
        get_reps = request.get_request(url=url + '/warehouseInfo/selCwhTypes')
        assertions.assert_code(get_reps.status_code, 200)
        reps_json = get_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'], '响应成功')

    @allure.story("产品类型下拉框查询")
    def test_cpxlcx(self):
        get_reps = request.get_request(url=url + '/warehouseInfo/selGoodTypes')
        assertions.assert_code(get_reps.status_code, 200)
        reps_json = get_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'], '响应成功')

    @allure.story("根据id修改仓库信息")
    def test_xgck(self):
        post_reps = request.post_request(url=url + '/warehouseInfo/updateById', params='id=166')
        assertions.assert_code(post_reps.status_code, 200)
        reps_json = post_reps.json()
        assertions.assert_in_text(reps_json['errorMsg'], '响应成功')



pass

