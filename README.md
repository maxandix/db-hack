# db-hack
**Набор скриптов, чтобы хакнуть электронный дневник. Полезно для двоечников ;-)**

Это скрипты для двоечников, которые хотят хакнуть свой дневник на [e-diary](https://github.com/devmanorg/e-diary)

### Как запустить:
Чтобы запустить скрипт можно его целиком "копипастнуть" в shell, а можно положить файл с кодом рядом с manage.py и подключить через import.

```console
$ python manage.py shell
```

### Как пользоваться

Есть 3 функции: 

- `fix_marks(schoolkid_name)` - исправляет все тройки и двойки на пятерки по имени ученика.
  - Пример использования: `fix_marks('Фролов Иван')`

- `remove_chastisements(schoolkid_name)` - удаляет все замечания учителя по имени ученика.
  - Пример использования: `remove_chastisements('Фролов Иван')`
  
- `create_commendation(schoolkid_name, subject_title)` - создает похвалу для указного ученика (его имени) и названия предмета
  - Пример использования: `create_commendation('Фролов Иван', 'Музыка')`


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).