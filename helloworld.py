import datetime

year = int(input("Enter Your Birth Year >>: "))
month = int(input("Enter Your Birth Month >>: "))
day = int(input("Enter Your Birth Day >>: "))

def ageCalc(y, m, d):

    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)

    return age

print("Your age is: " + ageCalc(year, month, day))