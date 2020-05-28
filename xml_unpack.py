
from collections import Counter
import xml.etree.ElementTree as ET
from Json_unpack import long_words_list_collector #Вроде бы правильно импорт выполнен


# def long_words_list_collector(description_text):
#     for word in description_text:
#         word_t = word.title()
#         if len(word_t) >= 6:
#             long_words_list.append(word_t)
#     return long_words_list



if __name__ == "__main__":
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    news = root.findall('channel/item')
    long_words_list = []
    for item in news:
        description_text = item.find('description').text.strip().split(' ')
        long_words_list_collector(description_text)
        '''
        Функция отрабатывает с ошибкой: "NameError: name 'long_words_list' is not defined"
        Если в файле стоим ммылка импортом, а не явно описана функция (незакоментирована)
        '''

    long_words_dict = Counter(long_words_list)
    top_ten = list(reversed(sorted(long_words_dict.values())))[:10]
    print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
    [print(value, key) for key, value in long_words_dict.items() if value >= top_ten[-1]]

