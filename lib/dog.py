#!/usr/bin/env python3

    # Remember that all methods use "self." We'll elaborate on this in a moment.
class Dog:
    def __init__(self, name, breed='Mutt'):
        self.name = name
        self.breed = breed

fido = Dog('Fido', "golden")
print(fido.name, fido.breed)


# class Dog:
#     def __init__(self, name, favorite_toy='Any'):
#         self.name = name
#         self.favorite_toy = favorite_toy

#     def bark(self):
#         print("Woof!")

#     def get_adopted(self, owner_name):
#         self.owner = owner_name
#     def go_walk(self, walker_name):
#         self.walker = walker_name
    
# fido = Dog('Fido', 'Doll')
# fido.get_adopted('Tyler')
# print(fido.owner)
# print(fido.favorite_toy)
# fido.go_walk('YUki')
# print(fido.walker)
# snoopy=Dog('Snoopy')
