# creater: xf
# time: 2022/7/12 12:17
import os
import time
import allure
from common.base_page import BasePage
from demo.element.element_router import ElementRouter
from demo import root_dir


class RoutePage(BasePage):

    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(RoutePage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__, "element")
        self.data = Data(self.driver).data

    @allure.step("点击并搜索框并输入")
    def click_and_input(self, f_name):
        data = self.data[f_name]["address"]
        self.find_element_and_input(plaintext=data, **self.element["searchBar"])

    @allure.step("点击搜索按钮")
    def click_button(self):
        self.find_element_and_click(check_toast=False, **self.element["searchButton"])
        time.sleep(2)

    @allure.step("选择第一个")
    def click_first(self, f_name):
        self.element["result"]["textContains"] = self.data[f_name]["textContains"]
        self.find_element_and_click(check_toast=False, **self.element["result"], index=0)
        time.sleep(2)

    @allure.step("查看路线")
    def click_route(self):
        self.find_element_and_click(check_toast=False, **self.element["route"])
        time.sleep(2)
        self.assert_element_exist(**self.element["resultCheck"])

    @allure.step("点击步行")
    def choose_walk(self, f_name):
        self.find_element_and_click(**self.element["walk"])
        data = self.data[f_name]["check_words"]
        self.assert_text_exist(data)

    @allure.step("点击开始导航")
    def click_navigation(self):
        try:
            image_dir = os.path.join(root_dir, "image", "navigation.jpg")
            self.find_element_and_click(check_toast=False, image=image_dir)
        except Exception as e:
            # 将没有找到图片的报错异常打印出来，将使用元素点击方式
            print(e)
            self.find_element_and_click(**self.element["start_navigation"])
        finally:
            self.assert_element_exist(**self.element["remain_time"])

    @allure.step("点击退出导航")
    def click_exit_navigation(self):
        check_exist = self.check_element_existence(**self.element["exit_navigation"])
        if check_exist:
            self.find_element_and_click(**self.element["exit_navigation"])
        else:
            self.find_element_and_click(**self.element["remain_time"])
            self.find_element_and_click(**self.element["exit_navigation"])
        time.sleep(0.5)
        self.assert_element_exist(**self.element["route"])


class Data(BasePage):
    def __init__(self, driver):
        self.platform = root_dir.split('\\')[-1]
        super(Data, self).__init__(driver)
        self.data = ElementRouter.select(self.__class__.__name__, "data")
