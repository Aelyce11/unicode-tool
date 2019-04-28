from flask import render_template, request
from app import app
import unicodedata
from random import randint
from urllib.parse import unquote


@app.route('/')
def index():
  rand = rand = randint(0, 230000)
  return render_template('index.html', random = rand)


@app.route('/search')
def search():

  rand = rand = randint(0, 230000)

  if request.args.get('research'):
    query = request.args.get('research')

    res = []

    if len(query) == 1:
      for i in range(230000):
        if chr(i) == query:
          res.append({
            'display': chr(i),
            'code': i,
            'name': unicodedata.name(chr(i), 'ANONYME')
          })
        elif query.upper() in unicodedata.name(chr(i), 'ANONYME'):
          res.append({
            'display': chr(i),
            'code': i,
            'name': unicodedata.name(chr(i), 'ANONYME')
          })
    else :
      for i in range(230000):
        if query.upper() in unicodedata.name(chr(i), 'ANONYME'):
          res.append({
            'display': chr(i),
            'code': i,
            'name': unicodedata.name(chr(i), 'ANONYME')
          })

    if query.isnumeric():

      for i in range(230000):
        if str(query) in str(i):
          res.append({
                  'display': chr(i),
                  'code': i,
                  'name': unicodedata.name(chr(i), 'ANONYME')
                })

        # UnicodeEncodeError raised < 1000 : surrogates not allowed
        # try does not catch the error ?
        # error comes from "query in str(i)"

    if query[0: 2] == 'u+' or query[0: 2] == 'U+':
      for i in range(230000):
        if ('U+%04x' % i) == unquote(query) or ('u+%04x' % i) == unquote(query):
          res.append({
            'display': chr(i),
            'code': i,
            'name': unicodedata.name(chr(i), 'ANONYME')
          })
          break


    return render_template('search.html', random = rand, results = res)

  return render_template('search.html', random = rand)


@app.route('/unicode/<codepoint>')
def uni(codepoint):

  rand = rand = randint(0, 230000)
  char = chr(int(codepoint))

  character = {
    'codepoint': ('U+%04x' % ord(char)),
    'display': char,
    'name': unicodedata.name(char, 'ANONYME'),
    'decimal': int(codepoint),
    'category': unicodedata.category(char)
  }

  return render_template('unicode.html', random = rand, char = character)