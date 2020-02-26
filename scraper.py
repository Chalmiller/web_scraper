import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/gp/product/B081FTNGNC/ref=ox_sc_saved_title_8?smid=ATQQBVXK188KS&psc=1"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    # priceblock_ourprice
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:6])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 2000):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('chalmiller1@gmail.com', <password>)

    subject = 'Price fell down!'
    body = "Check the Amazon link!"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('chalmiller1@gmail.com',
                    'chalmiller1@gmail.com',
                    msg
    )

    print("Email has been sent :)")

    server.quit()


