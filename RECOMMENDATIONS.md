PEP 8
=====

Соблюдайте (PEP8)[http://legacy.python.org/dev/peps/pep-0008/].
Обратите внимание, где надо ставить пробелы, а где они не нужны.


Работа с файлами
====================

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
