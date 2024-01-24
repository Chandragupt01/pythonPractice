#Use a loop to display elements from a given list present at odd index positions
'''Use a loop to display elements from a given list present at odd index positions'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for num in range(1,len(my_list)+1,2): # or for i in my_list[1::2]: --> print(i)
    print(my_list[num])
