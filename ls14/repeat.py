import json


with open('test/ls14/text.txt', 'w', encoding='utf-8') as my_file:
    my_file.write('Просто текст') 


student_score = {
    "Ruslan": 10,
    "Magomed": 11,
    'кекпе5пк': 435
}


with open('test/ls14/text.json', 'w', encoding='utf-8') as my_json:
    json.dump(student_score, my_json, ensure_ascii=False, indent=2)