
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
obj = Service("C:/Users/Admin/Downloads/chromedriver_win32(3).exe")
driver = webdriver.Chrome(service=obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.LINK_TEXT, " Login ").click()
driver.close()
driver.__exit__()