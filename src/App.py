import PySimpleGUI as sg
from User import User
from Database import Database
from Validator import Validator

DB = Database()


class App:
    @staticmethod
    def init():
        message = sg.Text('', key='-TEXT-', size=(30, 2))

        layout = [[sg.Text('Username'), sg.InputText()],
                  [sg.Text('Password'), sg.InputText(password_char='*')],
                  [sg.ReadButton('Register'), sg.Cancel(), message]]

        window = sg.Window('Simple Registration App', layout)
        window.set_icon('icon.ico')
        while True:
            event, values = window.read()
            if event == 'Cancel' or event == None:
                break
            if values and values[0] and values[1]:  # values[0] holds username, values[1] password
                if Validator.is_valid(values[1]):
                    new_user = User(values[0], values[1])
                    try:
                        new_user.add(DB)
                        message('User created!', text_color='dark green')
                    except TypeError:
                        message('User already exists!', text_color='red')
                else:
                    message('Enter strong password (at least 8 characters long)', text_color='red')
            else:
                message('Enter username and password', text_color='red')

        window.close()


App.init()
