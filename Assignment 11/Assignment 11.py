#Taking input from user
string = input("Enter a string : ")

#Initializing the variable 'vowelcount' with zero which will keep a track of all the vowels in the entered string
vowelcount = 0
       
#Making the entered string in lowercase
string = string.lower()
    
#Starting a 'for' loop which will run from char to string    
for char in string:
        
    #Checking the character to be a vowel
    if char in 'aeiou':

        #Increasing 'vowelcount' by 1 if the character is a vowel
        vowelcount += 1
    
#Printing the result
print("Number of vowels in the string:", vowelcount)
