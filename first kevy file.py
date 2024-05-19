import kivy
from kivy.app import App
from kivy.uix.label import Label

class myapp(App):
    def build(self):
        return Label(text='hello',font_size=72,color='red')
    
if __name__=='__main__':
    myapp().run()    