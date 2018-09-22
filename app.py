from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Usuário'))
        self.usuario = TextInput(multiline=False)
        self.add_widget(self.usuario)
        self.add_widget(Label(text='Senha'))
        self.senha = TextInput(password=True, multiline=False)
        self.add_widget(self.senha)
        
class MyApp(App):
    def build(self):
        return LoginScreen()

# from kivy.app import App
# from kivy.uix.label import Label

# class XUQNIMIRRAIN(App):
#     def build(self):
#         return Label(text='CU')


if __name__ == '__main__':
    MyApp().run()

