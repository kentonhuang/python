##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

data = pandas.read_csv("birthdays.csv")
# birthdays_dict = data.to_dict(orient="records")
# print(birthdays_dict)

today = dt.datetime.now()
today_tuple = (today.month, today.day)

my_email = "finanglindanglin@gmail.com"
password = "hyesqhavvyvnhnet"

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    random_num = random.randint(1,3)

    with open(f"letter_templates/letter_{random_num}.txt") as letter:
        text = letter.read()
        replaced = text.replace("[NAME]", birthday_person["name"])
        print(replaced)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{replaced}"
        )

# for birthday in birthdays_dict:
#     if birthday['month'] == month and birthday['day'] == day:
#         random_num = random.randint(1,3)
#
#         with open(f"letter_templates/letter_{random_num}.txt") as letter:
#             text = letter.read()
#             replaced = text.replace("[NAME]", birthday['name'])
#             print(replaced)
#
#         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=birthday['email'],
#                 msg=f"Subject:Happy Birthday!\n\n{replaced}"
#             )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




