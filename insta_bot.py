import time
from selenium import webdriver

driver = webdriver.Chrome("../chromedriver")
driver.implicitly_wait(5)


class InstaHome():
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://www.instagram.com/')


    def login_account(self,username,password):
        username_ = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)

        password_ = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)

        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')

        login.click()
        time.sleep(6)


    def search_user(self,user):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user)



username = input("enter your username\n")
password = input("enter your password\n")
home = InstaHome(driver)
home.login_account(username,password)

time.sleep(5)
user = input("enter user name to search \n")
home.search_user(user)
