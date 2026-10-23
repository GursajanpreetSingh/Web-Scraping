from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
google_form = "https://docs.google.com/forms/d/e/1FAIpQLSe0v09cGDS3hsCBd7rL1r6Pts-Vn275aIJgd1J2OoRUoxdZ5g/viewform?usp=sharing&ouid=104762560514420815950"

response = requests.get(zillow_url)
contents = response.text
soup = BeautifulSoup(contents,"html.parser")

address_list = []
price_list = []
link_list = []

all_cards = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
for card in all_cards:
    address = card.find(name = "address")
    address_list.append(address.text.strip().replace("|"," "))

    price = card.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    price_list.append(price.text.split('+')[0])

    link = card.find(name="a",class_="property-card-link")
    link_list.append(link.get("href"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options= chrome_options)


for i in range(len(address_list)):
    driver.get(google_form)
    time.sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address.send_keys(address_list[i])
    price.send_keys(price_list[i])
    link.send_keys(link_list[i])

    submit_button = driver.find_element(By.CSS_SELECTOR, value=".lRwqcd span")
    submit_button.click()



