# -*- coding: utf-8 -*-

class Person:

    # attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def whoAmI(self):
        print("I am Person Class")
    
    def sining(self, song):
        return "{} {}을/를 노래합니다.".format(self.name, song)

    def dancing(self):
        return "{} 현재 춤을 춘다.".format(self.name)

class Korean(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        print("Korean Class is ready!")

    def whoAmI(self):
        print("I am Korean Class")

    def study(self):
        print("Fast Runner")

class Japanese(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def whoAmI(self):
        print("I am Japanese")

    def lying(self):
        print("I am a liar!!")

    def study(self):
        print("한국애들보다 공부 더 잘함")

# Series DataFrame 다른 클래스

if __name__=="__main__":
    # kim = Person("Kim", 30)
    # kim.whoAmI()
    # print(kim.dancing())
    # print(kim.sining("000"))

    #a = Korean("kor_Kim", 20)
    #print(kor_kim.sining("000"))
    #a = Japanese("A", 20)

    # 아래 두개는 Japan 클래스
    a.whoAmI()
    a.lying()

    # Person 클래스
    print(a.dancing())
    a.study()







