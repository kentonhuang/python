from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

amazon_url = "https://camelcamelcamel.com/product/B06Y1YD5W7"
product_url = "https://www.amazon.com/dp/B06Y1YD5W7"
target_price = 100

my_email = "email"
password = "password"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(amazon_url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price = float(soup.find(class_="stat green").text.strip("$"))

if price < target_price:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="huangkenton0@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n Price of item is now ${float}. Click here {product_url}"
        )


