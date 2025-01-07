# Списочные выражения. Модель памяти для типов языка Python

### Список квадратов

```python
[x ** 2 for x in range(a, b + 1)]
```

### Таблица умножения 2.0

```python
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]
```

### Длины всех слов

```python
[len(x) for x in sentence.split()]
```

### Множество нечетных чисел

```python
{x for x in numbers if x % 2 != 0}
```

### Множество всех полных квадратов

```python
{x for x in numbers if int(x ** 0.5) ** 2 == x}
```

### Буквенная статистика

```python
{i: text.lower().count(i) for i in sorted(set(text.lower())) if i.isalpha()}
```

### Делители

```python
{i: [x for x in range(1, i + 1) if i % x == 0] for i in numbers}
```

### Аббревиатура

```python
"".join([x[0].upper() for x in string.split()])
```

### Преобразование в строку

```python
" - ".join([str(x) for x in sorted(set(numbers))])
```

### RLE наоборот

```python
"".join([i * j for i, j in rle])
```