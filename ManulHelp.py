from pyrogram import *
app = []
messages = []
max = 30528
config = open("config.txt", encoding='utf8') # Программе требуется файл config.txt, сожержащий Имя аккаунта, его api_id и hash_api, на каждой строке новый аккаунт, хотя можно и просто указать значения программе
chat = "manuls_LPR"
for i in config:
    j = i.rstrip()
    s = list(j.split())
    Name = s[0]
    api_id = int(s[1])
    api_hash = s[2]
    app.append(Client(Name, api_id = api_id, api_hash = api_hash))
app[2].start()
for msg in app[2].get_chat_history(chat):
    messages.append(msg)
num = set()                                    #Все числа, которые мы ожидаем увидеть
for j in range(0, max + 1):
    num.add(j)
    
integers = set()
for soob in messages:
    soo = str(soob.text)
    length = len(soo)
    m = 0
    while m < length:
        s_int = ''  # строка для нового числа
        separators = [' ', ',', '.', "'", '_', '!']
        while m < length and ('0' <= soo[m] <= '9' or soo[m] in separators):   #Не все числа записаны в одном нормальном виде 
            if not (soo[m] in separators):
                s_int += soo[m]
            m += 1
        m += 1
        if s_int != '':
            integers.add(int(s_int))       #Числа, которые мы увидели в чате

lack = num - integers
message = "Не хватает следующих количеств:\n"
for i in lack:
    message += str(i) + "\n"
print(message)
