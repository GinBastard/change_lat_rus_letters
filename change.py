import re


def change_lat_rus_letters(text, mode='lat_to_rus'):

    '''
    Функция проверяет значение колонки (text) на наличие латинских или русских символов
    (в зависимости от выбранного режима (mode)).
    Так же проверяет на наличие последовательности из трех (и более) лат. или рус. символов - детектор случайной замены одной или двух букв подряд.
    Если менее 3-х символов в последовательностях - заменяет символы в соответствии с выбранным словарем соответствий символов.

    :params text - значение из столбца:
    :params mode - режим перевода 'lat_to_rus', 'rus_to_lat':
    :return text:
    '''
    lat_rus_dict = {'A' : 'А', 'E' : 'Е', 'K' : 'К', 'M' : 'М', 'O' : 'О', 'T' : 'Т', 'H' : 'Н', 'C' : 'С', 'P' : 'Р', 'B' : 'В',
                    'a' : 'а', 'o' : 'о', 'k' : 'к', 'm' : 'м', 't' : 'т', 'y' : 'у', 'c' : 'с', 'e' : 'е', 'p' : 'р', 'lat' : 'rus'}
    rus_lat_dict = {'А' : 'A', 'Е' : 'E', 'К' : 'K', 'М' : 'M', 'О' : 'O', 'Т' : 'T', 'Н' : 'H', 'С' : 'C', 'Р' : 'P', 'В' : 'B',
                    'а' : 'a', 'о' : 'o', 'к' : 'k', 'м' : 'm', 'т' : 't', 'у' : 'y', 'с' : 'c', 'е' : 'e', 'р' : 'p', 'rus' : 'lat'}

    if mode == 'lat_to_rus':                                           # Выбираем режим замены символов
        if re.search(r'[a-zA-Z]', text):                               # Ищем латинские символы
            if re.search(r'[a-zA-Z]{3}', text):                        # Если в тексте встречается последовательность из трех символов подряд
                return text.strip()                                    # ...то необрабатываем текст (считаем что текст валидный - латинский)
            else:                                                      # если встречаются отдельный символ или два подряд
                text_ = change_letters_in_text(text, lat_rus_dict)     # заменяем ошибочные буквы используя словарь сопоставления
                return text_.strip()
        else:
            return text.strip()

    elif mode == 'rus_to_lat':
        if re.search(r'[а-яА-Я]', text):
            if re.search(r'[а-яА-Я]{3}', text):
                return text.strip()
            else:
                text_ = change_letters_in_text(text, rus_lat_dict)
                return text_.strip()
        else:
            return text.strip()


def change_letters_in_text(text, letters_dict):

    '''
    Функция заменяет символы, проверяя по выбранному словарю.
    :params text - значение из столбца:
    :params letters_dict - выбранный словарь соответствия символов:
    '''
    for key, value in letters_dict.items():
        text = text.replace(key, value)
    return text

# text = 'Ежевtика терttаяa'
# change_lat_rus_letters(text, 'lat_to_rus')
