# CScalp-Global-Settings-Manager
Fast way to set up your CScalp.

Данная программа написана на языке программирования Python. Причин написания на Python было несколько:

1. Код программы перед запуском можно просмотреть. Таким образом убедиться в безопасности кода.
2. На Python легко и быстро разрабатывается ПО ввиду простого синтаксиса и наличия большого числа бесплатных библиотек кода.
3. Это мой любимый язык программирования. <br />

Перед запуском основного окна пользователя встречает предупреждение о необходимости закрыть CScalp. Это сделано, т.к. программе необходим доступ к файлам настроек. После настройки можно будет снова запустить CScalp.

Перед нажатием кнопки "Применить" программа создаст zip-архив всей папки с настройками для возможности вернуть старую версию настроек просто распаковав содержимое архива обратно в папку настроек и заменив файлы. Архив находится снаружи папки с настройками и в имени содержит дату и время создания.

После создания архива программа вносит правки в файлы настроек стаканов с расширением ".tmp".

Последовательность вкладок с настройками подобна тем что в CScalp за исключением отсутствия настроек, которые не являются глобальными, например "Крупный объем" и дополнительной вкладки для настроек самой программы (1я вкладка). В данной вкладке можно поменять указанный по умолчанию параметр: расположение папки с файлами настроек.

Пока поддерживается только биржа Binance, но если нужно очень легко будет добавить новую биржу для настроек её стаканов.

## Скриншоты интерфейса программы:

![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/1.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/2.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/3.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/4.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/5.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/6.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/7.png?raw=true)<br />
![alt text](https://github.com/NickSkyyer/CScalp-Global-Settings-Manager/blob/main/screenshots_of_program/8.png?raw=true)<br />

!!! ВНИМАНИЕ !!!
Для нормальной работы требуется версия Python 3.10. Скачать установщики можно тут:
https://www.python.org/downloads/release/python-3100/
Ссылки на них находяться внизу страницы.

Пример команды для запуска приложения в командой строке (``путь\к\интерпретатору interface.py``):
``C:\Users\NickSky\AppData\Local\Programs\Python\Python310\python.exe interface.py``

Поменяйте в файле ``run_interface.bat`` NickSky на свое имя пользователя, если Python установлен по подобному пути или полностью замените данный путь на путь хранения установленного Python.
После этого можете создать ярлык на файл ``start.bat`` и запускать только его.

### Понравилась программа или хотите улучшенной версии?

Не поскупитесь и отсыпьте немножко цифрового золота в виде USDT (TRC-20): <br />
TTGqLY3sPcNJcCYeqTyRBB41Ty8MpSD2xy -- адрес моего Binance кошелька <br />
(P.S.: комиссия для переводов между счетами Binance отсутствует)
