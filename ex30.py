# Title: Check whether a specified value is contained in a group of values
# This program checks whether a specified value is contained within a group of values.

# Test Data:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def checkData(group_data,n):
    for x in group_data:
        if x == n:
            return True
    return False

print(checkData([1,5,8,3],3))    
print(checkData([1,5,8,3],-1))    
    