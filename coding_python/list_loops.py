# make list
marks = [93,96,99]
print (marks) #... all 3 marks are printed

print (marks[0]) #add [] to add index of particular element of list to print

# negative index also possible...[-1] it starts from backwards 
print (marks [-1]) # it will print last number 99..if -2...96

# to print a range of numbers from particular indexes...add starting index:end index
print ((marks [0:2])) # it will not count index 2 for print 

# for loop...display all marks as individual product of loop
for score in marks:
    print (score)

# to add new element in list at end
marks.append (100)
print (marks)

# to insert element in between of list...add index number and element
marks.insert (0,90)
print (marks)

# to check if any element exists in list
print (93 in marks)
print (94 in marks)

# to measure length of list
print (len(marks))

# while loop
i = 0 
while i < len(marks):
    print (marks[i])
    i = i + 1

# to clear the list
marks.clear()
print (marks)