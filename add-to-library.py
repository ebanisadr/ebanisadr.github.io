#!/usr/bin/env python3
import string
import datetime

no_punctuation = str.maketrans('', '', string.punctuation)

title = input('title: ')
link = input('link: ')
desc = input('description: ')
slug = title.translate(no_punctuation).lower().replace(' ', '-').replace('--', '-')
date = datetime.date.today().strftime("%B %d, %Y")

filename = '_library/'+ slug + '.md'
post = open(filename, 'a')
content = '''---
title: %s
link: %s
date: %s
---

%s
''' % (title, link, date, desc)

post.write(content)

print()
print('New file: ' + filename)
print(content)

