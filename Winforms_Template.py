#!/usr/bin/env python
#-*- coding: utf-8 -*-
# PLANTILLA PYTHON para WINDOWS FORMS
# Ultima edicion de esta plantilla 241125

# region BIBLIOTECAS ___________________________________________
#from re import T #da error, que T??? 
import clr
import System
# from System import Array
# from System.Collections.Generic import * 
# from System.Collections.Generic import List as netList # Para crear IList

# # Dynamo Core_______________________________________
# clr.AddReference('Protogeometry') 
# from Autodesk.DesignScript.Geometry import *

# clr.AddReference('DSCoreNodes')
# import DSCore
# from DSCore import *

# # Dynamo Revit________________________________________
# clr.AddReference('RevitNodes') 
# import Revit
# clr.ImportExtensions(Revit.Elements) 
# clr.ImportExtensions(Revit.GeometryConversion) 

clr.AddReference('RevitAPI') # Agrega las clases que se encuentran en el archivo dll de la API de Revit
import Autodesk
from Autodesk.Revit.DB import *
# import Autodesk.Revit.DB as DB

clr.AddReference('RevitAPIUI') 
import Autodesk
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

clr.AddReference('RevitServices') # Permite manejar documentos y modificarlos
import RevitServices 
from RevitServices.Persistence import DocumentManager # Permite acceder al documento del modelo, para hacer collector

doc = DocumentManager.Instance.CurrentDBDocument
app = DocumentManager.Instance.CurrentUIApplication.Application 
uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = uiapp.ActiveUIDocument 


# endregion


from System.Drawing import Size, Color, Icon, Point, Font, FontStyle, FontFamily, GraphicsUnit, ContentAlignment
from System.Windows.Forms import Application, Form, PictureBox, FormBorderStyle, Label, BorderStyle, FlatStyle, TextBox, HorizontalAlignment, ScrollBars, Button, ComboBox, ComboBoxStyle, CheckBox, GroupBox, RadioButton

# ----------------------------------------------------------------------------- # ENUMERATORS
# region
borderStyle =   {   'FixedSingle': BorderStyle.FixedSingle,
                    'Fixed3D': BorderStyle.Fixed3D    }

contentAlignment =  {   'TopLeft': ContentAlignment.TopLeft,
                        'TopCenter': ContentAlignment.TopCenter,
                        'TopRight': ContentAlignment.TopRight,
                        'MiddleLeft': ContentAlignment.MiddleLeft,
                        'MiddleCenter': ContentAlignment.MiddleCenter,
                        'MiddleRight': ContentAlignment.MiddleRight,
                        'BottomLeft': ContentAlignment.BottomLeft,
                        'BottomCenter': ContentAlignment.BottomCenter,
                        'BottomRight': ContentAlignment.BottomRight }

flatStyle = {   'Flat': FlatStyle.Flat,
                'Popup': FlatStyle.Popup,
                'Standard': FlatStyle.Standard,
                'System': FlatStyle.System  }

fontStyle = {   'Regular': FontStyle.Regular,
                'Bold': FontStyle.Bold,
                'Italic': FontStyle.Italic,
                'Underline': FontStyle.Underline,
                'Strikeout': FontStyle.Strikeout    }

horizontalAlignment =   {   'Left': HorizontalAlignment.Left,
                            'Right': HorizontalAlignment.Right,
                            'Center': HorizontalAlignment.Center    }

scrollBars =    {   'Horizontal': ScrollBars.Horizontal,
                    'Vertical': ScrollBars.Vertical,
                    'Both': ScrollBars.Both }
#endregion
# ----------------------------------------------------------------------------- # CLASSES

# region MyButton
class MyButton(Button):
    '''Creates a button.'''
    
    def __init__(self, form, name, distX, distY, text, font, style=FlatStyle.Standard):
        '''Instantiate a new button within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]
        style: The FlatStyle enum stored in flatStyle dict.  [flatStyle[Key]]'''

        self.button = Button()
        self.button.Name = name
        self.button.Location = Point(distX, distY)
        self.button.Text = text
        self.button.Font = font
        self.button.FlatStyle = style
        self.button.AutoSize = True

        self.button.Click += form.buttonPressed_CloseWindow
        form.Controls.Add(self.button)

    def chAppearance(self, dimX, dimY, bThickness, redBound, greenBound, blueBound, redSurface, greenSurface, blueSurface):
        '''Change the appearance of the button.
        
        dimX: Width of the rectangle of the button.  [Int]
        dimY: Height of the rectangle of the button.  [Int]
        bThickness: Border thickness in pixels.  [Int]
        redBound: Range of brightness of Red colour bewteen 0-255 for bounds.  [Int]
        greenBound: Range of brightness of Green colour bewteen 0-255 for bounds.  [Int]
        blueBound: Range of brightness of Blue colour bewteen 0-255 for bounds.  [Int]
        redSurface: Range of brightness of Red colour bewteen 0-255 for bounds.  [Int]
        greenSurface: Range of brightness of Green colour bewteen 0-255 for bounds.  [Int]
        blueSurface: Range of brightness of Blue colour bewteen 0-255 for bounds.  [Int]'''

        self.button.AutoSize = False
        self.button.SetClientSizeCore(dimX, dimY)
        self.button.FlatStyle = FlatStyle.Flat
        self.button.FlatAppearance.BorderSize = bThickness
        self.button.FlatAppearance.BorderColor = Color.FromArgb(redBound, greenBound, blueBound)
        self.button.FlatAppearance.MouseOverBackColor = Color.FromArgb(redSurface, greenSurface, blueSurface)

    def chBackColor(self, red, green, blue):
        '''Change the background color of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.button.BackColor = Color.FromArgb(red, green, blue)

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.button.ForeColor = Color.FromArgb(red, green, blue)
# endregion

# region MyCheckBox
class MyCheckBox(CheckBox):
    '''Creates a check box.'''
    
    def __init__(self, form, name, distX, distY, text, font):
        '''Instantiates a new check box within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]'''
        
        self.checkBox = CheckBox()
        self.checkBox.Name = name
        self.checkBox.Location = Point(distX, distY)
        self.checkBox.Text = text
        self.checkBox.Font = font
        self.checkBox.Autosize = True
        form.Controls.Add(self.checkBox)

    def chBackColor(self, red, green, blue):
        '''Change the background color of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.checkBox.BackColor = Color.FromArgb(red, green, blue)

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.checkBox.ForeColor = Color.FromArgb(red, green, blue)

    def chSize(self, dimX, dimY):
        '''Change the size of the check box.
    
        dimX: Width of the rectangle of the check box.  [Int]
        dimY: Height of the rectangle of the check box.  [Int]'''
        
        self.checkBox.AutoSize = False
        self.checkBox.SetClientSizeCore(dimX, dimY) 
# endregion

# region MyComboBox
class MyComboBox(ComboBox):
    '''Creates a combo box.'''
    
    def __init__(self, form, name, distX, distY, text, font, elements, style=FlatStyle.Standard):
        '''Instantiate a new combo box within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]'''
        
        self.comboBox = ComboBox()
        self.comboBox.Name = name
        self.comboBox.Location = Point(distX, distY)
        self.comboBox.Font = font
        self.comboBox.FlatStyle = style
        self.comboBox.DropDownStyle = ComboBoxStyle.DropDownList
        self.comboBox.Items.Insert(0, text)
        self.comboBox.SelectedIndex = 0        
        [self.comboBox.Items.Add(i) for i in elements]
        self.comboBox.AutoSize = True
        form.Controls.Add(self.comboBox)

    def chBackColor(self, red, green, blue):
        '''Change the background color of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.comboBox.BackColor = Color.FromArgb(red, green, blue)

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.comboBox.ForeColor = Color.FromArgb(red, green, blue)

    def chSize(self, dimX, dimY):
        '''Change the size of the combo box.
    
        dimX: Width of the rectangle of the text box.  [Int]
        dimY: Height of the rectangle of the text box.  [Int]'''
        
        self.comboBox.AutoSize = False
        self.comboBox.SetClientSizeCore(dimX, dimY) 
# endregion

# region MyGroupBox
class MyGroupBox(GroupBox):
    '''Creates a group box.'''
    
    def __init__(self, form, name, distX, distY, text, font, style=FlatStyle.Standard):
        '''Instantiates a new group box within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]
        style: The FlatStyle enum stored in flatStyle dict.  [flatStyle[Key]]'''
        
        self.groupBox = GroupBox()
        self.groupBox.Name = name
        self.groupBox.Location = Point(distX, distY)
        self.groupBox.Text = text
        self.groupBox.Font = font
        self.groupBox.FlatStyle = style
        self.groupBox.AutoSize = True
        form.Controls.Add(self.groupBox)

    def chBackColor(self, red, green, blue):
        '''Change the background color of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.groupBox.BackColor = Color.FromArgb(red, green, blue)

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.groupBox.ForeColor = Color.FromArgb(red, green, blue)

    def chSize(self, dimX, dimY):
        '''Change the size of the group box.
    
        dimX: Width of the rectangle of the group box.  [Int]
        dimY: Height of the rectangle of the group box.  [Int]'''
        
        self.groupBox.AutoSize = False
        self.groupBox.SetClientSizeCore(dimX, dimY) 
# endregion

# region MyLabel
class MyLabel(Label):
    '''Creates a label.'''

    def __init__(self, form, distX, distY, text, font):
        '''Instantiate a new label within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]'''

        self.label = Label()
        self.label.Location = Point(distX, distY)
        self.label.Text = text
        self.label.Font = font
        self.label.AutoSize = True
        form.Controls.Add(self.label)

    def chAlignment(self, alignment):
        '''Change the alignment of the text within the label.
        
        alignment: The ContentAlignment enum stored in contentAlignment dict.  [contentAlignment[Key]]'''
        
        self.label.AutoSize = False
        self.label.TextAlign = alignment

    def chBackColor(self, red, green, blue):
        '''Change the background color of the label.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.label.BackColor = Color.FromArgb(red, green, blue)

    def chBorderStyle(self, style, dimX, dimY):
        '''Change the BorderStyle of the label.
        
        style: The BorderStyle enum stored in borderStyle dict.  [borderStyle[Key]]
        dimX: Width of the rectangle of the label.  [Int]
        dimY: Height of the rectangle of the label.  [Int]'''

        self.label.AutoSize = False
        self.label.SetClientSizeCore(dimX, dimY)
        self.label.BorderStyle = style

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the label.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.label.ForeColor = Color.FromArgb(red, green, blue)
        
    def chFlatStyle(self, style):
        '''Change the appearance of the label.
        
        style: The FlatStyle enum stored in flatStyle dict.  [flatStyle[Key]]'''
        
        self.label.FlatStyle = style
# endregion

# region MyRadioButton
class MyRadioButton(RadioButton):
    '''Creates a radio button.'''

    def __init__(self, form, name, distX, distY, text, font):
        '''Instantiates a new radio button within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]'''
        
        self.radioButton = RadioButton()
        self.radioButton.Name = name
        self.radioButton.Location = Point(distX, distY)
        self.radioButton.Text = text
        self.radioButton.Font = font
        self.radioButton.AutoSize = True
        form.Controls.Add(self.radioButton)

    def chSize(self, dimX, dimY):
        '''Change the size of the radio button.
    
        dimX: Width of the rectangle of the group box.  [Int]
        dimY: Height of the rectangle of the group box.  [Int]'''
        
        self.radioButton.AutoSize = False
        self.radioButton.SetClientSizeCore(dimX, dimY)
# endregion

# region MyTextBox
class MyTextBox(TextBox):
    '''Creates a text box.'''
    
    def __init__(self, form, name, distX, distY, dimX, dimY, font, text=''):
        '''Instantiates a new text box within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        dimX: Width of the rectangle of the text box.  [Int]
        dimY: Height of the rectangle of the text box.  [Int]
        font: The font of the text displayed by the text box.  [System.Drawing.Font]
        text: The text associated with this text box.  [Str]'''
        
        self.textBox = TextBox()
        self.textBox.Name = name
        self.textBox.Location = Point(distX, distY)
        self.textBox.Size = Size(dimX, dimY)
        self.textBox.Font = font
        self.textBox.Text = text
        form.Controls.Add(self.textBox)
        
    def addPassword(self, char):
        '''Set the character used to mask characters within the text box.
        
        char: A symbol character.  [Str]'''
        
        self.textBox.PasswordChar = char

    def chAlignment(self, alignment):
        '''Change the alignment of the text within the text box.
        
        alignment: The HorizontalAlignment enum stored in horizontalAlignment dict.  [horizontalAlignment[Key]]'''
        
        self.textBox.AutoSize = False
        self.textBox.TextAlign = alignment

    def chBackColor(self, red, green, blue):
        '''Change the background color of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.textBox.BackColor = Color.FromArgb(red, green, blue)

    def chBorderStyle(self, style, dimX, dimY):
        '''Change the BorderStyle of the text box.
        
        style: The BorderStyle enum stored in borderStyle dict.  [borderStyle[Key]]
        dimX: Width of the rectangle of the text box.  [Int]
        dimY: Height of the rectangle of the text box.  [Int]'''

        self.textBox.AutoSize = False
        self.textBox.SetClientSizeCore(dimX, dimY)
        self.textBox.BorderStyle = style

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.textBox.ForeColor = Color.FromArgb(red, green, blue)

    def setMultiline(self, scrollBars=False):
        '''Set this text box as a multiline.
        
        scrollBar: The ScrollBars enum stored in scrollBar dict.  [scrollBar[Key]]'''
        
        self.textBox.Multiline = True
        if scrollBars:
            self.textBox.ScrollBars = scrollBars
# endregion

# region MySelectButton
class MySelectButton(Button):
    '''Creates a button for selecting elements in Dynamo.'''
    
    def __init__(self, form, name, distX, distY, text, font, style=FlatStyle.Standard):
        '''Instantiate a new button within a window.
        
        form: The window to which the control belongs.  [System.Windows.Forms.Form]
        name: The name associated with this control.  [Str]
        distX: The distance from the left edge of the window to the left edge of the control in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the control in pixels.  [Int]
        text: The text associated with this control.  [Str]
        font: The font of the text displayed by the control.  [System.Drawing.Font]
        style: The FlatStyle enum stored in flatStyle dict.  [flatStyle[Key]]'''

        self.button = Button()
        self.button.Name = name
        self.button.Location = Point(distX, distY)
        self.button.Text = text
        self.button.Font = font
        self.button.FlatStyle = style
        self.button.AutoSize = True

        self.button.Click += form.buttonPressed_SelectElements
        form.Controls.Add(self.button)

    def chAppearance(self, dimX, dimY, bThickness, redBound, greenBound, blueBound, redSurface, greenSurface, blueSurface):
        '''Change the appearance of the button.
        
        dimX: Width of the rectangle of the button.  [Int]
        dimY: Height of the rectangle of the button.  [Int]
        bThickness: Border thickness in pixels.  [Int]
        redBound: Range of brightness of Red colour bewteen 0-255 for bounds.  [Int]
        greenBound: Range of brightness of Green colour bewteen 0-255 for bounds.  [Int]
        blueBound: Range of brightness of Blue colour bewteen 0-255 for bounds.  [Int]
        redSurface: Range of brightness of Red colour bewteen 0-255 for bounds.  [Int]
        greenSurface: Range of brightness of Green colour bewteen 0-255 for bounds.  [Int]
        blueSurface: Range of brightness of Blue colour bewteen 0-255 for bounds.  [Int]'''

        self.button.AutoSize = False
        self.button.SetClientSizeCore(dimX, dimY)
        self.button.FlatStyle = FlatStyle.Flat
        self.button.FlatAppearance.BorderSize = bThickness
        self.button.FlatAppearance.BorderColor = Color.FromArgb(redBound, greenBound, blueBound)
        self.button.FlatAppearance.MouseOverBackColor = Color.FromArgb(redSurface, greenSurface, blueSurface)

    def chBackColor(self, red, green, blue):
        '''Change the background color of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.button.BackColor = Color.FromArgb(red, green, blue)

    def chForeColor(self, red, green, blue):
        '''Change the color of the font of the control.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.button.ForeColor = Color.FromArgb(red, green, blue)
# endregion

# region MyWindow
class MyWindow(Form):
    def __init__(self, windowTitle, dimX, dimY):
        self.Text = windowTitle
        self.ClientSize = Size(dimX, dimY)
        self.FormBorderStyle = FormBorderStyle.FixedSingle
        self.BackColor = Color.FromArgb(235, 235, 235)
        self.CenterToScreen()
        
        # Inicializar controlInfo
        self.controlInfo = {
            'TextBox': {},
            'ComboBox': {},
            'CheckBox': {},
            'RadioButton': {},
            'SelectedElements': {}
        }
        self.selected_elements = None  # Initialize selected elements

    # Método para capturar los datos de todos los controles
    def buttonPressed_CloseWindow(self, sender, args):
        '''Captura los datos de los controles al cerrar la ventana.'''
        
        for control in self.Controls:
            if isinstance(control, TextBox):
                self.controlInfo['TextBox'][control.Name] = control.Text
            elif isinstance(control, ComboBox):
                self.controlInfo['ComboBox'][control.Name] = control.SelectedItem
            elif isinstance(control, CheckBox):
                self.controlInfo['CheckBox'][control.Name] = control.Checked
            elif isinstance(control, RadioButton):
                self.controlInfo['RadioButton'][control.Name] = control.Checked
            elif isinstance(control, GroupBox):
                group_name = control.Name
                if group_name not in self.controlInfo['RadioButton']:
                    self.controlInfo['RadioButton'][group_name] = {}
                
                for sub_control in control.Controls:
                    if isinstance(sub_control, RadioButton):
                        self.controlInfo['RadioButton'][group_name][sub_control.Name] = sub_control.Checked

        if self.selected_elements is not None:
            self.controlInfo['SelectedElements'] = self.selected_elements

        self.Close()

    # Método para cancelar la operación
    def buttonPressed_Cancel(self, sender, args):
        '''Cierra la ventana y deja los diccionarios vacíos.'''
        
        # Vaciar todos los diccionarios en controlInfo
        self.controlInfo = {
            'TextBox': {},
            'ComboBox': {},
            'CheckBox': {},
            'RadioButton': {}
        }
        self.selected_elements = None  # Reset selected elements
        self.Close()
    
    # Método para agregar un botón "Aceptar" con tamaño personalizado
    def add_accept_button(self, x, y, text="Aceptar", font=None, width=100, height=30):
        boton_aceptar = Button()
        boton_aceptar.Text = text
        boton_aceptar.Location = Point(x, y)
        boton_aceptar.Size = Size(width, height)  # Definir tamaño personalizado
        boton_aceptar.Font = font
        boton_aceptar.Click += self.buttonPressed_CloseWindow
        self.Controls.Add(boton_aceptar)
        return boton_aceptar

    # Método para agregar un botón "Cancelar" con tamaño personalizado
    def add_cancel_button(self, x, y, text="Cancelar", font=None, width=100, height=30):
        boton_cancelar = Button()
        boton_cancelar.Text = text
        boton_cancelar.Location = Point(x, y)
        boton_cancelar.Size = Size(width, height)  # Definir tamaño personalizado
        boton_cancelar.Font = font
        boton_cancelar.Click += self.buttonPressed_Cancel
        self.Controls.Add(boton_cancelar)
        return boton_cancelar

    def addImage(self, path, dimX, dimY, distX, distY):
        '''Adds an image to the window.
        
        path: The path in the disk where the image is stored.  [Str]
        dimX: The dimension in the X axis in pixels.  [Int]
        dimY: The dimension in the Y axis in pixels.  [Int]
        distX: The distance from the left edge of the window to the left edge of the image in pixels.  [Int]
        distY: The distance from the top edge of the window to the top edge of the image in pixels.  [Int]'''
        
        self.picture = PictureBox()
        self.picture.Load(path)
        self.picture.ClientSize = Size(dimX, dimY)
        self.picture.Location = Point(distX, distY)
        self.Controls.Add(self.picture)

    def chBackColor(self, red, green, blue):
        '''Changes the background colour of the window.
        
        red: Range of brightness of Red colour bewteen 0-255.  [Int]
        green: Range of brightness of Green colour bewteen 0-255.  [Int]
        blue: Range of brightness of Blue colour bewteen 0-255.  [Int]'''
        
        self.BackColor = Color.FromArgb(red, green, blue)
    
    def chTransparency(self, boolean, value=0.75):
        '''Changes the level of transparency in the window.
        
        boolean: If True, transparency is allowed. If False, not.  [Bool]
        value: The level of transparency bewteen 1.00 (Opaque) & 0.00 (Transparent).'''
        
        self.AllowTransparency = boolean
        if self.AllowTransparency == True:
            self.Opacity = value

    def run(self):
        '''Shows the window.'''
        Application.Run(self)
        return self.controlInfo, self.selected_elements  # Return control info and selected elements after window closes
        
    def setIcon(self, path):
        '''Establishes an icon in the titlebar.
        
        path: The path in the disk where the icon is stored.  [Str]'''
        
        self.Icon = Icon(path)
        
    def setSizable(self, minX, minY, maxX, maxY):
        '''Sets the window sizable by the user.
        
        minX: The increased minimum dimension in the X axis in pixels.  [Int]
        minY: The increased minimum dimension in the Y axis in pixels.  [Int]
        maxX: The increased maximum dimension in the X axis in pixels.  [Int]
        maxY: The increased maximum dimension in the Y axis in pixels.  [Int]'''
        
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.MinimumSize = Size(self.ClientSize.Width - minX, self.ClientSize.Height - minY)
        self.MaximumSize = Size(self.ClientSize.Width + maxX, self.ClientSize.Height + maxY)

    def buttonPressed_SelectElements(self, sender, args):
        '''Handles the event when the select elements button is pressed.'''
        self.selected_elements = ui_seleccion_elementos_rectangulo(True)
        # Handle the selected elements as needed
        print(self.selected_elements)
# endregion

# ----------------------------------------------------------------------------- # FUNCTIONS
# region Fuentes
def crFont(name, size, style=FontStyle.Regular):
    '''Creates a new font.
        
    name: The font family for the new font.  [Str]
    size: The size of the new font in pixels.  [Int]
    style: The FontStyle enum stored in fontStyle dict.  [fontStyle[Key]]'''

    font = Font(FontFamily(name), size, style, GraphicsUnit.Pixel)
    return font
# endregion

# ----------------------------------------------------------------------------- # FUENTES
# region Fuentes seleccionadas
font_1 = crFont("Microsoft Sans Serif", 25, fontStyle['Regular'])
font_2 = crFont("Microsoft Sans Serif", 25, fontStyle['Bold'])
# endregion

# ----------------------------------------------------------------------------- # SELECCIONAR ELEMENTOS
# region Funciones
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
		# en el caso de que sea una lista
		else:
			variables.append(key)
			user_inputs.append(value)
	return inputs, variables, user_inputs

def ui_seleccion_elementos_rectangulo(inicio):
    """
    Uso: Selecciona una serie de elementos por parte del usuario.
    Entrada: [True] o mensaje de inicio para seleccionar un elemento.
    Salida: Elemento seleccionado o mensaje de cancelación.
    Codigo: 240924
    Atención: se puede usar la función mensaje_inicio para mostrar un mensaje de inicio.
    """
    if inicio:
        try:
            seleccion = uidoc.Selection.PickElementsByRectangle()
            salida = list(seleccion)
        except:
            salida = "Proceso cancelado"
    else:
        salida = "Introducir un True para seleccionar un elemento"

    return salida


# endregion