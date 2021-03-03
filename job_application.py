import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

websites = [
    # list your website urls here, go through s test run and make sure all your information in job street is updated! 
]

for website in websites:
    browser = webdriver.Chrome(executable_path=os.getenv("CHROME"))
    browser.get('https://www.jobstreet.com.sg/en/job/8291709?icmpid=vcfsg%3A20210301')
    browser.find_element_by_link_text('Apply Now').click()
    login_page = browser.window_handles[1]
    browser.switch_to_window(login_page)
    login_id = browser.find_element_by_name("login_id")
    login_id.send_keys(os.getenv("EMAIL"))
    password = browser.find_element_by_name("password")
    password.send_keys(os.getenv("PASSWORD"))
    browser.find_element_by_name("btn_login").click()
    browser.find_element_by_name("btnAction").click()
    browser.find_element_by_name("close").click()
    browser.quit()