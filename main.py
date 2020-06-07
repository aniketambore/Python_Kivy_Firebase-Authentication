from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from firebaseaut import MyFirebase

class HomeScreen(Screen) :
    pass

class SettingsScreen(Screen) :
    pass

class LoginScreen(Screen) :
    pass

class SignUpScreen(Screen) :
    pass

class ForgotPasswordScreen(Screen) :
    pass

class LabelButton(ButtonBehavior , Label) :
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App) :
    def build(self):
        self.my_firebase = MyFirebase()
        return GUI


    def change_screen(self , filename) :
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = filename
        pass

MainApp().run()