#//////////////////////////////////////////////////////////////////////////////////////////

#ASSIGNMENT

# Write a function that takes in a name and returns the amount of variables in the name.

# Write a function that takes a number and tells you if it is odd or even.

# Write a function that takes in a number and returns the factorial of that number.

# Write a function that take a string and reverses it.

# Write a function that takes a string and tells you if it is a palindrome.

#//////////////////////////////////////////////////////////////////////////////////////////


# Question 1 
def number_of_letters(your_name):
    your_name = input("Lets find out how many letters are in your name\n" "Enter your name:")
    print(len(your_name))

number_of_letters(your_name="mike")

# Question 2
def odd_or_even(number):
    number = int(input("Pick a number. I'll tell you if its odd or even. \n" "Enter a number:"))
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

odd_or_even(24)

#Question 3	
def factorial(num):
    num = int(input("I'm really smart. Test me. Enter a number and i'll tell you its factorial \n" "Enter a number:"))
    
    fac = 1
    
    for i in range(1, num + 1):
        fac = fac * i
    
    print("factorial of ", num, " is ", fac)

factorial(4)

#Question 4 
def reverse_it(word):
    word = input("Is it worth it? Lets reverse it.  \n" "Enter a word:")
    print(word[::-1])

reverse_it("Michael")

#Question 5
def palindrome(word):
    word = input("Let's see if you know any palindromes. \n" "Enter a palindrome:")
    if word == word[::-1]:
        print("Yes " + word + " is a palindrome" )
    else: 
        print( word + " is not a palindrome")

palindrome("word")