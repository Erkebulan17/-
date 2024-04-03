import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("6830271848:AAEgFqhVEqU-c9hOKGzU78vTq4Zh2IRfav4") 



@bot.message_handler(commands=['start'])
def main(message):

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Ужастики 👻')
    btn2 = types.KeyboardButton('Комедии 🤡')
    markup.row(btn1,btn2)
    btn3 = types.KeyboardButton('Боевики 🤯')
    btn7 = types.KeyboardButton('Сериалы 😶‍🌫️')
    markup.row(btn3,btn7)
    btn4 = types.KeyboardButton('Мультфилмы😜')
    btn5 = types.KeyboardButton('Драмы 🥺')
    markup.row(btn4,btn5)
    btn6 = types.KeyboardButton('Новинки 🤩')
    btn8 = types.KeyboardButton('Детективы 🥸')
    markup.row(btn6,btn8)
    btn9 = types.KeyboardButton('Аниме 😮‍💨')
    btn10 = types.KeyboardButton('Манга 📔')
    markup.row(btn9,btn10)
    bot.reply_to(message,'Қандай филімнің жаныры қалайсыз ? ', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    
def on_click(message):
    if message.text == 'Ужастики 👻':
        bot.send_message(message.chat.id,'Топ 5 фильмов(Ужастики)----------------------------------------------------------------------« Синистер » Sinister, 2012, 110 мин.США • ужасы  Режиссёр: Скотт Дерриксон В ролях: Итан Хоук, Джульет РайлэнсРейтинг Кинопоиска 66.6151 198 оценок (5471)--------------------------------------------------------------------------------------------« Астрал Онлайн  » Host, 2020, 57 мин.Великобритания • ужасы  Режиссёр: Роб СэвиджВ ролях: Хейли Бишоп, Джемма МурРейтинг Кинопоиска 5.45.49 198 оценок (6472)--------------------------------------------------------------------------------------------« Паранормальные явления ». Скинамаринк  Skinamarink, 2022, 100 мин. Канада • ужасы  Режиссёр: Кайл Эдвард Болл В ролях: Лукас Пол, Дали Роуз Тетро   Рейтинг Кинопоиска 4.94.97 283 оценки  (7473)--------------------------------------------------------------------------------------------« Улыбка Smile » 2022, 115 мин. США • ужасы  Режиссёр: Паркер Финн В ролях: Сози Бэйкон, Кайл Галлнер Рейтинг Кинопоиска 6.46.428 467 оценок (8474)--------------------------------------------------------------------------------------------« Два, три, демон, приди!» Talk to Me, 2022, 95 мин. Австралия • ужасы  Режиссёр: Дэнни Филиппу В ролях: Софи Уайлд, Александра Дженсен Рейтинг Кинопоиска 6.46.4230 452 оценки (9475)--------------------------------------------------------------------------------------------')                                                                                                                                   
    if message.text == 'Комедии 🤡':
        bot.send_message(message.chat.id,'Топ 5 фильмов(Комедии)-----------------------------------------------------------------------« Один дома » Home Alone, 1990, 103 мин. США • комедия  Режиссёр: Крис Коламбус В ролях: Маколей Калкин, Джо Пеши Рейтинг Кинопоиска 8.3. топ 2508.31 159 020 оценок (0012)--------------------------------------------------------------------------------------------« Бишарашки »2022, 90 мин. Казахстан • комедия  Режиссёр: Дархан Саркенов В ролях: Исбек Абильмажинов, Жан Байжанбаев Рейтинг Кинопоиска 7.07.046 675 оценок  (1804)--------------------------------------------------------------------------------------------« Квартиранты Күшік құда », 2020, 87 мин. Казахстан • комедия  Режиссёр: Дархан Саркенов В ролях: Жан Байжанбаев, Баян Алагузова Рейтинг Кинопоиска 7.27.239 710 оценок  (3244)--------------------------------------------------------------------------------------------« Хотя бы в кино 2 » Хотя бы кинода 2, 2023 Казахстан • комедия  Режиссёр: Ернар Нургалиев В ролях: Кайрат Адилгерей, Дарига Бадыкова Рейтинг Кинопоиска 7.07.023 386 оценок (8620)--------------------------------------------------------------------------------------------« Бизнес по-казахски в Индии » Қазақша бизнес Үндістанда , 2022, 80 мин. Казахстан • комедия  Режиссёр: Анвар Матжанов В ролях: Нурлан Коянбаев, Жан Байжанбаев Рейтинг Кинопоиска 6.76.719 981 оценка (7634)--------------------------------------------------------------------------------------------')
    if message.text == 'Боевики 🤯':  
        bot.send_message(message.chat.id,'Топ 5 фильмов(Боевики)------------------------------------------------------------------------« Гнев человеческий » Wrath of Man  2021, 119 мин. Великобритания • боевик  Режиссёр: Гай Ричи В ролях: Джейсон Стэйтем, Холт Маккэллани Рейтинг Кинопоиска 7.67.61 240 173 оценки  (6584)--------------------------------------------------------------------------------------------« Брат 2 » ,2000, 127 мин. Россия • боевик  Режиссёр: Алексей Балабанов В ролях: Сергей Бодров мл., Виктор Сухоруков Рейтинг Кинопоиска 8.2.2508.2 (0785)--------------------------------------------------------------------------------------------« Переводчик »,The Covenant , 2022, 123 мин. Великобритания • боевик  Режиссёр: Гай Ричи В ролях: Джейк Джилленхол, Дар Салим Рейтинг Кинопоиска 7.97.9  (8463)--------------------------------------------------------------------------------------------« Дэдпул »,Deadpool , 2016, 108 мин. США • боевик  Режиссёр: Тим Миллер В ролях: Райан Рейнольдс, Морена Баккарин  Рейтинг Кинопоиска 7.6 7.6666 830 оценок (3243)--------------------------------------------------------------------------------------------« Шерлок Холмс » Sherlock Holmes , 2009, 128 мин. США • боевик  Режиссёр: Гай Ричи В ролях: Роберт Дауни мл., Джуд Лоу Рейтинг Кинопоиска 8.18.1656 711 оценок (6574)--------------------------------------------------------------------------------------------')
    if message.text == 'Сериалы 😶‍🌫️':   
        bot.send_message(message.chat.id,'Топ 5 Сериалы----------------------------------------------------------------------------------------« Во все тяжкие » Breaking Bad  2008–2013, 47 мин. США • криминал  Режиссёр: Мишель Макларен В ролях: Брайан Крэнстон, Анна Ганн Рейтинг Кинопоиска  9.0112 454 оценки (7464)--------------------------------------------------------------------------------------------« Друзья Friends » , 1994–2004, 5280 мин. США • комедия  Режиссёр: Гари Хэлворсон В ролях: Дженнифер Энистон, Кортни Кокс Рейтинг Кинопоиска 8.938 875 оценок  (6322)--------------------------------------------------------------------------------------------« Гравити Фолз » Gravity Falls , 2012–2016, 22 мин. США • мультфильм  Режиссёр: Джо Питт В ролях: Джейсон Риттер, Алекс Хирш Рейтинг Кинопоиска 8,8.894 686 оценок   (0593)--------------------------------------------------------------------------------------------« Тед Лассо , Ted Lasso », 2020–2023, 30 мин. США • комедия  Режиссёр: Деклан Лауни В ролях: Джейсон Судейкис, Бретт Голдстин Рейтинг Кинопоиска 8.70009 оценок (1234)--------------------------------------------------------------------------------------------« Рюриковичи ».  История первой династии 2019, 52 мин. Россия • история  Режиссёр: Максим Беспалый В ролях: Иван Петков, Дмитрий Могучев Рейтинг Кинопоиска 8.6. топ 2508.628 376 оценок (8433)--------------------------------------------------------------------------------------------')
    if message.text == 'Мультфилмы😜':  
        bot.send_message(message.chat.id,'Топ 5 фильмов (Мультфилмы)------------------------------------------------------------------------------« Человек-паук »: Паутина вселенных Spider-Man: Across the Spider-Verse 2023, 140 мин. США • мультфильм  Режиссёр: Жуакин Душ Сантуш В ролях: Шамеик Мур, Хейли Стайнфелд Рейтинг Кинопоиска 8.4. 8.4119 557 оценок (2744)--------------------------------------------------------------------------------------------« Элементарно » Elemental, 2023, 101 мин. США • мультфильм  Режиссёр: Питер Сон В ролях: Леа Льюис, Мамуду Ати Рейтинг Кинопоиска 7.77.766 972 оценки (0674)--------------------------------------------------------------------------------------------« Братья Супер Марио в кино»  The Super Mario Bros. Movie  2023, 92 мин. США • мультфильм  Режиссёр: Аарон Хорват В ролях: Крис Пратт, Чарли Дэй Рейтинг Кинопоиска 7.07.030 530 оценок (7421)--------------------------------------------------------------------------------------------« Три богатыря и Пуп Земли » 2023, 85 мин. Россия • мультфильм  Режиссёр: Константин Феоктистов В ролях: Олег Куликович, Валерий Соловьев Скоро в подписке Рейтинг Кинопоиска 5.75.720 507 оценок (7654)-------------------------------------------------------------------------------------------- « Тролли 3 » Trolls Band Together , 2023, 91 мин. США • мультфильм  Режиссёр: Уолт Дорн В ролях: Анна Кендрик, Джастин Тимберлейк Рейтинг Кинопоиска 6.46.48 063 оценки (9502)--------------------------------------------------------------------------------------------')    
    if message.text == 'Драмы 🥺':
        bot.send_message(message.chat.id,'Топ 5 фильмов (Драмы)-----------------------------------------------------------------------------------------« Кунг-фу жеребец » Long ma jing shen , 2023, 126 мин.Китай • драма  Режиссёр: Ларри Ян В ролях: Джеки Чан, Лю Хаоцюнь Рейтинг Кинопоиска 8.8.0380 492 оценки  (5647)--------------------------------------------------------------------------------------------« Мастер и Маргарита» 2023, 157 мин.Россия • драма  Режиссёр: Михаил Локшин В ролях: Аугуст Диль, Юлия Снигирь Рейтинг Кинопоиска 8.8.0123 388 оценок (8643)--------------------------------------------------------------------------------------------« Мой Хатико » Zhong quan ba gong , 2023, 125 мин. Китай • драма  Режиссёр: Сюй Ан В ролях: Фэн Сяоган, Хуан Сюн Рейтинг Кинопоиска 8.6.8.674 079 оценок (7693)--------------------------------------------------------------------------------------------« Идеальные дни » .Perfect Days  2023, 123 мин. Япония • драма  Режиссёр: Вим Вендерс В ролях: Кодзи Якусё, Ариса Накано Рейтинг Кинопоиска 8.28.24 369 оценок  (0658)--------------------------------------------------------------------------------------------« Шаг к мечте »: Раз и навсегда Re lie , 2023, 124 мин. Китай • драма  Режиссёр: Дун Чэнпэн В ролях: Хуан Бо, Ван Ибо Рейтинг Кинопоиска 8.18.11 914 оценок (2144)--------------------------------------------------------------------------------------------   ')
    if message.text == 'Новинки 🤩':
        bot.send_message(message.chat.id,'Топ 5 фильмов (Новинки )-------------------------------------------------------------------------------------------------« Джон Уик 4 »  John Wick: Chapter 4, 2023, 169 мин. США • боевик  Режиссёр: Чад Стахелски В ролях: Киану Ривз, Донни Йен Рейтинг Кинопоиска 7.67.6540 429 оценок (7549)--------------------------------------------------------------------------------------------« Уикенд с батей » About My Father , 2023, 90 мин. США • комедия  Режиссёр: Лора Террузо В ролях: Себастьян Манискалко, Роберт Де Ниро Рейтинг Кинопоиска 7.7.1258 900 оценок  (5283)--------------------------------------------------------------------------------------------« Оппенгеймер» Oppenheimer , 2023, 180 мин. США • биография  Режиссёр: Кристофер Нолан В ролях: Киллиан Мерфи, Эмили Блант Рейтинг Кинопоиска 8.2.8.2188 660 оценок (8420)--------------------------------------------------------------------------------------------Стражи Галактики. Часть 3 » Guardians of the Galaxy Vol. 3 , 2023, 150 мин. США • фантастика  Режиссёр: Джеймс Ганн В ролях: Крис Пратт, Карен Гиллан Рейтинг Кинопоиска 8.1.8.1162 414 оценок (5893)--------------------------------------------------------------------------------------------« Coco & Janbo » 2023 Казахстан • комедия  Режиссёр: Ернар Нургалиев В ролях: Жанболат Найзабеков, Салтанат Серкебаева Рейтинг Кинопоиска 7.17.118 149 оценок  (4321)--------------------------------------------------------------------------------------------') 
    if message.text == 'Детективы 🥸':
        bot.send_message(message.chat.id,'Топ 5 фильмов (Детективы)------------------------------------------------------------------------------------------------« Башня лотоса с благоприятными узорами » Lian hua lou , 2023, 45 мин. Китай • детектив  Режиссёр: Го Ху В ролях: Чэн И, Джозеф Цзэн Рейтинг Кинопоиска 9.09.0694 оценки (0548)--------------------------------------------------------------------------------------------« Формула преступления » 2019–..., 50 мин.Россия • детектив  Режиссёр: Сергей Виноградов В ролях: Алина Ланина, Андрей Горбачев Рейтинг Кинопоиска 8.8.95 966 оценок (6748)--------------------------------------------------------------------------------------------« Мы встретились случайно » Eojjeoda majuchin, geudae 2023, 70 мин. Корея Южная • детектив  Режиссёр: Кан Су-ён В ролях: Ким Дон-ук, Чин Ги-джу Рейтинг Кинопоиска 8.48.41 104 оценки (7532)--------------------------------------------------------------------------------------------« Вампиры средней полосы » 2021–..., 50 мин. Россия • детектив  Режиссёр: Антон Маслов В ролях: Юрий Стоянов, Татьяна Догилева Рейтинг Кинопоиска 8.8.3677 522 оценки  (9353)--------------------------------------------------------------------------------------------« Тайны Салфер-Спрингс » Secrets of Sulphur Springs  2021, 24 мин. США • детектив  Режиссёр: Роберт Дж. Метойер В ролях: Престон Оливер, Кайли Кёрран Рейтинг Кинопоиска 8.28.268 369 оценок (1293)--------------------------------------------------------------------------------------------') 
    if message.text == 'Аниме 😮‍💨':     
        bot.send_message(message.chat.id,'Топ 5 Аниме ------------------------------------------------------------------------------------------------« Твоё имя » (яп. 君の名は。 Кими но на ва.) — полнометражный аниме-фильм Макото Синкая. Анимацией занималась студия CoMix Wave Films, дистрибьютором фильма выступила компания Toho. Кинопоиск 8,4 из 10 оценок  (0000)--------------------------------------------------------------------------------------------« Магическая битва » (англ. "Magical Battle") - это аниме сериал жанра фэнтези и экшн, рассказывающий о мире, где люди и различные магические существа живут вместе в одном мире. Кинопоиск 8,2 из 10 оценки    (0000)--------------------------------------------------------------------------------------------« Доктор Стоун » – это фантастическое аниме о далеком будущем нашей планеты. Однажды загадочная вспышка на Солнце обращает все живое на Земле в камень. Кинопоиск8,2 из 10  (0000)--------------------------------------------------------------------------------------------« Наруто »  Сёнэн-манга Масаси Кисимото, рассказывающая о жизни шумного и непоседливого ниндзя-подростка Наруто Удзумаки, мечтающего достичь всеобщего признания и стать Хокагэ MyShows.me 4,3 из 5  (0000)--------------------------------------------------------------------------------------------« Необъятный океан », ори Китахара поступил в университет в прибрежном городке и снял комнату у семьи Котэгава. Глава семьи владеет магазинчиком снаряжения для дайвинга, но эта тематика не близка сердцу Кинопоиск 8 из 10 (0000)--------------------------------------------------------------------------------------------')
    if message.text == 'Манга 📔':
        bot.send_message(message.chat.id,'Топ 5 Манги-------------------------------------------------------------------------------------------« Берсерк » (1997-1998)  Анимация, Боевик, Приключения  Гатс, странствующий наемник, присоединяется к Банде Ястреба после поражения на дуэли от Гриффита, лидера и основателя группы ,8.7  Оценить  (1111)--------------------------------------------------------------------------------------------« Стальной алхимик » Братство (2009-2010) Анимация, Боевик, Приключения Два брата ищут Философский камень после того, как попытка оживить их умершую мать провалилась и оставила их в поврежденной физической форме. 9.1  Оценить  (1111)--------------------------------------------------------------------------------------------  Странное приключение Джоджо » (1993-2002) Анимация, Боевик, Приключения Три члена семьи Джостар, клана бойцов-экстрасенсов, отправляются на поиски уничтожения древнего врага своей семьи. 7.7  Оценить (1111)--------------------------------------------------------------------------------------------« One Piece » (1999– ) Анимация, Боевик, Приключения Манки Д. Луффи отправляется в приключение со своей пиратской командой в надежде найти величайшее сокровище в истории, известное как "One Piece". 9  Оценить (1111)--------------------------------------------------------------------------------------------« Наруто » (2002-2007) Анимация, Боевик, Приключения Наруто Узумаки, озорной ниндзя-подросток, борется за признание и мечтает стать хокаге, лидером деревни и сильнейшим ниндзя. 8.4  Оценить (1111)--------------------------------------------------------------------------------------------')                    
@bot.message_handler()
def hor(message):
    if message.text == '5471':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=UljkvGAx26s&pp=ygUi0KHQuNC90LjRgdGC0LXRgCDCuyBTaW5pc3RlciwgMjAxMg%3D%3D')
    if message.text == '6472':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=JQ0cLb9F3LQ&pp=ygUpINCQ0YHRgtGA0LDQuyDQntC90LvQsNC50L0gIMK7IEhvc3QsIDIwMjA%3D')
    if message.text == '7473':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=tap3hgzRBMM&pp=ygVY0J_QsNGA0LDQvdC-0YDQvNCw0LvRjNC90YvQtSDRj9Cy0LvQtdC90LjRj8K7LiDQodC60LjQvdCw0LzQsNGA0LjQvdC6ICBTa2luYW1hcmluaywgMjAyMg%3D%3D')
    if message.text == '8474':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=usj9B7wFXZM&pp=ygUfwqsg0KPQu9GL0LHQutCwIFNtaWxlIMK7LCAyMDIyLA%3D%3D')
    if message.text == '9475':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=jL_rGSffxdA&pp=ygUrwqvQlNCy0LAsINGC0YDQuCwg0LTQtdC80L7QvSwg0L_RgNC40LTQuCHCuw%3D%3D')
    if message.text == '0012':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=cSatbCwltW0&pp=ygUR0J7QtNC40L0g0LTQvtC80LA%3D')
    if message.text == '1804':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=Xf2kFDRCgvs&pp=ygUS0JHQuNGI0LDRgNCw0YjQutC4')
    if message.text == '3244':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=M8BkClTStAc&pp=ygUq0JrQstCw0YDRgtC40YDQsNC90YLRiyDQmtKv0YjRltC6INKb0rHQtNCw')
    if message.text == '8620':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=sGrG3qMrUbI&pp=ygUr0YXQvtGC0Y8g0LHRiyDQsiDQutC40L3QviAyINGC0YDQtdC50LvQtdGAIA%3D%3D')
    if message.text == '7634':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=5VDuAszp8Uw&pp=ygUw0LHQuNC30L3QtdGBINC_0L4g0LrQsNC30LDRhdGB0LrQuCDQsiDQuNC90LTQuNC4')
    if message.text == '6584': 
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=YLw55x-zOSo&pp=ygUh0JPQvdC10LIg0YfQtdC70L7QstC10YfQtdGB0LrQuNC5')
    if message.text == '0785':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=nLKginNe-dw&pp=ygUK0JHRgNCw0YIgMg%3D%3D')
    if message.text == '8463':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=rybU9w_CmQ8&pp=ygUW0J_QtdGA0LXQstC-0LTRh9C40LrCuw%3D%3D')
    if message.text == '3243':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=EmH6VNG8QEE&pp=ygUf0JTRjdC00L_Rg9C7IMK7LERlYWRwb29sICwgMjAxNg%3D%3D')
    if message.text == '6574':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=QFq-FJmYFaI&pp=ygUc0YjQtdGA0LvQvtC6INGF0L7Rg9C80YEgMjAwOQ%3D%3D')
    if message.text == '7464':  
      bot.send_message(message.chat.id,'https://www.youtube.com/@TravelingBrostherS')
    if message.text == '6322':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=b7CeLWNOzLI&pp=ygUl0JTRgNGD0LfRjNGPIEZyaWVuZHMgwrsgLCAxOTk04oCTMjAwNA%3D%3D')
    if message.text == '0593':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=un59TPPOgpY&pp=ygUm0LPRgNCw0LLQuNGC0Lgg0YTQvtC70Lcg0YLRgNC10LnQu9C10YA%3D')
    if message.text == '1234':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=_brkQNdfMxs&pp=ygUs0YLQtdC0INC70LDRgdGB0L4gdGVkIGxhc3Nvwrsg0YLRgNC10LnQu9C10YA%3D')
    if message.text == '8433':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=BbFZkkvIaDM&pp=ygUX0KDRjtGA0LjQutC-0LLQuNGH0Lggwrs%3D')
    if message.text == '2744':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=RE1vNn7tvX4&pp=ygU_wqvQp9C10LvQvtCy0LXQui3Qv9Cw0YPQuiDCuzog0J_QsNGD0YLQuNC90LAg0LLRgdC10LvQtdC90L3Ri9GF')
    if message.text == '0674':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=InT1dDToa1c&pp=ygUU0Y3Qu9C40LzQtdC90YLQsNC70Yw%3D')
    if message.text == '7421':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=DurflEd-1tE&pp=ygUv0LHRgNCw0YLRjNGPINGB0YPQv9C10YAg0LzQsNGA0LjQviDQsiDQutC40L3QviA%3D')
    if message.text == '7654':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=J3xIDk0K5BM&pp=ygUs0YLRgNC4INCx0L7Qs9Cw0YLRi9GA0Y8g0Lgg0L_Rg9C_INC30LXQvNC70Lg%3D')
    if message.text == '9502':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=vleN3wA8f98&pp=ygUT0YLRgNC-0LvQu9C4INGC0YDQuA%3D%3D')
    if message.text == '5647':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=vigcDo4iz0Y&pp=ygUc0JrRg9C90LMt0YTRgyDQttC10YDQtdCx0LXRhg%3D%3D')
    if message.text == '8643':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=8uCvGtkOvTg&pp=ygU30LzQsNGB0YLQtdGAINC4INC80LDRgNCz0LDRgNC40YLQsCAyMDIzINGC0YDQtdC50LvQtdGAIA%3D%3D')
    if message.text == '7693':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=TsaJmJg9RIc&pp=ygUXINCc0L7QuSDQpdCw0YLQuNC60L4gwrs%3D')
    if message.text == '0658':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=LNbXEe7ACWU&pp=ygUo0LjQtNC10LDQu9GM0L3Ri9C1INC00L3QuCDRgtGA0LXQudC70LXRgA%3D%3D')
    if message.text == '2144':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=rrW-TDDJuzM&pp=ygUv0YjQsNCzINC6INC80LXRh9GC0LUg0YDQsNC3INC4INC90LDQstGB0LXQs9C00LA%3D')
    if message.text == '7549':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=04dwrLbAaTE&pp=ygUT0JTQttC-0L0g0KPQuNC6IDTCuw%3D%3D')
    if message.text == '5283':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=v3IVA68tedA&pp=ygUp0YPQuNC60LXQvdC0INGBINCx0LDRgtC10Lkg0YLRgNC10LnQu9C10YA%3D')
    if message.text == '8420':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=zU2vtD7npd0&pp=ygUl0L7Qv9C_0LXQvdCz0LXQudC80LXRgCDRgtGA0LXQudC70LXRgA%3D%3D')
    if message.text == '5893':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=2_eT32RQpzo&pp=ygUw0YHRgtGA0LDQttC4INCz0LDQu9Cw0LrRgtC40LrQuCAzINGC0YDQtdC50LvQtdGA')
    if message.text == '4321':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=uUQnBJtKr5k&pp=ygUV0LrQvtC60L4g0LTQttCw0LzQsdC-')
    if message.text == '0548':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=MEZ3Zvs6v1U&pp=ygVG0JHQsNGI0L3RjyDQu9C-0YLQvtGB0LAg0YEg0LHQu9Cw0LPQvtC_0YDQuNGP0YLQvdGL0LzQuCDRg9C30L7RgNCw0LzQuA%3D%3D')
    if message.text == '6748':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=4Xwp0eCBFuQ&pp=ygU20YTQvtGA0LzRg9C70LAg0L_RgNC10YHRgtGD0L_Qu9C10L3QuNGPINGC0YDQtdC50LvQtdGA')
    if message.text == '7532':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=xmI_Li6p7qo&pp=ygVH0JzRiyDQstGB0YLRgNC10YLQuNC70LjRgdGMINGB0LvRg9GH0LDQudC90L4gMjAyMyDQutC-0YDQtdGPINCu0LbQvdCw0Y8%3D')
    if message.text == '9353':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=FvB7pius1yY&pp=ygUswqvQktCw0LzQv9C40YDRiyDRgdGA0LXQtNC90LXQuSDQv9C-0LvQvtGB0Ys%3D')
    if message.text == '1293':  
      bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=oIfdPtgTzG4&pp=ygUm0KLQsNC50L3RiyDQodCw0LvRhNC10YAt0KHQv9GA0LjQvdCz0YE%3D')
    if message.text == '0000':  
      bot.send_message(message.chat.id,'https://jut.su/anime/')
    if message.text == '1111':  
      bot.send_message(message.chat.id,'https://mangalib.me/?ref=404&ysclid=lsmqyw4u9u513891599')




@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id,f'Привет!,  {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'?')





bot.infinity_polling()















































































