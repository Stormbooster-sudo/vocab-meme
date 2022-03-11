from kivy.app import App
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.label import CoreLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.button import Button

import random
import pandas as pd

from game_objects import Player,Items

Config.set('graphics', 'maxfps', '60')


class GameMain(Screen):
    # set ค่าเริ่มต้น
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._score_label = CoreLabel(text="Score: 0", font_size=20)
        self._score_label.refresh()
        self._score = 0

        # เก็บ key 
        self.item_type = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Bomb', 'Eraser']
        self._get_items = ""
        
        # รีเฟรชหน้าเกม
        self.register_event_type("on_frame")

        # ปุ่มกด 
        self.keysPressed = set()
        self._entities = set()

        Clock.schedule_interval(self._on_frame, 1/40)

        # Sound
        self.sound = SoundLoader.load('audio/sound.mp3')
        self.sound.loop = True
        self.sound.play()

    def test(self,level):
        print(level)

    # ค่าเริ่มต้นของโปรแกรม 
    def initial(self):
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self._df = pd.read_csv('words.csv')
        self.w = self._df['Word'].astype('str')
        m = (self.w.str.len() >= 8) & (self.w.str.len() < 10)
        print(self._df[m])
        print(len(self._df[m]))
        rand_word = random.randint(1, len(self._df['Word']))
        self.word_rand = self._df.iloc[rand_word]['Word']
        self.def_word = self._df.iloc[rand_word]['Definition']
        print(self.word_rand)

        self._word_label = CoreLabel(
            text="_ "*len(self.word_rand), font_size=60)
        self._word_label.refresh()
        self._def_label = CoreLabel(text=self.def_word.upper(), font_size=20)
        self._def_label.refresh()

        with self.canvas:
            print("Create canvas")
            Rectangle(source="image/background.png", pos=(0, 0),
                      size=(Window.width, Window.height))
            self._score_instruction = Rectangle(texture=self._score_label.texture, pos=(
                0, Window.height - 50), size=self._score_label.texture.size)
            self._word_instruction = Rectangle(texture=self._word_label.texture, pos=(
                (Window.width/2) - (self._word_label.texture.size[0]/2), Window.height - 70), size=self._word_label.texture.size)
            self._definition_instruction = Rectangle(texture=self._def_label.texture, pos=(
                (Window.width/2) - (self._def_label.texture.size[0]/2), Window.height - 90), size=self._def_label.texture.size)

        self._isPause = True

        Clock.schedule_interval(self.spawn_items, 3)
        Clock.schedule_interval(self.spawn_answer, 4)

        self.player = Player(self)
        self.player.pos = (Window.width - Window.width/3, 0)
        self.add_entity(self.player)

        self.pause_button = Button(size_hint = (None, None), size=(50,50), pos=(Window.width - 50, Window.height - 50),text="| |")
        self.pause_button.bind(on_press = self.pause)
        self.add_widget(self.pause_button)

    # summon all item from random. 
    def spawn_items(self, dt):
        print(Window.width)
        random_item_type = random.choice(self.item_type) # สุ่มค่าจาก self.item_type
        random_x = random.randint(0, Window.width) 
        y = Window.height - 80 # เก็บค่าความสูงความยาวหน้าต่างโปรแกรม 
        random_speed = random.randint(30, 100) # Item's speed drop.
        self.add_entity(Items((random_x, y), random_speed, random_item_type,self)) 
    
    # เฉลยคำตอบ
    def spawn_answer(self, dt):
        # print(Window.width)
        get_str = list(self.get_items)
        flag = 0
        for i in range(len(get_str)):
            if self.word_rand[i].upper() == get_str[i]:
                flag += 1
            else:
                flag = 0
        help_char = self.word_rand[flag].upper()
        # random_item_type = random.choice(help_list)
        random_x = random.randint(0, Window.width)
        y = Window.height - 80
        random_speed = random.randint(30, 100)
        self.add_entity(Items((random_x, y), random_speed, help_char,self))
    
    #
    def collides(self, e1, e2):
        r1x = e1.pos[0]
        r1y = e1.pos[1]
        r2x = e2.pos[0]
        r2y = e2.pos[1]
        r1w = e1.size[0]
        r1h = e1.size[1]
        r2w = e2.size[0]
        r2h = e2.size[1]

        if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
            return True
        else:
            return False

    def colliding_entities(self, entity):
        result = set()
        for e in self._entities:
            if self.collides(e, entity) and e != entity:
                result.add(e)
        return result
    
    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)
    
    def remove_entity(self, entity):
        if entity in self._entities:
            self._entities.remove(entity)
            self.canvas.remove(entity._instruction)

    
    # Word Display
    @property
    def get_items(self):
        return self._get_items

    def add_items(self, value):
        self._get_items += value
    
    def clear_items(self):
        self._get_items = ""
    
    def refresh_word(self,is_alpha):
        if len(self.get_items) < len(self.word_rand):
            self._word_label.text = self._get_items + " _ "*(len(self.word_rand) - len(self.get_items))
            self._word_label.refresh()
            self._word_instruction.texture = self._word_label.texture
            self._word_instruction.size = self._word_label.texture.size
            print(self._word_label.texture.size)
            print(self._word_instruction.pos[0])
            # print(is_alpha)
            if not is_alpha:
                self._word_instruction.pos = (Window.width - 450, Window.height - 70)
            self._word_instruction.pos = ((Window.width/2) - (self._word_label.texture.size[0]/2), Window.height - 70)

        elif self.get_items == self.word_rand.upper():
            self._score += len(self.word_rand)
            self._score_label.text = F"Score : {self._score}"
            self._score_label.refresh()
            self._score_instruction.texture = self._score_label.texture
            self._score_instruction.size = self._score_label.texture.size

            rand_word = random.randint(1,len(self._df['Word']))
            self.word_rand = self._df.iloc[rand_word]['Word']
            self.def_word = self._df.iloc[rand_word]['Definition'] 
            self._word_label.text = "_ "*len(self.word_rand)
            self._word_label.refresh()
            self._word_instruction.texture = self._word_label.texture
            self._word_instruction.size = self._word_label.texture.size
            self._word_instruction.pos = ((Window.width/2) - (self._word_label.texture.size[0]/2), Window.height - 70)

            self._def_label.text = self.def_word
            self._def_label.refresh()
            self._definition_instruction.texture = self._def_label.texture
            self._definition_instruction.size = self._def_label.texture.size
            self._definition_instruction.pos = ((Window.width/2) - (self._def_label.texture.size[0]/2), Window.height - 90)
            self.clear_items()
            print(self.word_rand)
        else:
            self._word_label.text = "_ "*len(self.word_rand)
            self._word_label.refresh()
            self._word_instruction.texture = self._word_label.texture

            self._score -= int(len(self.word_rand)/2)
            self._score_label.text = F"Score : {self._score}"
            self._score_label.refresh()
            self._score_instruction.texture = self._score_label.texture
            self._score_instruction.size = self._score_label.texture.size
            self.clear_items()
        # self._word_instruction.pos = (self._word_instruction.pos, Window.height - 70)
        
    # Bomb's result    
    def half_score(self):
        self._score = int( self._score/2)
        self._score_label.text = F"Score : {self._score}"
        self._score_label.refresh()
        self._score_instruction.texture = self._score_label.texture
        self._score_instruction.size = self._score_label.texture.size

    # เริ่มเกม
    def start_game_render(self):
        Clock.schedule_interval(self._on_frame, 1/40)
        Clock.schedule_interval(self.spawn_items, 3)
        Clock.schedule_interval(self.spawn_answer, 4)
    
    # After hold pause button
    def freeze_game(self):
        Clock.unschedule(self._on_frame)
        Clock.unschedule(self.spawn_items)
        Clock.unschedule(self.spawn_answer)
    
    # pause button 
    def pause(self, value):
        if self._isPause:
            self._isPause = not self._isPause
            self.freeze_game()
            self.resume_btn= Button(size_hint = (None, None),size=(200,70),pos=(Window.width/2, Window.height/2),text="resume")
            self.resume_btn.bind(on_press=self.pause)
            self.add_widget(self.resume_btn)
            
        else:
            self.start_game_render()
            self.remove_widget(self.resume_btn)
            self._isPause = not self._isPause
                                                                                                   
                                                                                                   

class GameLevelMenuScreen(Screen):
    def pressBtn(self, level):
        # print(level)
        GameMain().test(level)
    pass

class MenuScreen(Screen):
    pass

class SM(ScreenManager):
    pass

kv = Builder.load_file('style.kv')
class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()
