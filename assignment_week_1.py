#1. Type casting problem

#Asking user to enter a number 
decimal_num= float(input("Enter a number: "))
original_num_type= type(decimal_num)
print(f"Original Number: {decimal_num} with type {original_num_type}")

#type casting
converted_int= int(decimal_num)
int_num_type= type(converted_int)
print(f"Converted to int: {converted_int} with type {int_num_type}")

converted_string= str(decimal_num)
str_num_type= type(converted_string)
print(f"Converted to string:'{converted_string}' with type {str_num_type}")

#2. SLicing Initials
#asking for name
name = input("Enter your full name: ").strip()

# spliting the name into words
words = name.split()  # Split the name into words
initials = "".join(word[:1] for word in words) 

#printing and capitalizing the intials
print(f"Your initials are: {initials.upper()}")


#3.String slicing to reverse

#asking for a string
string = input("Enter a word: ")

#using sliceing to reverse
reverse = string[::-1]

print(string)
print(reverse)
