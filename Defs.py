

def long_words_list_collector(description_text):
    long_words_list_in_def = []
    for word in description_text:
        word_t = word.title()
        if len(word_t) > 6:
            long_words_list_in_def.append(word_t)
    return long_words_list_in_def
    # список из всех слов всех новостей длиннее 6 символов