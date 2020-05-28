
import json
from collections import Counter
from Defs import long_words_list_collector #Вроде бы правильно импорт выполнен



def long_words_list_collector(description_text):

    for word in description_text:
        word_t = word.title()
        if len(word_t) >= 6:
            long_words_list.append(word_t)
    return long_words_list

if __name__ == "__main__":

    with open('newsafr.json', encoding='utf-8') as json_file_input:
        json_data = json.load(json_file_input)
        long_words_list = []
        for block in json_data["rss"]["channel"]["items"]:
            description_text = (block['description']).strip().split(' ')
            long_words_list_collector(description_text)
            '''
           Функция отрабатывает с ошибкой: "NameError: name 'long_words_list' is not defined"
           Если в файле стоим ссылка импортом, а не явно описана функция (незакоментирована)
           
           '''
        long_words_dict = Counter(long_words_list)
        top_ten = list(reversed(sorted(long_words_dict.values())))[:10]
    print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
    [print(value, key) for key, value in long_words_dict.items() if value >= top_ten[-1]]





'''
Старая версия - без функции

with open('newsafr.json', encoding='utf-8') as json_file_input:
    json_data = json.load(json_file_input)
    long_words_list = []
    for block in json_data["rss"]["channel"]["items"]:
        description_text = (block['description']).strip().split(' ')
        for word in description_text:
            word_t = word.title()
            if len(word_t) >= 6:
                long_words_list.append(word_t)

    long_words_dict = Counter(long_words_list)
    top_ten = list(reversed(sorted(long_words_dict.values())))[:10]

print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
[print(value, key) for key, value in long_words_dict.items() if value >= top_ten[-1]]
'''