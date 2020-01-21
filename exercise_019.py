import random
st1 = str(input('Type the student name 1: '))
st2 = str(input('Type the student name 2: '))
st3 = str(input('Type the student name 3: '))
st4 = str(input('Type the student name 4: '))
list1 = [st1, st2, st3, st4]
chosen = random.choice(list1)
print(f'The student chosen was {chosen}!')