import telebot
from telebot import types
import config
import DataBase

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Молоко')
    item2 = types.KeyboardButton('Касса')
    item3 = types.KeyboardButton('Кофe')
    item4 = types.KeyboardButton('Разное')
    item5 = types.KeyboardButton('Отчет')
    markup.add(item1,item2,item3,item4,item5)

    bot.send_message(message.chat.id, "Choose",reply_markup=markup)

    DataBase.clear_temp()

@bot.message_handler(content_types=['text'])
def milk_out(message):

    if message.text == 'Отчет':
        bot.send_message(message.chat.id,f'{DataBase.get_stat()}')

    if message.text == 'Молоко': #Milk output
        config.table = 'milk'
        bot.send_message(message.chat.id,f'{DataBase.milk_output(DataBase.names,DataBase.count)}')
        # print(config.table)

    #keyboard
        choose_milk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        luga = types.KeyboardButton('Луга')
        cream = types.KeyboardButton(f'Сливки')
        koks = types.KeyboardButton(f'Кокс')
        nemol = types.KeyboardButton(f'Немолоко')
        prosto = types.KeyboardButton(f'Простоквашино')
        farm = types.KeyboardButton(f'Фермерское')
        sib = types.KeyboardButton(f'Сибмол')
        back = types.KeyboardButton(f'Назад')
        choose_milk.add(luga, cream, koks, nemol, prosto, farm, sib, back)
        bot.send_message(message.chat.id, "Choose Milk", reply_markup=choose_milk)

        # != 'Молоко' and message.text != 'Кофе' and message.text != 'Касса' and message.text != 'Разное':
         # get var
    elif message.text in DataBase.milk_output(DataBase.names,DataBase.count) or message.text == 'Назад':
        # if message.text != 'Кофе' and message.text !='Касса' and message.text !='Разное':
         DataBase.set_var(message.text)
         change_values = types.ReplyKeyboardMarkup(resize_keyboard=True)
         add_one = types.KeyboardButton('+1')
         add_five = types.KeyboardButton(f'+5')
         red_one = types.KeyboardButton(f'-1')
         red_five = types.KeyboardButton(f'-5')
         back = types.KeyboardButton(f'Назад')
         change_values.add(add_one, add_five, red_one, red_five, back)
         if message.text == 'Назад':
             welcome(message)
         if message.text != 'Назад':
               bot.send_message(message.chat.id, "Choose Operation", reply_markup=change_values)
    if message.text == '+1':
       DataBase.add_one(config.table,DataBase.get_var(1))
    if message.text == '+5':
       DataBase.add_five(config.table,DataBase.get_var(1))
    if message.text == '-1':
       DataBase.reduce_one(config.table,DataBase.get_var(1))
       if DataBase.stock_check(config.table, DataBase.get_var(1)) <= 5:
           #send message to Boss
           bot.send_message(chat_id = config.chat_ids, text = f"""Осталось мало: {DataBase.get_var(1)}""")
    if message.text == '-5':
       DataBase.reduce_five(config.table,DataBase.get_var(1))
       if DataBase.stock_check(config.table, DataBase.get_var(1)) <= 5:
           #send message to Boss
           bot.send_message(chat_id = config.chat_ids, text = f"""Осталось мало: {DataBase.get_var(1)}""")


    #keyboard
    if message.text == 'Кофe':  # coffee output
        config.table = 'coffee'
        bot.send_message(message.chat.id, f'{DataBase.coffee_output()}')
        # print(config.table)

        choose_coffee = types.ReplyKeyboardMarkup(resize_keyboard=True)
        coffee = types.KeyboardButton('Кофе')
        hot_chok = types.KeyboardButton(f'Горячий шоколад')
        cocoa = types.KeyboardButton(f'Какао')
        back = types.KeyboardButton(f'Назад')
        choose_coffee.add(coffee, hot_chok, cocoa, back)
        bot.send_message(message.chat.id, "Choose Coffee", reply_markup=choose_coffee)
        bot.register_next_step_handler(message, next_coffee)

    if message.text == 'Касса':
        bot.send_message(message.chat.id, f'''{DataBase.bank_output()}₽ ''')
        bank = types.ReplyKeyboardMarkup(resize_keyboard=True)
        change_bank = types.KeyboardButton(f'Изменить значение')
        back = types.KeyboardButton(f'Назад')
        bank.add(change_bank, back)
        bot.send_message(message.chat.id, "Изменить значение?", reply_markup=bank)
        bot.register_next_step_handler(message, bank_option)

    if message.text == 'Разное':
        bot.send_message(message.chat.id, f'''{DataBase.stuff_output()}''')
        choose_stuff = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cup_450 = types.KeyboardButton('Стакан 450')
        cup_350 = types.KeyboardButton(f'Стакан 350')
        cup_250 = types.KeyboardButton(f'Стакан 250')
        cap_big = types.KeyboardButton(f'Крышка большая')
        cap_small = types.KeyboardButton(f'Крышка маленькая')
        napkins = types.KeyboardButton(f'Салфетки')
        straws = types.KeyboardButton(f'Трубочки')
        sugar = types.KeyboardButton(f'Сахар')
        back = types.KeyboardButton(f'Назад')
        choose_stuff.add(cup_450, cup_350, cup_250, cap_big, cap_small, napkins, straws, sugar, back)
        bot.send_message(message.chat.id, "Choose Item", reply_markup=choose_stuff)
        if message.text == 'Назад':
            welcome(message)
        else:
            bot.register_next_step_handler(message, stuff_option)

def stuff_option(message):
    if not message.text in DataBase.stuff_output() and message.text != 'Назад':
        bot.send_message(message.chat.id, 'Wrong Data')
        welcome(message)

    else:
        if message.text == 'Назад':
            welcome(message)
        elif message.text:
            DataBase.set_var(message.text)
            # print(message.text)
            option = types.ReplyKeyboardMarkup(resize_keyboard=True)
            change = types.KeyboardButton(f'Изменить значение')
            back = types.KeyboardButton(f'Назад')
            option.add(change, back)
            bot.send_message(message.chat.id, "Choose Option", reply_markup=option)
            # print(message.text)
            bot.register_next_step_handler(message, stuff_option_2)

def stuff_option_2(message):
    if message.text != 'Изменить значение' and message.text != 'Назад':
        bot.send_message(message.chat.id, 'Wrong Data')
        welcome(message)
    else:
        if message.text == 'Назад':
            welcome(message)

        elif message.text == 'Изменить значение':
            stuff_option = types.ReplyKeyboardMarkup(resize_keyboard=True)
            true = types.KeyboardButton(f'Есть')
            false = types.KeyboardButton(f'Нет')
            back = types.KeyboardButton(f'Назад')
            stuff_option.add(true, false, back)
            bot.send_message(message.chat.id, "Choose Option", reply_markup=stuff_option)
            bot.register_next_step_handler(message, stuff_change)

def stuff_change(message):

    if message.text == 'Есть':
        DataBase.stuff_change(DataBase.get_var(1), message.text)
    elif message.text == 'Нет':
        DataBase.stuff_change(DataBase.get_var(1), message.text)
        bot.send_message(chat_id=config.chat_ids, text=f"""Закончились: {DataBase.get_var(1)}""")
    else:
        bot.send_message(message.chat.id, 'Wrong Data')
    welcome(message)
def bank_option(message):
    if message.text == 'Изменить значение':
        bot.send_message(message.chat.id, 'Введите значение')
        bot.register_next_step_handler(message, bank_change)

    elif message.text == 'Назад':
        welcome(message)

def bank_change(message):
    if message.text == 'Назад':
        welcome(message)
    else:
        if DataBase.bank_change(message.text) == False:
            bot.send_message(message.chat.id, 'Wrong Data')
            welcome(message)
        else:
            DataBase.bank_change(message.text)
            welcome(message)
def next_coffee(message):
    if not message.text in DataBase.coffee_output() and message.text != 'Назад' :
        bot.send_message(message.chat.id, 'Wrong Data')
        welcome(message)
    else:
        if message.text == 'Какао' or 'Горячий шоколад' or 'Кофе':

            DataBase.set_var(message.text)
            if message.text == 'Назад':
                welcome(message)

            elif message.text != 'Назад' and 'Изменить значение':
                option = types.ReplyKeyboardMarkup(resize_keyboard=True)
                change = types.KeyboardButton(f'Изменить значение')
                back = types.KeyboardButton(f'Назад')
                option.add(change, back)
                bot.send_message(message.chat.id, "Choose Option", reply_markup=option)
                bot.register_next_step_handler(message,change_value_coffee)
def change_value_coffee(message):
    if message.text == 'Назад':
        welcome(message)
    elif message.text == 'Изменить значение':
        bot.send_message(message.chat.id, 'Enter value')
        bot.register_next_step_handler(message, get_value_coffee)
    elif message.text != 'Назад' and message.text != 'Изменить значение':
        bot.send_message(message.chat.id, 'Wrong Data')
        welcome(message)

def get_value_coffee(message):
    DataBase.set_var(message.text)
    if message.text !='Назад':
        try:
            DataBase.change_value_coffee(config.table, DataBase.get_var(1), DataBase.get_var(2))
            if int(DataBase.get_var(2)) < 300:
                bot.send_message(chat_id=config.chat_ids, text=f"""Осталось мало: {DataBase.get_var(1)}""")
            welcome(message)
        except Exception:
            bot.send_message(message.chat.id, 'Wrong Data')
            welcome(message)
    else:
        welcome(message)


#RUN
bot.infinity_polling(none_stop = True)
