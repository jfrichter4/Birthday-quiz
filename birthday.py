"""
birthday.py
Author: Joe
Credit: None
Assignment:
Your program will ask the user the following questions, in this order:
1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").
If the user's birthday fell on October 31, then respond with:
  You were born on Halloween!
If the user's birthday fell on today's date, then respond with:
  Happy birthday!
Otherwise respond with a statement like this:
  Peter, you are a winter baby of the nineties.
Example Session
  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaymonth = month_name[todaymonth].lower()
todaydate = datetime.today().day
name = input("Hello, what is your name? ")
month = input("Hi " + name + ", what was the name of the month you were born in? ").lower()
year = int(input("And what year were you born in, " + name + "? "))
Day = int(input("And the day? "))
if month == todaymonth and Day == todaydate:
    print("Happy birthday!")
elif month == "january" and year < 1980:
    print("" + name + ", you are a Winter baby of the stone age.")
elif month == "october" and Day == 31:
    print("You were born on Halloween!")
elif month == "february" and year < 1980:
    print("" + name + ", you are a Winter baby of the stone age.")
elif month == "march" and year < 1980:
    print("" + name + ", you are a Spring baby of the stone age.")
elif month == "april" and year < 1980:
    print("" + name + ", you are a Spring baby of the stone age.")
elif month == "may" and year < 1980:
    print("" + name + ", you are a Spring baby of the stone age.")
elif month == "june" and year < 1980:
    print("" + name + ", you are a Summer baby of the stone age.")
elif month == "july" and year < 1980:
    print("" + name + ", you are a Summer baby of the stone age.")
elif month == "august" and year < 1980:
    print("" + name + ", you are a Summer baby of the stone age.")
elif month == "september" and year < 1980:
    print("" + name + ", you are a Fall baby of the stone age.")
elif month == "october" and year < 1980:
    print("" + name + ", you are a Fall baby of the stone age.")
elif month == "november" and year < 1980:
    print("" + name + ", you are a Fall baby of the stone age.")
elif month == "december" and year < 1980:
    print("" + name + ", you are a Winter baby of the stone age.")
elif month == "january" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Winter baby of the eighties.")
elif month == "october" and Day == 31:
    print("You were born on Halloween!")
elif month == "february" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Winter baby of the eighties.")
elif month == "march" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Spring baby of the eighties.")
elif month == "april" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Spring baby of the eighties.")
elif month == "may" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Spring baby of the eighties.")
elif month == "june" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Summer baby of the eighties.")
elif month == "july" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Summer baby of the eighties.")
elif month == "august" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Summer baby of the eighties.")
elif month == "september" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Fall baby of the eighties.")
elif month == "october" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Fall baby of the eighties.")
elif month == "november" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Fall baby of the eighties.")
elif month == "december" and year > 1980 and year <= 1989:
    print("" + name + ", you are a Winter baby of the eighties.")
elif month == "january" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Winter baby of the nineties.")
elif month == "october" and Day == 31:
    print("You were born on Halloween!")
elif month == "february" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Winter baby of the nineties.")
elif month == "march" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Spring baby of the nineties.")
elif month == "april" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Spring baby of the nineties.")
elif month == "may" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Spring baby of the nineties.")
elif month == "june" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Summer baby of the nineties.")
elif month == "july" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Summer baby of the nineties.")
elif month == "august" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Summer baby of the nineties.")
elif month == "september" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Fall baby of the nineties.")
elif month == "october" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Fall baby of the nineties.")
elif month == "november" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Fall baby of the nineties.")
elif month == "december" and year > 1990 and year <= 1999:
    print("" + name + ", you are a Winter baby of the nineties.")
elif month == "january" and year >= 2000:
    print("" + name + ", you are a Winter baby of the 2000s.")
elif month == "october" and Day == 31:
    print("You were born on Halloween!")
elif month == "february" and year >= 2000:
    print("" + name + ", you are a Winter baby of the 2000s.")
elif month == "march" and year >= 2000:
    print("" + name + ", you are a Spring baby of the 2000s.")
elif month == "april" and year >= 2000:
    print("" + name + ", you are a Spring baby of the 2000s.")
elif month == "may" and year >= 2000:
    print("" + name + ", you are a Spring baby of the 2000s.")
elif month == "june" and year >= 2000:
    print("" + name + ", you are a Summer baby of the 2000s.")
elif month == "july" and year >= 2000:
    print("" + name + ", you are a Summer baby of the 2000s.")
elif month == "august" and year >= 2000:
    print("" + name + ", you are a Summer baby of the 2000s.")
elif month == "september" and year >= 2000:
    print("" + name + ", you are a Fall baby of the 2000s.")
elif month == "october" and year >= 2000:
    print("" + name + ", you are a Fall baby of the 2000s.")
elif month == "november" and year >= 2000:
    print("" + name + ", you are a Fall baby of the 2000s.")
elif month == "december" and year >= 2000:
    print("" + name + ", you are a Winter baby of the 2000s.")
elif month == "october" and Day == 31:
    print("You were born on Halloween!")
