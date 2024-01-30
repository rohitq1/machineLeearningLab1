
import numpy as np

def range_difference(list1):
    list_length=len(list1)
    if list_length<3:
        # checks for the len if less than 3 elements
        return f"Range determination not possible with less than {list_length} elements"
    else:
    #   finding the maxi and mini elements
      maximum_element=max(list1)
      minimum_element=min(list1)
    #   calculating the absolute differnce
      absolute_value=maximum_element-minimum_element
      return f" the range is {absolute_value}"
    
def count_sum(list1,target):
    # for storing the pairs counts
    count_pairs=0
    #  i pointer starting from first index 
    for i in range(len(list1)):
        #  j pointer starting from secong index 
        for j in range(i+1,len(list1)):
            # checking if sum is equal or nt
            if list1[i]+list1[j]==target:
                count_pairs+=1
    return count_pairs

def occured_char(string):
    char_count={}
    count_charecter=0
    most_occured_char=''
    max_count=0
    # picking up individual char
    for char in string:
        # if already there then add it up by 1 sicne dictionary at that key
        if char in char_count:
            char_count[char]+=1
        else:
        #    if new char is found inital to 1 
           char_count[char]=1
        # checking for max count
        if char_count[char]>max_count:
            max_count=char_count[char]
            most_occured_char=char
    return max_count,most_occured_char


def multi_power(a,m):
    #  as a is list of list and numpy uses array for its operation
    a_matrix=np.array(a)
 # matrix_power  is a inbuilt func in scipy and numpy for matrix power
    return np.linalg.matrix_power(a_matrix,m)


print(range_difference([5,3,8,1,0,4]))
print(count_sum([2,7,4,1,3,6],10))
print(occured_char("hippopotamus"))
print(multi_power([[1,1],[2,1]],2))
