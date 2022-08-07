# creater: xf
# time: 2022/7/12 12:23
import allure
from demo.page.search_page import SearchPage


class SearchFlow(object):

    def __init__(self, driver):
        self.search_page = SearchPage(driver)

    @allure.story("搜索城市")
    def search_city(self, f_name):
        self.search_page.click_and_input(f_name)
        self.search_page.click_button()
        self.search_page.check_result(f_name)

    @allure.story("清空搜索记录")
    def clear_search_records(self, f_name):
        self.search_page.click_search()
        self.search_page.click_clear_history()
        self.search_page.check_clear_result(f_name)

    @allure.story("搜索地铁站")
    def search_subway(self, f_name):
        self.search_page.click_and_input(f_name)
        self.search_page.click_button()
        self.search_page.check_result(f_name)

    @allure.story("搜索超市")
    def search_supermarket(self, f_name):
        self.search_page.click_and_input(f_name)
        self.search_page.click_button()
        self.search_page.check_result(f_name)

    @allure.story("输入数字")
    def input_numbers(self, f_name):
        self.search_page.click_and_input(f_name)
        self.search_page.click_button()
        self.search_page.check_result(f_name)

    @allure.story("输入英文")
    def input_english(self, f_name):
        self.search_page.click_and_input(f_name)
        self.search_page.click_button()
        self.search_page.check_result(f_name)

    @allure.story("输入组合字符")
    def input_complex_character(self, f_name):
        self.search_page.click_and_input(f_name)
        self.search_page.click_button()
        self.search_page.check_non_result()
