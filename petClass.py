def main():

   name = input("What is your pet’s name?: ")
   animal_type = input("What type of animal is your pet?: ")
   age = int(input("How old is your pet?: "))
   pets = Pet(name, animal_type, age)
   print("Pet data:")
   print("Name: ", pets.get_name(name))
   print("Type: ", pets.get_animal_type(type))
   print("Age: ", pets.get_age(age))
class Pet(object):
   def __init__(self, name, animal_type, age):
       self.__name = name
       self.__animal_type = animal_type
       self.__age = age

   def set_name(self, name):
       self.__name = name

   def set_type(self, animal_type):
       self.__animal_type = animal_type

   def set_age(self, age):
       self.__age = age

   def get_name(self, name):
       return self.__name

   def get_animal_type(self, type):
       return self.__animal_type

   def get_age(self, age):
       return self.__age





main()
