def l1(list1,top,bottom,right,left):
    if(top<=bottom and left<=right):

        for i in range(top,right+1):
            print(list1[top][i])
        for i in range(top+1,bottom+1):
            print(list1[i][right])
        for i in range(right-1,left-1,-1):
            print(list1[bottom][i])
        for j in range(bottom-1,top-1,-1):
            print(list1[j][left])

        l1(list1,top+1,bottom-1,right-1,left+1)
    return 0    

list1=[[1,2,3],[4,5,6],[7,8,9]]
l1(list1,top=0,bottom=len(list1)-1,right=len(list1)-1,left=0)