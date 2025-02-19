text = "Hello this is 234 paul"

text_analysis = {}
lower_text = text.lower()
for char in lower_text:
    if char in text_analysis:
        i = text_analysis[char]
        i += 1
    else:
        i = 1
    text_analysis[char] = i



def remove_numeric_string_keys(d):
    keys_to_remove = [key for key in d if not key.isalpha() or key == '']
    for key in keys_to_remove:
        del d[key]
    return d
    
    
just_letters = remove_numeric_string_keys(text_analysis)

for c in just_letters:
    print(f"The '{c}' charcter was found {just_letters[c]} times")



print(just_letters)




