import winsound

symbols = ['@', '#', '%', '&']
alphabet = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
a = input("Введите пароль: ")
count_len = 0
count_upper = 0
count_lower = 0
count_numeric = 0
count_symbols = 0
count_english = 0
count_space = 0

if len(a) >= 5:
    count_len = count_len + 1

for c in a:
    if c.isupper() == True:
        count_upper = count_upper + 1
    if c.islower() ==True:
        count_lower = count_lower + 1
    if c.isnumeric() == True:
         count_numeric = count_numeric + 1
    if symbols.count(c) >0:
        count_symbols = count_symbols + 1
    if c == " ":
        count_space = count_space + 1
    c = c.upper()
    if alphabet.count(c) >0:
        count_english = count_english + 1


if count_len >= 1 and count_upper >= 1 and count_lower >= 1 and count_numeric >= 1 and count_symbols >= 1 and count_english >= 1 and count_space ==0:
    print("Пароль подходит :)")
    winsound.Beep(10000, 300)
    winsound.Beep(5000, 300)
    winsound.Beep(10000, 300)
else:
    winsound.Beep(1000, 500)
    print("Пароль не подходит ")
    if count_len == 0:
        print("Пароль должен быть от 5 символов")
    if count_upper == 0:
        print("В пароле должна присутствовать как минимум 1 заглавная буква")
    if count_lower == 0:
        print("В пароле должна присутствовать как минимум 1 маленькая буква")
    if count_numeric == 0:
        print("В пароле должна присутствовать как минимум 1 цифра")
    if count_symbols == 0:
        print("В пароле должен присутствовать как минимум 1 символ из списка ", symbols)
    if count_english == 0:
        print("Буквы в пароле должны быть только английские")
    if count_space == 1:
        print("В пароле не должны присутствовать пробелы")
