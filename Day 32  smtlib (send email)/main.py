import datetime as dt
import pandas
import random
from os import listdir
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

from os.path import isfile, join
letters = [f for f in listdir("letter_templates") if isfile(join("letter_templates", f))]


today = dt.datetime.now()
today.day
data = pandas.read_csv("birthdays.csv")


for (index, row) in data.iterrows():
    #print(row.Name)
    #print(row.email)
    if row.month == today.month and row.day == today.day:
        file_name = random.choice(letters)    
        with open(f"letter_templates/{file_name}") as letter:
            letter_content = letter.read()
            updated_letter = letter_content.replace("[NAME]", row.Name)
            print(updated_letter)
        #Send an email to the bday person using smtplib  
        #with smtplib.SMTP("smtp.gmail.com") as connection:
        #    connection.starttls()
        #    connection.login(MY_EMAIL,MY_PASSWORD)
        #    connection.sendmail(
        #        from_addr=MY_EMAIL,
        #        to_addrs=row.email,
        #        msg=f"Subject:Happy Birthday!\n\n{updated_letter}"
        #    )
