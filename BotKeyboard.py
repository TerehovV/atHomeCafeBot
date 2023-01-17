from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackQueryHandler


def main_keyboard():
    print('main_keyboard is running !')
    keyboard = [[InlineKeyboardButton(text='Замовити', callback_data='order')],
                [InlineKeyboardButton(text='Відгук', callback_data='mes')]]
    return InlineKeyboardMarkup(keyboard)

def menu_choice_keyboard(drink_menu_info, drink_category, d, coffee_choice):
    print('menu_choice_keyboard is running !')
    inl = InlineKeyboardButton
    keyboard = []
    for i in drink_category:
        for q in drink_menu_info:
            if i == q:
                x = [inl(text=str(drink_category[i]), callback_data=drink_category[i])]
                keyboard.append(x)
                d.add_handler(CallbackQueryHandler(coffee_choice, pattern=drink_category[i]))

    y = [inl(text='Смаколик 🧁', callback_data='sweet')]
    # create callback whith words !!!
    keyboard.append(y)
    z = [inl(text='Кошик 🛒', callback_data='basket'),
         inl(text='Назад ↩', callback_data='main')]
    keyboard.append(z)
    return InlineKeyboardMarkup(keyboard)

def coffee_choice_keyboard(choice, drink_menu, d, add_coffee):
    print('coffee_choice_keyboard is running !')
    inl = InlineKeyboardButton
    keyboard = []
    for i in drink_menu:
        if drink_menu[i][0] == choice:
            print(i, drink_menu[i])
            x = [inl(text=i, callback_data=i)]
            keyboard.append(x)
            d.add_handler(CallbackQueryHandler(add_coffee, pattern=i))
    y = [inl(text='Кошик 🛒', callback_data='basket'),
         inl(text='Назад ↩', callback_data='menu')]
    keyboard.append(y)
    return InlineKeyboardMarkup(keyboard)

def beaker_choice_keyboard(data_products, category_id, d, sweet_choice):
    print('beaker_choice_keyboard is running !')
    inl = InlineKeyboardButton
    keyboard = []
    for i in category_id:
        for q in data_products:
            if data_products[q][3] != '0.0000000' and data_products[q][1] == category_id[i]:
                x = [inl(text=str(i), callback_data=category_id[i])]
                keyboard.append(x)
                d.add_handler(CallbackQueryHandler(sweet_choice, pattern=category_id[i]))
                break
    y = [inl(text='Кошик 🛒', callback_data='basket'),
         inl(text='Назад ↩', callback_data='menu')]
    keyboard.append(y)
    return InlineKeyboardMarkup(keyboard)

def sweet_choice_keyboard(choice, data_products, d, add_sweet):
    print('sweet_choice_keyboard is running !')
    inl = InlineKeyboardButton
    keyboard = []
    for i in data_products:
        if data_products[i][1] == choice and data_products[i][3] != '0.0000000':
            print(data_products[i])
            x = [inl(text=data_products[i][2] + ' ' + str(int(float(data_products[i][3]))) + 'шт', callback_data=i)]
            keyboard.append(x)
            d.add_handler(CallbackQueryHandler(add_sweet, pattern=i))
    y = [inl(text='Кошик 🛒', callback_data='basket'),
         inl(text='Назад ↩', callback_data='sweet')]
    keyboard.append(y)
    return InlineKeyboardMarkup(keyboard)

def altern_choice_keyboard():
    print('altern_choice_keyboard is running !')
    inl = InlineKeyboardButton
    keyboard = [[inl(text='V-60 Пуровер 200мл', callback_data='v60')],
                [inl(text='Фільтр кава 200мл', callback_data='filter')],
                [inl(text='Кошик 🛒', callback_data='basket')],
                [inl(text='Назад ↩', callback_data='menu')]]
    return InlineKeyboardMarkup(keyboard)

def basket_keyboard():
    print('basket_keyboard is running !')
    keyboard = [[InlineKeyboardButton(text='💳', callback_data='pay')],
                [InlineKeyboardButton(text='Очистити', callback_data='clear')]]
    return InlineKeyboardMarkup(keyboard)
