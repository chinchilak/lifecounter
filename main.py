from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

LIFETOTAL = 40
BASECOUNTER = 0

W = 120
H = 120
S = 2
PAD = 20
FBTNTXT = 64

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.life_total = LIFETOTAL
        self.opponent = BASECOUNTER
        self.poison = BASECOUNTER
        
    def increase_number(self, button):
        for button_set in self.button_sets:
            if button in button_set["buttons"]:
                button_set["value"] += 1
                self.update_buttons(button_set)
                break

    def decrease_number(self, button):
        for button_set in self.button_sets:
            if button in button_set["buttons"]:
                button_set["value"] -= 1
                self.update_buttons(button_set)
                break

    def update_buttons(self, button_set):
        value = button_set["value"]
        if value < 0:
            value = 0
        digits = [int(digit) for digit in str(value)]
        if len(digits) < 2:
            digits.insert(0, 0)
        for button, digit in zip(button_set["buttons"], digits):
            button.text = str(digit)

    def reset_values(self):
        for button_set in self.button_sets:
            check = button_set["id"]
            if check != "life total":
                button_set["value"] = BASECOUNTER
                self.update_buttons(button_set)
            else:
                button_set["value"] = LIFETOTAL
                self.update_buttons(button_set)

    def build(self):
        layout = GridLayout(cols=2)
        Window.size = (1600, 800)

        self.button_sets = []
        # Window.fullscreen = "auto"
        layout.size = Window.size

        for i, _ in enumerate(range(4)):
            relative_layout = RelativeLayout()
 
            button_set = {}
            button_set2 = {}
            button_set3 = {}
            button_set4 = {}
            button_set5 = {}

            # life total
            left_button = Button(text=str(self.life_total)[0], size_hint=(None, None), size=(W, H), font_size=FBTNTXT, font_name="Roboto-Bold", on_release=self.decrease_number)
            left_button.pos=(Window.width // 4 - W // 2 - W //2, Window.height // 4 - H // 2)
            right_button = Button(text=str(self.life_total)[1], size_hint=(None, None), size=(W, H), font_size=FBTNTXT, font_name="Roboto-Bold", on_release=self.increase_number)
            right_button.pos=(Window.width // 4 - W // 2 + W - W //2, Window.height // 4 - H // 2)

            button_set["buttons"] = [left_button, right_button]
            button_set["value"] = self.life_total
            button_set["id"] = "life total"
            self.button_sets.append(button_set)

            relative_layout.add_widget(left_button)
            relative_layout.add_widget(right_button)

            # opponents corner
            pos1c = [(Window.width//2 - W//2 - W//2 - PAD, 0 + PAD), 
                     (0 + PAD, 0 + PAD), 
                     (Window.width//2 - W//2 - W//2 - PAD, Window.height//2 - H//2 - PAD), 
                     (0 + PAD, Window.height//2 - H//2 - PAD)]
            pos2c = [(Window.width//2 - W//2 - PAD, 0 + PAD), 
                     (W//2 + PAD, 0 + PAD), 
                     (Window.width//2 - W//2 - PAD, Window.height//2 - H//2 - PAD), 
                     (W//2 + PAD, Window.height//2 - H//2 - PAD)]
            op11 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.decrease_number)
            op11.pos=pos1c[i]
            op12 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.increase_number)
            op12.pos=pos2c[i]

            button_set2["buttons"] = [op11, op12]
            button_set2["value"] = self.opponent
            button_set2["id"] = ""
            self.button_sets.append(button_set2)

            relative_layout.add_widget(op11)
            relative_layout.add_widget(op12)
        
            # opponents left
            pos1l = [(Window.width//2 - W//2 - W//2 - 2*PAD - 2*(W//2), 0 + PAD), 
                     (0 + 2*PAD + 2*(W//2), 0 + PAD), 
                     (Window.width//2 - W//2 - W//2 - 2*PAD - 2*(W//2), Window.height//2 - H//2 - PAD), 
                     (0 + 2*PAD + 2*(W//2), Window.height//2 - H//2 - PAD)]
            pos2l = [(Window.width//2 - W//2 - 2*PAD - 2*(W//2), 0 + PAD), 
                     (W//2 + 2*PAD + 2*(W//2), 0 + PAD), 
                     (Window.width//2 - W//2 - 2*PAD - 2*(W//2), Window.height//2 - H//2 - PAD), 
                     (W//2 + 2*PAD + 2*(W//2), Window.height//2 - H//2 - PAD)]
            op21 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.decrease_number)
            op21.pos=pos1l[i]
            op22 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.increase_number)
            op22.pos=pos2l[i]

            button_set3["buttons"] = [op21, op22]
            button_set3["value"] = self.opponent
            button_set3["id"] = ""
            self.button_sets.append(button_set3)

            relative_layout.add_widget(op21)
            relative_layout.add_widget(op22)

            # opponents top
            pos1t = [(Window.width//2 - W//2 - W//2 - PAD, 0 + 2*PAD + H//2), 
                     (0 + PAD, 0 + 2*PAD + H//2), 
                     (Window.width//2 - W//2 - W//2 - PAD, Window.height//2 - H//2 - 2*PAD - H//2), 
                     (0 + PAD, Window.height//2 - H//2 - 2*PAD - H//2)]
            pos2t = [(Window.width//2 - W//2 - PAD, 0 + 2*PAD + H//2), 
                     (W//2 + PAD, 0 + 2*PAD + H//2), 
                     (Window.width//2 - W//2 - PAD, Window.height//2 - H//2 - 2*PAD - H//2), 
                     (W//2 + PAD, Window.height//2 - H//2 - 2*PAD - H//2)]
            op31 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.decrease_number)
            op31.pos=pos1t[i]
            op32 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.increase_number)
            op32.pos=pos2t[i]

            button_set4["buttons"] = [op31, op32]
            button_set4["value"] = self.opponent
            button_set4["id"] = ""
            self.button_sets.append(button_set4)

            relative_layout.add_widget(op31)
            relative_layout.add_widget(op32)

            # poison
            pos1p = [(0 + PAD, Window.height//2 - H//2 - PAD), 
                     (Window.width//2 - W//2 - W//2 - PAD, Window.height//2 - H//2 - PAD), 
                     (0 + PAD, 0 + PAD), 
                     (Window.width//2 - W//2 - W//2 - PAD, 0 + PAD)]
            pos2p = [(0 + PAD + W//2, Window.height//2 - H//2 - PAD), 
                     (Window.width//2 - W//2 - PAD, Window.height//2 - H//2 - PAD), 
                     (0 + PAD + W//2, 0 + PAD), 
                     (Window.width//2 - W//2 - PAD, 0 + PAD)]
            op41 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.decrease_number)
            op41.pos=pos1p[i]
            op42 = Button(text=str(self.opponent), size_hint=(None, None), size=(W//2, H//2), font_size=FBTNTXT//2, on_release=self.increase_number)
            op42.pos=pos2p[i]

            button_set5["buttons"] = [op41, op42]
            button_set5["value"] = self.poison
            button_set5["id"] = ""
            self.button_sets.append(button_set5)

            relative_layout.add_widget(op41)
            relative_layout.add_widget(op42)

            reset = Button(text="", size_hint=(None, None), size=(20, 20), font_size=FBTNTXT//4, on_release=lambda reset: self.reset_values())
            reset.pos=(Window.width//2 - 10, Window.height//2 - 10)
            relative_layout.add_widget(reset)

            layout.add_widget(relative_layout)

        return layout

MyApp().run()
