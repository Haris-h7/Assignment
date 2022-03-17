
def non_repeating_string_fast(sample_string):
    string_list = list(sample_string)
    non_repetitive_char = next((ele for ele in string_list if string_list.count(ele)==1))
    return non_repetitive_char



print(non_repeating_string_fast("adjebdedbekfrnkfznuwbdwkd"))

