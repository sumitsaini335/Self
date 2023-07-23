from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
import logging
from selenium.webdriver.common.by import By



service_obj = Service(executable_path= "./chromedriver");
driver = webdriver.Chrome(service=service_obj)
print(driver.title)
print("------------Start code ------------------------------------ ")

def list_of_elements():
    driver.implicitly_wait(5)
    driver.get("https://www.naukri.com/mnjuser/homepage")
    driver.find_element(By.ID,"usernameField").send_keys("Username")
    driver.find_element(By.ID,"passwordField").send_keys("Password")

    driver.find_element(By.CSS_SELECTOR,".waves-effect.waves-light.btn-large.btn-block.btn-bold.blue-btn.textTransform").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR,"div[class='heading-right'] a[class='view-all']").click()
    elements = driver.find_elements(By.CLASS_NAME,"titleAnchor")
    for ele in elements:

        print(ele.text)
        with open("file.txt","a",encoding='utf-8')as fi:

            filees = fi.write(ele.text + "\n")


code = list_of_elements()



import _self_learning_selenium_
