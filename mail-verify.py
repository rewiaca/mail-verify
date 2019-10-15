from validate_email import validate_email



def check(email):
    if email is list:
        emails = email
        i = 0
        goods = []
        for email in emails:
            status = str(validate_email(email, verify=True))
            if status == "True":
                goods.append(email)
                print(email + ' status: ' + status)
    else:
        return str(validate_email(email, verify=True))





email = input('Enter email OR use list[L]: ')

if email == "L":
    path = input('Enter path to list: ')
    f = open(path, 'r', errors='replace')
    emails = f.readlines()

    check(emails)
else:
    print(check(email))


