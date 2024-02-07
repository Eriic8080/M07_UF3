"""
Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). 
La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
Un root de nom students.
Cinc childs (del root) amb nom student.
Cada child student ha de tindre 4 subchilds:
 name
 surname
 email
 dni
Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
El text de cada etiqueta serà de la vostra elecció.
"""

import xml.etree.ElementTree as ET

def crear_xml():
    # Aqui creo el elemento principal students
    root = ET.Element('students')

    # Le creo 5 hijos llamados stundent al elemento principal
    for i in range(1, 6):
        student = ET.SubElement(root, 'student')

        # dentro de cada stundent le creo otros 4 hijos
        name = ET.SubElement(student, 'name')
        surname = ET.SubElement(student, 'surname')
        email = ET.SubElement(student, 'email')
        dni = ET.SubElement(student, 'dni')

        #Aqui le meto a cada sutudent un atributo id
        student.set('id', str(i))

        # Aqui meto el texto en cada hijo del student
        name.text = f'Nombre'
        surname.text = f'Apellido'
        email.text = f'email'
        dni.text = f'123432425'

    tree = ET.ElementTree(root)

    #Aqui muestro el xml por consola
    ET.dump(root)

crear_xml()
