#Python Group Assignment

#Answer to Question2
def check_palindrome(text):
    if text == text[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is a palindrome")

# Get User input
User_text = input("Enter a string to check if it's a palindrome")
check_palindrome(User_text)


#Answer to Question3
def combine_and_iterate(text1, text2):
    Combined = text1 + text2
    Char_list = [char for char in Combined]
    return Char_list

# Get User Input
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

# process and display result
result = combine_and_iterate(text1, text2)
print("list of characters from combined text: ", result)
print("Thank you for using my application \n after processing the Input.") 
