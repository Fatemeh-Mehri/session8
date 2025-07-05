import re

account_type=["kootahmoddat","bolandmoddat","gharzolhasane"]
status_list=["فعال", "عیر فعال"]

def account_validator(account):
    errors = []
    if not (type(account[0]) == int and account[0]>0):
        errors.append('Account ID must be an integer > 0')

    if not (type(account[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", account[1])):
        errors.append('Account Name is Invalid')


    if not (type(account[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", account[2])):
        errors.append('Account Family is Invalid')

    if not (type(account[3]) == int and account[3]>0):
        errors.append(' Account Amount must be an integer > 0')

    if not (type(account[4]) == str and account_type):
        errors.append(' Account Type is invalid!')


    if not (type(account[5]) == int and re.match(r"^[13]\d {2}$", account[5])):
        errors.append(' Account Careation Date is Invalid!')

    if not  status_list:
        errors.append(' Status is invalid!')

    return errors


