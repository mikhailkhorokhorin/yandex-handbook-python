{i: text.lower().count(i) for i in sorted(set(text.lower())) if i.isalpha()}
