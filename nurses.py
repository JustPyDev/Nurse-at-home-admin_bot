import datetime
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS


def city():
    return [
        [InlineKeyboardButton("Bizning mijozlar", callback_data=f"user")],
        [InlineKeyboardButton("Takliflar va Xabarlar", callback_data=f"ser")],
    ]


def services():
    return [
        [InlineKeyboardButton("Eng oxirgi mijoz", callback_data=f"1")],
        [InlineKeyboardButton("Eng oxirgi 5 ta mijozlar", callback_data=f"5")],
    ]


def follower():
    return [
        [InlineKeyboardButton("Eng oxirgi xabar", callback_data=f"01")],
        [InlineKeyboardButton("Eng oxirgi 5 ta xabarlar", callback_data=f"05")],
    ]


def back():
    return [
        [InlineKeyboardButton("Bosh sahifa", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")
    if data[0] == 'user':
        query.message.reply_text(f"""Bizning mijozlar!!!""",
                                 reply_markup=InlineKeyboardMarkup(services()))

    if data[0] == "1":
        while True:
            url = 'http://127.0.0.1:8000/User_follower_list/'
            request = requests.get(url)

            soup = BS(request.text, 'html.parser')
            user_name = soup.find('div', class_='medica-about-content')

            user_map = soup.find('div', class_='medical_map')

            user_services_name = soup.find('div', class_='medical_services_name')

            user_services = soup.find('div', class_='medical_services')

            user_price = soup.find('div', class_='medical_price')

            user_number = soup.find('div', class_='medical_number')
            query.message.reply_text(f"""Bizning mijoz!!!\n{user_name.text}{user_number.text}{user_map.text}
                                            {user_services_name.text}{user_services.text}{user_price.text}""",
                                     reply_markup=InlineKeyboardMarkup(back()))
            break
    if data[0] == '5':
        while True:
            url = 'http://127.0.0.1:8000/User_follower_list/'
            request = requests.get(url)

            soup = BS(request.text, 'html.parser')
            users = soup.find('div', class_='medical_1')
            a = users.text.replace('.', '{}'.format('\n'))
            users2 = soup.find('div', class_='medical_2')
            b = users2.text.replace('.', '{}'.format('\n'))
            users3 = soup.find('div', class_='medical_3')
            c = users3.text.replace('.', '{}'.format('\n'))
            users4 = soup.find('div', class_='medical_4')
            d = users4.text.replace('.', '{}'.format('\n'))
            users5 = soup.find('div', class_='medical_5')
            e = users5.text.replace('.', '{}'.format('\n'))
            query.message.reply_text(f"""Bizning mijoz!!!\n{a}{b}{c}{d}{e}""",
                                     reply_markup=InlineKeyboardMarkup(back()))
            break
    if data[0] == 'ser':
        query.message.reply_text(f"""Bizning mijozlardan xabarlar!!!""",
                                 reply_markup=InlineKeyboardMarkup(follower()))
    if data[0] == "01":
        while True:
            url = 'http://127.0.0.1:8000/User_follower_list/'
            request = requests.get(url)

            soup = BS(request.text, 'html.parser')
            users_name = soup.find('div', class_='user_name')

            user_email = soup.find('div', class_='user_email')

            users_number = soup.find('div', class_='user_number')

            user_message = soup.find('div', class_='user_message')

            query.message.reply_text(
                f"""Bizning mijoz!!!\n{users_name.text}{user_email.text}{users_number.text}{user_message.text}""",
                reply_markup=InlineKeyboardMarkup(back()))
            break
    if data[0] == '05':
        while True:
            url = 'http://127.0.0.1:8000/User_follower_list/'
            request = requests.get(url)

            soup = BS(request.text, 'html.parser')
            follower_1 = soup.find('div', class_='follower_1')
            a = follower_1.text.replace('.', '{}'.format('\n'))
            follower_2 = soup.find('div', class_='follower_2')
            b = follower_2.text.replace('.', '{}'.format('\n'))
            follower_3 = soup.find('div', class_='follower_3')
            c = follower_3.text.replace('.', '{}'.format('\n'))
            follower_4 = soup.find('div', class_='follower_4')
            d = follower_4.text.replace('.', '{}'.format('\n'))
            follower_5 = soup.find('div', class_='follower_5')
            e = follower_5.text.replace('.', '{}'.format('\n'))
            query.message.reply_text(f"""Bizning mijoz!!!\n{a}{b}{c}{d}{e}""",
                                     reply_markup=InlineKeyboardMarkup(back()))
            break

    elif data[0] == 'back1':
        query.message.edit_text(
            f"""Salom\nBu bot "Медсестра на дом" saytining admin boti\nFoydalanuvchilarni ko`rmoqchi bo`lsangiz 👇""",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(
        f"""Salom {user.first_name}\nBu bot "Медсестра на дом" saytining admin boti\nFoydalanuvchilarni ko`rmoqchi bo`lsangiz 👇""",
        reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = '5130566635:AAGtNMU5YbPoNew213UWIl9AcCnQoEa-tEA'
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
