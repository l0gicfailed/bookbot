#count the number of words

def get_num_words(words):
    return len(words)

#counts letters
def count_letters(text):

    #take input of text and return a dictonary of letter counts
    letter_counts = {}
    lowercase_text = text.lower()
    for letter in lowercase_text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

#sort the letter count by greatest to least

def sort_letter_count(letter_counts):
    def sort_on(items):
        return items["num"]

    report_list = []

    for key, value in letter_counts.items():
        report_dict = {"char": key, "num": value}
        report_list.append(report_dict)

    report_list.sort(reverse=True, key=sort_on)
    
    return report_list
        
