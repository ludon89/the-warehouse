'''
##########
# PART 1 #
##########
'''

# Retrieving data from txt file and storing it in a list/array
def convert_txt_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()

    return data

file_path = "input.txt"
box_ids = convert_txt_file(file_path)

# Array of IDs
ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]


# Checking if there are duplicate letters in an ID
def check_duplicate_letters(id):
    # An object/dict stores the amount of occurrences for each letter (key-value pairs)
    letter_counter = {}

    # A counter iterates through each string in the array/list and counts how many times a letter appears in a single string
    for letter in id:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1

    # Return true if any letter appears exactly twice
    for letter, count in letter_counter.items():
        if count == 2:
            return True

    return False

# Checking if there are triplicate letters in an ID
def check_triplicate_letters(id):
    letter_counter = {}

    for letter in id:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1

    for letter, count in letter_counter.items():
        if count == 3:
            return True

    return False


# Store IDs where a letter appears exactly twice in an array
duplicates_result = []
for id in box_ids:
    if check_duplicate_letters(id):
        duplicates_result.append(id)

# Count the amount of IDs where a letter appears exactly twice
duplicates_amount = len(duplicates_result)

# Store IDs where a letter appears exactly three times in another array
triplicates_result = []
for id in box_ids:
    if check_triplicate_letters(id):
        triplicates_result.append(id)

# Count the amount of IDs where a letter appears exactly three times
triplicates_amount = len(triplicates_result)

# Calculate the checksum
checksum = duplicates_amount * triplicates_amount


# print("IDs with duplicate letters:", duplicates_result)
# print("IDs with triplicate letters:", triplicates_result)

print("Number of IDs with duplicate letters:", duplicates_amount)
print("Number of IDs with triplicate letters:", triplicates_amount)

print("The checksum is:", checksum)



'''
##########
# PART 2 #
##########
'''

# Checking the Hamming distance between two strings of equal length
# (number of positions in two strings where the corresponding symbols are different)
def hamming_distance(string1: str, string2: str) -> int:
    if len(string1) != len(string2):
        raise ValueError("Strings must be of equal length.")
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
    return dist_counter

# Returning the strings whose Hamming distance is equal to 1
# (they differ by exactly one character in the same position)
def strings_hamming_one(string_list):
    result = []
    length = len(string_list[0])
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if hamming_distance(string_list[i], string_list[j]) == 1:
                result.append(string_list[i])
                result.append(string_list[j])
    return result

# Finding the common letters between two strings
def find_common_letters(string1, string2):
    if len(string1) != len(string2):
        raise ValueError("Strings must be of equal length.")
    common_letters = set(string1) & set(string2)
    return list(common_letters)


# Find the two boxes with robot parts in them
robot_boxes_ids = strings_hamming_one(box_ids)
robot_boxes_ids_str = ", ".join(robot_boxes_ids)
print ("The IDs of the two boxes with robot parts are:", robot_boxes_ids_str)

# Find the common letters between the two box IDs
robot_boxes_common_letters = find_common_letters(robot_boxes_ids[0], robot_boxes_ids[1])
robot_boxes_common_letters_str = ", ".join(robot_boxes_common_letters)
print ("The common letters between the two box IDs are:", robot_boxes_common_letters_str)