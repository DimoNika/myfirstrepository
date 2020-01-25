import telebot
import time

# run in background and detach terminal:
# nohup python3 whilebot.py &


bot = telebot.TeleBot("TOKEN")

# my
chat_id = 844162808


bot.send_message(chat_id, 'Bot started')

lessons = {
    'PE' : 'PE',
    'Eng' : 'English',
    'UkrL' : 'Ukranian literature',
    'Ukr' : 'Ukranian',
    'Bio' : 'Biology',
    'Chem' : 'Chemistry',
    'UkrH' : 'History of Ukraine',
    'Alg' : 'Algebra',
    'WorldL' : 'World literature',
    'Geog' : 'Geography',
    'Phys' : 'Phisics',
    'AorO' : 'Art/O.B.ZH',
    'Trud' : 'Trud',
    'Geom' : "Geometry",
    'PrZ' : 'Pravoznavstvo',
    'Spn' : 'Spanish',
    'Inf' : 'Inform',
    'Art/O.B.ZH' : 'Art/O.B.ZH',
    'WorldH' : 'World History'
}

numbers = {
    'l1' : ' - 1 lesson',
    'l2' : ' - 2 lesson',
    'l3' : ' - 3 lesson',
    'l4' : ' - 4 lesson',
    'l5' : ' - 5 lesson',
    'l6' : ' - 6 lesson',
    'l7' : ' - 7 lesson',
    'l8' : ' - 8 lesson',
    'l2.3' : ' - 2(3) lesson',
    'l4.5' : ' - 4(5) lesson',
    'endl' : 'Lesson have been ended',
}




def qwer(number):
    op = open('testtxt.txt')
    listid = op.readlines()
    for chat_id in listid:
        bot.send_message(chat_id, number)
        op.close()

def qwe(lesson, number):
    op = open('testtxt.txt')
    listid = op.readlines()
    for chat_id in listid:
        bot.send_message(chat_id, lesson + number)
        op.close()


while True:
    # Monday
    if int(time.strftime('%w')) == 1:
        if int(time.strftime('%H')) == 8:
            if int(time.strftime('%M')) == 25:
                qwe(lessons['Spn'], numbers['l1'])
        if int(time.strftime('%H')) == 9:
            if int(time.strftime('%M')) == 15:
                qwe(lessons['UkrL'], numbers['l2'])
        if int(time.strftime('%H')) == 10:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Eng'], numbers['l3'])
        if int(time.strftime('%H')) == 11:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['UkrH'], numbers['l4'])
        if int(time.strftime('%H')) == 12:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Ukr'], numbers['l5'])
        if int(time.strftime('%H')) == 13:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Inf'], numbers['l6'])
        if int(time.strftime('%H')) == 14:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Bio'], numbers['l7'])
        if int(time.strftime('%H')) == 15:
            if int(time.strftime('%M')) == 00:
                qwe(lessons['PE'], numbers['l8'])
        if int(time.strftime('%H')) == 15:
            if int(time.strftime('%M')) == 55:
                qwer(numbers['endl'])
    # Tuesday
    if int(time.strftime('%w')) == 2:
        if int(time.strftime('%H')) == 8:
            if int(time.strftime('%M')) == 25:
                qwe(lessons['Chem'], numbers['l1'])
        if int(time.strftime('%H')) == 9:
            if int(time.strftime('%M')) == 15:
                qwe(lessons['WorldH'], numbers['l2'])
        if int(time.strftime('%H')) == 10:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Alg'], numbers['l3'])
        if int(time.strftime('%H')) == 11:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['WorldL'], numbers['l4.5'])
        if int(time.strftime('%H')) == 12:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['WorldL'], numbers['l5'])
        if int(time.strftime('%H')) == 13:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['PE'], numbers['l6'])
        if int(time.strftime('%H')) == 14:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Eng'], numbers['l7'])
        if int(time.strftime('%H')) == 15:
            if int(time.strftime('%M')) == 00:
                qwer(numbers['endl'])
    # Wednesday
    if int(time.strftime('%w')) == 3:
        if int(time.strftime('%H')) == 8:
            if int(time.strftime('%M')) == 25:
                qwe(lessons['Inf'], numbers['l1'])
        if int(time.strftime('%H')) == 9:
            if int(time.strftime('%M')) == 15:
                qwe(lessons['Phys'], numbers['l2.3'])
        if int(time.strftime('%H')) == 10:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Phys'], numbers['l3'])
        if int(time.strftime('%H')) == 11:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Eng'], numbers['l4'])
        if int(time.strftime('%H')) == 12:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Chem'], numbers['l5'])
        if int(time.strftime('%H')) == 13:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Spn'], numbers['l6'])
        if int(time.strftime('%H')) == 14:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Art/O.B.ZH'], numbers['l7'])
        if int(time.strftime('%H')) == 15:
            if int(time.strftime('%M')) == 00:
                qwer(numbers['endl'])
    # Thursday
    if int(time.strftime('%w')) == 4:
        if int(time.strftime('%H')) == 8:
            if int(time.strftime('%M')) == 25:
                qwe(lessons['Trud'], numbers['l1'])
        if int(time.strftime('%H')) == 9:
            if int(time.strftime('%M')) == 15:
                qwe(lessons['UkrL'], numbers['l2'])
        if int(time.strftime('%H')) == 10:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Alg'], numbers['l3'])
        if int(time.strftime('%H')) == 11:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Eng'], numbers['l4'])
        if int(time.strftime('%H')) == 12:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Geom'], numbers['l5'])
        if int(time.strftime('%H')) == 13:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['PrZ'], numbers['l6'])
        if int(time.strftime('%H')) == 14:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['UkrH'], numbers['l7'])
        if int(time.strftime('%H')) == 15:
            if int(time.strftime('%M')) == 00:
                qwer(numbers['endl'])
    # Friday
    if int(time.strftime('%w')) == 5:
        if int(time.strftime('%H')) == 8:
            if int(time.strftime('%M')) == 25:
                qwe(lessons['Geom'], numbers['l1'])
        if int(time.strftime('%H')) == 9:
            if int(time.strftime('%M')) == 15:
               qwe(lessons['Eng'], numbers['l2'])
        if int(time.strftime('%H')) == 10:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Ukr'], numbers['l3'])
        if int(time.strftime('%H')) == 11:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Phys'], numbers['l4'])
        if int(time.strftime('%H')) == 12:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['PE'], numbers['l5'])
        if int(time.strftime('%H')) == 13:
            if int(time.strftime('%M')) == 10:
                qwe(lessons['Bio'], numbers['l6'])
        if int(time.strftime('%H')) == 14:
            if int(time.strftime('%M')) == 5:
                qwe(lessons['Geog'], numbers['l7'])
        if int(time.strftime('%H')) == 15:
            if int(time.strftime('%M')) == 00:
                qwer(numbers['endl'])
    time.sleep(60)


bot.polling()
