color = ["red", "green", "blue"]
print('--'.join(color))


#Replace values of variables
a = 10
b = 5
a, b = b, a
print(a)


#Arithmetic operations
#1st priority - exponentiation and root of number
a = 10
b = 3
c = a**b
print(c)
c = c**(1/b)
print(c)


#2nd priority - unary minus
a = 5
b = -a


#3rd priority - Integer division and remainder of division
#=>5*3+(-3)
print(-12//5) #not -2
print(-12%5)  #not -2.


#4th priority - addition and subtraction (plus and minus)
x = 1 + 1
x += 1
x -= 1


#Loop WHILE
while 1 == 1:
    print('one iteration')
    break
    #continue - 'go to start'
else:
    print('Don\'t work if break')


#Loop FOR
for i in range(10, 1, -1): #[10, 1)
    print(i)
    #break
    #continue
else:
    print('Don\'t work if break')