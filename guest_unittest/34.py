# class Person():
#     def __init__(self,name):
#         self.__name=name
#
#
#     def get_name(self):
#         return self.__name
# P=Person("Ervin")
# P.get_name()
class Animal():
    __location="Asia"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def set_location(cls,location):
        cls.__location=location
    @classmethod
    def get_location(cls):
        return cls.__location
print(Animal.get_location())
Animal.set_location("Afraca")
print(Animal.get_location())