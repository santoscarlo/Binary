def decimal_to_binary(number):
    binary_list = [] # make sure empty number
    old_number = number # Reference number
    while(number >.5): #loop
        if number % 2 != 0: #if the number is .5
            binary_list.append(1)
        else:
            binary_list.append(0)
        number /=2 # set the number to the new number
        number = int(number)
        print(binary_list)
        print()
        print("the binary " + str(old_number)+ "is")
        print(binary_list[::-1]) # print the list to show correctly
def main():
    switch = 0
    while(switch == 0):
        number = int(input("please input a decimal:"))
        decimal_to_binary(number)# calls our funcction
        print()
        
main()
            
                
                
        
