import os

WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

banner = f'''{REDL}

  $$\      $$\ $$\ $$\       $$\                           $$\ $$\                  $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\ 
  $$ | $\  $$ |\__|$$ |      \__|                          $$ |\__|                $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|
  $$ |$$$\ $$ |$$\ $$ |  $$\ $$\  $$$$$$\   $$$$$$\   $$$$$$$ |$$\  $$$$$$\        $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ |   
  $$ $$ $$\$$ |$$ |$$ | $$  |$$ |$$  __$$\ $$  __$$\ $$  __$$ |$$ | \____$$\       $$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |   
  $$$$  _$$$$ |$$ |$$$$$$  / $$ |$$ /  $$ |$$$$$$$$ |$$ /  $$ |$$ | $$$$$$$ |      $$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |   
  $$$  / \$$$ |$$ |$$  _$$<  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |$$  __$$ |      $$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |   
  $$  /   \$$ |$$ |$$ | \$$\ $$ |$$$$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |\$$$$$$$ |       $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |   
  \__/     \__|\__|\__|  \__|\__|$$  ____/  \_______| \_______|\__| \_______|       \______/  \______/ \______|\__|  \__|   \__|   
                                 $$ |                                                                                              
                                 $$ |                                                                                              
                                 \__|                                                                                     
'''
page_emails = f'''
  {GNSL}Поиск по Email, Gmail {GNSL}                                 

  {REDL}01.{REDL} {GNSL}haveibeenpwned.com {GNSL} — {WHSL} проверка почты в слитых базах {WHSL}
  {REDL}02.{REDL} {GNSL}emailrep.io{GNSL} — {WHSL}найдет на каких сайтах был зарегистрирован аккаунт использующий определенную почту {WHSL}
  {REDL}03.{REDL} {GNSL}dehashed.com{GNSL} —{WHSL} проверка почты в слитых базах {WHSL}
  {REDL}04.{REDL} {GNSL}@Smart_SearchBot{GNSL} — {WHSL}найдет ФИО, дату рождения и адрес с телефоном{WHSL}
  {REDL}05.{REDL} {GNSL}intelx.io{GNSL} — {WHSL}многофункциональный поисковик, поиск осуществляется еще и по даркнету {WHSL}
  {REDL}06.{REDL} {GNSL}@mailsearchbot{GNSL} —{WHSL} ищет по базе, дает часть пароля{WHSL}
  {REDL}07.{REDL} {GNSL}@info_baza_bot{GNSL} —{WHSL} покажет из какой базы слита почта, 2 бесплатных скана{WHSL}
  {REDL}08.{REDL} {GNSL}leakedsource.ru{GNSL} —{WHSL} покажет в каких базах слита почта {WHSL}
  {REDL}09.{REDL} {GNSL}mostwantedhf.info{GNSL} —{WHSL} найдет аккаунт skype{WHSL}
  {REDL}10.{REDL} {GNSL}spiderfoot.net{GNSL} (r) — {WHSL}автоматический поиск с использованием огромного количества методов, можно использовать в облаке если пройти регистрацию {WHSL}
  {REDL}11.{REDL} {GNSL}reversegenie.com{GNSL} —{WHSL} найдет местоположение, Первую букву имени и номера телефонов{WHSL}
  {REDL}12.{REDL} {GNSL}@last4mailbot{GNSL} — {WHSL}бот найдет последние 4 цифры номера телефона клиента Сбербанка {WHSL}
  {REDL}13.{REDL} {GNSL}searchmy.bio {GNSL}— {WHSL}найдет учетную запись Instagram с электронной почтой в описании {WHSL}
  {REDL}14.{REDL} {GNSL}leakprobe.net{GNSL} —{WHSL} найдет ник и источник слитой базы {WHSL}
  {REDL}15.{REDL} {GNSL}recon.secapps.com{GNSL} —{WHSL} автоматический поиск и создание карт взаимосвязей{WHSL}
  {REDL}16.{REDL} {GNSL}account.lampyre.io {GNSL}(r) —{WHSL} веб версия поиска по email, поиск по аккаунтам  в соц. сетях и мессенджерам {WHSL}
  {REDL}17.{REDL} {GNSL}@EyeGodBot {GNSL}— {WHSL}найдет аккаунт в ВК и найдет утекшие пароли{WHSL}
  {REDL}18.{REDL} {GNSL}@GetPhone_bot{GNSL} —{WHSL} поиск в утекших базах {WHSL}
  {REDL}19.{REDL} {GNSL}@StealDetectorBOT {GNSL}— {WHSL}найдет утекшие пароли {WHSL}
  {REDL}20.{REDL} {GNSL}[TOP] @GetGmail_bot {GNSL}— {WHSL}бот найдет ID аккаунта, даст ссылку на Google Maps и альбомы, 2 бесплатных результата и бесконечное число попыток{WHSL}
  {REDL}21.{REDL} {GNSL}scylla.sh{GNSL} —{WHSL} поисковик по базам утечек, найдет пароли, IP, ники и многое другое, в поле поиска введите email: и после e-mail адрес {WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''

page_fio = f'''
  {REDL}01.{REDL}{GNSL}@egrul_bot{GNSL} —{WHSL} Найдет ИП и компании {WHSL}
  {REDL}02.{REDL}{GNSL}reestr-zalogov.ru{GNSL}— {WHSL} Поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д. {WHSL}
  {REDL}03.{REDL}{GNSL}https://zytely.rosfirm.info/m/ {GNSL} —{WHSL} Найдет адрес прописки и дату рождения, необходимо знать город {WHSL}
  {REDL}04.{REDL}{GNSL}mmnt.ru {GNSL}—{WHSL} Найдет упоминания в документах {WHSL}
  {REDL}05.{REDL}{GNSL}kad.arbitr.ru {GNSL} {WHSL} Дела, рассматриваемые арбитражными судами {GNSL}
  {REDL}06.{REDL}{GNSL}bankrot.fedresurs.ru {GNSL}— {WHSL} Поиск по банкротам, можно узнать ИНН, СНИЛС и адрес {WHSL}
  {REDL}07.{REDL}{GNSL}sudact.ru {GNSL}—{WHSL} Судебные и нормативные акты РФ, поиск по участникам и судам {WHSL}
  {REDL}08.{REDL}{GNSL}spra.vkaru.net{GNSL} —{WHSL} Телефонный справочник по России, Украине, Белоруссии, Казахстану, Литве и Молдове{WHSL}
  {REDL}09.{REDL}{GNSL}fssprus.ru http://fssprus.ru/iss/ip/ {GNSL} —{WHSL} Проверка задолженностей, для физ. лица {WHSL}
  {REDL}10.{REDL}{GNSL}fio.stop-list.info{GNSL} —{WHSL} Поиск по ИП и судам, если есть ИНН, то можно узнать больше {WHSL}
  {REDL}11.{REDL}{GNSL}gcourts.ru {GNSL}— {WHSL} Поиск решений судов общей юрисдикции {WHSL}
  {REDL}12.{REDL}{GNSL}service.nalog.ru https://service.nalog.ru/inn.do {GNSL}— {WHSL} Найдет ИНН, нужно знать полное ФИО, дату рождения и документ удостоверяющий личность{WHSL}
  {REDL}13.{REDL}{GNSL}reestr-dover.ru https://www.reestr-dover.ru/revocations {GNSL} —{WHSL} Поиск в списке сведений об отмене доверенности {WHSL}
  {REDL}14.{REDL}{GNSL}судебныерешения.рф {GNSL}—{WHSL} Найдет судебные решения, документы с ФИО датой и статьей {WHSL}
  {REDL}15.{REDL}{GNSL}notariat.ru{GNSL} —{WHSL} Поиск в реестре наследственных дел, найдет дату смерти человека и адрес нотариуса оформившее дело {WHSL}
  {REDL}16.{REDL}{GNSL}@EyeGodsBot {GNSL}—{WHSL} Обратный поиск по GetContact, находит часть номера телефона {WHSL}
  {REDL}17.{REDL}{GNSL}@imole_bot{GNSL} {WHSL} Поиск по слитым базам, находит паспорт, прописку, авто, ИП и многое другое, нужно знать год, или месяц, или день рождения {WHSL}
  {REDL}18.{REDL}{GNSL}nalog.ru (https://service.nalog.ru/inn.do) {GNSL}— {WHSL} Найдет ИНН, необходимо указать дату рождения и паспортные данные{WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_numbers = f'''
  {WHSL}Поиск по номерам России {WHSL}
  {GNSL}Осторожнее с ботами, не использовать со своим номером, не давать доступ к контактам приложению telegram во время использования ботов. {GNSL}

  {REDL}01.{REDL}{GNSL}@Smart_SearchBot{GNSL} —{WHSL} Найдет ФИО, дату рождения и адрес {WHSL}
  {REDL}03.{REDL}{GNSL}@mailsearchbot{GNSL}—{WHSL} Найдет часть пароля {WHSL}
  {REDL}06.{REDL}{GNSL}@get_kontakt_bot {REDL}—{WHSL} Найдет как записан номер в контактах, большая база контактов/ НЕ В КОЕМ СЛУЧАИ НЕ ДАВАЙ ДОСТУП К КОНТАКТАМ{WHSL} 
  {REDL}07.{REDL}{GNSL}PhoneInfoga https://demo.phoneinfoga.crvx.fr/#/ {GNSL}—{WHSL} Определят тип номера, дает дорки для номера, определяет город {WHSL}
  {REDL}08.{REDL}{GNSL}truecaller.com{GNSL} —{WHSL} Телефонная книга, найдет имя и оператора телефона {GNSL}
  {REDL}09.{REDL}{GNSL}mirror.bullshit.agency {GNSL}—{WHSL} Поиск объявлений по номеру телефона {WHSL}
  {REDL}10.{REDL}{GNSL}bases-brothers.ru {GNSL}—{WHSL} Поиск номера в объявлениях {WHSL}
  {REDL}11.{REDL}{GNSL}account.live.com {GNSL}—{WHSL} Проверка привязанности номера к microsoft аккаунту{WHSL}
  {REDL}12.{REDL}{GNSL}avinfo.guru {GNSL}—{WHSL} Проверка телефона владельца авто, иногда нужен VPN {WHSL}
  {REDL}13.{REDL}{GNSL}telefon.stop-list.info {GNSL} —{WHSL} Поиск по всем фронтам, иногда нет информации{WHSL}
  {REDL}14.{REDL}{GNSL}spravnik.com {GNSL} —{WHSL} Поиск по городскому номеру телефона, найдет ФИО и адрес {WHSL}
  {REDL}15.{REDL}{GNSL}nuga.app{GNSL} —{WHSL} Найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка {WHSL}
  {REDL}16.{REDL}{GNSL}@MyGenisBot {GNSL} {WHSL} Найдет имя и фамилию владельца номера {WHSL}
  {REDL}17.{REDL}{GNSL}contacts.google.com{GNSL} —{WHSL} Находит аккаунт в Google, чтобы узнать как его находить нажмите - /GoogleID {WHSL}
  {REDL}18.{REDL}{GNSL}@usersbox_bot {GNSL} —{WHSL} Найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер {WHSL}
  {REDL}20.{REDL}{GNSL}mysmsbox.ru {GNSL} —{WHSL} Определяет чей номер, поиск в Instagram, VK, OK, FB, а так же найдет аккаунты в мессенджерах {WHSL}
  {REDL}23.{REDL}{GNSL}imole_bot{GNSL}{WHSL} Поиск по слитым базам, находит данные владельца номера, доступна всего 1 бесплатная попытка на аккаунт {WHSL}
  {REDL}24.{REDL}{GNSL}@GetFb_bot {GNSL} —{WHSL} Бот находит Facebook {WHSL}
  {REDL}25.{REDL}{GNSL}globfone.com (https://globfone.com/call-phone/) {GNSL}—{WHSL} Бесплатные анонимные звонки на любой номер телефона {WHSL}
  {REDL}26.{REDL}{GNSL}@phone_avito_bot{GNSL}—{WHSL} Найдет аккаунт на Авито {WHSL}
  {REDL}27.{REDL}{GNSL}@Quick_OSINT_bot {GNSL}{WHSL} Найдет оператора, email, адрес, как записан в контактах и многое другое {WHSL}
  {REDL}28.{REDL}{GNSL}https://pipl.com/ {GNSL}-{WHSL} Поисковик по социальным сетям {WHSL}
  {REDL}29.{REDL}{GNSL}https://where-you.com/{GNSL}-{WHSL} Поисковик по социальным сетям(СНГ) {WHSL}
  {REDL}30.{REDL}{GNSL}http://vk.city4me.com/ {GNSL}-{WHSL} Шпион ВК {WHSL}
  {REDL}31.{REDL}{GNSL}https://www.social-searcher.com/{GNSL}-{WHSL} Все посты пользователя {WHSL}
  {REDL}32.{REDL}{GNSL}http://socialmention.com/ {GNSL}-{WHSL} Все упоминания о человеке {WHSL}
  {REDL}33.{REDL}{GNSL}http://nomerorg.me/{GNSL} -{WHSL} Телефонная база СНГ (только крупные города) {WHSL}
  {REDL}34.{REDL}{GNSL}https://phonenumber.to/{GNSL} -{WHSL} Поиск по номеру телефона, адрессу, ФИО {WHSL}
  {REDL}35.{REDL}{GNSL}http://spra.vkaru.net/{GNSL} -{WHSL} Телефонный справочник Россия, Украина, Беларусь, Казахстан, Латвия, Молдова {WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_browsers = f'''{WHSL}
  {REDL}01.{REDL}{GNSL}xinit.ru https://xinit.ru/whois/ {GNSL} — {WHSL} Тотальный скан сайта по всем направлениям {WHSL}
  {REDL}03.{REDL}{GNSL}@WhoisDomBot{GNSL}—{WHSL} Узнать информацию об домене {WHSL}
  {REDL}04.{REDL}{GNSL}riskiq.com {GNSL} —{WHSL} Автоматизированный поиск по всем фронтам {WHSL}
  {REDL}05.{REDL}{GNSL}Knock Subdomain Scan (https://github.com/guelfoweb/knock) {GNSL}—{WHSL} Находит субдомены и FTP {WHSL}
  {REDL}06.{REDL}{GNSL}builtwith.com — Технологический профиль сайта, взаимосвязи между сайтами
  {REDL}07.{REDL}{GNSL}crimeflare.org (http://www.crimeflare.org:82/cfs.html) {GNSL} {WHSL} — Сloudflare Раскрыватель {WHSL}
  {REDL}08.{REDL}{GNSL}cyber-hub.net (https://cyber-hub.net/domain_resolver.php) {GNSL} {WHSL} — Распознаватель cloudflare, статус DNS, перебор поддоменов{WHSL}
  {REDL}09.{REDL}{GNSL}suip.biz (https://suip.biz/ru/?act=amass) {GNSL} —{WHSL} Быстрый и мощный поиск субдоменов, найдет все {WHSL}
  {REDL}10.{REDL}{GNSL}urlscan.io {GNSL} {WHSL} Сервис для сканирования и анализа сайтов {WHSL}
  {REDL}11.{REDL}{GNSL}dnsdumpster.com {GNSL} —{WHSL} Инструмент исследования домена который может обнаружить хосты связанные с доменом {WHSL}
  {REDL}12.{REDL}{GNSL}cachedview.com {GNSL}—{WHSL} Поиск по кэшу Google {WHSL}
  {REDL}13.{REDL}{GNSL}recon.secapps.com (https://recon.secapps.com/) {GNSL} {WHSL} — Автоматический поиск и создание карт взаимосвязей {WHSL}
  {REDL}14.{REDL}{GNSL}censys.io {GNSL}—{WHSL} Находит какие серверы и устройства выставлены в сети{WHSL}
  {REDL}15.{REDL}{GNSL}virustotal.com {GNSL} —{WHSL} Служба пассивного DNS, поиск суб-доменов, поиск в whois и история сертификатов SSL {WHSL}
  {REDL}16.{REDL}{GNSL}atsameip.intercode.ca {GNSL} —{WHSL} Найдет одинаковые IP у сайта, можно узнать субдомены {WHSL}
  {REDL}17.{REDL}{GNSL}spiderfoot.net {GNSL}(r) —{WHSL} Автоматический поиск с использованием огромного количества методов{WHSL}
  {REDL}18.{REDL}{GNSL}oldweb.today {GNSL} — {WHSL} Просмотреть исторические версии сайтов, можно выбрать вид браузера и дату{WHSL}
  {REDL}19.{REDL}{GNSL}crimeflare.net (http://crimeflare.net:83/repeats.html) {GNSL} {WHSL} Дает возможность узнать настоящий IP адрес сайта за CloudFlare {WHSL}
  {REDL}20.{REDL}{GNSL}dirhunt (https://github.com/Nekmo/dirhunt) (t) {GNSL}—{WHSL} Поиск директорий сайта без брута{WHSL}
  {REDL}21.{REDL}{GNSL}Amass (https://github.com/OWASP/Amass) (t) {GNSL}—{WHSL} Сетевое картирование поверхностей атаки и обнаружение внешних ресурсов. {WHSL}
  {REDL}22.{REDL}{GNSL}Photon (https://github.com/s0md3v/Photon) {GNSL} —{WHSL} Найдет на сайте файлы, секретные ключи, JS файлы, URL с параметрами {WHSL}
  {REDL}23.{REDL}{GNSL}spyse.com (https://spyse.com/search/subdomain) {GNSL} —{WHSL} Поиск поддоменов{WHSL} 
  {REDL}24.{REDL}{GNSL}webcookies.org {GNSL} —{WHSL} Анализ cookies сайта {WHSL}
  {REDL}25.{REDL}{GNSL}dnslytics.com (https://dnslytics.com/reverse-analytics) {GNSL} —{WHSL} Сайт помогает найти трекеры на сайте{WHSL}
  {REDL}26.{REDL}{GNSL}domainwat.ch {GNSL} {WHSL} Может искать информацию такую как имя регистранта, адрес, номер телефона{WHSL}
  {REDL}27.{REDL}{GNSL}findomain (https://github.com/Edu4rdSHL/findomain) {GNSL} —{WHSL} Ищет поддомены{WHSL}
  {REDL}28.{REDL}{GNSL}yuleak.com {GNSL} — {WHSL} Найдет серверы, домены, поддомены, услуги, darkweb, пароли, уязвимости, идентификаторы и многое другое {WHSL}
  {REDL}29.{REDL}{GNSL}shodan.io{GNSL} {WHSL} Найдет IP адреса и сайты с упоминанием искомого сайта {WHSL}
  {REDL}30.{REDL}{GNSL}phonebook.cz {GNSL}—{WHSL} Найдет e-mails, субдомены, директории сайта {WHSL}
  {REDL}31.{REDL}{GNSL}visualsitemapper.com (http://www.visualsitemapper.com/) {GNSL}—{WHSL} Визуализация карты сайта одним грaфиком{WHSL}
  {REDL}32.{REDL}{GNSL}@iptools_robot{GNSL} —{WHSL} Бот для быстрого поиска информации о домене и ip адресе, найдет whois, настоящий IP за Cloudflare{WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_mail = f'''
  {WHSL}Находим профиль в сервисе Мой Мир                     Узнаем ID пользователя {GNSL}
  http://my.mail.ru/mail/НИКНЕЙМ                        http://appsmail.ru/platform/mail/НИКНЕЙМ {WHSL}

  Ищем по никнейму в соцсетях {GNSL} 
  https://go.mail.ru/search_social?q=НИКНЕЙМ {WHSL}

  Получаем аватарку {GNSL}
  http://filin.mail.ru/pic?width=180&height=180&email=example@mail.ru {WHSL}

  Восстановление пароля                                 Ищем аккаунты через соцсети {GNSL}
  https://account.mail.ru/recovery                      my.mail.ru/ok/ОДНОКЛАССНИКИ_ID
  https://github.com/martinvigo/email2phonenumber       my.mail.ru/vk/ВКОНТАКТЕ_ID
                                                        my.mail.ru/fb/ФЕЙСБУК_ID  {WHSL}
  Ищем аккаунты через адрес эл.почты {GNSL}

  my.mail.ru/gmail.com/LOGIN (часть email без @gmail.com)
  my.mail.ru/yandex.ru/LOGIN (часть email без @yandex.ru)
  my.mail.ru/mail/LOGIN (часть email без @mail.ru)
  my.mail.ru/SITE/LOGIN (поиск по любому никнейму)
  
  {WHSL}Узнаем владельца яндекс почты. При помощи ID

  {WHSL}Переходим на yandex.ru/collections/user/НИКНЕЙМ. Нажимаем правой кнопкой мыши и выбираем "Просмотр кода страницы"
  находим "public_id" и публичный ID рядом (например: c48fhxw0qppa50289r5c9ku4k4)
  Подставляем public_id в ссылки
        {GNSL}
  https://yandex.ru/user/public_id
  https://yandex.ru/collections/user/public_id
  https://zen.yandex.ru/user/public_id
  https://yandex.ru/q/profile/public_id
  https://local.yandex.ru/users/public_id
  https://n.maps.yandex.ru/#!/users/public_id
        {WHSL}
  Восстановление пароля
        {GNSL}
  https://passport.yandex.ru/auth/restore/password
  https://github.com/martinvigo/email2phonenumber

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
banner_end = f'''
  {WHSL}Дата последнего обновления:{GNSL} вторник 26 Февраля 2021г. {GNSL}Проматай вверх сразу.

{REDL}__________________________________________________________________________________________________________________________________{WHSL}

  {GNSL}[ {REDL}99{GNSL} ] {WHSL}Выйти в главное меню...

'''

page_ip = f'''{REDL}
  {WHSL}OSINT IP адреса

  {REDL}01.{REDL}{GNSL}HostHunter https://github.com/SpiderLabs/HostHunter {WHSL} — обнаружение и извлечение имен хостов из набора целевых IP-адресов
  {REDL}02.{REDL}{GNSL}censys.io {WHSL} находит какие серверы и устройства выставлены в сети.
  {REDL}03.{REDL}{GNSL}cyber-hub.net https://cyber-hub.net/ip2skype.php — {WHSL} Найдет Skype аккаунт.
  {REDL}04.{REDL}{GNSL}spiderfoot.net — {WHSL}Автоматический поиск с использованием огромного количества методов, 
              ножно использовать в облаке если пройти регистрацию.
  {REDL}05.{REDL}{GNSL}iknowwhatyoudownload http://iknowwhatyoudownload.com — {WHSL} Покажет что скачивают в интернете
  {REDL}06.{REDL}{GNSL}recon.secapps.com https://recon.secapps.com/ {WHSL} Автоматический поиск и создание карт взаимосвязей.
  {REDL}07.{REDL}{GNSL}check.torproject.org https://check.torproject.org/cgi-bin/TorBulkExitList.py {WHSL} — 
              найдет список всех выходных узлов Tor за последние 16 часов, которые мог связаться с IP
  {REDL}08.{REDL}{GNSL}dnslytics.com https://dnslytics.com/reverse-ip — {WHSL} Найдет домены.
  {REDL}09.{REDL}{GNSL}yuleak.com — {WHSL} Найдет серверы, домены, поддомены, услуги, darkweb, пароли, уязвимости, идентификаторы и многое другое.

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_nicknames_2 = f'''
  {REDL}01.{REDL}{GNSL} https://namecheckup.com - {WHSL} Проверка сайтов и приложений
  {REDL}02.{REDL}{GNSL} https://nstantusername.com - {WHSL} Проверка сайтов и приложений
  {REDL}03.{REDL}{GNSL} https://suip.biz - {WHSL} Проверь 300 сервисов, работает очень медленно
  {REDL}04.{REDL}{GNSL} https://namechk.com - {WHSL} Проверка сайтов, приложений и доменных имен
  {REDL}05.{REDL}{GNSL} sherlock https://github.com/sherlock-project/sherlock - {WHSL} Поиск аккаунта с этим ником
  {REDL}06.{REDL}{GNSL} https://elody.com - {WHSL} Поиск по сайтам, поиск аккаунтов с таким же старым ником, поиск долго
  {REDL}07.{REDL}{GNSL} @mailsearchbot - {WHSL} Поиск пароля, поиск по логину
  {REDL}08.{REDL}{GNSL} https://whatsmyname.app - {WHSL} Быстрая проверка сайтов
  {REDL}09.{REDL}{GNSL} https://boardreader.com - {WHSL} Поисковик по форумам, также поиск по нику
  {REDL}10.{REDL}{GNSL} https://leakedsource.ru - {WHSL} Поиск по базам данных.
  {REDL}11.{REDL}{GNSL} http://dumpedlqezarfife.onion -  {WHSL} Найдет письмо с паролем
  {REDL}12.{REDL}{GNSL} https://Leakprobe.net - {WHSL} Найдет адрес электронной почты и источник утечки базы данных.
  {REDL}13.{REDL}{GNSL} https://yasni.com - {WHSL} Автоматический поиск в Интернете.
  {REDL}14.{REDL}{GNSL} https://social-searcher.com - {WHSL} Найдет упоминания в социальных сетях и на сайтах
  {REDL}15.{REDL}{GNSL} https://socialmention.com - {WHSL} Найдет упоминания 
  {REDL}16.{REDL}{GNSL} https://namecheckup.com{GNSL}—{WHSL} Найдет аккаунты с искомым ником{WHSL}
  {REDL}17.{REDL}{GNSL} https://instantusername.com{GNSL} —{WHSL} Проверка по сайтам и приложениям{WHSL}
  {REDL}18.{REDL}{GNSL} https://suip.biz/ru/?act=sherlock {GNSL} — {WHSL} Автоматический поиск по 300 сервисам
  {REDL}19.{REDL}{GNSL} https://namechk.com{GNSL} — {WHSL} Проверка по сайтам, приложениям и доменам {WHSL}
  {REDL}20.{REDL}{GNSL} sherlock http://github.com/sherlock-project/sherlock {GNSL} —{WHSL} Поиск аккаунтов с таким ником {WHSL}
  {REDL}21.{REDL}{GNSL} @mailsearchbot{GNSL} — {WHSL} Найдет часть пароля, поиск по логину{WHSL}
  {REDL}22.{REDL}{GNSL} https://whatsmyname.app{GNSL} —{WHSL} Очень быстрый поиск по сотням сайтов{WHSL}
  {REDL}23.{REDL}{GNSL} https://boardreader.com{GNSL} —{WHSL} Поисковик по форумам, ищет и по нику{WHSL}
  {REDL}24.{REDL}{GNSL} https://leakedsource.ru{GNSL} —{WHSL} Покажет в каких базах есть ник{WHSL}
  {REDL}25.{REDL}{GNSL} https://dumpedlqezarfife.onion {GNSL} — {WHSL} Найдет почту с паролем{WHSL}
  {REDL}26.{REDL}{GNSL} https://leakprobe.net/search.php {GNSL} —{WHSL} Найдет почту и источник слитой базы {WHSL} 
  {REDL}27.{REDL}{GNSL} http://www.yasni.com/ {GNSL} —{WHSL} Автоматический поиск по интернету {WHSL}
  {REDL}28.{REDL}{GNSL} https://social-searcher.com {GNSL}— {WHSL} Найдет упоминания в соц. сетях и на сайтах{WHSL}
  {REDL}29.{REDL}{GNSL} http://socialmention.com {GNSL}—{WHSL} Найдет упоминания{WHSL}
  {REDL}30.{REDL}{GNSL} @StealDetectorBOT{GNSL}—{WHSL} Найдет утекшие пароли аккаунта{WHSL}
  {REDL}31.{REDL}{GNSL} https://pastebeen.com {GNSL} —{WHSL} Поиск в базе текстов pastebin, поиск может занять несколько часов {WHSL}
  {REDL}32.{REDL}{GNSL} scylla.sh{GNSL} —{WHSL} Поисковик по базам утечек, найдет пароли
  {REDL}33.{REDL}{GNSL} Maigret https://github.com/soxoj/maigret {GNSL}  —{WHSL} Найдет аккаунты с таким же ником
{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_phones = f'''
  {WHSL}Поиск по телефону Боты telegram 2 / Используйте осторожно, с левых номеров ( аккаунтов )


  {REDL}01.{REDL}{GNSL}@Quick_OSINT_bot —{WHSL} найдет оператора, email, как владелец записан в контактах, 
             базах данных и досках объявлений, аккаунты в соц. сетях и мессенджерах, в каких чатах состоит, документы, адреса и многое другое
  {REDL}02.{REDL}{GNSL}@clerkinfobot —{WHSL} бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
  {REDL}03.{REDL}{GNSL}@dosie_Bot —{WHSL} как и в боте uabaza дает информацио о паспорте только польностью, 3 бесплатные попытки
  {REDL}04.{REDL}{GNSL}@find_caller_bot —{WHSL} найдет ФИО владельца номера телефона
  {REDL}05.{REDL}{GNSL}@get_caller_bot —{WHSL} поиск по утечкам персональных данных и записным книгам абонентов, может найти ФИО, дату рождения, e-mail
  {REDL}06.{REDL}{GNSL}@get_kolesa_bot —{WHSL} найдет объявления на колеса.кз
  {REDL}07.{REDL}{GNSL}@get_kontakt_bot —{WHSL} найдет как записан номер в контактах, дает результаты что и getcontact
  {REDL}08.{REDL}{GNSL}@getbank_bot —{WHSL} дает номер карты и полное ФИО клиента банка
  {REDL}09.{REDL}{GNSL}@GetFb_bot —{WHSL} бот находит Facebook
  {REDL}10.{REDL}{GNSL}@GetPhone_bot — {WHSL} поиск номера телефона в утекших базах
  {REDL}11.{REDL}{GNSL}@Getphonetestbot —{WHSL}бот берет данные из приложения getcontact, показывает как записан номер телефона в контактах
  {REDL}12.{REDL}{GNSL}@info_baza_bot —{WHSL} поиск в базе данных
  {REDL}13.{REDL}{GNSL}@mailsearchbot —{WHSL} найдет часть пароля
  {REDL}14.{REDL}{GNSL}@MyGenisBot — {WHSL}найдет имя и фамилию владельца номера
  {REDL}15.{REDL}{GNSL}@phone_avito_bot —{WHSL} найдет аккаунт на Авито
  {REDL}16.{REDL}{GNSL}@SafeCallsBot — {WHSL}бесплатные анонимные звонки на любой номер телефона с подменой Caller ID
  {REDL}17.{REDL}{GNSL}@usersbox_bot — {WHSL}бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_resources = f'''{WHSL}
  {REDL}01.{REDL}{GNSL}lampyre.io —{WHSL} программа выполняет поиск аккаунтов, паролей и многих других данных
  {REDL}02.{REDL}{GNSL}avinfo.guru —{WHSL} проверка телефона владельца авто, иногда нужен VPN
  {REDL}03.{REDL}{GNSL}fa-fa.kz —{WHSL} найдет ФИО, проверка наличия задолженностей, ИП, и ограничения на выезд
  {REDL}04.{REDL}{GNSL}getcontact.com —{WHSL} найдет информацию о том как записан номер в контактах
  {REDL}05.{REDL}{GNSL}globfone.com —{WHSL} бесплатные анонимные звонки на любой номер телефона
  {REDL}06.{REDL}{GNSL}mirror.bullshit.agency —{WHSL} поиск объявлений по номеру телефона
  {REDL}07.{REDL}{GNSL}mysmsbox.ru — {WHSL}определяет чей номер, поиск в Instagram, VK, OK, FB, Twitter, 
             поиск объявлений на Авито, Юла, Из рук в руки, а так же найдет аккаунты в мессенджерах
  {REDL}08.{REDL}{GNSL}nuga.app — {WHSL}найдет Instagram аккаунт, авторизация через Google аккаунт и всего 1 попытка
  {REDL}09.{REDL}{GNSL} umberway.com — {WHSL}найдет телефонный справочник
  {REDL}10.{REDL}{GNSL}personlookup.com.au —{WHSL} найдет имя и адрес
  {REDL}11.{REDL}{GNSL}phoneInfoga.crvx.fr — {WHSL}определят тип номера, дает дорки для номера, определяет город
  {REDL}12.{REDL}{GNSL}spravnik.com —{WHSL} поиск по городскому номеру телефона, найдет ФИО и адрес
  {REDL}13.{REDL}{GNSL}spravochnik109.link —{WHSL} поиск по городскому номеру телефона, найдет ФИО и адрес
  {REDL}14.{REDL}{GNSL}teatmik.ee — {WHSL}поиск в базе организаций, ищет номер в контактах
  {REDL}15.{REDL}{GNSL}truecaller.com —{WHSL} телефонная книга, найдет имя и оператора телефона
{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_restore = f'''
  {WHSL}Восстановление доступа

  {REDL}1.{REDL}{GNSL}ICQ — icq.com/password/ru
  {REDL}2.{REDL}{GNSL}Yahoo — login.yahoo.com/?display=login
  {REDL}3.{REDL}{GNSL}Steam — help.steampowered.com/ru/wizard/HelpWithLoginInfo
  {REDL}4.{REDL}{GNSL}Twitter — twitter.com/account/begin_password_reset
  {REDL}5.{REDL}{GNSL}VK.com — vk.com/restore
  {REDL}6.{REDL}{GNSL}Facebook — facebook.com/login/identify?ctx=recover
  {REDL}7.{REDL}{GNSL}Microsoft — account.live.com/acsr
  {REDL}8.{REDL}{GNSL}Instagram — instagram.com/accounts/password/reset

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_maps = f'''

 {WHSL} Все уже автоматизированно для вас в главном меню.


{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_vk_osint = f'''

  {WHSL}OSINT в vk.

  Узнаем регистрационные данные {GNSL}

  https://regvk.com
  https://regvk.com/id
  https://vk.com/foaf.php?id=ВВЕДИТЕ_ID
  https://valery.shostak.ru/vk
  @Quick_OSINT_bot
{WHSL}
  Упоминания пользователя {GNSL}

  https://vk.com/feed?obj=1379097&q=&section=mentions1379097 - номер ID
{WHSL}
  Закрытый аккаунт{GNSL}

  https://online-vk.ru/pivatfriends.php?id=123456789  {WHSL}

  Поиск в сохраненных профилях {GNSL}

  https://ruprofile.pro/vk_user/id123456789
  https://rusfinder.pro/vk/user/id123456789 {WHSL}

  Полноценные сервисы по ВК {GNSL}

  http://vk.city4me.com
  https://220vk.com
  https://vkdia.com

{WHSL}
  Строим дерево связей {GNSL}

  https://www.yasiv.com/vk {WHSL}

  Архив страницы в ВК {GNSL}

  https://archive.org
  https://www.google.ru
  https://vk.watch/ID/profile
{WHSL}
{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_offenosint = f'''{WHSL}
  OffenOsint Virtual Machine - Виртуальная машина OffenOsint

  Система собрана для исключения необходимости развертывания боевого дистрибутива с нуля при работе на новой машине. 
  Сочетает в себе мощные инструменты активной разведки репозитария Kali Linux, 
  несколько фреймворков разведки полного цикла, прочие наиболее полезные скрипты, 
  инструменты для анонимизации своих действий в сети, инструменты  анализа собранных данных, а так же инструменты визуализации. 
  Plug and Play.
{GNSL}
  https://github.com/Double2Sky/OffenOsint

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_instagram_osint = f'''{WHSL}

  Определение Instagram ID {GNSL}
  https://codeofaninja.com/tools/find-instagram-user-id {WHSL}

  Определение аккаунта по телефону {GNSL}
  https://nuga.app/ {WHSL}

  Восстановление пароля {GNSL}
  https://www.instagram.com/accounts/password/reset/ {WHSL}

  Архив страницы {GNSL}
  https://archive.org/
  https://www.google.ru/
  https://yandex.ru/ {WHSL}

  Выгрузка данных бизнес-аккаунта {GNSL}
  https://i.instagram.com/api/v1/users/profilePage_ID/info/ {WHSL}

  JSON формат страницы {GNSL}
  https://www.instagram.com/НИКНЕЙМ/?__a=1  {WHSL}

  Анализ профиля {GNSL}

  https://picalytics.ru/ 
  https://minter.io/
  https://nativeflow.io/

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_ru_gov = f'''{WHSL}
  Оценка благонадежности граждан России.

  Нахождение в розыске {GNSL}

  https://www.interpol.int/notice/search/wanted
  https://mvd.ru/wanted
  http://fsin.su/criminal/
  https://fssp.gov.ru/iss/ip_search
{WHSL}
  Список террористов {GNSL}

  http://fedsfm.ru/documents/terrorists-catalog-portal-act {WHSL}

  Действительность паспорта {GNSL}

  http://сервисы.гувм.мвд.рф/info-service.htm?sid=2000 {WHSL}

  Проверка ИНН {GNSL}

  https://service.nalog.ru/inn.do {WHSL}

  Кредиты {GNSL}

  https://app.exbico.ru/ {WHSL}

  Исполнительные производства {GNSL}

  http://fssprus.ru/iss/ip {WHSL}

  Налоговые задолженности {GNSL}

  https://peney.net/ {WHSL}

  Залоги имущества {GNSL}

  https://www.reestr-zalogov.ru/state/index# {WHSL}

  Банкротство {GNSL}

  https://bankrot.fedresurs.ru/ {WHSL}

  Участие в судопроизводстве {GNSL}

  https://bsr.sudrf.ru/bigs/portal.html
  https://sudact.ru/
  https://mos-sud.ru/search
  https://mirsud.spb.ru/ {WHSL}

  Участие в бизнесе {GNSL}

  https://zachestnyibiznes.ru/ {WHSL}

  Поиск в соцсетях {GNSL}

  https://go.mail.ru/search_social {WHSL}

  Проверка диплома {GNSL}

  http://obrnadzor.gov.ru/ru/activity/main_directions/reestr_of_education/ {WHSL}

'''

page_telegram_osint = f'''
  {WHSL}Инструменты для расследований в Telegram. 
                                                                         {WHSL}Выгружаем участников чата {WHSL}
  Узнаем User ID {GNSL}                                                        @list_member_bot  @quant_parserbot{WHSL}

  @userinfobot                                                           {WHSL}Чаты пользователя {GNSL}
  @CheckID_AIDbot                                                        @telesint_bot  @tgscanrobot
  @username_to_id_bot {WHSL}

  История смены никнеймов                                                Узнаем телефон {GNSL}
  @SangMataInfo_bot                                                      @deanonym_bot   @EyeGodsBot  {WHSL}

  Поиск совпадений никнейма                                              Узнаем IP-адрес пользователя {GNSL}
  @maigret_osint_bot {GNSL}                                                    https://iplogger.ru/   
                                                                         https://grabify.link/ {WHSL}
  Дата создания аккаунта {GNSL}
  @creationdatebot {WHSL}

  Поисковики по Telegram {GNSL}

  https://search.buzz.im/ 
  https://telemetr.me/
  http://telegcrack.com
  https://lyzem.com/
  https://tgstat.ru/
  https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg#gsc.tab=0 {WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}   
'''
page_deanon_face = f'''
  Инструменты для деанонимизации по лицу.

  Поиск по фото в соцсетях {GNSL}

  https://vk.watch/
  https://findclone.ru/
  https://pimeyes.com/en/
  https://search4faces.com/ {WHSL}

  Боты {GNSL}

  @AvinfoBot
  @Smart_SearchBot {WHSL}

  Данные из поисковиков {GNSL}
  https://yandex.ru/images/
  https://images.google.com/
  https://go.mail.ru/search_images
  https://tineye.com/ {WHSL}

  Специализированное ПО {GNSL}

  http://www.pictriev.com/
  http://betaface.com/demo.html
  https://azure.microsoft.com/ru-ru/services/cognitive-services/face/ {WHSL}

  Ищем следы фотомонтажа {GNSL}

  https://29a.ch/photo-forensics/#error-level-analysis {WHSL}

  Определяем возраст {GNSL}

  https://www.how-old.net/ {WHSL}

  Определяем расу {GNSL}

  https://en.vonvon.me/quiz/9447 {WHSL}

  Составление фоторобота {GNSL}

  http://foto.hotdrv.ru/fotorobot {WHSL}

  Улучшение фото {GNSL}

  https://www.myheritage.nl/photo-enhancer
  https://letsenhance.io/
  https://online-fotoshop.ru/fotoredaktor-online/ {WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}  
'''
page_br_gov = f'''{WHSL}
  Оценка благонадежности граждан Беларуси.

  Международный розыск {GNSL}

  https://www.interpol.int/How-we-work/Notices/View-Red-Notices {WHSL}

  Национальный розыск {GNSL}
  https://mvd.gov.by/ru/wanted {WHSL}

  Банкротство {GNSL}
  https://bankrot.gov.by/Debtors/DebtorsList {WHSL}

  Исполнительные производства {GNSL}
  https://minjust.gov.by/directions/enforcement/debtors/ {WHSL}

  Налоговые задолженности {GNSL}
  http://www.portal.nalog.gov.by/grp/#!fl {WHSL}

  Участие в бизнесе {GNSL}
  http://egr.gov.by/egrn/ {WHSL}

  Участие в судопроизводстве {GNSL}
  http://service.court.by/ru/public/schedule  {WHSL}

  Поиск в соцсетях {GNSL}
  https://go.mail.ru/search_social
  https://pipl.com 
{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_equipment = f'''{WHSL}
  Мониторинг самолетов: {GNSL}
  flightradar24.com
  radarbox.com
  planefinder.net {WHSL}

  Мониторинг поездов:  {GNSL}
  pass.rzd.ru {WHSL}

  Мониторинг кораблей: {GNSL}
  shipfinder.co
  vesselfinder.com
  marinetraffic.com {WHSL}

  Мониторинг самолетов, поездов и маршрутного транспорта: {GNSL}
  rasp.yandex.ru/map/ {WHSL}

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_shodan = f''' {WHSL}
  Как искать в Shodan?

  Для более быстрого поиска нужно использовать фильтры. Это специальные слова, 
  которые ограничивают поиск на основе метаданных, служб или устройств. 
  Давайте разберем, какие основные моменты нужно почерпнуть, чтобы ускорить поиск.
  {GNSL}
  city:"New York" //результаты по определенному городу 
  port:22 //результаты по конкретному порту
  country:"RU" //результаты по определенной стране
  org:"VimpelCom" //результаты по конкретной компании 
  port 8080 -country:"RU" //поиск по порту 8080 и ограничение -country:"RU" чтобы не выдавать запросы по России
  А так же, есть еще множество других фильтров:
  after // результаты только после определенной даты (ДД/ММ/ГГГГ)
  asn // автономный номер системы
  before // результаты только до определенной даты (ДД/ММ/ГГГГ)
  category // главный баннер службы
  city // название города
  country // двухбуквенный код страны 
  hash // хэш свойства data
  hash Ipv6 // True/False
  has_screenshot // True/False
  hostname // полное имя хостя для устройтсва 
  ip // псевдоним для сетевого фильтра 
  isp // ISP, отвчающая за блок IP-адрессов 
  net // сетевой диапазон в CIDR-нотации 
  org // поиск по конкретной организации 
  os // операционная система 
  port // номер порта для устройства 
  postal // почтовый индекс(США)
  product // название продукта/программы 
  region // название региона/штата 
  state // псевдоним региона 
  version // версия продукта 
  vuln // идентификатор CVE для уязвимости
  author // автор уязвимости
  description //описание 
  platform //целевая платформа (php, windows, linux)
  type //тип эксплоита (dos, remote)
  {WHSL}
  Вот тебе еще ссылка, там много информации по доркам.
  {GNSL}
  https://github.com/jakejarvis/awesome-shodan-queries
  
  https://google.com
'''
page_millitary = f'''

  {GNSL}Военные авиабазы планеты земля {REDL}

  {REDL}{WHSL}Китайские военные авиабазы:{WHSL} {GNSL} https://www.google.com/maps/d/u/0/viewer?mid=1dHrv7E_0mLVEzXdRxIGwaHBU16KEhrTj {GNSL}

  {REDL}{WHSL}Военные авиабазы по всему миру:{WHSL} {GNSL}https://www.google.com/maps/d/u/0/viewer?mid=1XmSGWNOcO2IwQnB-FFH4ueFPl6WIzKEC {GNSL}
  
{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''

page_sun_geolocation = f'''{WHSL}
  Используем Солнце и тени для определения геолокации по фотографии {GNSL}

  https://telegra.ph/Ispolzuem-Solnce-i-teni-dlya-opredeleniya-geolokacii-po-fotografii-12-22
  {WHSL}
  Определяем геолокацию человека перешедшего по ссылке.{GNSL}
  https://github.com/Bafomet666/OSINT-SAN
  https://github.com/Bafomet666/Bigbro

{REDL}__________________________________________________________________________________________________________________________________{WHSL}
'''
page_social_osint = f'''
{WHSL}  OSINT в социальных сетях.
{GNSL}
  Search by account in VK:
  searchlikes.ru • tutnaidut.com • 220vk.com  • @Smart_SearchBot • @VKUserInfo_bot • vk5.city4me.com • 
  vk.watch • vk-photo.xyz • vk-express.ru • archive.org • yasiv.com  • archive.is • @InfoVkUser_bot •
  @FindNameVk_bot • yzad.ru • vkdia.com • @EyeGodsBot

{WHSL}  OSINT for account Twitter:
 {GNSL}
  followerwonk.com • sleepingtime.org(r) • foller.me • socialbearing.com • keyhole.co  • analytics.mentionmapp.com  
  burrrd.com • keitharm.me • archive.org • @usersbox_bot • undelete.news • 

{WHSL}  OSINT for account Facebook:
 {GNSL}
  graph.tips • whopostedwhat.com • lookup-id.com • keyhole.co (r) • archive.org • @usersbox_bot • @GetPhone_bot •

{WHSL}  OSINT For Instagram account:
 {GNSL}
  gramfly.com • storiesig.com • codeofaninja.com • sometag.org • keyhole.co (r) • archive.org • @InstaBot • @usersbox_bot •
  undelete.news

{WHSL}  OSINT For Reddit account:
 {GNSL}
  snoopsnoo.com • redditinsight.com • redditinvestigator.com • archive.org • redditcommentsearch.com • 

{WHSL}  OSINT For skype account:
 {GNSL}
  mostwantedhf.info • cyber-hub.pw • webresolver.nl • @usersbox_bot 
'''
