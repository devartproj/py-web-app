#!C:\Users\Alex\AppData\Local\Programs\Python\Python313\python.exe

import os
envs = os.environ


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
    <h1>CGI працює</h1>
    
</body>
</html>''')

for name, value in envs.items():
    print(f'<li>{name} = {value}</li>')

print('''
    </ul>
</body>
</html>''')