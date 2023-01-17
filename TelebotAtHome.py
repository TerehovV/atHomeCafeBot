#test new callback func
#telegram.ext

#create a
################################ Import moduls ########################################
from telegram import LabeledPrice, ShippingOption, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
    CallbackContext,
    CallbackQueryHandler
)
from BotMessages import main_menu_message, hello_message, err_basket_message, clear_basket_message, \
    add_in_basket_message, successful_pay_msg, err_call_ship_msg, err_send_ship_msg
from BotKeyboard import beaker_choice_keyboard, sweet_choice_keyboard, altern_choice_keyboard,\
    coffee_choice_keyboard, menu_choice_keyboard, basket_keyboard, main_keyboard
from config import bot_key, provider_key
from GetPosterProductsData import get_products_data
from GetPosterBatchticketsData import get_menu_data
from GetPosterCategoryData import get_category
from ConvertBasket import convert_basket
import logging

############################## Initialization ########################################

logging.basicConfig(
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
sessions = dict()
final_check = ''

################################## Bot ###############################################

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(hello_message())
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_keyboard())
    print(update.message.chat_id)
    global sessions
    basket = []
    price_basket = []
    suma = 0
    sessions[update.message.chat_id] = (basket, price_basket, suma)

def main_menu(update: Update, context: CallbackContext) -> None:    
    update.callback_query.message.edit_text(main_menu_message(),
                                            reply_markup=main_keyboard())
    
def menu_choice(update: Update, context: CallbackContext) -> None:
    print('menu_choice is running !')
    drink_menu_info = {'4': 'Класична кава', '5': 'Велика кава', '38': 'Фільтрова кава',
                       '16': 'Кава на рослинному молоці',
                       '18': 'Кава на безлактозному молоці', '76': 'Зимове меню  TO GO', '36': 'Чай'}
    data_category = get_category()
    d = dispatcher
    update.callback_query.message.edit_text(main_menu_message(),
                                            reply_markup=menu_choice_keyboard(drink_menu_info, data_category,
                                                                              d, coffee_choice))
    
def coffee_choice(update: Update, context: CallbackContext) -> None:
    choice = update['callback_query']['data']
    print('coffee_choice is running, data:', choice)
    menu_data = get_menu_data()
    d = dispatcher
    update.callback_query.message.edit_text(main_menu_message(),
                                            reply_markup=coffee_choice_keyboard(choice, menu_data, d, add_coffee))

def sweet_choice(update: Update, context: CallbackContext) -> None:
    choice = update['callback_query']['data']
    print('sweet_choice is running, data:', choice)
    data_products = get_products_data()
    d = dispatcher
    update.callback_query.message.edit_text(main_menu_message(),
                                            reply_markup=sweet_choice_keyboard(choice, data_products,
                                                                               d, add_sweet))

def beaker_choice(update: Update, context: CallbackContext) -> None:
    print('beaker_choice is running !')
    category_id = {'Выпечка': '2', 'BeakerStreet': '11', 'GOOD FOOD': '64', 'Сэндвич': '77', 'Maya Cake': '79',
                   'Slice Cake': '82'}
    data_products = get_products_data()
    d = dispatcher
    update.callback_query.message.edit_text(main_menu_message(),
                                            reply_markup=beaker_choice_keyboard(data_products, category_id,
                                                                                d, sweet_choice))

def altern_choice(update: Update, context: CallbackContext) -> None:
    print('altern_choice is running !')
    update.callback_query.message.edit_text(main_menu_message(),
                                            reply_markup=altern_choice_keyboard())

def clear_basket(update: Update, context: CallbackContext):
    print('clear_basket is running !')
    global sessions
    (basket, price_basket, suma) = sessions[update.callback_query.from_user.id]
    basket.clear()
    price_basket.clear()
    update.callback_query.message.reply_text(clear_basket_message())
    suma = 0
    sessions[update.callback_query.from_user.id] = (basket, price_basket, suma)

def create_basket(update: Update, context: CallbackContext):
    print('create_basket is running !')
    global sessions
    global final_check
    (basket, price_basket, suma) = sessions[update.callback_query.from_user.id]
    suma = 0
    if basket:
        basket_c = {}.fromkeys(basket, 0)        
        for a in basket:
            basket_c[a] += 1
        for i in price_basket:
            suma += i            
        final_check = convert_basket(basket_c)
        update.callback_query.message.reply_text('Кошик: \n'
                                                 + final_check + '\n'
                                                 + 'До сплати: ' + str(suma)+ 'UAH',
                                                 reply_markup=basket_keyboard())
    else:
        update.callback_query.message.reply_text(err_basket_message())
    sessions[update.callback_query.from_user.id] = (basket, price_basket, suma)
    print(sessions)

def start_shipping_callback(update: Update, context: CallbackContext) -> None:
    global sessions
    global final_check
    if update.callback_query.from_user.id not in sessions:
        print('error: msg from unknown user!')
        return
    (_, _, suma) = sessions[update.callback_query.from_user.id]
    if suma:
        chat_id = update.callback_query.from_user.id
        title = 'Оплата Замовлення "Заберу сам"'
        description = final_check
        payload = 'Custom-Payload'
        provider_token = provider_key
        currency = 'UAH'
        price = suma
        prices = [LabeledPrice('Test', price * 100)]
        context.bot.send_invoice(
            chat_id, title, description, payload, provider_token, currency, prices
            )
    else:
        update.callback_query.message.reply_text(err_send_ship_msg())

def shipping_callback(update: Update, context: CallbackContext):
    query = update.shipping_query
    if query.invoice_payload != 'Custom-Payload':
        query.answer(ok=False, error_message=err_call_ship_msg())
        return

def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query   
    if query.invoice_payload != 'Custom-Payload':
        query.answer(ok=False, error_message=err_call_ship_msg())
    else:
        query.answer(ok=True)

def successful_payment_callback(update: Update, context: CallbackContext):
    update.message.reply_text(successful_pay_msg())

############################# Add Positions ##########################################

def add_coffee(update: Update, context: CallbackContext):
    global sessions
    (basket, price_basket,_ ) = sessions[update.callback_query.from_user.id]
    menu_data = get_menu_data()
    choice = str(update['callback_query']['data'])
    print('add coffee is run, data:', choice)
    name = choice
    price = int(float(menu_data[choice][3])/100)
    basket.append(name)
    price_basket.append(price)
    update.callback_query.message.reply_text(add_in_basket_message() + name)

def add_sweet(update: Update, context: CallbackContext):
    global sessions
    (basket, price_basket,_ ) = sessions[update.callback_query.from_user.id]
    data_products = get_products_data()
    choice = str(update['callback_query']['data'])
    print('add_sweet is run, data:', choice)
    price = int(data_products[choice][0])
    name = data_products[choice][2]
    '''block add position over leftover'''
    basket.append(name)
    price_basket.append(price)
    update.callback_query.message.reply_text(add_in_basket_message() + name)

############################### Handlers #############################################

updater = Updater(bot_key)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", hello))
dispatcher.add_handler(CallbackQueryHandler(menu_choice, pattern='order'))
#dispatcher.add_handler(CallbackQueryHandler(coffee_choice, pattern='coffee'))
dispatcher.add_handler(CallbackQueryHandler(altern_choice, pattern='altern'))
dispatcher.add_handler(CallbackQueryHandler(beaker_choice, pattern='sweet'))
dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
dispatcher.add_handler(CallbackQueryHandler(menu_choice, pattern='menu'))
dispatcher.add_handler(CallbackQueryHandler(create_basket, pattern='basket'))
dispatcher.add_handler(CallbackQueryHandler(clear_basket, pattern='clear'))
dispatcher.add_handler(CallbackQueryHandler(start_shipping_callback, pattern='pay'))

# Optional handler if your product requires shipping
dispatcher.add_handler(ShippingQueryHandler(shipping_callback))

# Pre-checkout handler to final check
dispatcher.add_handler(PreCheckoutQueryHandler(precheckout_callback))

# Success! Notify your user!
dispatcher.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))

    # Start the Bot
updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()

if __name__ == '__main__':
    updater.polling()