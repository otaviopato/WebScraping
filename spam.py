from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui

browser = webdriver.Chrome()
browser.maximize_window()

def escMultipleTimes(times):
    for i in range(0,times):
        pyautogui.press("esc")

def messageNTimes(message, times):
    browser.find_element(By.XPATH, '//*[@role="textbox"]').click()
    for i in range(0, times):
        browser.find_element(By.XPATH, '//*[@role="textbox"]').send_keys(str(message) + str(i))
        pyautogui.press("enter")

def awaitFromSpecificXpath(specificXPath):
    try:
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, specificXPath))
        )
        escMultipleTimes(10)
    except:
        print('Can\'t found specified xpath')
        browser.quit()

try:
    browser.get("https://www.facebook.com/")
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("COLOCAR O E-MAIL")#IMPORTANTE
    browser.find_element(By.XPATH, '//*[@id="pass"]').send_keys("COLOCAR A SENHA")#IMPORTANTE
    browser.find_element(By.NAME, 'login').click()

    awaitFromSpecificXpath('//*[@aria-label="Conta"]')
    browser.get("Link do usuário para enviar mensagem")
    awaitFromSpecificXpath('//*[@role="textbox"]')
    
    messageNTimes('Hello! ', 5)
    print('Normal exit.')
except:
    print('Some error occurred')
    
finally:
    browser.quit()

"""
time.sleep(10)
for i in range(0,10):
    pyautogui.press("esc")

browser.get("https://www.facebook.com/messages/t/100000503376090")
time.sleep(5)
for i in range(0,10):
    pyautogui.press("esc")

browser.find_element(By.XPATH, '//*[@role="textbox"]').click()
browser.find_element(By.XPATH, '//*[@role="textbox"]').send_keys("teste aaaaa")
pyautogui.press("enter")

time.sleep(2)
"""



#pyautogui.press("enter")
#time.sleep(5)
#pyautogui.position()
#https://www.facebook.com/messages/t/100000503376090
#//*[@id="mount_0_0_qp"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[1]/p

