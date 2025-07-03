from validator import *



class Account :

    def __init__(self,Id,Name,Family,Amount,Account_type,Creation_date, Status): # noqa
        self.Id = Id
        self.Name = Name
        self.Family = Family
        self.Amount = Amount
        self.Account_type = Account_type
        self.Creation_date = Creation_date
        self. Status =  Status

    def validate(self):
        return account_validator(self)

    def to_tuple(self):
        return (self.id, self.Family, self.amount, self.Account_type, self.creation_date, self. Status) # noqa