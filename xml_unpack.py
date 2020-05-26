
from collections import Counter
import xml.etree.ElementTree as ET

long_words_list = []
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
news = root.findall('channel/item')
for item in news:
    description_text = item.find('description').text.strip().split(' ')
    for word in description_text:
        if len(word) >= 6:
            long_words_list.append(word)

long_words_dict = Counter(long_words_list)
top_ten = list(reversed(sorted(long_words_dict.values())))[:10]
print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
[print(value, key) for key, value in long_words_dict.items() if value >= top_ten[-1]]

