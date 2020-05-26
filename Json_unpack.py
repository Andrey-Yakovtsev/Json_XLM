
import json
from collections import Counter



with open('newsafr.json', encoding='utf-8') as json_file_input:
    json_data = json.load(json_file_input)
    long_words_list = []
    for block in json_data["rss"]["channel"]["items"]:
        description_text = (block['description']).strip().split(' ')
        for word in description_text:
            if len(word) >= 6:
                long_words_list.append(word)

    long_words_dict = Counter(long_words_list)
    top_ten = list(reversed(sorted(long_words_dict.values())))[:10]

print('TOP-10 популярных слов длиннее 6 символов в новостях про Африку:')
[print(value, key) for key, value in long_words_dict.items() if value >= top_ten[-1]]
