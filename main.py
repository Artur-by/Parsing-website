# Файл по организации меню для выбора парсинга сайта, категорий, товаров
import Parsing_web

print(" Данная программа позволяет считать  и сохранить данный с заданного сайта ")

while True:
    inp_site = input(" Выберите сайт: 1 - sila.by, 2 - 21vek.by ")


    if inp_site == '1':
        inp_cat = input(" Выберите категорию товаров:\n"
                        " 1- Смартфоны, ноутбуки, компьютеры \n"
                        " 2- Телевизоры, аудио, фото \n"
                        " 3- Бытовая техника \n"
                        " 4- Встраиваемая техника \n"
                        " 5- Посуда и аксессуары \n"
                        " 6- Дом, сад, ремонт авто ")
        if inp_cat == '1':
            Parsing_web.start_parsing('ntkp_url.txt')
            inp = input("Продолжить парсинг?  Да - любая клавиша , 1-Выход ")
            if inp == '1':
                break
            else:
                continue
        elif inp_cat == '2':
            Parsing_web.start_parsing('av_url.txt')
            inp = input("Продолжить парсинг?  Да - любая клавиша , 1-Выход ")
            if inp == '1':
                break
            else:
                continue
        elif inp_cat == '3':
            Parsing_web.start_parsing('bt_url.txt')
            inp = input("Продолжить парсинг?  Да - любая клавиша , 1-Выход ")
            if inp == '1':
                break
            else:
                continue
        elif inp_cat == '4':
            Parsing_web.start_parsing('vt_url.txt')
            inp = input("Продолжить парсинг?  Да - любая клавиша , 1-Выход ")
            if inp == '1':
                break
            else:
                continue
        elif inp_cat == '5':
            Parsing_web.start_parsing('pa_url.txt')
            inp = input("Продолжить парсинг?  Да - любая клавиша , 1-Выход ")
            if inp == '1':
                break
            else:
                continue
        elif inp_cat == '6':
            Parsing_web.start_parsing('dsra_url.txt')
            inp = input("Продолжить парсинг?  Да - любая клавиша , 1-Выход ")
            if inp == '1':
                break
            else:
                continue

    elif inp_site == '2':
        print('В разработке!')
    else:
        break


# библиотека ссылок для категории Смартфоны, ноутбуки, компьютеры
'''ntpk_aksessuary_apple = 'https://sila.by/ntpk/aksessuary_apple'
page_aksessuary_apple = 1
ntpk_aksessuary_mobile = 'https://sila.by/ntpk/aksessuary_mobile'
page_aksessuary_mobile = 6
ntpk_aksessuary_dlya_noutbukov = 'https://sila.by/ntpk/aksessuary_dlya_noutbukov'
page_aksessuary_dlya_noutbukov = 3
ntpk_aksessuary_k_igrovym_pristavkam = 'https://sila.by/ntpk/aksessuary_k_igrovym_pristavkam'
page_aksessuary_k_igrovym_pristavkam = 1
ntpk_web_kamery = 'https://sila.by/ntpk/web-kamery'
page_web_kamery = 1
ntpk_vneshnie_akkumulyatory ='https://sila.by/ntpk/vneshnie_akkumulyatory'
page_vneshnie_akkumulyatory = 4
ntpk_external_hard_drive ='https://sila.by/ntpk/external_hard_drive'
page_external_hard_drive = 3
gaming = 'https://sila.by/gaming'
page_gaming = 1
ntpk_gejmpady = 'https://sila.by/ntpk/gejmpady-dzhojstiki-ruli'
page_gejmpady = 1
ntpk_graficheskie_planshety = 'https://sila.by/ntpk/graficheskie_planshety'
page_graficheskie_planshety = 1
ntpk_zarjadnie_ystroistva = 'https://sila.by/ntpk/zarjadnie_ystroistva'
page_zarjadnie_ystroistva = 5
ntpk_zashhitnye_plenki = 'https://sila.by/ntpk/zashhitnye_plenki_stekla'
page_zashhitnye_plenki = 7
ntpk_ibp = 'https://sila.by/ntpk/ibp'
page_ibp = 3
ntpk_igrovye_kresla = 'https://sila.by/ntpk/igrovye_kresla'
page_igrovye_kresla = 1
ntpk_igrovye_pristavki = 'https://sila.by/ntpk/igrovye_pristavki'
page_igrovye_pristavki = 1
ntpk_igry_k_pristavkam = 'https://sila.by/ntpk/igry_k_pristavkam'
page_igry_k_pristavkam = 3
ntpk_kabel_telefonny = 'https://sila.by/ntpk/kabel_telefonny'
page_kabel_telefonny = 1
ntpk_usb_flash = 'https://sila.by/ntpk/usb_flash'
page_usb_flash = 4
ntpk_klaviatury = 'https://sila.by/ntpk/klaviatury'
page_klaviatury = 4
ntpk_myshi_i_klaviatury = 'https://sila.by/ntpk/myshi_i_klaviatury'
page_myshi_i_klaviatury = 2
ntpk_monitory = 'https://sila.by/ntpk/monitory'
page_monitory = 7
ntpk_monobloki = 'https://sila.by/ntpk/monobloki'
page_monobloki = 1
ntpk_monopody = 'https://sila.by/ntpk/monopody'
page_monopody = 1
ntpk_kompyuternye_myshi ='https://sila.by/ntpk/kompyuternye_myshi'
page_hkompyuternye_myshi = 8
ntpk_garnitury_i_microfony = 'https://sila.by/ntpk/garnitury_i_microfony'
page_garnitury_i_microfony = 20
ntpk_noutbuki = 'https://sila.by/ntpk/noutbuki'
page_noutbuki = 23
ntpk_planshety = 'https://sila.by/ntpk/planshety'
page_planshety = 2
ntpk_printery_i_mfu = 'https://sila.by/ntpk/printery_i_mfu'
page_printery_i_mfu = 2
ntpk_provodnye_telefony = 'https://sila.by/ntpk/provodnye_telefony'
page_provodnye_telefony = 1
ntpk_radiotelefony = 'https://sila.by/ntpk/radiotelefony'
page_radiotelefony = 1
tpk_rashodnye_materialy = 'https://sila.by/ntpk/rashodnye_materialy'
page__rashodnye_materialy = 5
ntpk_setevoe_oborudovanie = 'https://sila.by/ntpk/setevoe_oborudovanie'
page_setevoe_oborudovanie = 4
ntpk_sistemnye_bloki = 'https://sila.by/ntpk/sistemnye_bloki'
page_sistemnye_bloki = 1
ntpk_mobilnye_telefony = 'https://sila.by/ntpk/mobilnye_telefony'
page__mobilnye_telefony = 15
ntpk_sumki_dlya_noutbukov = 'https://sila.by/ntpk/sumki_dlya_noutbukov'
page_sumki_dlya_noutbukov = 5
ntpk_smartwatch = 'https://sila.by/ntpk/smartwatch'
page_smartwatch = 11
ntpk_chehly = 'https://sila.by/ntpk/chehly'
page_chehly = 16
ntpk_chistyashhie_sredstva = 'https://sila.by/ntpk/chistyashhie_sredstva'
page_chistyashhie_sredstva = 1
ntpk_elektronnye_knigi = 'https://sila.by/ntpk/elektronnye_knigi'
page_elektronnye_knigi = 2'''


