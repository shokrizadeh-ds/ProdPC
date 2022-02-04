path = r"C:\Users\LI2BTL\OneDrive - Industrial Alliance\Documents\Batch 1\MODIFIED 625\OUT\XML"

stripper = r'{file:////ia.iafg.net/r01/Svc/SCOPC-PRODPC/COEUR/schema/ProdPCXMLSchema.xsd}'

l = []


def extract_xml_2(path):
    l = []
    for file in os.listdir(path):
        filePath = f'{path}\{file}'
        #         print(filePath)
        tree = ET.parse(filePath)
        root = tree.getroot()

        #         c = []
        #         c.append(filePath)

        for elem in root:
            c = []
            c.append(filePath)
            elem_tag = elem.tag.split('}')[1]
            #             print('1  ' + elem_tag, end=',')
            c.append(elem_tag)
            elem_text = elem.text.replace(stripper, '').replace('\n', ' ').strip(' \n\r')
            c.append(elem_text)
            print(c)

            for child in elem:
                for element in child:
                    for item in element:


#                         print(c)

#                         print(filePath, end=',')
#                         elem_tag = elem.tag.split("}")[1].replace('\n', ' ').strip(' \n\r')
#                         elem_tag = elem.tag
#                         elem_text = elem.text.replace(stripper, '').replace('\n', ' ').strip(' \n\r')
#                         child_tag = child.tag.split("}")[1].replace('\n', ' ').strip(' \n\r')
#                         child_text = child.text.replace(stripper, '').replace('\n', ' ').strip(' \n\r')
#                         element_tag = element.tag.split("}")[1].replace('\n', ' ').strip(' \n\r')
#                         element_text = element.text.replace(stripper, '').replace('\n', ' ').strip(' \n\r')
#                         item_tag = item.tag.split("}")[1].replace('\n', ' ').strip(' \n\r')
#                         item_text = item.text.replace(stripper, '').replace('\n', ' ').strip(' \n\r')

#                         l.append([c[0],
#                                  c[1],
#                                  c[2],
#                                  child_tag,
#                                  child_text,
#                                  element_tag,
#                                  element_text,
#                                  item_tag,
#                                  item_text]
#                                 )


#                         print('2  ' + c[1], end=',')
#                         print(c[2] , end='\n')
#                         print(child_tag, end=',')
#                         print(child_text, end=',')
#                         print(element_tag, end=',')
#                         print(element_text, end=',')
#                         print(item_text, end=',')
#                         print(item_text, end=',')
#     return l


extract_xml_2(path)