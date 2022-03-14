import pickle

class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color

class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

mary = Sheep("white")
joni = Sheep("black")

print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))
my_pickled_mary = pickle.dumps(mary)

print ("Would you like to see her pickled? Here she is!")
print (my_pickled_mary)

unpickled_mary = pickle.loads(my_pickled_mary)
print(str.format("Mary is {0} and has {1} paws", unpickled_mary.color, unpickled_mary.number_of_paws))