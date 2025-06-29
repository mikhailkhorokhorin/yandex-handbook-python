# 3.3. Списочные выражения. Модель памяти для типов языка Python
### A. Список квадратов
```python
[x**2 for x in range(a, b + 1)]
```
### B. Список квадратов 2
```python
[x**2 for x in range(a, b + (1 if a < b else -1), 1 if a < b else -1)]
```
### C. Основы фильтрации
```python
[i for i in sorted(range((a + d - 1) // d * d, b + 1, d))]
```
### D. Множество нечетных чисел
```python
{x for x in numbers if x % 2 != 0}
```
### E. Множество всех полных квадратов
```python
{x for x in numbers if int(x**0.5) ** 2 == x}
```
### F. Длины всех слов
```python
[len(x) for x in sentence.split()]
```
### G. Цифровая выжимка
```python
"".join([i for i in text if i.isdigit()])
```
### H. Аббревиатура
```python
"".join([x[0].upper() for x in string.split()])
```
### I. Преобразование в строку
```python
" - ".join([str(x) for x in sorted(set(numbers))])
```
### J. Огласите список
```python
[
    i
    for i in words.split()
    if sum(1 for letter in i if letter.lower() in "аяуюоёэеиыaeiouy") >= 3
]
```
### K. Выявление уникальности
```python
{i for i in numbers if numbers.count(i) == 1}
```
### L. Максимальное произведение
```python
max(i * j for i in numbers for j in numbers if i != j)
```
### M. Словарный минимум
```python
min([(sum(number), word) for word, number in data.items()])[1]
```
### N. Поиск ошибок
```python
{word for word, number in data.items() if len(number) != len(set(number))}
```
### O. Буквенная статистика
```python
{i: text.lower().count(i) for i in sorted(set(text.lower())) if i.isalpha()}
```
### P. RLE наоборот
```python
"".join([i * j for i, j in rle])
```
### Q. Таблица умножения 2.0
```python
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]
```
### R. Делители
```python
{i: [x for x in range(1, i + 1) if i % x == 0] for i in numbers}
```
### S. Простое множество
```python
{
    i
    for i in numbers
    if i
    in [
        x
        for x in range(2, max(numbers) + 1)
        if all(x % y != 0 for y in range(2, int(x**0.5) + 1))
    ]
}
```
### T. Обобщение
```python
{
    tuple(sorted([i, j]))
    for i in text.split()
    for j in text.split()
    if i != j and len(set(i) & set(j)) >= 3
}
```
