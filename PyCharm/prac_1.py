from bs4 import BeautifulSoup
import lxml
import xml.etree.ElementTree as ET

import os

path = r"C:\Users\LI2BTL\OneDrive - Industrial Alliance\Documents\Batch 1\MODIFIED 625\OUT\XML"

# print(os.listdir(path))



for file in os.listdir(path):
    filePath = f"{path}\{file}"
    print(filePath)

    tree = ET.parse(filePath)

    root = tree.getroot()

    # print(root.tag)

    # xml_namespace = root.tag.split('}')
    xml_namespace = root.tag[:root.tag.find('}')+1]
    #
    # print(xml_namespace)

    for Etapes in root.findall(xml_namespace+'Etapes'):
        for Etape in Etapes.findall(xml_namespace+'Etape'):
            # print('\t' , Etape)
            for Nom in Etape.findall(xml_namespace+'Nom'):
                print('\t\t', Nom.text)

    # for elem in root:
    #     print(elem.tag)
    #     for child in elem:
    #         print(f'\t\t{child.tag}')

    # for child in root:
    #     print(f'\t{child.tag}, {child.attrib}')

    # for etape in root.findall('Description'):
    #     print(etape)


    # print(root.findall('Etapes'))
    # print(list(root.iter('Etapes')))
    # root.



    # with open(filePath, encoding='utf-8') as f:
    #     content = f.read()
    #
    #     tree = ET.parse(content)
    #     print(tree)


        # soup =  BeautifulSoup(content, 'xml')
        # # desc = soup.find_all('Description')
        # # print(desc)
        #
        # steps = soup.find_all('Etapes')
        # # step = steps.find_all('Etape')
        # # nom = step.find_all('nom')
        # print(steps)
        #
        # next_sibling = soup.find_previous_siblings('Etapes')
        # print(next_sibling)