import tkinter

import pyodbc
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image


#Establish connection to the MSSQL database
try:
    connection = pyodbc.connect(
        'DRIVER={SQL Server};Server=DESKTOP-T1A9G8E\SQLEXPRESS;Database=EquipmentProject;Trusted_Connection=True;')
    print("Connected to Equipment Database")
except pyodbc.Error as err:
    print("Failed to connect ....", err)


#creation of GUI
window = tkinter.Tk()
window.geometry("600x800")
window.config(background="#4F2683")

image = Image.open('logo.jpg')
logo = ImageTk.PhotoImage(image)
logo_label = tkinter.Label(window, image=logo)
logo_label.pack(pady=5)

Headline = tkinter.Label(window, text="Helmet Order", bg="#4F2683")
Headline.pack(anchor='center', pady=5)
Headline.config(font=("Font", 20))

lastName = tkinter.Label(text="Last Name", bg="#4F2683" )
lastNameentry = tkinter.Entry()
lastName.pack()
lastName.config(font=("Font", 11))
lastNameentry.pack()

firstName = tkinter.Label(text="First Name", bg="#4F2683" )
firstNameentry = tkinter.Entry()
firstName.pack()
firstName.config(font=("Font", 11))
firstNameentry.pack()

POS = tkinter.Label(text="Position", bg="#4F2683" )
POSentry = tkinter.Entry()
POS.pack()
POS.config(font=("Font", 11))
POSentry.pack()

jerseryNo = tkinter.Label(text="Jersey Number", bg="#4F2683")
jerseryNoentry = tkinter.Entry()
jerseryNo.pack()
jerseryNo.config(font=("Font", 11))
jerseryNoentry.pack()

# Creating a list of brands to chose from
brandChoice = {
    'Schutt': 1,
    'Riddell': 2,
    'VICIS': 3
}
brandOption = StringVar()
brandOption.set('Choose Brand')
brand = ttk.Combobox(window, textvariable=brandOption, values=list(brandChoice.keys()))
brand.pack(anchor='center', pady=5)


def pick_style(event):
    """
    This function displays a list of styles the user can choose from based on the brand previously selected

    :param event: on brand selection the corresponding styles are displayed to the user
    :return styles_id: the id of the choice of which style the user chooses
    """
    if brand.get() == 'Schutt':
        style.config(value=list(SchuttChoiceStyles.keys()))
        style_id = SchuttChoiceStyles.get(StyleOption.get())

    elif brand.get() == 'Riddell':
        style.config(value=list(RiddellChoiceStyles.keys()))
        style_id = RiddellChoiceStyles.get(StyleOption.get())

    elif brand.get() == 'VICIS':
        style.config(value=list(VICISChoiceStyles.keys()))
        style_id = VICISChoiceStyles.get(StyleOption.get())

    return style_id


brand.bind("<<ComboboxSelected>>", pick_style)

# list of styles choices based on the schutt brand
SchuttChoiceStyles = {
    'F7UR1': 1,
    'F7UR2': 2,
    'F7UR1 2.0': 3,
    'F7 2.0': 4,
    'F7 VTD ll': 5,
    'AIR XP Pro Q11 LTD': 6

}

#list of styles choices based on the Riddell brand
RiddellChoiceStyles = {
    'Axiom': 7,
    'Speedflex': 8,
    'Speedflex P-Fit': 9,
    'Speedflex Diamond': 10,
    'Speedflex Diamond P-Fit': 11,
    'Speedflex True': 12

}

#list of styles choices based on the VICIS brand
VICISChoiceStyles = {
    'Zero2 matrix QB': 13,
    'Zero2-R': 14
}

StyleOption = StringVar()
StyleOption.set('Choose Style')
style = ttk.Combobox(window, textvariable=StyleOption, values={})
style.pack(anchor='center', pady=5)


def pick_size(event):
    """
    This function displays a list of sizes the user can choose from based on the style previously selected


    :param event: on styles selection the corresponding sizes are displayed to the user
    :return: size_id: the id of the choice of which size the user selected
    """
    if brand.get() == 'Schutt':
        size.config(value=list(SchuttChoiceSizes.keys()))
        size_id = SchuttChoiceSizes.get(SizeOption.get())

    elif brand.get() == 'Riddell':
        size.config(value=list(RiddellChoiceSizes.keys()))
        size_id = RiddellChoiceSizes.get(SizeOption.get())

    elif brand.get() == 'VICIS':
        size.config(value=list(VICISChoiceSizes.keys()))
        size_id = VICISChoiceSizes.get(SizeOption.get())

    return size_id


style.bind("<<ComboboxSelected>>", pick_size)

#list of sizes based on the Schutt brand
SchuttChoiceSizes = {
    'M': 1,
    'L': 2,
    'L+': 3,
    'XL': 4,
    'Custom': 5
}

#list of sizes based on the Riddell brand
RiddellChoiceSizes = {
    'Custom': 6,
    'M': 7,
    'L': 8,
    'XL': 9
}

#list of sizes based on the VICIS brand
VICISChoiceSizes = {
    'Standard': 10,
    'Trench': 11
}

SizeOption = StringVar()
SizeOption.set('Choose Size')
size = ttk.Combobox(window, textvariable=SizeOption, values={})
size.pack(anchor='center', pady=5)


def pick_facemask(event):
    """
    This function displays a list of facemasks the user can choose from based on the sizes previously selected


    :param event: on size selection the corresponding facemasks are displayed to the user
    :return: facemask_id: the id of the choice of which facemask the user selected

    """
    if brand.get() == 'Schutt':
        facemask.config(value=list(SchuttChoiceFacemask.keys()))
        facemask_id = SchuttChoiceFacemask.get(FacemaskOption.get())


    elif brand.get() == 'Riddell':
        facemask.config(value=list(RiddellChoiceFacemask.keys()))
        facemask_id = RiddellChoiceFacemask.get(FacemaskOption.get())

    elif brand.get() == 'VICIS':
        facemask.config(value=list(VICISChoiceFacemask.keys()))
        facemask_id = VICISChoiceFacemask.get(FacemaskOption.get())

    return facemask_id


size.bind("<<ComboboxSelected>>", pick_facemask)

##list of facemasks based on the Schutt brand
SchuttChoiceFacemask = {
    'TROPO-SW': 1,
    'TROPO': 2,
    'TROPO-DW': 3,
    'TEGOP': 4,
    'TEGOPll': 5,
    'TEGOPll-DW': 6,
    'TRJOP-DW': 7,
    'TRJOP-DW UB': 8,
    'TRKOP': 9,
    'SF-3BD RR': 10
}

##list of facemasks based on the Riddell brand
RiddellChoiceFacemask = {
    'Axiom 2B- SW-TI': 11,
    'Axiom 2BC-TI': 12,
    'SF-2BD': 13,
    'SF-2BD-SW': 14,
    'SF-2BDC': 15,
    'SF-2BDC-HD': 16,
    'SF-2EG-SW': 17,
    'SF-2EG-SW-HD': 18,
    'SF-2EG-ll': 19,
    'SF-2EG-ll-HD': 20,
    'SF-3BD': 21,
    'SF-Kicker': 22,
    'CU-SF-2B-SW': 23,
    'CU-SF-2B-PW': 24
}

#list of facemasks based on the VICIS brand
VICISChoiceFacemask = {
    'Z02-SO-212E': 25,
    'Z02-SO-212': 26,
    'Z02-SO-223E': 27,
    'Z02-SO-223': 28,
    'Z02-SC-223E': 29,
    'Z02-SC-223': 30,
    'Z02-SK-212': 31,
    'Z02-SO-213E': 32,
    'Z02-SO-215T': 33
}

FacemaskOption = StringVar()
FacemaskOption.set('Choose Facemask')
facemask = ttk.Combobox(window, textvariable=FacemaskOption, values={})
facemask.pack(anchor='center', pady=5)


def pick_jawMaterial(event):
    """
    This function displays a list of jaw pad materials the user can choose from based on the size previously selected

    :param event: on size selection the corresponding jaw pad material are displayed to the user
    :return: size_id: the id of the choice of which material the user selected

    """
    if brand.get() == 'Schutt':
        material.config(value=list(SchuttChoiceMaterial.keys()))
        material_id = SchuttChoiceMaterial.get(MaterialOption.get())

    elif brand.get() == 'Riddell':
        material.config(value=list(RiddellChoiceMaterial.keys()))
        material_id = RiddellChoiceMaterial.get(MaterialOption.get())

    elif brand.get() == 'VICIS':
        material.config(value=list(VICISChoiceMaterial.keys()))
        material_id = VICISChoiceMaterial.get(MaterialOption.get())

    return material_id

facemask.bind("<<ComboboxSelected>>", pick_jawMaterial)

#list of jaw materials based on the Schutt brand
SchuttChoiceMaterial = {
    '2.0': 1,
    'Leather': 2
}

#list of jaw materials based on the Riddell brand
RiddellChoiceMaterial = {
    '2.0': 3,
    'SF':4
}

#list of jaw materials based on the VICIS brand
VICISChoiceMaterial = {
    'NONE': 5
}

MaterialOption = StringVar()
MaterialOption.set('Choose JawPad(Material)')
material = ttk.Combobox(window, textvariable=MaterialOption, values={})
material.pack(anchor='center', pady=5)

def pick_jawSize(event):
    """
    This function displays a list of jaw pad sizes the user can choose from based on the jaw pad material previously selected


    :param event: on jaw pad material selection the corresponding sizes are displayed to the user
    :return: jaw_size_id: the id of the choice of which size the user selected
    """
    if material.get() == '2.0' and brand.get() == 'Schutt':
        jawSize.config(value=list(SchuttChoiceJawSize.keys()))
        jaw_size_id = SchuttChoiceJawSize.get(jawSizeOption.get())

    elif material.get() =='Leather':
        jawSize.config(value=list(SchuttChoiceJawSizeL.keys()))
        jaw_size_id = SchuttChoiceJawSizeL.get(jawSizeOption.get())

    elif material.get() == '2.0' and brand.get() == 'Riddell':
        jawSize.config(value=list(RiddellChoiceJawSize.keys()))
        jaw_size_id = RiddellChoiceJawSize.get(jawSizeOption.get())

    elif material.get() == 'SF':
        jawSize.config(value=list(RiddellChoiceJawSizeSF.keys()))
        jaw_size_id = RiddellChoiceJawSizeSF.get(jawSizeOption.get())

    elif material.get() == 'NONE':
        jawSize.config(value=list(VICISChoiceJawSize.keys()))
        jaw_size_id = VICISChoiceJawSize.get(jawSizeOption.get())

    return jaw_size_id


material.bind("<<ComboboxSelected>>", pick_jawSize)

#list of jaw pad sizes based on the Schutt brand with material 2.0
SchuttChoiceJawSize = {
    '1/2"':1,
    '3/8"':2,
    '3/4"':3,
    '1"':4
}
#list of jaw pad sizes based on the Schutt brand with Leather material
SchuttChoiceJawSizeL = {
    '1/2"':5,
    '3/8"':6,
    '3/4"':7,
    '1"':8
}

#list of jaw pad sizes based on the Riddell brand with SF material
RiddellChoiceJawSizeSF = {
'SF 3/4"':9,
    'SF 1"':10
}
#list of jaw pad sizes based on the Riddell brand with 2.0 material
RiddellChoiceJawSize = {
    '2.0 J0':11,
    '2.0 J1':12,
    '2.0 J2':13,
    '2.0 J3':14,
    '2.0 J4':15,
    '2.0 J5':16,
    '2.0 J6':17,
    '2.0 J7':18,
    '2.0 J8':19
}

#list of jaw pad sizes based on the VICIS brand
VICISChoiceJawSize = {
    '.625"': 20,
    '0.75"': 21,
    '1"': 22
}

jawSizeOption = StringVar()
jawSizeOption.set('Choose Jaw Pad(Size)')
jawSize = ttk.Combobox(window, textvariable=jawSizeOption, values={})
jawSize.pack(anchor='center', pady=5)

#list of visor choices
visorChoice ={
    'PRIZM': 1,
    'CLEAR' : 2,
    'DARK' : 3,
    'NONE': 4
}

visorOption = StringVar()
visorOption.set('Choose Visor')
visor = ttk.Combobox(window, textvariable=visorOption, values=list(visorChoice.keys()))
visor.pack(anchor='center', pady=5)

#list of chinstrap choices
chinStrapChoice ={
    'Sports Star': 1,
    'Sports Star XD' : 2,
    'Riddell Hard Cup Lrg' : 3,
    'Riddell Hard Cup Med' : 4,
    'Sports Star Leather' :5
}

chinStrapOption = StringVar()
chinStrapOption.set('Choose Chin Strap')
chinstrap = ttk.Combobox(window, textvariable=chinStrapOption, values=list(chinStrapChoice.keys()))
chinstrap.pack(anchor='center', pady=5)

brand.bind("<<ComboboxSelected>>", pick_style)

e = 'placeholder'


def insert():
    """
    Takes values based on all user equipment selections from dropdown menus and inserts them into the
    Equipment database in MSSQL into the Test Table.

    :return: NONE
    """
    try:
        connection.execute(f"INSERT INTO Test (LastName, FirstName, POS, Jersey, BrandID, StylesID,  SizeID , FacemaskID, MaterialID, JawSizeID,VisorID, ChinStrapID) "
                           f"VALUES ('{lastNameentry.get()}', '{firstNameentry.get()}', '{POSentry.get()}', '{jerseryNoentry.get()}', '{brandChoice.get(brandOption.get())}', '{pick_style(e)}',"
                           f"'{pick_size(e)}', '{pick_facemask(e)}'  , '{pick_jawMaterial(e)}', '{pick_jawSize(e)}' , '{visorChoice.get(visorOption.get())}', '{chinStrapChoice.get(chinStrapOption.get())}')")
        print('Success')
        tkinter.messagebox.showinfo(message='Submitted!')
        connection.autocommit = True

    except pyodbc.Error as err:
        print("Failed to submit Helmet Data", err)
        tkinter.messagebox.ERROR = 'Error in submission'

# submit button for GUI
submitButton = tkinter.Button(
    text="Submit",
    width=8,
    bg="grey",
    fg="#4F2683",
    command=insert
)
submitButton.pack()

window.mainloop()
