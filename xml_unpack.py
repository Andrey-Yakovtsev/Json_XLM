
from collections import Counter
import xml.etree.ElementTree as ET
from Json_unpack import long_words_list_collector




if __name__ == "__main__":
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    news = root.findall('channel/item')
    long_words_list = []
    max_list = []
    most_frequent_words = {}
    for item in news:
        description_text = item.find('description').text.strip().split(' ')
        max_list.extend(long_words_list_collector(description_text))  # добавляем список слов из одной новости к списку другой новости
        long_words_dict = Counter(max_list)  # посчитали кол-во вхождений в списке
    print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
    [print(value, key) for key, value in long_words_dict.items() if value >= (sorted(long_words_dict.values())[-10])]


