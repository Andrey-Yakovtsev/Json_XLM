from pprint import pprint
import json
from collections import Counter
from Defs import long_words_list_collector



if __name__ == "__main__":

    with open('newsafr.json', encoding='utf-8') as json_file_input:
        json_data = json.load(json_file_input)
        long_words_list = []
        max_list = []
        most_frequent_words = {}
        for block in json_data["rss"]["channel"]["items"]:
            description_text = (block['description']).strip().split(' ')
            max_list.extend(long_words_list_collector(description_text)) #добавляем список слов из одной новости к списку другой новости
            long_words_dict = Counter(max_list) #посчитали кол-во вхождений в списке
    print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
    [print(value, key) for key, value in long_words_dict.items() if value >= (sorted(long_words_dict.values())[-10])]






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
# Если в функции defs.py закомментировать long_words_list = [], то
# Функция отрабатывает с ошибкой: Traceback (most recent call last):
#  File "C:/Users/3311/PycharmProjects/Json_XLM/Json_unpack.py", line 23, in <module>
#  long_words_list_collector(description_text)
#  File "C:\Users\3311\PycharmProjects\Json_XLM\Defs.py", line 8, in long_words_list_collector
#  long_words_list.append(word_t)
#  NameError: name 'long_words_list' is not defined
# Если в файле стоим ссылка импортом, а не явно описана функция (незакоментирована)
#
# А если не закомментировать, то похоже, что функция затирает словарь при отрабатывании в цикле For
# Незакомментированная функция в этом же файле отрабатывает правильно без long_words_list = []
