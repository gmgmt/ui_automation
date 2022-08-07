# creater: xf
# time: 2022/7/12 12:11

import time
import allure
from common.base_page import BasePage
from demo.element.element_router import ElementRouter
from demo import root_dir


class SearchPage(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(SearchPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = Data(self.driver).data

    @allure.step("点击并搜索框并输入")
    def click_and_input(self, f_name):
        data = self.data[f_name]["address"]
        self.find_element_and_input(plaintext=data, **self.element["searchBar"])

    @allure.step("点击并搜索框")
    def click_search(self):
        self.find_element_and_click(**self.element["searchBar"])

    @allure.step("点击搜索按钮")
    def click_button(self):
        self.find_element_and_click(check_toast=False, **self.element["searchButton"])
        time.sleep(2)

    @allure.step("验证用例")
    def check_result(self, f_name):
        self.element["result"]["textContains"] = self.data[f_name]["textContains"]
        self.find_element_and_click(check_toast=False, **self.element["result"])
        time.sleep(2)

    @allure.step("验证无搜索结果")
    def check_non_result(self):
        self.assert_element_exist(**self.element["non_result"])
        time.sleep(2)

    @allure.step("点击第一条搜索结果")
    def click_item(self, f_name):
        index = self.data[f_name]["number"] - 1
        self.find_element_and_click(index=index, **self.element["result"])
        time.sleep(2)

    @allure.step("清除历史记录")
    def click_clear_history(self):
        self.find_element_and_click(check_toast=False, **self.element["clearHistory"])
        time.sleep(2)

    @allure.step("检查是否清除历史记录")
    def check_clear_result(self, f_name):
        data = self.data[f_name]["clear_history"]
        self.assert_text_non_exist(plaintext=data)
        time.sleep(2)


class Data(BasePage):
    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(Data, self).__init__(driver)
        self.data = ElementRouter.select(self.__class__.__name__, "data")
