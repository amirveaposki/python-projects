from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calcolatrice(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.input = TextInput(multiline=False, readonly=True, halign='right', font_size=32)
        self.add_widget(self.input)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=24)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        text = instance.text
        if text == 'C':
            self.input.text = ''
        elif text == '=':
            try:
                self.input.text = str(eval(self.input.text))
            except:
                self.input.text = 'Errore'
        else:
            self.input.text += text

class CalcolatriceApp(App):
    def build(self):
        return Calcolatrice()

if __name__ == '__main__':
    CalcolatriceApp().run()
