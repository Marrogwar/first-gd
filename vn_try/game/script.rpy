﻿# Сценарий

# Определение персонажей игры.
define z = Character('Заря', color="#DF3A01")

# Игра начинается здесь:
label start:

    #Показать дату
    #show forestRide #Картинка, а не фон, поэтому show
    #Звук машины, движущейся по лесу

    #Анимация аварии
    #image forestCrash = Animation("forestCrash1.png", 0.3,
    #                               "forestCrash2.png", 0.3,
    #                               "forestCrash3.png", 0.3)

    #Добавить POV из машины, где открывается бардачок с аптечкой
    #Что-то с обработкой ран нужно и вылезанием из машины

    #show afterCrash #Тут она уже сидит у багажника

    #scene bg afterCrashPOV #От первого лица c телефоном в руке,
    #Считаю, что набор текста одновременно в двух окнах лишнее
    "Я не могу тебе объяснить, почему так получилось. Я скоро умру, и мне нужна твоя помощь."
    #show fullMoon
    #Затухание
    #Звук волков

    return
