class Bank_Account:
    def __init__(self, name,DOB, balance):
        self.name = name  ## public
        self._DOB = DOB ## protected
        self.__balance = balance ## private
        
    ## To access private variables we use getter and setter methods
    def get_balance(self):
        return self.__balance
    def set_balance(self, new_balance):
        self.__balance = new_balance

acc_1 = Bank_Account("Haseeb", 4-11-2006, 40_000)
print(acc_1.get_balance())