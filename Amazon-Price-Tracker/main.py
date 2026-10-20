from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

static_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {"Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6,ru;q=0.5,de;q=0.4",
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

response = requests.get(url=static_url, headers=header)
content = response.text

soup = BeautifulSoup(content,"html.parser")

# price for static url
price = float(soup.find(name="span",class_="aok-offscreen").get_text().split("$")[1])
print(price)

# price = float(soup.find(name="span",class_="aok-offscreen").get_text().split("$")[1].split()[0])
# print(price)

title = ' '.join(soup.find(id="productTitle").get_text().split()[0:2])
print(title)

buy_price = 100

if price < buy_price:
    message= f"{title} is on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"],port = 587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"], password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
                            from_addr=os.environ["EMAIL_ADDRESS"],
                            to_addrs=os.environ["EMAIL_ADDRESS"],
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}"
                            )