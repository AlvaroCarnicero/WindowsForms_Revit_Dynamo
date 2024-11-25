#-*- coding: utf-8 -*-
#______________________________________________________________________________________________________
"""
241101 últimos 7 días: se acumulan las hora de trabajo de varios archivos en los que se ha trabajado sobre este tema
5 hrs 6 mins
3 hrs 18 mins
1 hr 47 mins
1 hr 41 mins
1 hr 5 mins
1 hr 3 mins
34 mins
32 mins
30 mins
27 mins
23 mins
11 mins
2 mins
6 min
Suma de todos los tiempos: 15 hrs 47 mins
241115 ultimos 7 días: 3 hrs 29 mins


"""

import os
import sys
import clr



#* REFERENCIAS FUNCIONES LOCALES
# region
import os
clr.AddReference('DynamoServices')
from Dynamo.Events import *
ruta_completa = ExecutionEvents.ActiveSession.CurrentWorkspacePath
# Obtener solo la ruta del directorio
directorio_dynamo = os.path.dirname(ruta_completa)
# Crear la ruta completa a la carpeta de funciones
# ruta_archivo_winforms = os.path.join(directorio_dynamo, 'PlantillaWinforms_241029.py')
# Añadir la ruta al sys.path
import sys
sys.path.append(directorio_dynamo)

# endregion

# Importar las clases necesarias de la plantilla
from Winforms_Template import * #MyWindow, MyLabel, MyTextBox, MyCheckBox, MyComboBox, MyGroupBox, MyRadioButton, MyButton, font_1

# Crear la ventana principal
# Crear la ventana principal
win = MyWindow("Ventana con Ejemplos de Inputs", 1000, 1000)

# Crear y agregar RadioButtons al primer GroupBox
ckbs1 = ["Grupo 1", "Grupo 2", "Grupo 3"]
distY = 40  # Ajuste inicial de Y para posición interna en el GroupBox
radioButtons_1 = []
for i, nombre in enumerate(ckbs1):
    ckb1 = MyRadioButton(win, f"rb1_{i+1}", 30, distY, nombre, font_1)
    ckb1.chSize(200, 30)
    radioButtons_1.append(ckb1)
    distY += 40  # Ajuste de espacio entre RadioButtons

gp1 = MyGroupBox(win, "grupoNumeros", 20, 20, "Seleccione su numero:", font_1)
gp1.chSize(350, 200)
for rb in radioButtons_1:
    gp1.groupBox.Controls.Add(rb.radioButton)  # Añadir los RadioButtons al GroupBox

# Añadir el primer GroupBox a la ventana principal
win.Controls.Add(gp1.groupBox)


# Crear y agregar RadioButtons al segundo GroupBox
ckbs2 = ['Opción A', 'Opción B', 'Opción C']
distY = 40
radioButtons_2 = []
for i, nombre in enumerate(ckbs2):
    ckb2 = MyRadioButton(win, f"rb2_{i+1}", 0, distY, nombre, font_1)
    ckb2.chSize(200, 30)
    radioButtons_2.append(ckb2)
    distY += 40

gp2 = MyGroupBox(win, "grupoOpciones", 400, 20, "Seleccione una opción:", font_1)
gp2.chSize(350, 200)
for rb in radioButtons_2:
    gp2.groupBox.Controls.Add(rb.radioButton)

# Añadir el segundo GroupBox a la ventana principal
win.Controls.Add(gp2.groupBox)



# Agregar un label
label = MyLabel(win, 20, 250, "Escriba su nombre y apellido:", font_1)

# Agregar un campo de entrada de texto (textbox)
textbox = MyTextBox(win, "campoNombre_1", 20, 300, 250, 30, font_1)

# Agregar un campo de entrada de texto (textbox)
textbox = MyTextBox(win, "campoNombre_2", 300, 300, 250, 30, font_1)

# Agregar un checkbox
checkbox = MyCheckBox(win, "checkAceptar_1", 20, 350, "Aceptar términos y condiciones 1", font_1)
checkbox.chSize(500, 30)

# Agregar un checkbox
checkbox = MyCheckBox(win, "checkAceptar_2", 20, 400, "Aceptar términos y condiciones 2", font_1)
checkbox.chSize(500, 30)


# Agregar un combobox con opciones
combo = MyComboBox(win, "comboOpciones", 20, 450, "Seleccione una opción:", font_1, ["Opción 1", "Opción 2", "Opción 3"])
combo.chSize(500, 30)

# meter button
boton = MySelectButton(win, "seleccionarElementos", 150, 550, "Seleccionar elementos", font_1)


# Crear los botones "Aceptar" y "Cancelar" con tamaños personalizados
win.add_accept_button(50, 900, "Aceptar", font_1, width=120, height=40)
win.add_cancel_button(300, 900, "Cancelar", font_1, width=120, height=40)

# # Establecer el ícono en la parte inferior de la ventana utilizando un enlace de imagen
imagePath = os.path.join(directorio_dynamo, 'image 512px.png')
win.addImage( imagePath, 512, 512, 450, 0)


OUT = windowsform_ejecutar_y_extraer(win)

# todo hacer que los rediobuttons de un grupo tengan uno seleccionado por defecto
# todo hacer grupos de checkbox, al menos dos grupos.
