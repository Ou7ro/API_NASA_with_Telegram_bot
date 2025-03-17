# Космический Телеграм
Проект представляет собой интеграцию 3 APi: Nasa, SpaceX и Telegram Api. С помощью Nasa и SpaceX API, мы получаем фотографии космоса, которые в послеющем выкладываем в телеграм канале, с помощью telegram API.
## Зависимости
- Python3 должен быть установлен.
- При разработке был использован Python3.10. С версиями выше есть конфликт у python-telegram-bot.
- Затем используйте pip для установки зависимостей:
```
pip install -r requirements.txt
```
Для публикаций полученных фото в Телеграм канале потребуется создать [телеграм канал](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)

## Переменные окружения
Требуется создать файл `.env` и прописать следующие переменные окружения:
- NASA_TOKEN
- TG_TOKEN
- TG_CHAT_ID
- TIME (необязательный)

`NASA_TOKEN` можно сгенерировать на сайте [NASA](https://api.nasa.gov). Нужен для снижения риска утечки данных и других угроз безопасности.

`TG_TOKEN` можно сгенерировать у [Отца Ботов](https://telegram.me/BotFather). Нужен для взаимодействия с ботом.

`TG_CHAT_ID` инструкция по получению id чата [здесь](https://lumpics.ru/how-find-out-chat-id-in-telegram/). Нужен для отправки фото в Телеграм чат.

`TIME` отвечает за время, с какой периодичность будут поститься картинки в телеграм чате. Принимает значение в секундах, по умолчанию стоит 14400 секунд (4 часа). 

## Скрипты и их запуск
### fetch_spacex_launch.py

Cкачивает картинки запусков ракеты. По умолчанию скачивает фотографии последнего запуска ракеты.
Полученный файл сохраняется в папке `images`.
Имеет не обязательный аргумент, который даёт возможность задать id конкретного запуска. 

Пример:
```
python fetch_spacex_launch.py --id <id запуска>
```
### fetch_nasa_apod.py

Скачивает случайный фотоснимок из вселенной. Полученный файл сохраняется в папке `images`.
Запуск производится с помощью команды прописанной в консоль:
```
python fetch_nasa_apod.py
```
### fetch_nasa_epic.py

Скачивает картинку земли. Запуск производися с помощью команды прописанной в консоль:
```
python fetch_nasa_epic.py
```
### send_one_image_tg.py

Производит публикацию случайной картинки из папки `images`. 
Имеет не обязательный аргумент, который даёт возможность публикации определенного фото.
```
python send_one_image_tg.py --name <название фото>
```
### send_all_images_tg.py

Запускает цикл публикаций в ваш телеграм чат. Изображения для публикации берутся из папки `images`.
С какой периодичностью будут выкладываться фотографии, указывается в переменной окружения `TIME`.
По умолчанию публикация производится раз в 4 часа.
Имеет не обязательный аргумент, который даёт возможность публикации определенного фото. В таком случае цикл публикаций будет состоять только из указанного изображения.
```
python send_all_images_tg.py --name <название фото>
```
