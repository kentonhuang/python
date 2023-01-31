import smtplib

my_email = "finanglindanglin@gmail.com"
password = "hyesqhavvyvnhnet"

import random

with open("quotes.txt") as file:
    lines = file.read().splitlines()
    print(lines)

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if(day_of_week == 1):

    quote = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="finnanglindanglin@yahoo.com",
            msg=f"Subject:Motivational Quote\n\n{quote}"
        )