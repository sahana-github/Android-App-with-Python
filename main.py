import kivy
from kivy.app import App #importing App class from kivy library
from kivy.uix.label import Label#used to display text on screen where label is widget
from kivy.uix.gridlayout import GridLayout#used for layout (used to arrange widgets)
from kivy.uix.textinput import TextInput#textinput for user to feed input
from kivy.uix.button import Button#buttons for submitting and interaction


class SpartanGrid(GridLayout):
    # build  constructor init where **kwargs means it can take any no. of arguments
    def __init__(self,**kwargs):
        #invoke constructor of grid
        super(SpartanGrid, self).__init__()

        self.cols=1

        #add widgets i.e. labels
        self.add_widget(Label(text="Student Name"))
        self.s_name=TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        #button name is press
        self.press=Button(text="Click me")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):

        #[.text because you want to print them on console in text]
        print("Name of student is "+self.s_name.text)

        print("Marks of student is " + self.s_marks.text)

        print("Gender of student is " + self.s_gender.text)
        print("You have entered your details Successfully....")


'''
SpartanApp class is inheriting from Class App,where App is parent class and SpartanApp is child class
'''
class SpartanApp(App):

    def build(self):
        #return layout
        return SpartanGrid()

if __name__ == "__main__":
    SpartanApp().run()

