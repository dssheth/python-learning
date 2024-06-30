# tuple..similar to lists but cannot modify....use () but not necessary
marks = (94, 95 ,98, 95)

# can count the element repeats
 
print (marks.count(95))

# can tell index of element

print (marks.index(98))

# set...similar to tuple...use{}
# set do not have index... thus have random order... cannot define based on index...use only loops
# set stores unique values so repeated values are not printed

marks = {92, 96, 94, 93, 92, 93}

for score in marks:
    print(score)