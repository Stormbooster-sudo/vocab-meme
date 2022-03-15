from kivy.uix.image import Image
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
from kivy.properties import StringProperty

import random
import pandas as pd

from game_objects import Player,Items

Config.set('graphics', 'maxfps', '60')


class GameMain(Screen):
    # set ค่าเริ่มต้น
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._score_label = CoreLabel(text="Score: 0", font_size=20, font_name="impact")
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

    def test(self,level):
        self.level = level
        print(level)

    # ค่าเริ่มต้นของโปรแกรม 
    def initial(self):
        self.clear_items()
        self.health = 5

        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        #Get level
        self.game_level = self.manager.get_screen('game_level')
        self.level = self.game_level.g_level
        print(self.game_level.g_level)

        #Random word by level
        self._df = pd.read_csv('words.csv')
        self._w = self._df['Word'].astype('str')
        if self.level == "hard":
            self.m = (self._w.str.len() >= 8) & (self._w.str.len() <= 12) 
            self.word = self._df[self.m].sample()
        else:
            self.m = (self._w.str.len() >= 4)
            self.word = self._df[self.m].sample()
        self.word_rand = (self.word['Word'].to_string(index=False)).strip()
        self.def_word = (self.word['Definition'].to_string(index=False)).lstrip()
        print(self.word_rand)

        if self.level == "easy":
            self._word_label = CoreLabel(
                text= self.word_rand[0].upper() + "_ "*(len(self.word_rand) - 1), font_size=60, font_name="impact")
            self.add_items(self.word_rand[0].upper())
        else:
            self._word_label = CoreLabel(
            text="_ "*len(self.word_rand), font_size=60, font_name="impact")
        self._word_label.refresh()
        self._def_label = CoreLabel(text=self.def_word.upper(), font_size=20, font_name="impact")
        self._def_label.refresh()

        with self.canvas:

            Rectangle(source="image/background.png", pos=(0, 0),
                      size=(Window.width, Window.height))
            self._hp_display = Rectangle(source="image/hp/hp5.png", pos=(0, Window.height - 40),
                      size=(100,50))
            self._score_instruction = Rectangle(texture=self._score_label.texture, pos=(
                15, Window.height - 60), size=self._score_label.texture.size)
            self._word_instruction = Rectangle(texture=self._word_label.texture, pos=(
                (Window.width/2) - (self._word_label.texture.size[0]/2), Window.height - 70), size=self._word_label.texture.size)
            self._definition_instruction = Rectangle(texture=self._def_label.texture, pos=(
                (Window.width/2) - (self._def_label.texture.size[0]/2), Window.height - 90), size=self._def_label.texture.size)

        #Set game status
        self._isPause = True
        #Set entities set to empty set
        self._entities = set()
        #Start render game
        self.start_game_render()

        self.player = Player(self)
        self.player.pos = (Window.width - Window.width/3, 0)
        self.add_entity(self.player)

        self.pause_button = Button(size_hint = (None, None), size=(50,50), pos=(Window.width - 50, Window.height - 50),text="| |", font_name="impact")
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
        if self.level == 'easy':
            get_str = get_str[1:] 
        flag = 1
        for i in range(len(get_str)):
            if self.word_rand[i + 1].upper() == get_str[i]:
                flag += 1
            else:
                flag = 1
        help_char = self.word_rand[flag].upper()
        # random_item_type = random.choice(help_list)
        random_x = random.randint(0, Window.width)
        y = Window.height - 80
        random_speed = random.randint(30, 100)
        self.add_entity(Items((random_x, y), random_speed, help_char,self))
    
    # ตรวจจับการชนของ item with ตัวละคร
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
    # ตรวจจับ item ที่ถูกชน
    def colliding_entities(self, entity):
        result = set()
        for e in self._entities:
            if self.collides(e, entity) and e != entity:
                result.add(e)
        return result
    # การเรนเดอร์ภาพ
    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)
    # การเรนเดอร์ภาพ
    def on_frame(self, dt):
        pass
    # ออกจากเกม --> ตัดระบบ keyboard
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None
    # ตอนเอานิ้วกดปุ่ม
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)
    # ตอนเอานิ้วออก
    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    # funtion สำหรับใส่ player and items
    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)

    # funtion สำหรับ นำ player and items ออก 
    def remove_entity(self, entity):
        if entity in self._entities:
            self._entities.remove(entity)
            self.canvas.remove(entity._instruction)

    
    # Word Display
    @property
    def get_items(self):
        return self._get_items
    # เพิ่มตัวอักษรหลังเก็บ
    def add_items(self, value):
        self._get_items += value
    # Eraser
    def clear_items(self):
        self._get_items = ""

    # refresh word and display word that have been gotten
    def refresh_word(self,is_alpha):
        if len(self.get_items) < len(self.word_rand):
            self._word_label.text = self._get_items + " _ "*(len(self.word_rand) - len(self.get_items))
            print(self._word_label.texture.size)
            print(self._word_instruction.pos[0])
            # print(is_alpha)
            if not is_alpha and self.level == "easy":
                self._word_label.text = self.word_rand[0].upper() + "_ "*(len(self.word_rand) - 1)
                self.add_items(self.word_rand[0].upper())
            self._word_label.refresh()
            self._word_instruction.texture = self._word_label.texture
            self._word_instruction.size = self._word_label.texture.size
            self._word_instruction.pos = ((Window.width/2) - (self._word_label.texture.size[0]/2), Window.height - 70)

        elif self.get_items == self.word_rand.upper():
            self._score += len(self.word_rand)
            self._score_label.text = F"Score : {self._score}"
            self._score_label.refresh()
            self._score_instruction.texture = self._score_label.texture
            self._score_instruction.size = self._score_label.texture.size

            self.clear_items()
            self.word = self._df[self.m].sample()
            self.word_rand = (self.word['Word'].to_string(index=False)).strip()
            self.def_word = (self.word['Definition'].to_string(index=False)).lstrip() 
            if self.level == "easy":
                self._word_label.text = self.word_rand[0].upper() + "_ "*(len(self.word_rand) - 1)
                self.add_items(self.word_rand[0].upper())
            else:
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
            print(self.word_rand)
        else:
            self.clear_items()
            if self.level == "easy":
                self._word_label.text = self.word_rand[0].upper() + "_ "*(len(self.word_rand) - 1)
                self.add_items(self.word_rand[0].upper())
            else:
                self._word_label.text = "_ "*len(self.word_rand)
            self._word_label.refresh()
            self._word_instruction.texture = self._word_label.texture

            self.health -= 1
            self._hp_display.source = F"image/hp/hp{self.health}.png"
            if self.health == 0:
                self.play_again()
                
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
            self.resume_btn= Button(size_hint = (None, None),size=(200,70),pos=(Window.width/2 - 200, Window.height/2 - 230),text="Resume", font_name="impact", font_size = 30, outline_color=(0, 0, 0), outline_width=2)
            self.resume_btn.bind(on_press=self.pause)
            self.add_widget(self.resume_btn)

            self.to_level_scn_btn = Button(size_hint = (None, None),size=(200,70),pos=(Window.width/2, Window.height/2 - 230),text="Back To Level", font_name="impact", font_size = 30, outline_color=(0, 0, 0), outline_width=2)
            self.to_level_scn_btn.bind(on_press=self.change_to_level_screen)
            self.add_widget(self.to_level_scn_btn)

            self.meme_image = Image(source="image/meme/pause_menu.jpg",size_hint = (None, None),size=(700, Window.height), pos=(Window.width/2 - 350, Window.height/2 - Window.height/4 - 70) )
            self.add_widget(self.meme_image)

        else:
            self.start_game_render()
            self.remove_widget(self.to_level_scn_btn)
            self.remove_widget(self.resume_btn)
            self.remove_widget(self.meme_image)
            self._isPause = not self._isPause

     # กลับไปหน้าเลือกระดับความยาก                                                                                                
    def change_to_level_screen(self, value):
        self.manager.current = "game_level" 
        self.manager.transition.direction = 'right'   
    
    def play_again(self):
        self.freeze_game()
        # self.play_again_btn= Button(size_hint = (None, None),size=(200,70),pos=(Window.width/2 - 200, Window.height/2 - 230),text="Play Again", font_name="impact", font_size = 30, outline_color=(0, 0, 0), outline_width=2)
        # self.play_again_btn.bind(on_press=self.change_to_game_screen)
        # self.add_widget(self.play_again_btn)
        
        self.to_level_scn_btn = Button(size_hint = (None, None),size=(200,70),pos=(Window.width/2 - 100, Window.height/2 - 230),text="Back To Level", font_name="impact", font_size = 30, outline_color=(0, 0, 0), outline_width=2)
        self.to_level_scn_btn.bind(on_press=self.change_to_level_screen)
        self.add_widget(self.to_level_scn_btn)

        self.meme_image = Image(source="image/meme/pause_menu.jpg",size_hint = (None, None),size=(700, Window.height), pos=(Window.width/2 - 350, Window.height/2 - Window.height/4 - 70) )
        self.add_widget(self.meme_image)

                                                                                   



class GameLevelMenuScreen(Screen):
    g_level = StringProperty('')
    def pressBtn(self, level):
        self.g_level = level



class MenuScreen(Screen):
    pass

class SM(ScreenManager):
    pass
kv = Builder.load_file('style.kv')
class MyApp(App):
    # Sound
    sound = SoundLoader.load('audio/sound.mp3')
    sound.loop = True
    sound.play()   

    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()
