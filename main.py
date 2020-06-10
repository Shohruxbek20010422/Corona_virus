from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

from typing import Dict, List
import requests

class Covid19(object):
    url = ""

    def __init__(self, url="https://covid.delalify.com/api"):
        self.url = url

    def _request(self, endpoint, params=None):
        if params is None:
            params = {}
        response = requests.get(self.url + endpoint, {**params})
        response.raise_for_status()
        if response:
            return response.json()['response']
        else:
            return False

    def getLatest(self) -> List[Dict[str, int]]:
        """
        :return: The latest amount of total confirmed cases, deaths, and recoveries.
        """
        data = self._request("/latest")
        return data


    def getByCountryCode(self, country_code) -> List[Dict]:
        """
        :param country_code: String denoting the ISO 3166-1 alpha-2 code (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country
        :return: A list of areas that correspond to the country_code. If the country_code is invalid, it returns an empty list.
        """
        data = self._request("/countries", {"country_code": country_code})
        return data

buttons = ReplyKeyboardMarkup([['🇺🇿 UZB statistikasi'], ['🌎 Dunyo statistikasi'],["🌐 Boshqa Davlatlar statistikasi"], ["💠 Qo`shni Davlatlar statistikasi"], ["🤖 Bot haqida 🤖"]], resize_keyboard=True)
covid = Covid19()

def start(update, context):
    update.message.reply_html(
        "<b>Assalomu alaykum </b>✋, {}\n \nMen <u><i>Koronovirus</i></u> statistikasi haqida ma`lumot beruvchi botman. \n\n<i>Eslatma</i> bu bot rasmiy emas❗️. Lekin rasmiy malumotlardan foydalangan holda malumot statistikani ko'rsatib beradi✅.\n\n🤖Bot yaratuvchisi : TATU FF🏛  1-kurs  talabasi <b><i>Asqarov Shohruxbek</i></b>👨‍💻\n🤖 Bot yaratuvchining telegram manzili : <i>@smarthackeruz</i> 👨‍💻\n🤖 Bot yaratuvchining telefon no`meri : <b><i>+998 93 427 1995</i></b>".format(update.message.from_user.first_name), reply_markup=buttons)
    return 1

def uzbek(update, context):
    data = covid.getByCountryCode('UZ')
    a = data['confirmed']-data['deaths']-data['recovered']
    update.message.reply_html(
        "🇺🇿 <b>O‘zbekiston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)

def world(update, context):
    data = covid.getLatest()
    update.message.reply_html(
        "🌎 <b>Dunyo</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b> Hozirda kasallanganlar</b> :<i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['active'])), reply_markup=buttons)

def bot_haqida(update, context):
    update.message.reply_html("<b>Assalomu alaykum </b>✋ {} . Bu bot  <u><i>Koronovirus</i></u> statistikasini ko'rsatib berish uchun yaratildi 💻. Bot Toshkent Axborot Texnalogiyalar Universiteti Farg'ona Filialining 🏛 1-kurs  talabasi <b><i>Asqarov Shohruxbek</i></b>👨‍💻 tomonidan yaratildi🛠. Agar botdan xato va kamchilik topsangiz🚱 bot yaratuvchisiga murojat qilishingiz so'raladi🗣. \n\n🤖 Bot yaratuvchining telegram manzili : <i>@smarthackeruz</i> 👨‍💻\n🤖 Bot yaratuvchining telefon no`meri : <b><i>+998 93 427 1995</i></b>\n\n<b>Inshaalloh</b> bemoqlarning hammasiga allohim shifo bersin 🤲".format(update.message.from_user.first_name))

def boshqa(update, context):
    buttons2 = [
        [
                InlineKeyboardButton("🇦🇷 Argentina",callback_data="argentina"),
                InlineKeyboardButton("🇦🇺 Avstraliya",callback_data="avstraliya")
        ],
        [
                InlineKeyboardButton("🇧🇷 Brazilya",callback_data="brazilya"),
                InlineKeyboardButton("🇨🇦 Canada",callback_data="canada")
        ],
        [
                InlineKeyboardButton("🇨🇳 Xitoy",callback_data="xitoy"),
                InlineKeyboardButton("🇨🇺 Cuba",callback_data="cuba")
        ],
        [
                InlineKeyboardButton("🇫🇷 Fransiya",callback_data="fransiya"),
                InlineKeyboardButton("🇩🇪 Germaniya",callback_data="germaniya")
        ],
        [
                InlineKeyboardButton("🇮🇳 Hindiston",callback_data="hind"),
                InlineKeyboardButton("🇮🇩 Indoneziya",callback_data="indoneziya")
        ],
        [
                InlineKeyboardButton("🇮🇶 Iroq",callback_data="iroq"),
                InlineKeyboardButton("🇮🇹 Italiya",callback_data="italiya")
        ],
        [
                InlineKeyboardButton("🇯🇵 Yaponiya",callback_data="yaponiya"),
                InlineKeyboardButton("🇲🇾 Malayziya",callback_data="malayziya")
        ],
        [
                InlineKeyboardButton("🇲🇽 Meksika",callback_data="meksika"),
                InlineKeyboardButton("🇳🇵 Nepal",callback_data="nepal")
        ],
        [
                InlineKeyboardButton("🇳🇿 Yangi Zelandiya",callback_data="yangi_zellandiya"),
                InlineKeyboardButton("🇱🇰 Shri-Lanka",callback_data="shri_lanka")
        ],
        [
                InlineKeyboardButton("🇵🇰 Pokiston",callback_data="pokiston"),
                InlineKeyboardButton("🇵🇹 Portugaliya",callback_data="portugaliya")
        ],
        [
                InlineKeyboardButton("🇶🇦 Qatar",callback_data="qatar"),
                InlineKeyboardButton("🇷🇴 Ruminiya",callback_data="ruminiya")
        ],
        [
                InlineKeyboardButton("🇸🇦 Saudiya Arabiston",callback_data="saudiya_arabiston"),
                InlineKeyboardButton("🇻🇳 Vetnam",callback_data="vetnam")
        ],
        [
                InlineKeyboardButton("🇸🇬 Singapur",callback_data="singapur"),
                InlineKeyboardButton("🇿🇦 Janubiy Afrika",callback_data="janubiy_afrika")
        ],
        [
                InlineKeyboardButton("🇹🇭 Tailand",callback_data="tailand"),
                InlineKeyboardButton("🇹🇷 Turkiya",callback_data="turkiya")
        ],
        [
                InlineKeyboardButton("🇺🇦 Ukraina",callback_data="ukraina"),
                InlineKeyboardButton("🇺🇾 Urugvay",callback_data="urugvay")
        ]
                ]
    update.message.reply_html("O'zingizga kerakli davlatni tanlang 🏳️",reply_markup=InlineKeyboardMarkup(buttons2)
        )
    return 2
def qoshni(update, context):
    buttons3 =  [
        [
                InlineKeyboardButton("🇦🇫 Afg'oniston",callback_data="afgoniston"),
                InlineKeyboardButton("🇰🇿 Qozog'iston",callback_data="qozogiston")
        ],
        [
                InlineKeyboardButton("🇰🇬 Qirgʻiziston",callback_data="qirgiziston"),
                InlineKeyboardButton("🇹🇯 Tojikiston",callback_data="tojikiston")
        ],
        [
                InlineKeyboardButton("🇹🇲 Turkmaniston",callback_data="turkmaniston")
        ],
                ]
    update.message.reply_html("O'zingizga kerakli davlatni tanlang 🏳️",reply_markup=InlineKeyboardMarkup(buttons3)
        )
    return 2
def argentina(update, context):
    data = covid.getByCountryCode('AR')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇦🇷 <b>Argentina</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def avstraliya(update, context):
    data = covid.getByCountryCode('AU')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇦🇺 <b>Avstraliya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def brazilya(update, context):
    data = covid.getByCountryCode('BR')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇧🇷<b>Brazilya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def canada(update, context):
    data = covid.getByCountryCode('BR')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇨🇦<b> Canada</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def xitoy(update, context):
    data = covid.getByCountryCode('CN')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇨🇳 <b>Xitoy</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def cuba(update, context):
    data = covid.getByCountryCode('CU')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇨🇺 <b>Cuba</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def fransiya(update, context):
    data = covid.getByCountryCode('FR')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇫🇷 <b>Fransiya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def germaniya(update, context):
    data = covid.getByCountryCode('DE')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇩🇪<b> Germaniya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def hind(update, context):
    data = covid.getByCountryCode('IN')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇮🇳 <b>Hindiston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def indoneziya(update, context):
    data = covid.getByCountryCode('ID')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇮🇩 <b>Indoneziya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def iroq(update, context):
    data = covid.getByCountryCode('IQ')
    query.message.delete()
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.reply_html(
        "🇮🇶<b> Iroq</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def italiya(update, context):
    data = covid.getByCountryCode('IT')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇮🇹<b> Italiya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def yaponiya(update, context):
    data = covid.getByCountryCode('JP')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇯🇵<b> Yaponiya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def malayziya(update, context):
    data = covid.getByCountryCode('MY')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇲🇾 <b>Malayziya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def meksika(update, context):
    data = covid.getByCountryCode('MX')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇲🇽 <b>Meksika</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def nepal(update, context):
    data = covid.getByCountryCode('NP')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇳🇵<b> Nepal</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def yangi_zellandiya(update, context):
    data = covid.getByCountryCode('NZ')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇳🇿<b> Yangi Zelandiya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def pokiston(update, context):
    data = covid.getByCountryCode('PK')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇵🇰 <b>Pokiston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def portugaliya(update, context):
    data = covid.getByCountryCode('PT')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇵🇹 <b>Portugaliya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def qatar(update, context):
    data = covid.getByCountryCode('QA')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇶🇦<b> Qatar</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def ruminiya(update, context):
    data = covid.getByCountryCode('RO')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇷🇴 <b>Ruminiya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)

def saudiya_arabiston(update, context):
    data = covid.getByCountryCode('SA')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇸🇦 <b>Saudiya Arabiston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def singapur(update, context):
    data = covid.getByCountryCode('SG')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇸🇬 <b>Singapur</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def janubiy_afrika(update, context):
    data = covid.getByCountryCode('ZA')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇿🇦 <b>Janubiy Afrika</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def shri_lanka(update, context):
    data = covid.getByCountryCode('LK')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇱🇰<b> Shri-Lanka</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons) 
def tailand(update, context):
    data = covid.getByCountryCode('TH')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇹🇭 <b>Tailand</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def turkiya(update, context):
    data = covid.getByCountryCode('TR')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇹🇷 <b>Turkiya</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def ukraina(update, context):
    data = covid.getByCountryCode('UA')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇺🇦 <b>Ukraina</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def urugvay(update, context):
    data = covid.getByCountryCode('UY')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇺🇾<b> Urugvay</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def vetnam(update, context):
    data = covid.getByCountryCode('VN')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇻🇳 <b> Vetnam</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def afgoniston(update, context):
    data = covid.getByCountryCode('AF')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇦🇫 <b>Afg'oniston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def qozogiston(update, context):
    data = covid.getByCountryCode('KZ')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇰🇿<b> Qozog'iston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def qirgiziston(update, context):
    data = covid.getByCountryCode('KG')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇰🇬<b> Qirgʻiziston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def tojikiston(update, context):
    data = covid.getByCountryCode('UZ')
    a = data['confirmed']-data['deaths']-data['recovered']
    query = update.callback_query
    query.message.delete()
    query.message.reply_html(
        "🇹🇯 <b> Tojikiston</b>da\n \n<b>Jami tasdiqlanganlar :</b> <i>{}</i>\n<b>Bugun tasdiqlanganlar :</b> <i>{}</i>\n<b>Tuzalganlar :</b> <i>{}</i>\n<b>Vafot etganlar :</b><i>{}</i>\n<b>Bugun vafot etganlar</b> : <i>{}</i>\n<b>Davolanayotganlar</b> : <i>{}</i>".
            format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['confirmedToday']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths']),
            "{:,}".format(data['deathsToday']),
            "{:,}".format(a)), reply_markup=buttons)
def turkmaniston(update, context):
        query = update.callback_query
        query.message.delete()
        query.message.reply_html(
        "🚫 Kechirasiz serverda Turkmaniston haqida 📶 malumot mavjud emas ❌")

updater = Updater('1187341291:AAF2FXjMwCX6jraDogFVRNKF0Gd5-cULhHo', use_context=True)

dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],
    states={
        1: [
            MessageHandler(Filters.regex('^(🇺🇿 UZB statistikasi)$'), uzbek),
            MessageHandler(Filters.regex('^(🌎 Dunyo statistikasi)$'), world),
            MessageHandler(Filters.regex('^(🌐 Boshqa Davlatlar statistikasi)$'), boshqa),
            MessageHandler(Filters.regex('^(💠 Qo`shni Davlatlar statistikasi)$'), qoshni),
            MessageHandler(Filters.regex('^(🤖 Bot haqida 🤖)$'), bot_haqida)],
        2: [
            CallbackQueryHandler(argentina, pattern='^'+"argentina"+'$'),
            CallbackQueryHandler(avstraliya, pattern='^'+"avstraliya"+'$'),
            CallbackQueryHandler(brazilya, pattern='^'+"brazilya"+'$'),
            CallbackQueryHandler(canada, pattern='^'+"canada"+'$'),
            CallbackQueryHandler(xitoy, pattern='^'+"xitoy"+'$'),
            CallbackQueryHandler(cuba, pattern='^'+"cuba"+'$'),
            CallbackQueryHandler(fransiya, pattern='^'+"fransiya"+'$'),
            CallbackQueryHandler(germaniya, pattern='^'+"germaniya"+'$'),
            CallbackQueryHandler(hind, pattern='^'+"hind"+'$'),
            CallbackQueryHandler(indoneziya, pattern='^'+"indoneziya"+'$'),
            CallbackQueryHandler(iroq, pattern='^'+"iroq"+'$'),
            CallbackQueryHandler(italiya, pattern='^'+"italiya"+'$'),
            CallbackQueryHandler(yaponiya, pattern='^'+"yaponiya"+'$'),
            CallbackQueryHandler(malayziya, pattern='^'+"malayziya"+'$'),
            CallbackQueryHandler(nepal, pattern='^'+"nepal"+'$'),
            CallbackQueryHandler(yangi_zellandiya, pattern='^'+"yangi_zellandiya"+'$'),
            CallbackQueryHandler(pokiston, pattern='^'+"pokiston"+'$'),
            CallbackQueryHandler(portugaliya, pattern='^'+"portugaliya"+'$'),
            CallbackQueryHandler(qatar, pattern='^'+"qatar"+'$'),
            CallbackQueryHandler(ruminiya, pattern='^'+"ruminiya"+'$'),
            CallbackQueryHandler(saudiya_arabiston, pattern='^'+"saudiya_arabiston"+'$'),
            CallbackQueryHandler(singapur, pattern='^'+"singapur"+'$'),
            CallbackQueryHandler(janubiy_afrika, pattern='^'+"janubiy_afrika"+'$'),
            CallbackQueryHandler(vetnam, pattern='^'+"vetnam"+'$'),
            CallbackQueryHandler(shri_lanka, pattern='^'+"shri_lanka"+'$'),
            CallbackQueryHandler(tailand, pattern='^'+"tailand"+'$'),
            CallbackQueryHandler(turkiya, pattern='^'+"turkiya"+'$'),
            CallbackQueryHandler(ukraina, pattern='^'+"ukraina"+'$'),
            CallbackQueryHandler(urugvay, pattern='^'+"urugvay"+'$'),
            CallbackQueryHandler(meksika, pattern='^'+"meksika"+'$'),
            CallbackQueryHandler(afgoniston, pattern='^'+"afgoniston"+'$'),
            CallbackQueryHandler(qozogiston, pattern='^'+"qozogiston"+'$'),
            CallbackQueryHandler(qirgiziston, pattern='^'+"qirgiziston"+'$'),
            CallbackQueryHandler(tojikiston, pattern='^'+"tojikiston"+'$'),
            CallbackQueryHandler(turkmaniston, pattern='^'+"turkmaniston"+'$'),
            MessageHandler(Filters.regex('^(🇺🇿 UZB statistikasi)$'), uzbek),
            MessageHandler(Filters.regex('^(🌎 Dunyo statistikasi)$'), world),
            MessageHandler(Filters.regex('^(🌐 Boshqa Davlatlar statistikasi)$'), boshqa),
            MessageHandler(Filters.regex('^(💠 Qo`shni Davlatlar statistikasi)$'), qoshni),
            MessageHandler(Filters.regex('^(🤖 Bot haqida 🤖)$'), bot_haqida)],
    },
    fallbacks=[CommandHandler('start', start)]
)
#dispatcher.add_handler(CallbackQueryHandler(inline_callback))
updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
