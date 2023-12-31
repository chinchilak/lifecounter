from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from random import randint, choice

# Screens
class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass
    # def toggle_buttons(self):
    #     overlay_layout = self.ids.overlay_layout
    #     if overlay_layout.opacity == 0:
    #         overlay_layout.opacity = 1
    #         overlay_layout.size_hint_y = 1
    #     else:
    #         overlay_layout.opacity = 0
    #         overlay_layout.size_hint_y = None
    #         overlay_layout.height = 0

class MainScreen(Screen):
    coin_flip_label_text = "coin flip"
    settings_label_text = "menu"
    die_roll_label_text = "die roll"
    start_roll_label_text = "start roll"
    reset_values_label_text = "reset"
    font_color = [1, 1, 1, 1]
    font_color_poison = [0, 0.5, 0, 1]
    color_top_left = [0.5, 0, 0, 1]
    color_top_right = [0, 0.5, 0, 1]
    color_bottom_left = [0, 0, 0.5, 1]
    color_bottom_right = [0.5, 0.5, 0, 1]

    values = {
        "top_left_label": 40,
        "top_right_label": 40,
        "bottom_left_label": 40,
        "bottom_right_label": 40,

        "top_left_cmd_dmg_across": 0,
        "top_left_cmd_dmg_right": 0,
        "top_left_cmd_dmg_down": 0,

        "top_right_cmd_dmg_across": 0,
        "top_right_cmd_dmg_left": 0,
        "top_right_cmd_dmg_down": 0,

        "bottom_left_cmd_dmg_across": 0,
        "bottom_left_cmd_dmg_right": 0,
        "bottom_left_cmd_dmg_up": 0,

        "bottom_right_cmd_dmg_across": 0,
        "bottom_right_cmd_dmg_left": 0,
        "bottom_right_cmd_dmg_up": 0,

        "top_left_poison": 0,
        "top_right_poison": 0,
        "bottom_left_poison": 0,
        "bottom_right_poison": 0}

    def die_roll(self):
        label = self.ids['die_roll_label']
        roll = str(randint(1, 6))
        label.text = roll
        label.bold = True
        label.font_size = 48
        Clock.schedule_once(lambda dt: self.reset_die_roll(label), 5)

    def reset_die_roll(self, label):
        label.text = self.die_roll_label_text
        label.bold = False
        label.font_size = 36

    def coin_flip(self):
        label = self.ids['coin_flip_label']
        result = choice(["Heads", "Tails"])
        label.text = result
        label.bold = True
        label.font_size = 48
        Clock.schedule_once(lambda dt: self.reset_coin_flip(label), 5)

    def reset_coin_flip(self, label):
        label.text = self.coin_flip_label_text
        label.bold = False
        label.font_size = 36

    def roll_dice(self):
        results = []
        totals = []
        for _ in range(4):
            dice_rolls = []
            total = 0
            for _ in range(3):
                roll = randint(1, 6)
                dice_rolls.append(roll)
                total += roll

            results.append(dice_rolls)
            totals.append(total)

        max_total = max(totals)
        max_indices = [i for i, val in enumerate(totals) if val == max_total]

        if len(max_indices) > 1:
            self.roll_dice()
            return

        for i in range(4):
            label = self.ids[f"result_label_{i}"]
            dice_rolls = results[i]
            total = totals[i]
            if i in max_indices:
                label.color = (0, 1, 0, 1)
            else:
                label.color = (1, 1, 1, 1)
            label.text = f"{dice_rolls} = {total}"
        Clock.schedule_once(self.reset_roll_dice, 5)

    def reset_roll_dice(self, dt):
        for i in range(4):
            label = self.ids[f"result_label_{i}"]
            label.color = (1, 1, 1, 1)
            label.text = ""

    def increment_value(self, label_id):
        if label_id in self.values:
            self.values[label_id] += 1
            self.update_label_text(label_id)

    def decrement_value(self, label_id):
        if label_id in self.values:
            self.values[label_id] -= 1
            self.update_label_text(label_id)

    def update_label_text(self, label_id):
        label = self.ids[label_id]
        if label is not None:
            formatted_value = "{:02d}".format(self.values[label_id])
            label.text = str(formatted_value)

    def on_touch_up(self, touch):
        for label_id in self.values:
            label = self.ids[label_id]
            if label.collide_point(*touch.pos):
                touch_y = touch.pos[1]
                label_y = label.to_window(*label.pos)[1] + label.height
                label_height = label.size[1]
                check = label_y - (label_height / 2)
                if label.rotated:
                    if touch_y > check:
                        self.decrement_value(label_id)
                    else:
                        self.increment_value(label_id)
                    break
                else:
                    if touch_y > check:
                        self.increment_value(label_id)
                    else:
                        self.decrement_value(label_id)
                    break

    def reset_values(self):
        for label in self.values.keys():
            label_widget = self.ids[label]
            if "label" in label:
                label_widget.text = str("{:02d}".format(40))
            else:
                label_widget.text = str("{:02d}".format(0))


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(SettingsScreen(name="settings"))
sm.add_widget(MainScreen(name="main"))

# Load the .kv file
kv = Builder.load_file("app.kv")

# Create the application
class MyApp(App):
    def build(self):
        return kv
    
    def exit_app(self):
        App.get_running_app().stop()

    def toggle_rotation(self):
        if Window.rotation == 0:
            Window.rotation = 90
        elif Window.rotation == 90:
            Window.rotation = 180
        elif Window.rotation == 180:
            Window.rotation = 270
        else:
            Window.rotation = 0

if __name__ == "__main__":
    MyApp().run()
