from datetime import date
import time
import math 
# (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)


def calculate_end_of_year():
    today = date.today()

    end_of_year = date(today.year, 12, 31)
    remaining = end_of_year - today
    print(f"Days left: {remaining.days}")


def main():
    now = time.localtime() 
    print(time.strftime("%Y - %m - %d", now)) 
    print(time.strftime("%H:%M:%S", now))
    print(time.strftime("%Y", now))

    #birth_from_year = int(time.strftime("%Y", now)) 

    # date_birth = int(input("enter your birth year: "))
    #yearsOld = birth_from_year - date_birth 
    #print(f"you are {yearsOld} years old.")

    calculate_end_of_year()
    today = time.strftime("%A", now)
    if today == "Friday" or today == "Saturday":
        print("today is weekend")
    else:
        print("today is not a weekend")


if __name__ == "__main__":
    main()