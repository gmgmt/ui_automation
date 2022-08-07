# creater: xf
# time: 2022/7/12 12:30
import allure
import pytest
import inspect

from demo.flow.search_flow import SearchFlow
from demo import root_dir

test_data = [root_dir.split('\\')[-1]]


@allure.epic("search")
class TestSearch:

    @allure.feature("POI搜索")
    @allure.title("点击清空历史记录")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_clear_history(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.clear_search_records(inspect.stack()[0][3])

    @allure.feature("POI搜索")
    @allure.title("搜索城市")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_city(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.search_city(inspect.stack()[0][3])

    '''
    根据以上示例，完成以下搜索相关的用例
    用例步骤：
            1.点击搜索框并输入对应的检索条件（data数据）
            2.点击搜索按钮
            3.根据检索条件判断搜索结果是否包含对应字段
    编写过程：
            1.在data.yaml文件中补充对应用例所需的关键字与数据
            2.在search_page.py中检查是否存在页面操作的公有方法，
            3.在search_flow.py中新增对应用例的操作流程,方法名与test_search.py中的保持一致
    '''

    @allure.feature("POI搜索")
    @allure.title("搜索地铁站")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_search_subway(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.search_subway(inspect.stack()[0][3])

    @allure.feature("POI搜索")
    @allure.title("搜索超市")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_search_supermarket(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.search_supermarket(inspect.stack()[0][3])

    @allure.feature("POI搜索")
    @allure.title("输入数字")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_input_numbers(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.input_numbers(inspect.stack()[0][3])

    @allure.feature("POI搜索")
    @allure.title("输入英文")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_input_english(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.input_english(inspect.stack()[0][3])

    @allure.feature("POI搜索")
    @allure.title("输入组合字符")
    @pytest.mark.S
    @pytest.mark.parametrize('driver', test_data, indirect=True)
    def test_search_input_complex_character(self, driver, start_stop_app):
        search_flow = SearchFlow(driver)
        search_flow.input_complex_character(inspect.stack()[0][3])
