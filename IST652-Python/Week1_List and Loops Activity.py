# -----------------------------------------------------------------------------------
# Title: 1.5 List and Loops Activity
# Name: Sathish Kumar Rajendiran
# Date: 06/29/2020
# -----------------------------------------------------------------------------------
# Exercise:
#         List and Loops Activity

# Exercise 1:

Samples = ['at', 'book', 'catch', 'dog', 'elephant', 'famous', 'girl', 'he', 'india', 'joey']
print('\nExercise 1: Results')
for elem in Samples:
    if len(elem) > 2:
        print('Label[', Samples.index(elem), '] is', elem)

# Exercise 1: Results
# Label[ 1 ] is book
# Label[ 2 ] is catch
# Label[ 3 ] is dog
# Label[ 4 ] is elephant
# Label[ 5 ] is famous
# Label[ 6 ] is girl
# Label[ 8 ] is india
# Label[ 9 ] is joey


# Exercise 2:
print('\nExercise 2:Results')
Samples = ['at', '‘book’', 'catch', 'dog', 'elephant', 'famous', 'girl', 'he', 'india', 'joey']
for elem in Samples:
    if 2 < len(elem) < 5:
        print('Label[', Samples.index(elem), '] is', elem)

# Exercise 2:Results
# Label[ 3 ] is dog
# Label[ 6 ] is girl
# Label[ 9 ] is joey
