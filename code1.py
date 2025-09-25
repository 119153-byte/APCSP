
#declares the variable name x to be equal to the string hello world
x = "Hello World"

#declares variable count1 and assigns it an integer value of 17
count1 = 1 

# define a function named Hello
def Hello():
    global count1
    while count1 >= 10:
        count1 += 1
        print(x)
        break

Hello()

        
