c = 5

# while c != 0:
#     print(c)
#     c -=1


#explicit is better then implicit - use first option
# while c:
#     print(c)
#     c -=1
    
# how to break out of a While loop
while True:
    response  = input()
    if int(response) %7 ==0:
        print(f"Input  = {response}, this is divisable to 7 therefore program will end ")
        break



