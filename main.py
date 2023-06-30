from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time
import json

from setting import *

if __name__ == "__main__":
    with open("elements.json") as fp:
        elements = json.loads(fp.read())
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    driver.get(f"https://www.smythstoys.com/uk/en-gb/brand/jurassic-world/c/SM060614")
    # time.sleep(5)

    btn_yes = fnGetElementXpath(driver, False, elements["btn_yes"])

    try:
        btn_yes.click()
    except:
        print("Can't click Yes button!")
    time.sleep(3)
    i = 0
    while True:
        i += 1
        label_xpath = f"/html/body/div[8]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[{i}]/div/a/div/div[2]/h5/span"
        price_xpath = f"/html/body/div[8]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[{i}]/div/a/div/div[2]/div[1]/div/span"
        try:
            label = fnGetElementXpath(driver, False, label_xpath).__getattribute__(
                "text"
            )
            price = fnGetElementXpath(driver, False, price_xpath).__getattribute__(
                "text"
            )
            print(f"{i}th label is {label} and price is {price}.")

        except:
            print("Press Load More button!")
            btn_load_more = fnGetElementXpath(driver, False, elements["btn_load_more"])

            try:
                btn_load_more.click()
            except:
                print("Can't click Load More button!")
                break
            time.sleep(1)
    driver.close()
