#-*- coding: utf-8 -*-
#______________________________________________________________________________________________________

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

#* FUNIONES LOCALES
# region
def windowsform_ejecutar_y_extraer(ventana):
	"""
	Uso: Ejecutar la ventana y extraer la información de los controles en dos lista, una de variables y otra de valores.
	Entrada: ventana (MyWindow) - Ventana con los controles a extraer. Nombre por defecto: win
	Salida: Dos listas, una con las variables de los controles y otra con los valores de los inputs
	"""
    # Ejecutar la ventana
	ventana.run()
	# Extraer la información de los controles
	inputs = ventana.controlInfo

	# Devolver la información de los controles de cada uno de los diccionarios en una lista
	variables, user_inputs = [], []
	for key, value in inputs.items():
		# comprobar que value es un diccionario
		if isinstance(value, dict):
			for k, v in value.items():
				variables.append(k)
				user_inputs.append(v)
	return inputs, variables, user_inputs

# endregion



# Importar las clases necesarias de la plantilla
from Template import * #MyWindow, MyLabel, MyTextBox, MyCheckBox, MyComboBox, MyGroupBox, MyRadioButton, MyButton, font_1

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

# Crear los botones "Aceptar" y "Cancelar" con tamaños personalizados
win.add_accept_button(50, 550, "Aceptar", font_1, width=120, height=40)
win.add_cancel_button(300, 550, "Cancelar", font_1, width=120, height=40)

# # Establecer el ícono en la parte inferior de la ventana utilizando un enlace de imagen
imagePath = os.path.join(directorio_dynamo, 'image 512px.png')
win.addImage( imagePath, 512, 512, 450, 0)


# # Ejecutar la ventana
# win.run()
# inputs = win.controlInfo
# result = windowsform_ejecutar_y_extraer(inputs)
# # Ahora `result` contiene el diccionario con los valores y puedes usarlo como una variable
# OUT = inputs, result

OUT = windowsform_ejecutar_y_extraer(win)

# todo hacer que los rediobuttons de un grupo tengan uno seleccionado por defecto
# todo hacer grupos de checkbox, al menos dos grupos.
