from kivy.app import App
from kivy. uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# I think I had Kivy extension added in my VS code but still getting the error
# "No module name Kivy" so not sure whats wrong.

class root(App):
    def build(self):
        la=BoxLayout(orientation='vertical')
        lb=Label(text="Hello Sneha")
        la.add_widget(lb)
        return la

        if __name__=="__main__":
            root().run()