# OOP

class PlayerCharacter:

    def __init__(self, name, age):
        if (age > 18):
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Reddy', num1 + num2)


    @staticmethod
    def adding_things2(num1, num2):
        return (num1 + num2)

    # Class Ojbect Attribute
    membership = True


player1 = PlayerCharacter('Chandra', 40)
player2 = PlayerCharacter('Shekar', 40)
player3 = PlayerCharacter('Suchi', 30)

# player4 = PlayerCharacter()

print(player1)
print(player1.name)
print(player1.age)
print(player1.run())

print(player2)
print(player2.name)
print(player2.run())

print(player3)
print(player3.name)
print(player3.run())
# help(player1)

print(player1.membership)
print(player2.membership)
print(player3.membership)

player4 = PlayerCharacter.adding_things(20, 3)
# print(player1.adding_things(2, 3))

print(player4.age)


# print(player4.name)
