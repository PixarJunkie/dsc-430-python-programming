#Kyle Chinn 9/24/2018 I have not given or received any unauthorized assistance on this assignment.  

sq1 = [1, 0, 2]
sq2 = [2, 1, 5]
sq3 = [4, 3, 1]
sq4 = [1, 5, 3]
sq5 = [6, 4, -3]
sq6 = [6, 4, 'three']

def min_max(lst):
    x_max = lst[0] + lst[2] 
    x_min = lst[0]
    y_max = lst[1] + lst[2]
    y_min = lst[1]
    return [x_max, x_min, y_max, y_min]

#Part A
print('Part A with test lists [1, 2, 3] and [1, 2, "a"]')

#Test lists
lst_1 = [1, 2, 3]
lst_2 = [1, 2, 'a']

#Check list length and type
def list_check(lst):
    if len(lst) != 3:
        print(str(lst) + ' ' + 'is not a valid list')
        return False
    try:
        if any(str(x).isdigit() == False for x in lst):
            print('')
            print(str(lst) + ' ' + 'is not a valid list')
            return False
        else:
            print('')
            print(str(lst) + ' ' + 'is a valid list')
            return True
    except ValueError:
        print('')
        print(str(lst) + ' ' + 'is not a valid list')
        return False

print(list_check(lst_1))
print(list_check(lst_2))

#Part B
print('')
print('Part B with test squares [1, 2, 3] and [1, 2, -1]')
print('')

#Test squares
lst_1 = [1, 2, 3]
lst_2 = [1, 2, -1]

#Valid square
def valid_square(square):
    try:
        if list_check(square) == True and square[2] > 0:
            print(str(square) + ' ' + 'is a valid square')
            return True
        print(str(square) + ' ' + 'is not a valid square')
        return False
    except TypeError: 
        return False

print(valid_square(lst_1))
print('')
print(valid_square(lst_2))
print('')

#Part C
print('Part C with test squares [1, 2, 3] and [4, 6, -2]')

#Test squares
lst_1 = [1, 2, 3]
lst_2 = [4, 6, -2]

#Perimeter 
def perim(square):
    if valid_square(square) == True:
        return 4 * square[2]
    return -1

print('The perimeter of [1, 2, 3] =' + ' ' + str(perim(lst_1)))
print(perim(lst_2))
print('')

#Part D
print('Part C with test squares [1, 2, 3] and [4, 6, -2]')
print('')

#Test squares
lst_1 = [1, 2, 3]
lst_2 = [4, 6, -2]

#Area
def area(square):
    if valid_square(square) == True:
        return square[2] ** 2
    return -1 

print('The area of [1, 2, 3] =' + ' ' + str(area(lst_1)))
print('')
print(area(lst_2))
print('')

#Part E
print('Part E - overlap function (did not print the whole function. Refer to p_2.py #Part E for the code')
print('')

#Overlap area

#min_max fucntion
def min_max(lst):
    x_max = lst[0] + lst[2] 
    x_min = lst[0]
    y_max = lst[1] + lst[2]
    y_min = lst[1]
    return [x_max, x_min, y_max, y_min]

def overlap(square_1, square_2):
    if valid_square(square_1) == True and valid_square(square_2) == True:
        square_1_mm = min_max(square_1)
        square_2_mm = min_max(square_2)
        x = min(square_1_mm[0], square_2_mm[0]) - max(square_1_mm[1], square_2_mm[1])
        y = min(square_1_mm[2], square_2_mm[2]) - max(square_2_mm[3], square_2_mm[3])
        if x <= 0 or y <= 0:
            return -1
        else:
            print('The overlap of ' + str(square_1) + ' and ' + str(square_2) + ' is ' + str(x * y))
            return abs(x * y)
    else:
        print('Cannot calulate overlap')
        return -1

#Part F
print('Part F')
overlap(sq1,sq2)
overlap(sq2,sq3)
overlap(sq2,sq4)
overlap(sq1,sq4)
overlap(sq1,sq5)
overlap(sq1,sq6)


