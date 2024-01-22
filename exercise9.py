# check if the number is a palindrome
# define a function with a parameter of a number
def palindrome_checker(num):
    # takes the parameter of a number and create a variable that converted to a string
    converted_num_to_str = str(num)
    # create a variable for reverse number
    reversed_num = converted_num_to_str[::-1]
    # if number and reverse number is same: it is a palindrome number
    if converted_num_to_str == reversed_num:
        print("Given number palindrome")
    # otherwise: its not
    else:
        print('Given number is not palindrome')


palindrome_checker(121) # Given number palindrome
palindrome_checker(125) # Given number is not palindrome