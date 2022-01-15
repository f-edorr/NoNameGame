# NoNameGame
(название я ещё не придумала)
____
## Описание
  Я хочу сделать игру, где (не знаю как жанр такой называется(загуглить не получилось), опишу словами) персонаж, управляемый через wasd, бегает по 2д полю, и отовсюду появляются враги, которые его атакуют. Для прохождения уровня нужно убить всех появившихся врагов, не истратив очки здоровья до нуля.
- У игрока две жизни(уровни будут сбалансированы так, что этого будет достаточно), но каждая жизнь - это отдельный персонаж, со своими характеристиками и видом атаки(ближники/дальники). 
- Первый персонаж - главный герой, второй - определённый персонаж, появление которого объясняется в сюжете. На некоторых уровнях второго персонажа можно выбрать.
- В игре несколько уровней, с каждым уровнем сложность повышается
- Возможно добавлю головоломки/лабиринты
- Может даже несколько концовок будет, они будут зависеть от успешности прохождения уровней
____
## ТЗ
...

- Игровой процесс должен делится на некие блоки, каждый из которых представляет из себя 2 этапа - небольшое обучение/какой-то сюжет и очередной уровень. 
- Повествование будет происходить, наверное, как в каких-нибудь новеллах. 


### Используемые модули:

- PyGame
- os
- sys
- math
- ...

### Нужно создать txt файлы:

- N файлов для каждого из уровней (с параметрами врагов, может быть картой и тп). Или один файл со всеми уровнями.
- Файл с параметрами(Очки здоровья, атаки) всех персонажей, за которых может играть пользователь
- Файл с хранением всех текстов(диалогов, текстов для обучения и тп)
- ...

### Примерная структура базы данных:

- Таблица с хранением информации о пользователе
- Таблица с информацией о сохранениях прогресса каждого пользователя
- Таблица с хранением статистики пользователя
- Внешний ключ - id пользователя

### Ещё нужно разобраться:

- Со звуковым сопровождением
- С длиной игры, кол-вом и сложностью уровней
- С графикой, в т.ч. анимацией
- ...
