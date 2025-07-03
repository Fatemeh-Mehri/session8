from validator import *



class Account :

    def __init__(self,id,Name,Family,amount,Account_type,creation_date, Status): # noqa
        self.id = id
        self.Name = Name
        self.Family = Family
        self.amount = amount
        self.Account_type = Account_type
        self.creation_date = creation_date
        self. Status =  Status

    def validate(self):
        return account_validator(self)

    def to_tuple(self):
        return (self.id, self.Family, self.amount, self.Account_type, self.creation_date, self. Status) # noqa