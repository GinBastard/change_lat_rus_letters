import re

def contains_russian(text):
    return bool(re.search(r'[а-яА-Я]', text))

def find_russian_indices(text):
    russian_indices = [m.start() for m in re.finditer(r'[а-яА-Я]', text)]
    return russian_indices

def find_russian_characters(text):
    russian_chars = re.findall(r'[а-яА-Я]', text)
    return russian_chars

# Функция проверки текста на замены символов
text = 'Betonica grandiflora = В. macrantha = Stachys grandiflora'  #'Salix purpureа ‘Pendulа’ = S. purpurea f. pendula'

if contains_russian(text):
    print("Строка содержит русские символы.")
else:
    print("Строка не содержит русских символов.")
print(find_russian_indices(text))
print(find_russian_characters(text))



def contains_lat(text):
    return bool(re.search(r'[a-zA-Z]', text))

def find_lat_indices(text):
    lat_indices = [m.start() for m in re.finditer(r'[a-zA-Z]', text)]
    return lat_indices

def find_lat_characters(text):
    lat_chars = re.findall(r'[a-zA-Z]', text)
    return lat_chars

def count_latin_characters(text):
    latin_count = sum(1 for char in text if char.isalpha() and char.isascii())
    return latin_count

# Функция проверки текста на замены символов
text = 'Cитник развесистый'

if contains_lat(text):
    print("Строка содержит латинские символы.")
else:
    print("Строка не содержит латинских символов.")
print(find_lat_indices(text))
print(find_lat_characters(text))
print("Количество латинских символов:", count_latin_characters(text))
