
from random import random

import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]
random_letter = random.choice(letters)

with open(f"letter_templates/{random_letter}","r") as file:
    letter_text = file.readlines()


#details of sender
email = "andreeaiulianabadiu@gmail.com"
password = "ylgxghadqewecgfg"


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day
for birthday in birthdays:
    if today == birthday["day"]:
        letter_text[0] =letter_text[0].replace("[NAME]", birthday["name"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

#remove the \n characters from the letter text
letter_str = ""
for line in letter_text:
    letter_str += line.strip("\n")
    letter_str += "\n"

#4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs="yulya05@yahoo.com",msg=f"Subject:Happy birthday!\n\n{letter_str}")




