# creater: xf
# time: 2022/7/12 12:30
import allure
import pytest
import inspect

from demo.flow.route_flow import RouteFlow
from demo import root_dir

# test_data = [(root_dir.split('\\')[-1], "devices")]
test_data = [root_dir.split('\\')[-1]]


@allure.epic("route")
class TestRoute:

    @allure.feature("路线规划")
    @allure.title("查看路线")
    @pytest.mark.D
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_route_view(self, driver, start_stop_app):
        route_flow = RouteFlow(driver)
        route_flow.route_plan(inspect.stack()[0][3])

    @allure.feature("路线规划")
    @allure.title("切换步行")
    @pytest.mark.D
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_route_switch_walk(self, driver, start_stop_app):
        route_flow = RouteFlow(driver)
        route_flow.change_walk(inspect.stack()[0][3])

    '''
        根据以上示例，完成以下导航相关的用例
        用例步骤：
                1.点击搜索框并输入对应的检索条件（data数据）
                2.点击搜索按钮
                3.选择第n条搜索结果
                4.点击路线按钮
                5.点击开始导航并同步至手机（使用图片定位方式），图片已保存在image文件夹下 （开始导航）
                6.点击结束导航（结束导航）
        编写过程：
                1.在data.yaml文件中补充对应用例所需的关键字与数据
                2.在search_page.py中检查是否存在页面操作的公有方法
                3.在search_flow.py中新增对应用例的操作流程,方法名与test_search.py中的保持一致
        '''

    @allure.feature("路线规划")
    @allure.title("开始导航")
    @pytest.mark.D
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_route_start_navigation(self, driver, start_stop_app):
        route_flow = RouteFlow(driver)
        route_flow.start_navigation(inspect.stack()[0][3])

    @allure.feature("路线规划")
    @allure.title("结束导航")
    @pytest.mark.D
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_route_end_navigation(self, driver, start_stop_app):
        route_flow = RouteFlow(driver)
        route_flow.end_navigation(inspect.stack()[0][3])
