# creater: xf
# time: 2022/7/12 12:23
import allure

from demo.page.route_page import RoutePage, Data


class RouteFlow(object):

    def __init__(self, driver):
        self.route_page = RoutePage(driver)
        self.data = Data(driver).data

    @allure.story("规划路线")
    def route_plan(self, f_name):
        self.route_page.click_and_input(f_name)
        self.route_page.click_button()
        self.route_page.click_first(f_name)
        self.route_page.click_route()

    @allure.story("切换步行路线")
    def change_walk(self, f_name):
        self.route_page.click_and_input(f_name)
        self.route_page.click_button()
        self.route_page.click_first(f_name)
        self.route_page.click_route()
        self.route_page.choose_walk(f_name)

    @allure.story("开始导航")
    def start_navigation(self, f_name):
        self.route_page.click_and_input(f_name)
        self.route_page.click_button()
        self.route_page.click_first(f_name)
        self.route_page.click_route()
        self.route_page.click_navigation()

    @allure.story("结束导航")
    def end_navigation(self, f_name):
        self.route_page.click_and_input(f_name)
        self.route_page.click_button()
        self.route_page.click_first(f_name)
        self.route_page.click_route()
        self.route_page.click_navigation()
        self.route_page.click_exit_navigation()
