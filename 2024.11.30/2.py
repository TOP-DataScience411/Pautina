import utils

def main() -> None:
    
    """ Запрашивает тект от пользователя и, 
    с помощью функции important_message() из модуля utils, выводит его"""
    message = input("текст сообщения:")

    print(utils.important_message(message))
    

main()



#текст сообщения:ЗАГОЛОВОК ПРОГРАММЫ
#=====================================================================================================================#
#                                                                                                                     #
#                                                 ЗАГОЛОВОК ПРОГРАММЫ                                                 #
#                                                                                                                     #
#=====================================================================================================================#
#>>> msg = "Белогорская крепость находилась в сорока верстах от Оренбурга». В первый же день Гринев познакомился с комендантом и его женой. На следующий день Петр Андреич познакомился с офицером Алексеем Иванычем Швабриным.Его отправили сюда «за смертоубийство» - «заколол поручика» во время поединка. Швабрин постоянно подшучивал над семейством коменданта. Дочь Миронова Марью Ивановну Швабрин описывал как «совершенную дурочку», поэтому сначала Петруша относился к ней с предубеждением. Однако через некоторое время она очень понравилась Петру Андреичу."

#>>> txt = utils.important_message(msg)
#>>> print(txt)
#=====================================================================================================================#
#                                                                                                                     #
#        Белогорская крепость находилась в сорока верстах от Оренбурга». В первый же день Гринев познакомился с       #
#   комендантом и его женой. На следующий день Петр Андреич познакомился с офицером Алексеем Иванычем Швабриным.Его   #
#     отправили сюда «за смертоубийство» - «заколол поручика» во время поединка. Швабрин постоянно подшучивал над     #
#   семейством коменданта. Дочь Миронова Марью Ивановну Швабрин описывал как «совершенную дурочку», поэтому сначала   #
#     Петруша относился к ней с предубеждением. Однако через некоторое время она очень понравилась Петру Андреичу.    #
#                                                                                                                     #
#=====================================================================================================================#

