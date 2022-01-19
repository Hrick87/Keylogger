from subprocess import Popen
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

def getPublicIP(driver):
    driver.get("https://www.google.com/")
    
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a"))
            )
    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a").click()
    time.sleep(3)
        
    Email = driver.find_element(By.NAME, "identifier")
    Email.send_keys("infosecpwned87@gmail.com")

    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
            )
    
    driver.find_element(By.CLASS_NAME ,"VfPpkd-vQzf8d").click()

    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
            )

    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("YouGotRekt99")

    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
            )
    
    driver.find_element(By.CLASS_NAME ,"VfPpkd-vQzf8d").click()

    try:
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
                )
        
        driver.find_element(By.CLASS_NAME ,"VfPpkd-vQzf8d").click()
    except:
        pass
    
    try:
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "RveJvd snByac"))
                )
        
        driver.find_element(By.CLASS_NAME ,"RveJvd snByac").click()
    except:
        pass

    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "gb_d"))
                )
        
    driver.find_element(By.CLASS_NAME ,"gb_d").click()
    
    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div/div[2]/span/a"))
                )
        
    driver.find_element(By.XPATH ,"/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div/div[2]/span/a").click()

    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/div/table/tbody/tr/td[5]/div/div/div/span/span"))
                )
    Public_IP = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/div/table/tbody/tr/td[5]/div/div/div/span/span").text
    
    driver.quit()

    return Public_IP
# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())
chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')

# Pass in the `Service` instance with the `service` keyword: 
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://google.com")

Public_IP = getPublicIP(driver)
print(Public_IP) 
Popen('wget -r {Public_IP}', shell=True)