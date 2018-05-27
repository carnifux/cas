import sys
import os
from xml.etree.ElementTree import ElementTree, tostring

if os.path.isfile(sys.argv[2]):
    print('deleting already existing output file')
    os.remove(sys.argv[2])

xmls = list(filter((lambda f: str(f).endswith('.xml')), list(os.listdir(sys.argv[1]))))
out = ''
ingredients = {}
for x in xmls:
    path = sys.argv[1] + '\\' + x
    print('reading ' + path)
    et = ElementTree(file=path)
    for e in et.findall('.//Ingredient'):
        ingredients.update({e.find('CasNumber').text: e})

cas = []
for i in ingredients.items():
    cas.append(i[0])
    out = out + tostring(i[1], encoding='unicode') + '\n'

list.sort(cas)
print('unique cas numbers: ', end='')
for c in cas:
    print(c + ', ', end='')
print('')

with open(sys.argv[2], 'w') as output:
    output.write(out)
print('done')