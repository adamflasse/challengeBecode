#specify each variables that I need 

i = 0
zero = [' _ ', '| |', '|_|', '   ']
one = ['   ', '  |', '  |', '   ']
two = [' _ ', ' _|', '|_ ', '   ']
three = [' _ ', ' _|', ' _|', '   ']
four = ['   ', '|_|', '  |', '   ']
five = [' _ ', '|_ ', ' _|', '   ']
six = [' _ ', '|_ ', '|_|', '   ']
seven = [' _ ', '  |', '  |', '   ']
eight = [' _ ', '|_|', '|_|', '   ']
nine = [' _ ', '|_|', ' _|', '   ']


# go through each line of the file and get every characters each 4 lines and store the value in the variable
""" with open('/Users/adamflasse/Development/python/challenges/assets/numerical_fonts.txt', 'r') as file :
    for row in file:
        i += 1
        if i in range(4):
            zero.append(row.rstrip())
           
        if i in range(5,8):
            one.append(row.rstrip())
            
        if i in range(9,12):
            two.append(row.rstrip())
            
        if i in range(13,16):
            three.append(row.rstrip())
            
        if i in range(17,20):
            four.append(row.rstrip())
            
        if i in range(21,24):
            five.append(row.rstrip())
            
        if i in range(25,28):
            six.append(row.rstrip())
            
        if i in range(29,32):
            seven.append(row.rstrip())
            
        if i in range(33,36):
            eight.append(row.rstrip())
            
        if i in range(37,40):
            nine.append(row.rstrip())
            
# get the blank line for each number
one.append("   ")
two.append("   ")
three.append("   ")
four.append("   ")
five.append("   ")
six.append("   ")
seven.append("   ")
eight.append("   ")
nine.append("   ") """

#checks if the list that we get is okay or not
def check_input(list_to_check):
    if zero == list_to_check:
        return '0'
    elif one == list_to_check:
        return '1'
    elif two == list_to_check:
        return '2'
    elif three == list_to_check:
        return '3'
    elif four == list_to_check:
        return '4'
    elif five == list_to_check:
        return '5'
    elif six == list_to_check:
        return '6'
    elif seven == list_to_check:
        return '7'
    elif eight == list_to_check:
        return '8'
    elif nine == list_to_check:
        return '9'
    else: 
        return '?'


def divide_digits(list_of_digits):
    first_row = []
    second_row = []
    third_row = []
    fourth_row = ['   ']

    result_list =[]
    i = 0
    for element in list_of_digits:
        if len(element) > 3:
            i += 1
            if i == 1:
                for x in range(0,len(element), 3):
                    first_row.append(element[x : x+3])
            if i == 2 :
                for x in range(0,len(element), 3):
                    second_row.append(element[x : x+3])
            if i == 3:
                for x in range(0,len(element), 3):
                    third_row.append(element[x : x+3])
            
        else:
            return check_input(list_of_digits)
    
    for y in range(len(second_row)):
        result_list.append([first_row[y], second_row[y], third_row[y], fourth_row[0]])
    return result_list

test_list = [" _     _  _  _     _  _  _  _ ", " _|  ||_||_ |_ |_|  | _||_|| |", " _|  ||_||_| _|  |  ||_  _||_|", "                              "]
answer_list = divide_digits(test_list)

def get_the_numbers_right(provided_list):
    result_string = ''
    for element in provided_list:
        var = check_input(element)
        result_string += var
    return result_string


print(get_the_numbers_right(answer_list))




            


        
