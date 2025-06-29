[
    i
    for i in words.split()
    if sum(1 for letter in i if letter.lower() in "аяуюоёэеиыaeiouy") >= 3
]
