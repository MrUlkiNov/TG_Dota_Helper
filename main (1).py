import telebot

import requests
from bs4 import BeautifulSoup
from telebot import types

f = open('Bot/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close() 
f = open('Bot/Heroes.txt', 'r', encoding='UTF-8')
Heroes = f.read().split('\n')
f.close()
print(facts)
print(Heroes)
bot = telebot.TeleBot('5610020225:AAGuILRd242o3O_g2YSE4I2KVW1gmOhv30w')

@bot.message_handler(commands=["start"])
def start(m, res=False):
      
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         item1 = types.KeyboardButton("Герой")
        
         markup.add(item1)
        
         bot.send_message(m.chat.id, 'Нажми: \nГерой — для получения  описания персонажа ',  reply_markup=markup)

def Build(m):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(m.chat.id, 'Напиши ключевую слово "Билд" и имя героя')

def aue(m):
  markup = types.ForceReply(selective=False)
  bot.send_message(m.chat.id, 'Введи имя героя')
  
def skill(m):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(m.chat.id, 'Напиши ключевое слово "Скиллы " и имя героя')

def contr(m):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(m.chat.id, 'Напиши ключевое слово "Контрпик" и имя героя')

def parser(m):
    URL = 'https://dota2.ru/news/updates/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    post = soup.find("a", class_="index__news-link")
    title = post.find("div", class_="index__news-name").text.strip()
    url = f'https://dota2.ru{post.get("href")}'
    return f'{title}\n\n{url}'
  




@bot.message_handler(content_types=['text'])

def search(m, res=False):
     striped_message = m.text.strip()
     print(m.text)
     if m.text.strip() == "Герой":
         markup_reply=types.ReplyKeyboardMarkup(resize_keyboard=True)
         item_1 = types.KeyboardButton("Описание")
         item_2 = types.KeyboardButton("Билд")
         back = types.KeyboardButton("Скиллы")
         item_3 = types.KeyboardButton("Контрпик")
         markup_reply.add(item_1, item_2, back, item_3)
         
         bot.send_message(m.chat.id,'Выбери категорию', reply_markup=markup_reply)
     elif striped_message in Heroes:
         markup = types.ForceReply(selective=False)         
         fact_index = Heroes.index(striped_message)      
         bot.send_message(m.chat.id, facts[fact_index], reply_markup=markup)
     elif m.text.strip() == "Описание":
         aue(m)
     elif m.text.strip() == "Парсер":
         parser(m)
     elif m.text.strip() == "Билд":
         Build(m)   
     elif m.text.strip() == "Скиллы":
         skill(m)
     elif m.text.strip() == "Контрпик":
         contr(m)  

     elif m.text.strip() == 'Билд цк':
         p =open('Bot/Билды бота/Цк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд хускар':
         p =open('Bot/Билды бота/хускар.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд антимаг':
         p =open('Bot/Билды бота/Амр.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд вк':
         p =open('Bot/Билды бота/вк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд войд':
         p =open('Bot/Билды бота/войд.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд гуль':
         p =open('Bot/Билды бота/гуль.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд джагернаут':
         p =open('Bot/Билды бота/джага.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд луна':
         p =open('Bot/Билды бота/луна.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд медуза':
         p =open('Bot/Билды бота/вк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд мк':
         p =open('Bot/Билды бота/мк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд морф':
         p =open('Bot/Билды бота/морф.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд нага':
         p =open('Bot/Билды бота/нага.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд пл':
         p =open('Bot/Билды бота/пл.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд рики':
         p =open('Bot/Билды бота/рики.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд свен':
         p =open('Bot/Билды бота/свен.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд сларк':
         p =open('Bot/Билды бота/сларк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд спектра':
         p =open('Bot/Билды бота/спектр.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд тб':
         p =open('Bot/Билды бота/тб.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд тини':
         p =open('Bot/Билды бота/тини.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд тракса':
         p =open('Bot/Билды бота/тракса.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд троль':
         p =open('Bot/Билды бота/троль.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд урса':
         p =open('Bot/Билды бота/урса.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд фантомка':
         p =open('Bot/Билды бота/фантомка.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд хускар':
         p =open('Bot/Билды бота/хускар.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд темпларка':
         p =open('Bot/Билды бота/темпларка.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик антимаг':
         p =open('Bot/Контрпики бота/ам.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик вивер':
         p =open('Bot/Контрпики бота/вивер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик вк':
         p =open('Bot/Контрпики бота/вк.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Контрпик войд':
         p =open('Bot/Контрпики бота/войд.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Контрпик гуль':
         p =open('Bot/Контрпики бота/гуль.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик джагернаут':
         p =open('Bot/Контрпики бота/джага.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик луна':
         p =open('Bot/Контрпики бота/луна.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик медуза':
         p =open('Bot/Контрпики бота/вивер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик мк':
         p =open('Bot/Контрпики бота/мк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик морф':
         p =open('Bot/Контрпики бота/морф.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Контрпик нага':
         p =open('Bot/Контрпики бота/нага.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик пл':
         p =open('Bot/Контрпики бота/пл.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Контрпик рики':
         p =open('Bot/Контрпики бота/рики.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик свен':
         p =open('Bot/Контрпики бота/свен.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик сларк':
         p =open('Bot/Контрпики бота/сларк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик спектра':
         p =open('Bot/Контрпики бота/спектр.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик темпларка':
         p =open('Bot/Контрпики бота/темплар.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик тини':
         p =open('Bot/Контрпики бота/тини.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик тракса':
         p =open('Bot/Контрпики бота/тракса.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик троль':
         p =open('Bot/Контрпики бота/троль.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Контрпик урса':
         p =open('Bot/Контрпики бота/урса.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Контрпик фантомка':
         p =open('Bot/Контрпики бота/фантом.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик хускар':
         p =open('Bot/Контрпики бота/хуск.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Контрпик цк':
         p =open('Bot/Контрпики бота/Цк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд аббадон':
         p =open('Bot/Билды бота/аббадон.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд акс':
         p =open('Bot/Билды бота/акс.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд алхимик':
         p =open('Bot/Билды бота/алхимик.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд андаинг':
         p =open('Bot/Билды бота/андаинг.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд андерлорд':
         p =open('Bot/Билды бота/андерлорд.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд аппарат':
         p =open('Bot/Билды бота/апарат.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд арк':
         p =open('Bot/Билды бота/арк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд бабка':
         p =open('Bot/Билды бота/бабка.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд бистмастер':
         p =open('Bot/Билды бота/бист мастер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд бладсикер':
         p =open('Bot/Билды бота/бладсикер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд бристлбек':
         p =open('Bot/Билды бота/бристлбек.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд бруда':
         p =open('Bot/Билды бота/бруда.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд брюмастер':
         p =open('Bot/Билды бота/брюмастер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд бх':
         p =open('Bot/Билды бота/бх.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд бэйн':
         p =open('Bot/Билды бота/бэйн.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд бэтрайдер':
         p =open('Bot/Билды бота/бэтрайдер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд вайпер':
         p =open('Bot/Билды бота/вайпер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд варлок':
         p =open('Bot/Билды бота/варлок.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд вд':
         p =open('Bot/Билды бота/вд.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд венга':
         p =open('Bot/Билды бота/венга.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд веномансер':
         p =open('Bot/Билды бота/веномансер.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд вивер':
         p =open('Bot/Билды бота/вивер.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд виверна':
         p =open('Bot/Билды бота/виверна.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд вр':
         p =open('Bot/Билды бота/виндренджер.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд висаж':
         p =open('Bot/Билды бота/висаж.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд висп':
         p =open('Bot/Билды бота/висп.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд войд спирит':
         p =open('Bot/Билды бота/войд спирит.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд гирокоптер':
         p =open('Bot/Билды бота/гирокоптер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд гримстрок':
         p =open('Bot/Билды бота/гримстрок.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд дв':
         p =open('Bot/Билды бота/дарквилоу.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд дазл':
         p =open('Bot/Билды бота/даззл.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд дарксир':
         p =open('Bot/Билды бота/дарскир.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд даунбрейкер':
         p =open('Bot/Билды бота/даунбрейкер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд профетка':
         p =open('Bot/Билды бота/дез профет.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд джакиро':
         p =open('Bot/Билды бота/джакиро.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд дизраптор':
         p =open('Bot/Билды бота/дизраптор.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд дк':
         p =open('Bot/Билды бота/дк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд дум':
         p =open('Bot/Билды бота/дум.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд зевс':
         p =open('Bot/Билды бота/зевс.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд земеля':
         p =open('Bot/Билды бота/земеля.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд инвокер':
         p =open('Bot/Билды бота/инвокер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд квопа':
         p =open('Bot/Билды бота/квопа.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд кентавр':
         p =open('Bot/Билды бота/кентавр.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд клинкз':
         p =open('Bot/Билды бота/клинкз.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд темпларка':
         p =open('Bot/Билды бота/темпларка.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд клокверк':
         p =open('Bot/Билды бота/клокверк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд котел':
         p =open('Bot/Билды бота/котел.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд кунка':
         p =open('Bot/Билды бота/кунка.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд легионка':
         p =open('Bot/Билды бота/легионка.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд лешрак':
         p =open('Bot/Билды бота/лешрак.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд лина':
         p =open('Bot/Билды бота/лина.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд лион':
         p =open('Bot/Билды бота/лион.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд лич':
         p =open('Bot/Билды бота/лич.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд друид':
         p =open('Bot/Билды бота/лон друид.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд луна':
         p =open('Bot/Билды бота/луна.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд люкан':
         p =open('Bot/Билды бота/люкан.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд магнус':
         p =open('Bot/Билды бота/магнус.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд марс':
         p =open('Bot/Билды бота/марс.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд марси':
         p =open('Bot/Билды бота/марси.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд мипо':
         p =open('Bot/Билды бота/мипо.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд мирана':
         p =open('Bot/Билды бота/мирана.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд некр':
         p =open('Bot/Билды бота/некр.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд никс':
         p =open('Bot/Билды бота/никс.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд найтсталкер':
         p =open('Bot/Билды бота/нс.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд огр':
         p =open('Bot/Билды бота/огрмаг.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд омник':
         p =open('Bot/Билды бота/омник.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд оракл':
         p =open('Bot/Билды бота/оракл.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд пак':
         p =open('Bot/Билды бота/пак.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд панга':
         p =open('Bot/Билды бота/пангольер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд петух':
         p =open('Bot/Билды бота/петух.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд пл':
         p =open('Bot/Билды бота/пл.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд праймал бист':
         p =open('Bot/Билды бота/праймал бист.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд пугна':
         p =open('Bot/Билды бота/пугна.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд пудж':
         p =open('Bot/Билды бота/пудж.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд разор':
         p =open('Bot/Билды бота/разор.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд рики':
         p =open('Bot/Билды бота/рики.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд рубик':
         p =open('Bot/Билды бота/рубик.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд сало':
         p =open('Bot/Билды бота/сайленсер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд свен':
         p =open('Bot/Билды бота/свен.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд ск':
         p =open('Bot/Билды бота/ск.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд слардар':
         p =open('Bot/Билды бота/слардар.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд бара':
         p =open('Bot/Билды бота/спирит брейкер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд снайпер':
         p =open('Bot/Билды бота/снайпер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд сф':
         p =open('Bot/Билды бота/сф.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд арбуз':
         p =open('Bot/Билды бота/тайдхантер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд тб':
         p =open('Bot/Билды бота/тб.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд течес':
         p =open('Bot/Билды бота/течес.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд тимбер':
         p =open('Bot/Билды бота/тимбер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд тинкер':
         p =open('Bot/Билды бота/тинкер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд трент':
         p =open('Bot/Билды бота/трент.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд туск':
         p =open('Bot/Билды бота/туск.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд феникс':
         p =open('Bot/Билды бота/феникс.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд фура':
         p =open('Bot/Билды бота/фура.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд белка':
         p =open('Bot/Билды бота/худвинк.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд цм':
         p =open('Bot/Билды бота/цм.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд чен':
         p =open('Bot/Билды бота/чен.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд демон':
         p =open('Bot/Билды бота/шадоудемон.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд шаман':
         p =open('Bot/Билды бота/шаман.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд шейкер':
         p =open('Bot/Билды бота/шейкер.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд шторм':
         p =open('Bot/Билды бота/шторм.jpg', 'rb')
         bot.send_photo(m.chat.id, p)
     elif m.text.strip() == 'Билд титан':
         p =open('Bot/Билды бота/элдер титан.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Билд эмбер':
         p =open('Bot/Билды бота/эмбер.jpg', 'rb')
         bot.send_photo(m.chat.id, p)  
     elif m.text.strip() == 'Билд энча':
         p =open('Bot/Билды бота/энча.jpg', 'rb')
         bot.send_photo(m.chat.id, p) 
     elif m.text.strip() == 'Скиллы вк':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ВК/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ВК/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ВК/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ВК/d.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы антимаг':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Антимаг/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Антимаг/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Антимаг/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Антимаг/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Антимаг/e.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы темпларка':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/e.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/f.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Ассасинка/g.jpg', 'rb'))]) 
     elif m.text.strip() == 'Скиллы войд':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Войд/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Войд/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Войд/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Войд/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Войд/e.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы гуль':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Гуль/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Гуль/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Гуль/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/гуль/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Гуль/e.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы джага':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Джага/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Джага/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Джага/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Джага/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Джага/e.jpg', 'rb'))]) 
     elif m.text.strip() == 'Скиллы пл':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Лансер/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Лансер/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Лансер/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Лансер/d.jpg', 'rb'))])  
     elif m.text.strip() == 'Скиллы луна':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Луна/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Луна/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Луна/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Луна/d.jpg', 'rb'))])  
     elif m.text.strip() == 'Скиллы медуза':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Медуза/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Медуза/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Медуза/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Медуза/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Медуза/e.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы морф':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Морф/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Морф/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Морф/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Морф/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Морф/e.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Морф/f.jpg', 'rb'))]) 
     elif m.text.strip() == 'Скиллы нага':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Нага/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Нага/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Нага/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Нага/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Нага/e.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы рики':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Рики/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Рики/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Рики/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Рики/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Рики/e.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы свен':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Свен/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Свен/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Свен/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Свен/d.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы сларк':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сларк/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сларк/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сларк/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сларк/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сларк/e.jpg', 'rb'))]) 
     elif m.text.strip() == 'Скиллы спектра':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Спектр/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Спектр/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Спектр/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Спектр/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Спектр/e.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Спектр/f.jpg', 'rb'))]) 
     elif m.text.strip() == 'Скиллы мк':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/e.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/f.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/g.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Сунь Укун/h.jpg', 'rb'))])  
     elif m.text.strip() == 'Скиллы тб':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ТБ/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ТБ/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ТБ/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ТБ/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ТБ/e.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ТБ/f.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы тини':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тини/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тини/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тини/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тини/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тини/e.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тини/f.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы тракса':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тракса/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тракса/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тракса/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Тракса/d.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы троль':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Троль/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Троль/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Троль/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Троль/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Троль/e.jpg', 'rb')), telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Троль/f.jpg', 'rb'))])  
     elif m.text.strip() == 'Скиллы урса':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Урса/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Урса/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Урса/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Урса/d.jpg', 'rb'))])
     elif m.text.strip() == 'Скиллы фантомка':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Фантомка/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Фантомка/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Фантомка/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Фантомка/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Фантомка/e.jpg', 'rb'))])  
     elif m.text.strip() == 'Скиллы хускар':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Хускар/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Хускар/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Хускар/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Хускар/d.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/Хускар/e.jpg', 'rb'))]) 
     elif m.text.strip() == 'Скиллы цк':
         bot.send_media_group(m.chat.id, [telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ЦК/a.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ЦК/b.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ЦК/c.jpg', 'rb')),telebot.types.InputMediaPhoto(open('Bot/Спелы бота/ЦК/d.jpg', 'rb'))])  
      
     else:
         bot.send_message(m.chat.id, 'Что то не так :/')

    
     
       
bot.polling(none_stop=True, interval=0)