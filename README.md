# Парсер позиции товара в поиске по ключевому слову на Wildberries
Поиск осуществляется по артикулу товарa. WARNING! если по ключевому слову в поиске находится более 3000 позиций, 
то скрипт отключается, так как у сайта есть количество лимитов подключения.

![Screenshot](https://github.com/valhallajazzy/WB_parser/blob/main/picture_for_readme/picture.png)

## Подготовка и запуск скрипта

* В терминале, в корневой папке проекта создаем виртуальное окружение и устанавливаем
требуемые библиотеки, запускаем виртуальное окружение:

```console
$ poetry install
$ poetry shell
```

* Из корневой директории проекта запускаем скрипт командой:

```console
$ python3 main.py
```
