import pyrebase
from firebase import firebase
import json
from kivy.app import App

config = {
    "apiKey": "AIzaSyDerqMdKQ_7k2s-m87QMwLdgqkwOPLVyww",
    "authDomain": "kivy-auth-test.firebaseapp.com",
    "databaseURL": "https://kivy-auth-test.firebaseio.com",
    "projectId": "kivy-auth-test",
    "storageBucket": "kivy-auth-test.appspot.com",
    "messagingSenderId": "493226155473",
    "appId": "1:493226155473:web:a3dc83f728c1801b5514f0",
    "measurementId": "G-DTXZNBCL0X"
}

firebase_auth = pyrebase.initialize_app(config)
firebase_data = firebase.FirebaseApplication("https://kivy-auth-test.firebaseio.com/" , None)

class MyFirebase() :
    def sign_up(self , fullname , email , password):

        try :
            # RealTime Database
            data = {
                "Name": fullname,
                "Email": email,
                "Password": password
            }
            result = firebase_data.post("/kivy-auth-test/Student", data)

            # Creating User
            signup_auth = firebase_auth.auth()
            user_signup = signup_auth.create_user_with_email_and_password(email, password)
            print("SignUp Successfully")
            App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#FF0000]Signup Succesfully.[/color][/b]"
        except:
            App.get_running_app().root.ids["signup_screen"].ids["signup_screen"].text = "[b][color=#0000FF]Please enter correct details.[/color][/b]"




    def sign_in(self , email , password):
        signin_auth = firebase_auth.auth()

        try :
            user_login = signin_auth.sign_in_with_email_and_password(email,password)
            print("Login Successfully !!!")
            print(user_login["registered"])
            path_to_home = user_login["registered"]

            if path_to_home == True :
                print("hello")
                App.get_running_app().root.ids["login_screen"].ids["login_message"].text = ""
                App.get_running_app().change_screen("home_screen")
                App.get_running_app().root.ids["home_screen"].ids["passing_email"].text = "[b]%s[/b]" %email

        except :
            App.get_running_app().root.ids["login_screen"].ids["login_message"].text = "[b]Invalid Email or Password[/b]"

    def forgot_password(self , email) :
        try:
            auth = firebase_auth.auth()
            auth.send_password_reset_email(email)
            App.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b]Thanks! Please check your email .[/b]"
        except:
            App.get_running_app().root.ids["forgot_password_screen"].ids["forgot_message"].text = "[b][color=#FF0000]Please Enter Correct Email !.[/color][/b]"



