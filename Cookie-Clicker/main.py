from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import time,sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

print("Looking for language selection....")
try:
    language_button = driver.find_element(By.ID, value="langSelect-EN")
    print("Found language button.Clicking....")
    language_button.click()
    sleep(2)
except NoSuchElementException:
    print("Language selection not found")

sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")

wait_time = 5
timeout = time() + 5
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time()>timeout:
        try:
            cookies_element = driver.find_element(By.ID,value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",",""))

            products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID,value="cookies")
            final_cookie_count = int(cookies_element.text.split()[0].replace(",",""))
            final_cookie_per_second = float(cookies_element.text.split()[4])
            print(f"Final result: Total cookies:{final_cookie_count},Cookies/second:{final_cookie_per_second}")
        except NoSuchElementException:
            print("Couldn't find final cookie count")
        break


