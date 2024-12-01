# get string from the user
user = input("enter the string:")

#using set initial the vowels
vowels = {'a','e','i','o','u','A','E','I','O','U'}

count = 0 #initilize count

# create c put vowels in c 
for c in vowels : 
    # create i put user in i
    for i in user:
        #check if the string are same increase +1
        if c==i:
            #+1 <-- that is this
            count +=1


print(count,"vowels in the user input")
