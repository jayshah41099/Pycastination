import datetime
import sys

def age_calculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = today.year - dob.year - int((today.month, today.day) < (dob.month, dob.day))
    return age

def main():
    year = int(sys.argv[3])
    month = int(sys.argv[2])
    day = int(sys.argv[1])
    age = age_calculator(year, month, day)
    print(age)

if __name__ == "__main__":
    main()



