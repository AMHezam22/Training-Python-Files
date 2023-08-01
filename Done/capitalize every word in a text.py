def capitalize_each_word(original_str):
    result = ""
    # Split the string and get all words in l list
    list_of_words = original_str.split()
    # Iterate over all elements in list
    for elem in list_of_words:
        # capitalize first letter of each word and add to l string
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
    # If result is still empty then return original string else returned capitalized.
    if not result:
        return original_str
    else:
        return result


sample_text = "33a. it's GONE too far"
result = capitalize_each_word(sample_text)
print(result)

def to_jaden_case(string):
    # a = string.split()
    # saying = ""
    # for word in a:
    #     saying = saying + " " + word.capitalize()
    # return saying
    return " ".join(list(map(str.capitalize,string.split())))
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

