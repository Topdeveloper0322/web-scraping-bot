from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def fnGetElementXpath(driver, flag, xpath):
    try:
        ele = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if flag == False:
            return ele
        else:
            ele.click()
    except:
        print(f"fnGetElementXpath() is error because {xpath} can't find")
        return False

def fnGetElementsClass(driver, ClassName):
    try:
        eles = WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, ClassName)))
        return eles
    except:
        print(f"fnGetElementXpath() is error because {ClassName} can't find")
        return False

