#!C:\Users\Alex\AppData\Local\Programs\Python\Python313\python.exe

import os

def send_redirect(location:str):
    print("Status: 302 Found")
    print (f"location: {location}")
    print()
    exit ()

query_params = {k : v for k, v in 
                (pair.split('=') for pair in
                 os.environ['QUERY_STRING'].split('&'))}

titles = {
    'uk': 'Вітаємо у магазині',
    'en': 'Welcome to the shop',
    'de': "Willkommen im Laden"
}
lang = query_params.get('lang', 'uk') #query_params['lang'] if 'lang' in query_params else 'uk'
if lang not in titles:
   send_redirect("/uk/shop/")

title = titles[lang]

print ("Content-Type: text/html; сharset=cp1251")
print ("Connection: close")
print()
print(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="cp1251">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{lang}</p>
</body>
</html>''')