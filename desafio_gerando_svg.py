import random

arquivo = open('circle.svg', 'w')
arquivo.write('<svg width = "200" height = "200" xmlns = "http://www.w3.org/2000/svg">\n<circle cx = "100" cy = "100" r = "100" fill = "red"/>')

aleatoriox = random.randint(1,200)
aleatorioy = random.randint(1,200)

for i in range(100):
    arquivo.write(f'<circle cx ="{aleatoriox}" cy="{aleatorioy}"/>')
    i+=1
arquivo.write('</svg>')

arquivo.close()
