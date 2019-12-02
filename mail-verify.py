from validate_email import validate_email
import os
import sys


def check(email):
    if isinstance(email, list):
        emails = email
        i = 0
        goods = []

        for email in emails:
            email=email.replace("\n","")
            print("Checking " + email)
            status = validate_email(email, verify=True)
            if status:
                goods.append(email)
                print(str(status))
            else:
                print(status)
                
        return print(goods)
    else:
        return "Exist" if validate_email(email, verify=True) else "Not exist"
    


if  len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]} - {check(sys.argv[i])}")
    sys.exit()
email = input('Enter email OR use list[L]: ')

if email == "L":
    path = input('Enter path to list: ')
    f = open(path, 'r', errors='replace')
    emails = f.readlines()

    check(emails)
    
else:
    print(check(email))


