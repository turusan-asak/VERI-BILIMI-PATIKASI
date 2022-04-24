# Patika Veri Analizi Patikası Python Temel dersi sonu proje ödevi

# Task 1

input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list= []

def flatten(a):
    for i in a:
        if isinstance(i,list):
                flatten(i)
        else:
                flatten_list.append(i)
flatten(input1)
print(flatten_list)

#Task 2

input2=[[1, 2], [3, 4], [5, 6, 7]]
reversed_list =[]

def reverse(a):
    a.reverse()
    for i in a:
        if  isinstance(i,list):
            i.reverse()
            reversed_list.append(i)

reverse(input2)
print(reversed_list)
