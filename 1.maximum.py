def greatest(x,y,z):
    maximum = x

    if y > maximum:
        maximum = y

    if z > maximum:
        maximum = z

    return maximum

a = int(input("Enter 1st integer:") ) #enter 1st number
b = int(input("Enter 2nd integer:") ) #enter 2nd number
c = int(input("Enter 3rd integer:") ) #enter 3rd number

print ("Greatest integer is:", greatest(a,b,c)) #invoke greatest function to compare greatest among 3 inputed number