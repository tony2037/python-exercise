def translate(arr):
    return_arr=[]
    for tem in arr:
        return_arr.append(str(tem)+'t')
    return return_arr

temperatures=[10,-20,-289,100]
temperatures=translate(temperatures)

for tem in temperatures:
    print(tem)
