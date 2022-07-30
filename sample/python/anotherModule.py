from mymodule import Student, Game

s1 = Student("Luning")
s1.greeting('Haoning')
s1.greeting('Andy')

g1 = Game('boxel')
s1.play(g1)

s1.pauseGame(g1)

ls = ['a', 'b', 'c']
print(ls[0])
print(ls[0:1])
ls[0:1] = 'mn'
print(ls)

a = 3
if a == 1:
    b = 3
elif a == 2:
    b = 2
else:
    b = 1

a = 1
while a < 3:
    b = b + 1
    a = a + 1

for a in range(6):
    print(a)


steps = [
    {
        'step': 1,
        'object': 'MotorPair',
        'params': 'A, E',
        'action': 'start',
        'position': 0
    },
    {
        'step': 1,
        'object': 'MotorPair',
        'params': 'A, E',
        'action': 'move',
        'distance': 15,
        'speed': -10
    }
]

[
    {
        'object': 'tea',
        'begin': 7,
        'end': 4
    },
    {
        'object': 'tea',
        'begin': 4,
        'end': 2
    },
    {
        'object': 'tea',
        'begin': 2,
        'end': 0.5
    }
]