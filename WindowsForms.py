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
# Añadir la ruta al sys.path
import sys
sys.path.append(directorio_dynamo)

# endregion

# Importar las clases necesarias de la plantilla
from Template import *

# Crear la ventana principal
win = MyWindow("Ventana con Ejemplos de Inputs", 1000, 600)

# Agregar un label
label = MyLabel(win, 20, 20, "Escriba su nombre y apellido:", font_1)

# Agregar un campo de entrada de texto (textbox)
textbox = MyTextBox(win, "campoNombre_1", 20, 60, 250, 30, font_1)

# Agregar un campo de entrada de texto (textbox)
textbox = MyTextBox(win, "campoNombre_2", 300, 60, 250, 30, font_1)

# Agregar un checkbox
checkbox = MyCheckBox(win, "checkAceptar_1", 20, 150, "Aceptar términos y condiciones 1", font_1)
checkbox.chSize(500, 30)

# Agregar un checkbox
checkbox = MyCheckBox(win, "checkAceptar_2", 20, 200, "Aceptar términos y condiciones 2", font_1)
checkbox.chSize(500, 30)


# Agregar un combobox con opciones
combo = MyComboBox(win, "comboOpciones", 20, 250, "Seleccione una opción:", font_1, ["Opción 1", "Opción 2", "Opción 3"])
combo.chSize(500, 30)


# # Agregar un groupbox con radio buttons
# nota no esta funcionando correctamente, no se agregan los radio buttons al groupbox
# nota esta es la unica forma de hacer funcionar los radiobuttons, poniendolos por separado pero sin agrupar
# groupbox = MyGroupBox(win, "grupoGenero", 20, 500, "Seleccione su género:", font_1)
# groupbox.chSize(500, 400)
radio_1 = MyRadioButton(win, "radio_1", 30, 330, "Grupo 1", font_1)
radio_1.chSize(200, 30)
radio_2 = MyRadioButton(win, "radio_2", 30, 370, "Grupo 2", font_1)
radio_2.chSize(200, 30)
radio_3 = MyRadioButton(win, "radio_3", 30, 410, "Grupo 3", font_1)
radio_3.chSize(200, 30)
# Agregar un botón para finalizar la captura de datos en la posición (50, 300)
button = MyButton(win, "btnSubmit", 50, 450, "Enviar", font_1)

# # Establecer el ícono en la parte inferior de la ventana utilizando un enlace de imagen
imagePath = os.path.join(directorio_dynamo, 'image 512px.png')
win.addImage( imagePath, 512, 512, 450, 0)


def windowsform_ejecutar_y_extraer(ventana: MyWindow) -> tuple:
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
	return variables, user_inputs
		

OUT =  win.controlInfo, windowsform_ejecutar_y_extraer(win)

