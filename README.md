# Обрезка ссылок с помощью Битли

Данная программа делает из длинной ссылки короткую. Но если вставить уже укороченную ссылку то выведется сколько раз нажали на ссылку и перешли по ней.
### Как установить
Вам надо зарегистрироваться на сайте [bitly](https://app.bitly.com/bbt2/).

Ps. **Битли не работает с гугл аккаунтами.**

Справа сверху нажать на: **профиль>Настройки>Айпи**.
Справа надо будет ввести пароль, далее нажимаете _Сгенерировать_. Копируете набор цифр и букв.
Создайте файл под названием .env * _**ОБЯЗАТЕЛЬНО**_ *

Пишите туда вот это ↓
```
BITLY_TOKEN=ccex4c77d886f1fп5d245829dd07dc637c6258d6
```
Это пример, можете даже не пытайтесь меня хекнуть.

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
requirements.txt файлик, каторый вам нужен.

### Для запуска нужно
Чтобы открыть командную строку нужно нажать win+r
Вписываем в открывшееся окошко ↓
```
cmd
```
В командную строку вписать
```
python main.py *ваша ссылка*
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

конец :D
