def num_of_words(content):
    
    list_of_words = content.split()
    word_count = len(list_of_words)

    return word_count

def num_of_each_character(content):
    letters = {}
    list_of_words = content.split()
    for word in list_of_words:
        for letter in word:
            low_letter = letter.lower()
            if low_letter not in letters:
                letters[low_letter] = 1
            else:
                letters[low_letter] += 1
    
    return letters


def sort_dict(dict):
    letter_list = []
    
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        letter_list.append(new_dict)

    def sort_on(items):
        return items["num"]
    
    letter_list.sort(reverse = True, key=sort_on)

    
    return letter_list
        

