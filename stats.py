

# returns the number of words in a string
def get_num_words(text):
    words = text.split()
    num_words = 0

    for word in words:
        num_words += 1

    return num_words


# takes a string as input
# and returns a dictionary with the number of times each character appears
def get_char_count(text):
    char_count = {}

    for word in text.lower():

        for char in word.split():

            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


# function that takes a dict as input
# and returns the value of the key "values"
# used for the sort method key parameter below
def sort_on(dict):
    return dict["value"]


# takes a dict as input
# returns a sorted list of dict
def sorted_dict(dict):
    sorted_list = []

    for key, value in dict.items():
        new_dict = {"char": key, "value": value}
        sorted_list.append(new_dict)

    # !! sort before returning !!
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
