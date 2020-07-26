from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from xvfbwrapper import Xvfb
import sys

# Fake screen to allow  headless

if len(sys.argv) < 3:
    print('provide the proper arguments')
    print('python3 vanguard.py <username> <password>')
    exit(1)


with Xvfb() as xvfb:
    # Run the bot
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(960,1080)
    page = driver.get('https://secure.vanguardinvestor.co.uk/Login')

    # Go to the login page

    # Enter username

    userform = driver.find_element_by_xpath('//*[@id="__GUID_1007"]')
    userform.send_keys(sys.argv[1])

    # Enter password

    passform = driver.find_element_by_xpath('//*[@id="__GUID_1008"]')
    passform.send_keys(sys.argv[2])

    loginbutton = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[2]/div/form/div[2]/div[3]/button')
    loginbutton.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div[1]/section/div/div/div[2]/div/div/span'))
        )
    except:
        element = "element not found"
    finally:
        print(element.text)
        
        driver.quit()
