#In Python, square brackets ( [] ) indicate a list, and individual elements in the list are separated by commas
friend = ['Aniket','Chirag','Devarshi','Sagar']
print(friend)

#To access an element in a list, write the name of the list followed by the index of the item in [ ]
print("friend at position 2 ",friend[2])

#for accessing the last element in a list use -1 as index
print("friend at position -1 ",friend[-1])

#The index - 2 returns the second item from the end of the list
print("friend at position -2 ",friend[-2])

#To change value of item in list
friend[1] = 'Rahul'
print("New friend list after changing value ",friend)

#to add a new element to a list is to append the item to the list.
friend.append('Chirag')
print("New friend list after appending value ",friend)

#To add a new element at any position in list
friend.insert(3,'Gaurav')
print("New friend list after inserting value ",friend)

#To sort a list we use sort() function in ascending order
friend.sort()
print("Friend list after sort ascending order",friend)

#To sort list in reverse alphabetical order use sort(reverse=True) method
friend.sort(reverse=True)
print("Friend list after sort in descending order",friend)

#The sorted() function display list in a sorted order but doesn’t affect the actual order of the list
print("Friend List in sorted order",sorted(friend))
print("Friend list in original order",friend)

#To remove an item or a set of items from a list.
friend.remove('Gaurav')
print("Friend list after removing value ",friend)

#If you know the position of the item you want to remove from a list
del friend[1]
print("Friend list after deleting value ",friend)

#The pop() method removes the last item in a list
pop_item = friend.pop()
print("Pop value",pop_item)
print("Friend list after pop ",friend)

#To remove an item in a list at any position
pop_item = friend.pop(2)
print("Pop value by using position",pop_item)
print("Friend list after pop ",friend)

#To reverse the original order of a list
friend.reverse()
print("Friend list in reverse order ",friend)

#To find the length of a list
print("Lenght of Friend list is",len(friend))

#Creating List using range() function
numbers = list(range(5))
print("List using range function",numbers)

#maximum, minimum, addition of list
print("Maximum number in list",min(numbers))
print("Minimum number in list",max(numbers))
print("Addition of number in list",sum(numbers))

#You can generate any subset of a list.
print("Slicing list")
print(numbers[1:3])
print(numbers[ :4])
print(numbers[2:])
print(numbers[ : :-1])
print(numbers[1: :-1])

