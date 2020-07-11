#Write your function here
def every_three_nums(start):
  empty = []
  notempty = list(range(start, 101, 3))
  if start > 100:
    return empty
  else:
    return notempty


print(every_three_nums(91))


#Create a function named remove_middle which has three parameters named lst, start, and end.

#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.

#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

def remove_middle(lst,start,end):
  return lst[:start] + lst[end + 1:]


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))




#Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

#Return either item1 or item2 depending on which item appears more often in lst.

#If the two items appear the same number of times, return item1.


def more_frequent_item(lst,item1,item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))




#Create a function named double_index that has two parameters: a list named lst and a single number named index.

#The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.

#If index is not a valid index, the function should return the original list.

#For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

#double_index([1, 2, 3, 4], 2)
#After writing your function, un-comment the call to the function that we’ve provided for you to test your results.


def double_index(lst, index):
  if index >=len(lst):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst  

print(double_index([3, 8, -10, 12], 2))




#Create a function called middle_element that has one parameter named lst.

#If there are an odd number of elements in lst, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
  if len(lst) % 2 == 0:
    return (lst[int(len(lst) / 2 )] + lst[int(len(lst) / 2 ) - 1]) / 2
  else:
    return lst[int(len(lst) / 2)]

print(middle_element([5, 2, -10, -4, 4, 5]))















