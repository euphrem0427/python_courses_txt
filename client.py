# coding: utf-8
import os
import sys
import cgi
from multiprocessing.pool import CLOSE 
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

fichier = open("best-time.txt", "r")
line = fichier.readlines()
    
alitta_origin = line[0]
alitta_line = line[0].split()
alitta_score = alitta_line[1]

anne_origin = line[1]
anne_line = line[1].split()
anne_score = anne_line[1]

alfred_origin = line[2]
alfred_line = line[2].split()
alfred_score = alfred_line[1]

fichier.close()
    
result = form.getvalue("name")
if (result) == "fin":
    sys.exit(1)
score = str(result).rsplit(None, 1)[-1]
entrer = str(result).split()
name = entrer[0]


if name == 'alitta-caouette':
        fichier = open("alitta.txt", "a")
        fichier.write(score + '\n')
        fichier.close()
        if score < alitta_score:
            replacement = ""
            fichier = open("best-time.txt", "r")
            line = fichier.readlines()
            changes = line[0].replace(alitta_score, score)
            replacement = replacement + changes
            replacement = replacement + str(anne_origin)
            replacement = replacement + str(alfred_origin)
            fichier.close()
            file = open("best-time.txt", "w")
            file.write(replacement)
            file.close()
        
elif name == 'anne-leon':
        fichier = open("anne.txt", "a")
        fichier.write(score + '\n')
        fichier.close()
        if score < anne_score:
            replacement = ""
            fichier = open("best-time.txt", "r")
            line = fichier.readlines()
            changes = line[1].replace(anne_score, score)
            replacement = replacement + str(alitta_origin)
            replacement = replacement + changes
            replacement = replacement + str(alfred_origin)
            fichier.close()
            file = open("best-time.txt", "w")
            file.write(replacement)
            file.close()
        
elif name == 'alfred-blanken':
        fichier = open("alfred.txt", "a")
        fichier.write(score + '\n')
        fichier.close()
        if score < alfred_score:
            replacement = ""
            fichier = open("best-time.txt", "r")
            line = fichier.readlines()
            changes = line[2].replace(alfred_score, score)
            replacement = replacement + str(alitta_origin)
            replacement = replacement + str(anne_origin)
            replacement = replacement + changes
            fichier.close()
            file = open("best-time.txt", "w")
            file.write(replacement)
            file.close()

fichier = open("best-time.txt", "r")
line = fichier.readlines()
for l in line:
    print(l + '***')
fichier.close()

html = """<!DOCTYPE html>
<head>
    <title>Course</title>
</head>
<body>
    <h1>Course</h1>
    <form action="/client.py" method="post">
        <input type="text" name="name" placeholder="alitta-caouette 5min31" value="" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
</body>
</html>
"""

print(html)