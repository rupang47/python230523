# class1.py
#1)클래스 형식
class Person:
    #초기화 메서드
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    def print(self):
        print("My name is {0}" .format(self.name))
        
#2)인스턴스 생성
p1 = Person()

#3)메서드 호출
p1.print()
