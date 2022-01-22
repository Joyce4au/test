from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
import random


class Content(BoxLayout):
    pass


class NumberGuess(MDApp):
    dialog = None
    msg = ""
    random_n = 0

    def luck_guess(self, arg):
        pass

    def creat_random_int(self, obj):
        w = 0
        x = 0
        y = 0
        z = 0

        list_number = list(range(1, 10))
        w = random.choice(list_number)
        list_number.remove(w)
        list_number.append(0)
        x = random.choice(list_number)
        list_number.remove(x)
        y = random.choice(list_number)
        list_number.remove(y)
        z = random.choice(list_number)
        self.random_n = int(str(w) + str(x) + str(y))
        self.random.text = str(self.random_n)

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Lucky guess game JJ")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [["rotate-3d-variant", lambda x: self.luck_guess()]]
        screen.add_widget(self.toolbar)

        self.lable = MDLabel(
            text="Enter a 3 digits number to guess",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            font_size=18
        )
        screen.add_widget(self.lable)

        self.random = MDLabel(
            text=str(self.random_n),
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            font_size=18
        )

        screen.add_widget(self.random)

        self.result = MDLabel(
            text="",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            font_size=18
        )
        screen.add_widget(self.result)

        self.input = MDTextField(
            text="",
            halign="center",
            size_hint=(0.6, 0.5),
            multiline=False,
            max_text_length=3,
            hint_text="000",
            helper_text_mode="on_error",
            helper_text="please input a 3-digits number",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            font_size=30
        )
        screen.add_widget(self.input)

        self.guess = MDFillRoundFlatButton(
            text="Guess",
            size_hint=(0.7, 0.20),
            pos_hint={"center_x": 0.5, "center_y": 0.20},
            font_size=22
            # on_release=self.dialog
        )
        self.guess.bind(on_press=self.match)
        screen.add_widget(self.guess)

        return screen

    def msg_box(self,obj):
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title="Info",
                               text=self.msg,
                               size_hint=(0.8, 1),
                               buttons=[close_button]
                               )

        self.dialog.open()

    def close_dialog(self, obj):
        self.input.text = ""
        self.dialog.dismiss()

    def match(self, arg):
        guess_n = []
        input_n = []
        a = 0
        b = 0
        a_list = [0, 0, 0, 0]
        b_list = [0, 0, 0, 0]
        if self.random_n == 0:
            self.creat_random_int

        ss = str(self.input.text.rstrip())
        if len(ss) == 3:
            input_n = [int(a) for a in ss]
        else:
            self.msg = "please input a 3-digits number!"
            self.msg_box
            return

        guess_n = [int(b) for b in str(self.random_n)]

        self.msg = f"guess_n: {guess_n}, input_n: {input_n} "
        self.msg_box

        for x in input_n:
            index = input_n.index(x)
            if x == guess_n[index]:
                a_list[index] = 1
            else:
                a_list[index] = 0
                if x in guess_n:
                    b_list[index] = 1
                else:
                    b_list[index] = 0

        a = a_list.count(1)
        b = b_list.count(1)

        if a == 3:
            ss = f"Bingo!The number is {self.random_n}!"
            self.result = ss
        else:
            ss = f"Try again! The result is {a}A{b}B."
            self.result = ss


if __name__ == '__main__':
    NumberGuess().run()
