PEP 8
=====

Соблюдайте [PEP8](http://legacy.python.org/dev/peps/pep-0008/).
Обратите внимание на то, где надо ставить пробелы, а где они не нужны.


Работа с файлами
================

**Всегда** используйте конструкцию
```python
with open('file.txt') as f:
    do_something()
```

Это столько же символов, как и пара `open/close`, но намного надёжнее, так как код
```python
f = open('file.txt')
do_something()
f.close()
```
не закроет файл, если do_something кинет исключение!


Старайтесь минимизировать работу внутри with блока.

Хорошо
```python
result = do_something_complicated()
with open('file.txt') as f:
    print_result()
```
Плохо
```python
with open('file.txt') as f:
    result = do_something_complicated()
    print_result()
```

Разделяйте вычисления и ввод-вывод. Лучше использовать две функции, одну
для нахождения ответа, другую для его печати, чем использовать одну функцию,
которая и считает, и печатает.

Проверка коллекций на пустоту
=============================

Чтобы проверить коллекцию или строку(list, dict, set, queue...: всё у чего можно спросить длину) на пустоту, пишите так:

```python
if my_collection:
    # not empty
else:
    # empty
```

Не нужно сравнивать длину с нулём. Подробности в документации: https://docs.python.org/3.4/library/stdtypes.html#truth-value-testing.

Структура скрипта
=================

Часто приходится писать на питоне маленький скрипт из одного файла, например для решения домашек.
В идеальном мире он выглядит так.

```python
#!/usr/bin/env python3 (http://stackoverflow.com/questions/2429511/)
import foo
import bar

def quux():
    ...

def spam():
    ...

def main():
    read input
    use defined functions to the get answer
    write output

if __name__ == '__main__':
    main()
```

Но может выглядеть и так.

```python
import foo
import bar

def quxx():
    ...

def spam():
    ...

read input
use defined functions to get the answer
write output
```

* импорты всегда в самом верху
* все функции следом за импортами, без кусков кода между ними
* в самом низу файла код, который собственно запускается
* как можно меньше глобальных переменных(допускаются глобальные константы)
* функции либо только производят вычисления, либо только совершают IO

Чтение строки из двух чисел
===========================

Вместо

```python
xy = [int(i) for i in sys.stdin.read().split()]
x = xy[0]
y = xy[1]
```

лучше писать

```python
x, y = [int(i) for i in sys.stdin.read().split()]
```

по двум причинам.

* короче и понятнее
* если вдруг в строке окажется три числа, то это не останется незамеченным
