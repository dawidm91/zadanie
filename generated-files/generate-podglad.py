with open('szablon.html', 'r', encoding='utf-8') as f:
    szablon = f.read()

with open('article.html', 'r', encoding='utf-8') as f:
    article = f.read()

body_start = szablon.find('<body>') + len('<body>')
body_end = szablon.find('</body>')

szablon = szablon[:body_start] + article + szablon[body_end:]

with open('podglad.html', 'w', encoding='utf-8') as f:
    f.write(szablon)