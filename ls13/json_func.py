import json

with open("ls13/data.json", encoding="UTF-8") as json_file:
    info = json.load(json_file)


print(info[0]['FIO'])

film_info = {
    'genre': ['fantasy', 'horror', 'sitcom'], 
    'title': ['ewfewrf', 'ergerge', "wertgrg"]
}


with open("ls13/films.json", 'w', encoding="UTF-8") as json_file:
    json.dump(film_info, json_file, ensure_ascii=False, indent=2)