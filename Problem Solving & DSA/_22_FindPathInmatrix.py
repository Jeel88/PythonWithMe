def paths(list1,i=0,j=0):
    result=0
    if(i>=len(list1) or j>=len(list1)):
        return 0
    
    if(i==len(list1)-1 and j == len(list1)-1):
        return 1

    rightside=paths(list1,i+1,j)
    downside=paths(list1,i,j+1)
    return rightside+downside


list1=[[1,2,3],[4,5,6],[7,8,9]]
print(paths(list1))