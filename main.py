from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox
from time import sleep


#updates status bar 
def updateStatusBar():
    #assigning number of lines and columns to variable
    line, column = map(int, textWidget.index(INSERT).split('.'))
    #geting number of characters
    numberOfCharacters = len(textWidget.get('1.0', END)) - 1
    #assigning text on label to number of characters, columns and lines
    statusBar.config(text=f'Line {line}, Column {column}, Number of characters {numberOfCharacters}')

#class that contains all commands that for menu bar 
class Commands:
    def __init__(self):
        self.fileBeenOpened = False
        self.pathOfOpenedFile = ''
        self.currentFont = 'Arial'
        self.currentFontSize = 12
        
    
    #function that creates new document 
    def newFileCommand(self):
        #display message to validate user wants to create new file 
        if messagebox.askokcancel("Create new file", 'Do you want to create a new file any unsaved changes will be lost'):
            #clear editor 
            textWidget.delete(1.0, END)
            sleep(1)
            #insert message into the editor and set file been opened to false
            textWidget.insert('1.0', 'You have created a new file')
            self.fileBeenOpened = False
            
    #function that saves file
    def saveFileCommand(self):
        #checking if the text in editor came from a file if so, saves to that file if not calls saveFileAs function
        if self.fileBeenOpened:
            print('Saving changes to the original file')
            #opening file that the text in editor came from
            with open(self.pathOfOpenedFile, 'w') as f:
                f.write(textWidget.get(1.0, END))
            #updating status bar
            updateStatusBar()
        else:
            print('prompting user to choose location')
            self.saveFileAsCommand()

    #function that opens a selected file
    def openFileCommand(self):
        #asks user to select file to be opened only allows for txt files to be opened
        self.pathOfOpenedFile = filedialog.askopenfilename(filetypes=[('Text files', '*txt')])
        #if path been chosen all text in editor deleted and text in file inserted into the editor 
        if self.pathOfOpenedFile:
            with open(self.pathOfOpenedFile, 'r') as f:
                textWidget.delete('1.0', END)
                textWidget.insert('1.0', f.read())
                #fileBeenOpened True to determine what will happen when the save button is pressed
                self.fileBeenOpened = True
            #updating status bar
            updateStatusBar()
                
    #function that allows users to save text in editor to specific file
    def saveFileAsCommand(self):
        #asks user to select file path
        filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text file', '*txt')])
        #if path selected open file and write all text in editor to that file
        if filePath:
            with open(filePath, 'w') as f:
                f.write(textWidget.get('1.0', END))
                #set fileBeenOpened to True and pathOfOpenedFile to the opened file's path so when save button pressed the save is written to file that text was saved to 
                self.fileBeenOpened = True
                self.pathOfOpenedFile = filePath
            #updating status bar 
            updateStatusBar()

    #function that allows users to exit out of the editor
    def exitCommand(self):
        #displays message box asking user if they want to exit if yes the main window is destroyed, if false nothing happens
        if messagebox.askokcancel('Exit', 'Do you want to exit'):
            window.destroy()

    #function that copys selected text to clipboard
    def copyCommand(self):
        #error handiling for if no text is selected when copy button pressed
        try:
            #getting selected text then clearing clipboard and appending selected text to clipboard
            textToCopy = textWidget.get(SEL_FIRST, SEL_LAST)
            window.clipboard_clear()
            window.clipboard_append(textToCopy)
        except TclError:
            print('No text selected to copy')

    #function that pastes text in the clipboard into the editor
    def pasteCommand(self):
        #error handiling for if not text is in the clipboard when paste button is pressed
        try:
            #assigning text in clipboard to variable then inserting that text into editor
            textToPaste = window.clipboard_get()
            textWidget.insert(INSERT, textToPaste)
        except TclError:
            print('There is nothing in the clipboard to paste')  

    #function that cuts selected text and appends it to the clipboard
    def cutCommand(self): 
        #error handiling for if not text was selected when cut button pressed
        try:
            #assigning current selecte text to variable 
            textToCut = textWidget.get(SEL_FIRST, SEL_LAST)
            #deleteing current selected text 
            textWidget.delete(SEL_FIRST, SEL_LAST)
            #clearing clipboard and appending selected text to it 
            window.clipboard_clear()
            window.clipboard_append(textToCut)
        except TclError:
            print('No text was selected to cut')

    #function that sets font to Arial
    def arialFontCommand(self):
        #setting font to Arial in the size that the font currently is
        textWidget.config(font=('Arial', self.currentFontSize))
        #setting currentFont to Arial
        self.currentFont = 'Arial'
    
    #function that sets font to Times New Roman 
    def timesNewRomanFontCommand(self):
        #setting font to Times New Roman in the size that the font currently is
        textWidget.config(font=('Times New Roman', self.currentFontSize))
        #setting currentFont to Times New Roman
        self.currentFont = 'Times New Roman'

    #function that sets font to Calibri
    def calibriFontCommand(self):
        #setting font to Calibri in the size that the font currently is
        textWidget.config(font=('Calibri', self.currentFontSize))
        #setting currentFont to Calibri
        self.currentFont = 'Calibri'

    #function that sets font to Verdana
    def verdanaFontCommand(self):
        #setting font to Verdana in the size that the font currently is
        textWidget.config(font=('Verdana', self.currentFontSize))
        #setting currentFont to Verdana
        self.currentFont = 'Verdana'
    
    #function that sets font size to 12
    def twelveFontSizeCommand(self):
        #setting font size to 12 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 12))
        #setting currentFontSize to 12 
        self.currentFontSize = 12

    #function that sets font size to 14
    def fourteenFontSizeCommand(self):
        #setting font size to 14 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 14))
        #setting currentFontSize to 14
        self.currentFontSize = 14

    #function that sets font size to 16
    def sixteenFontSizeCommand(self):
        #setting font size to 16 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 16))
        #setting currentFontSize to 16
        self.currentFontSize = 16

    #function that sets font size to 18
    def eighteenFontSizeCommand(self):
        #setting font size to 18 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 18))
        #setting currentFontSize to 18
        self.currentFontSize = 18

    #function that sets font size to 20
    def twentyFontSizeCommand(self):
        #setting font size to 20 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 20))
        #setting currentFontSize to 20
        self.currentFontSize = 20

    #function that sets font size to 22
    def twentyTwoFontSizeCommand(self):
        #setting font size to 22 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 22))
        #setting currentFontSize to 22
        self.currentFontSize = 22

    #function that sets font size to 24
    def twentyFourFontSizeCommand(self):
        #setting font size to 24 in the font that the text currently is
        textWidget.config(font=(self.currentFont, 24))
        #setting currentFontSize to 24
        self.currentFontSize = 24

    #function that sets the text widgets appearance to a light mode
    def lightModeCommand(self):
        #setting text widgets background to white and text to black
        textWidget.config(background='White', foreground='Black')
        
    #function that sets the text widgets appearance to a dark mode
    def darkModeCommand(self):
        #setting text widgets background to black and text to white
        textWidget.config(background='Black', foreground='White')
        
    #function that sets the text widgets appearance to a contrast mode   
    def contrastModeCommand(self):
        #setting text widgets background to grey and text to white
        textWidget.config(background='Grey', foreground='White')
        


#creating main window
window = Tk()

#setting windows title, geometry and its minimum size
window.title('Simple text editor')
window.geometry('560x560')
window.minsize(height=560, width=560)

#creating a scrolledText widget
textWidget = ScrolledText(window, background='white', foreground='black', font=('Arial', 12), width=200, wrap=WORD)
#creating a status bar label
statusBar = Label(window, text='', bd=1, relief=SUNKEN, anchor=W)
#packing status bar
statusBar.pack(side=BOTTOM, fill=X)

#packing scrolled text widget 
textWidget.pack(fill= BOTH, expand=True)
#inserting the text welcome to my text editor into the text widget 
textWidget.insert(END, 'Welcome to my text editor')

#creating menu widget
menuWidget = Menu(window)

#creating menu widgets for file, edit, font, font size and appearance attaching them to menu widget 
fileMenu = Menu(menuWidget, tearoff=0)
editMenu = Menu(menuWidget, tearoff=0)
fontMenu = Menu(menuWidget, tearoff=0)
fontSizeMenu = Menu(menuWidget, tearoff=0)
appearanceMenu = Menu(menuWidget, tearoff=0)


#crating instance of commands class 
commands = Commands()

#adding file menu options and attaching corresponding commands to them
fileMenu.add_command(label='New file', command=commands.newFileCommand)
fileMenu.add_command(label='Save file', command=commands.saveFileCommand)
fileMenu.add_command(label='Open file', command=commands.openFileCommand)
fileMenu.add_command(label='Save as', command=commands.saveFileAsCommand)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=commands.exitCommand)

#adding edit menu options and attaching corresponding commands to them 
editMenu.add_command(label='Copy', command=commands.copyCommand, accelerator='Ctrl+C')
editMenu.add_command(label='Paste', command= commands.pasteCommand, accelerator='Ctrl+V')
editMenu.add_command(label='Cut', command= commands.cutCommand, accelerator='Ctrl+X')

#adding font menu options and attaching corresponding commands to them
fontMenu.add_command(label='Arial', command=commands.arialFontCommand)
fontMenu.add_command(label='Times New Roman', command=commands.timesNewRomanFontCommand)
fontMenu.add_command(label='Calibri', command=commands.calibriFontCommand)
fontMenu.add_command(label='Verdana', command=commands.verdanaFontCommand)

#adding font size menu options and attaching corresponding commands to them
fontSizeMenu.add_command(label='12', command=commands.twelveFontSizeCommand)
fontSizeMenu.add_command(label='14', command=commands.fourteenFontSizeCommand)
fontSizeMenu.add_command(label='16', command=commands.sixteenFontSizeCommand)
fontSizeMenu.add_command(label='18', command=commands.eighteenFontSizeCommand)
fontSizeMenu.add_command(label='20', command=commands.twentyFontSizeCommand)
fontSizeMenu.add_command(label='22', command=commands.twentyTwoFontSizeCommand)
fontSizeMenu.add_command(label='24', command=commands.twentyFourFontSizeCommand)

#adding appearance menu options and attaching corresponding commands to them
appearanceMenu.add_command(label='Light mode', command=commands.lightModeCommand)
appearanceMenu.add_command(label='Dark mode', command=commands.darkModeCommand)
appearanceMenu.add_command(label='Contrast mode', command=commands.contrastModeCommand)



#adding sub menus as cascading menus to the main menu bar
menuWidget.add_cascade(label='File', menu=fileMenu)
menuWidget.add_cascade(label='Edit', menu=editMenu)
menuWidget.add_cascade(label='Font', menu=fontMenu)
menuWidget.add_cascade(label='Font size', menu=fontSizeMenu)
menuWidget.add_cascade(label='Appearance', menu=appearanceMenu)


#updating status bar when started
updateStatusBar()
#configuring menu widget 
window.config(menu=menuWidget)
#starting event loop
window.mainloop()


