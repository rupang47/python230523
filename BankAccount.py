# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화
    def __init__(self, id, name, balance):
        #멤버숨김 : __변수명
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        self.__balance += amount 
    #지급
    def withdraw(self, amount):
        self.__balance -= amount
    #문자열의 결과를 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#print(account1.__balance)
#백도어(약간 테스트 용도로만)
print(account1._BankAccount__balance)