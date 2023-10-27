import telebot
from telebot import types
import os
import time
import datetime
import pyowm
import datetime
print('start')

bot = telebot.TeleBot('TOKEN')


# echotoken = 
# schooltoken = 

owm = pyowm.OWM('pyowm token')
# observation = owm.weather_at_place('Kiev, UA')
# w = observation.get_weather()


def qwe(chatid):
    op = open('testtxt.txt', 'r+')
    listid = op.readlines()
    if str(chatid + '\n') not in listid:
        op.write(str(chatid) + '\n')
        op.close()

# def qwer(number):
#     op = open('testtxt.txt')
#     listid = op.readlines()
#     for chat_id in listid:
#         bot.send_message(chat_id)
#         op.close()


def vector(deg):
    deg = float(deg)
    if deg > 0 and deg <= 22.5:
        return "North"
    if deg > 22.5 and deg <= 45:
        return 'North-East'
    if deg > 45 and deg <= 67.5:
        return 'North-East'
    if deg > 67.5 and deg <= 90:
        return 'East'
    if deg > 90 and deg <= 112.5:
        return 'East'
    if deg > 112.5 and deg <= 135:
        return 'East-South'
    if deg > 135 and deg <= 157.5:
        return 'Nonth-South'
    if deg > 157.5 and deg <= 180:
        return 'South'
    if deg > 180 and deg <= 202.5:
        return 'South'
    if deg > 202.5 and deg <= 225:
        return 'South-West'
    if deg > 225 and deg <= 247.5:
        return 'South-West'
    if deg > 247.5 and deg <= 270:
        return 'West'
    if deg > 270 and deg <= 292.5:
        return 'West'
    if deg > 292.5 and deg <= 315:
        return 'North-West'
    if deg > 315 and deg <= 337.5:
        return 'Nonth-West'
    if deg > 337.5 and deg <= 360:
        return 'North'

def ntime():
    ntime = None
    ntime = time.strftime('%H') + ':'
    ntime = ntime + time.strftime('%M') + ':'
    ntime = ntime + time.strftime('%S')
    ntime = str(datetime.date.today()) + '  ' + ntime
    return ntime

def temp():
    observation = owm.weather_at_place('Kiev, UA')
    w = observation.get_weather()
    temp = w.get_temperature(unit='celsius')
    tmax = '\n       Max temperature:   ' + str(temp['temp_max'])
    tavg = '\n   Average temperature:   ' + str(temp['temp'])
    tmin = '\n       Min temperature:   ' + str(temp['temp_min'])
    tem = tmax + tavg + tmin
    return tem

def rain():
    observation = owm.weather_at_place('Kiev, UA')
    w = observation.get_weather()
    r = str(w.get_rain())
    rain = r[:-1]
    rain = rain[:0]
    if rain == '':
        rain = '__None__'
    return rain   

def snow():
    observation = owm.weather_at_place('Kiev, UA')
    w = observation.get_weather()
    s = str(w.get_snow())
    snow = s[:-1]
    snow = snow[:0]
    if snow == '':
        snow = '__None__'
    return snow

def wind():
    observation = owm.weather_at_place('Kiev, UA')
    w = observation.get_weather()
    wi = w.get_wind()
    speed = '\n        Speed - ' + str(wi['speed'])
    deg = wi['deg']
    frm = '\n          From - ' + str(vector(deg))
    wind = speed + frm
    return wind


# weather = 'Current date:  ' + str(time()) + '\n\nWeather status:     ' + str(w.get_detailed_status()) + '\n\nTemperature:' + str(temp()) + '\n\nRain:  ' + str(rain()) + '\n\nSnow:  ' + str(snow()) + '\n\nWind:  ' + str(wind())




holdate = datetime.date(2020, 3, 21)
daydelta = str(holdate - datetime.date.today()) 
# print(daydelta)


def tohol():
    toholi = None
    toholi = str(24 - int(time.strftime('%H'))) + ':'
    if len(str(60 - int(time.strftime('%M')))) == 2:
        toholi = toholi + str(60 - int(time.strftime('%M'))) + ':'
    else:
        toholi = toholi + '0' + str(60 - int(time.strftime('%M'))) + ':'
    if len(str(60 - int(time.strftime('%S')))) == 2:
        toholi = toholi + str(60 - int(time.strftime('%S')))
    else:
        toholi = toholi + '0' + str(60 - int(time.strftime('%S')))
    return toholi        
            





# print(str(int(daydelta1) // 7) + ' weeks ' + daydelta1 + ' days, ' + tohol())



infor = {
    'mon' : 'Monday timetable\n1. Inform / Spanish - (8:30 - 9:15)\n2. Ukranian Literature - (9:25 - 10:20)\n3. English - (10:20 - 12:05)\n4. Ukranian history - (11:20 - 12:05)\n5. Ukranian - (12:25 - 13:10)\n6. Spanish / Inform - (13:20 - 14:05)\n7. Biology - (14:15 - 15:00)\n8. PE - (15:10 - 15:55)',
    'tue' : 'Tuesday timetable\n1. Chemistry - (8:30 - 9:15)\n2. World history - (9:25 - 10:10)\n3. Agebra - (10:20 - 11:05)\n4. World literature - (11:20 - 12:05)\n5. World literature - (12:25 - 13:10)\n6. PE - (13:20 - 14:05)\n7.English - (14:15-15:00)',
    'wed' : 'Wadnesday timetable\n1. Spanish / Inform- (8:30 - 9:15)\n2. Physics - (9:25 - 10:10)\n3. Physics - (10:20 - 10:05)\n4. English - (11:20 - 12:05)\n5. Chemistry - (12:25 - 13:10)\n6. Inform / Spanish - (13:20 - 14:05)\n7. Art / O.B.ZH. - (14:15 - 15:00)',
    'thu' : 'Thursday timetable\n1. Trud - (8:30 - 9:15)\n2. Ukranian literature - (9:25 - 10:10)\n3.Algebra - (10:20 - 11:05)\n4. English - (11:20 - 12:05)\n5. Geometry - (12:25 - 13:10)\n6. Pravoznavstvo - (13:20 - 14:05)\n7. History of Ukraine - (14:15 - 15:00)',
    'fri' : 'Friday timetable\n1. Geomerty - (8:30 - 9:15)\n2. English - (9:25 - 10:10)\n3. Ukranian - (10:20 - 11:05)\n4. Phisics - (11:20 - 12:05)\n5. PE - (12:25 - 13:10)\n6. Biology - (13:20 - 14:05)\n7. Geography - (14:15 - 15:00)',
    'rtable' : 'Rings table\n1. 8:30 - 9:15\n2. 9:25 - 10:10\n3. 10:20 - 11:05\n4. 11:20 - 12:05\n5. 12:25 - 13:10\n6. 13:20 - 14:05\n7. 14:15 - 15:00\n8. 15:10 - 15:55',
    'info' : 'Hi!\nI`m dima. I am doing my bot for fun. It sends messeges for me about my next lesson, because I dont like to find my dictionary to check what is me next lesson. Im going to do more functions for you SOON. If you have suggestions, suggest it to me.',
    'help' : 'COMMANDS\n1. /k - to open special keyboard.\n2. /info - for information about my bot\n3. /ttable - today timetable.\n4. /w - Check current weather.\n5. /ttable(x) - x = number of workday.\n6. /ttable(x) - x = mon(Monday), tue(Tuesday), wed(Wednesday), thu(Thursday), fri(Friday).\n7. /rtable - rings timetable.\n8. /tohol - time to holidays.\n9. /ping - to check bot connection:-)'
}
# prepare:
#
# pip3 install setuptools
# pip3 install pyTelegramBotAPI
#
# run:
# python3 commands2.py
#
# run in background and detach terminal:
# nohup python3 commands2.py &
#
# find running proccess:
# ps aux |grep "[c]ommands.py"
# output like this:
# dima     12975  0.4  1.4  44836 14840 pts/3    Sl   02:19   0:02 python3 commands.py
#
# 12975 - your pid
# killing command:
# kill 12975

###
markup = types.ReplyKeyboardMarkup(row_width=3)


@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Write < /help > for help:)')
    chatidstr = str(message.chat.id)
    chatidfloat = float(message.chat.id)
    qwe(chatidstr)

@bot.message_handler(commands=['help'])
def help(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['help'])

@bot.message_handler(commands=['ping'])
def ping(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'pong')

@bot.message_handler(commands=['info'])
def info(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['info'])

@bot.message_handler(commands=['k'])
def k(message):
    print(message.chat.id)
    chatidfloat = float(message.chat.id)
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.one_time_keyboard = False
    itembtn1 = types.KeyboardButton('/help')
    itembtn2 = types.KeyboardButton('/ttable')
    itembtn3 = types.KeyboardButton('/rtable')
    itembtn4 = types.KeyboardButton('/w')
    itembtn5 = types.KeyboardButton('/tohol')
    itembtn6 = types.KeyboardButton('/ping')
    markup.one_time_keyboard = False
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(chatidfloat, "To close keyboard - /kc (keybooard close)", reply_markup=markup)

@bot.message_handler(commands=['kc'])
def kc(message):
    print(message.chat.id)
    chatidfloat = float(message.chat.id)
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn6 = types.KeyboardButton('Close')
    markup.one_time_keyboard = True
    markup.add(itembtn6)
    bot.send_message(chatidfloat, "Keyboard closed", reply_markup=markup)


@bot.message_handler(commands=['ttable'])
def ttable(message):
    print(message.chat.id)
    if int(time.strftime('%w')) == 1:
        bot.send_message(message.chat.id, infor['mon'])
    if int(time.strftime('%w')) == 2:
        bot.send_message(message.chat.id, infor['tue'])
    if int(time.strftime('%w')) == 3:
        bot.send_message(message.chat.id, infor['wed'])
    if int(time.strftime('%w')) == 4:
        bot.send_message(message.chat.id, infor['thu'])
    if int(time.strftime('%w')) == 5:
        bot.send_message(message.chat.id, infor['fri'])    

@bot.message_handler(commands=['ttable1','ttablemon'])
def ttable1(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['mon'])

@bot.message_handler(commands=['ttable2','ttabletue'])
def ttable2(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['tue'])

@bot.message_handler(commands=['ttable3','ttablewed'])
def ttable3(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['wed'])

@bot.message_handler(commands=['ttable4','ttablethu'])
def ttable4(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['thu'])

@bot.message_handler(commands=['ttable5','ttablefri'])
def ttable5(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['fri'])

@bot.message_handler(commands=['rtable'])
def rtable(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, infor['rtable'])

@bot.message_handler(commands=['tohol'])
def toholi(message):
    daydelta1 = daydelta[:daydelta.find(' ')]
    print(message.chat.id)
    text = str(int(daydelta1) // 7) + ' weeks ' + daydelta1 + ' days, ' + tohol()
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['w'])
def weather(message):
    observation = owm.weather_at_place('Kiev, UA')
    w = observation.get_weather()
    # global weather
    # wshort = weather
    # wshort = 'Current date:  ' + str(ntime()) + '\n\nWeather status:     ' + str(w.get_detailed_status()) + '\n\nTemperature:' + str(temp()) + '\n\nRain:     ' + str(rain()) + '\n\nSnow:     ' + str(snow()) + '\n\nWind:  ' + str(wind())
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Current date:  ' + str(ntime()) + '\n\nWeather status:     ' + str(w.get_detailed_status()) + '\n\nTemperature:' + str(temp()) + '\n\nRain:     ' + str(rain()) + '\n\nSnow:     ' + str(snow()) + '\n\nWind:  ' + str(wind()))

@bot.message_handler(commands=['t'])
def test(message):
    observation = owm.weather_at_place('Kiev, UA')
    w = observation.get_weather()
    bot.send_message(message.chat.id, str( w.get_temperature(unit='celsius')))




# me
# Nik
# Boz




bot.polling()

print('end')
