import re
from collections import Counter

def count_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Регулярные выражения — специальная последовательность символов, которая помогает сопоставлять или находить строки python с использованием специализированного синтаксиса, содержащегося в шаблоне. Регулярные выражения распространены в мире UNIX.

Модуль re предоставляет полную поддержку выражениям, подобным Perl в Python. Модуль re поднимает исключение re.error, если возникает ошибка при компиляции или использовании регулярного выражения.

Давайте рассмотрим две функции, которые будут использоваться для обработки регулярных выражений. Важно так же заметить, что существуют символы, которые меняют свое значение, когда используются в регулярном выражении.Чтобы избежать путаницы при работе с регулярными выражениями, записывайте строку как r'expression'.

Функция match
Эта функция ищет pattern в string и поддерживает настройки с помощью дополнительного flags.
Ниже можно увидеть синтаксис данной функции:

re.match(pattern, string, flags=0)
Описание параметров:

№	Параметр & Описание
1	pattern — строка регулярного выражения (r'g.{3}le')
2	string — строка, в которой мы будем искать соответствие с шаблоном в начале строки ('google')
3	flags — модификаторы, перечисленными в таблице ниже. Вы можете указать разные флаги с помощью побитового OR
Функция re.match возвращает объект match при успешном завершении, или None при ошибке. Мы используем функцию group(num) или groups() объекта match для получения результатов поиска.

№	Метод совпадения объектов и описание
1	group(num=0) — этот метод возвращает полное совпадение (или совпадение конкретной подгруппы)
2	groups() — этот метод возвращает все найденные подгруппы в tuple
Пример функции re.match
import re


title = "Error 404. Page not found"
exemple = re.match( r'(.*)\. (.*?) .*', title, re.M|re.I)

if exemple:
   print("exemple.group() : ", exemple.group())
   print("exemple.group(1) : ", exemple.group(1))
   print("exemple.group(2) : ", exemple.group(2))
   print("exemple.groups():", exemple.groups())
else:
   print("Нет совпадений!")
Когда вышеуказанный код выполняется, он производит следующий результат:

exemple.group(): Error 404. Page not found
exemple.group(1): Error 404
exemple.group(2): Page
exemple.groups(): ('Error 404', 'Page')
Функция search
Эта функция выполняет поиск первого вхождения pattern внутри string с дополнительным flags.
Пример синтаксиса для этой функции:

re.search(pattern, string, flags=0)
Описание параметров:

№	Параметр & Описание
1	pattern — строка регулярного выражения
2	string — строка, в которой мы будем искать первое соответствие с шаблоном
3	flags — модификаторы, перечисленными в таблице ниже. Вы можете указать разные флаги с помощью побитового OR
Функция re.search возвращает объект match если совпадение найдено, и None, когда нет совпадений. Используйте функцию group(num) или groups() объекта match для получения результата функции.

№	Способы совпадения объектов и описание
1	group(num=0) — метод, который возвращает полное совпадение (или же совпадение конкретной подгруппы)
2	groups() — метод возвращает все сопоставимые подгруппы в tuple
Пример функции re.search
import re


title = "Error 404. Page not found"
# добавим пробел в начало паттерна
exemple = re.search( r' (.*)\. (.*?) .*', title, re.M|re.I)

if exemple:
   print("exemple.group():", exemple.group())
   print("exemple.group(1):", exemple.group(1))
   print("exemple.group(2):", exemple.group(2))
   print("exemple.groups():", exemple.groups())
else:
   print("Нет совпадений!")
Запускаем скрипт и получаем следующий результат:

exemple.group():  404. Page not found
exemple.group(1): 404
exemple.group(2): Page
exemple.groups(): ('404', 'Page')
Match и Search
Python предлагает две разные примитивные операции, основанные на регулярных выражениях: match выполняет поиск паттерна в начале строки, тогда как search выполняет поиск по всей строке.

Пример разницы re.match и re.search
import re


title = "Error 404. Page not found"
match_exemple = re.match( r'not', title, re.M|re.I)

if match_exemple:
   print("match --> match_exemple.group():", match_exemple.group())
else:
   print("Нет совпадений!")

search_exemple = re.search( r'not', title, re.M|re.I)
if search_exemple:
   print("search --> search_exemple.group():", search_exemple.group())
else:
   print("Нет совпадений!")
Когда этот код выполняется, он производит следующий результат:

Нет совпадений!
search --> search_exemple.group(): not
Метод Sub
Одним из наиболее важных методов модуля re, которые используют регулярные выражения, является re.sub.
Пример синтаксиса sub:

re.sub(pattern, repl, string, max=0)
Этот метод заменяет все вхождения pattern в string на repl, если не указано на max. Он возвращает измененную строку."""

print(count_10_words(text))