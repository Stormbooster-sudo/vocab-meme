from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import CoreLabel
import random

class GameMain(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self._score_label = CoreLabel(text="Score: 0",font_size=20)
        self._score_label.refresh()
        self._score = 0

        self.register_event_type("on_frame")

        with self.canvas:
            Rectangle(source="image/background.png", pos=(0, 0),
                      size=(Window.width, Window.height))
            self._score_instruction = Rectangle(texture=self._score_label.texture, pos=(
                0, Window.height - 50), size=self._score_label.texture.size)

        self.keysPressed = set()
        self._entities = set()

        Clock.schedule_interval(self.on_frame, 0)

        #Sound
        self.sound = SoundLoader.load('audio/sound.mp3')
        self.sound.loop = True
        self.sound.play()

        
    #Spawn_enemies 
    
    def on_frame(self, dt):
        pass
        
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None
    
    def _on_key_down(self,keyboard,keycode,text,modifiers):
        self.keysPressed.add(text)

    def _on_key_up(self,keyboard,keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)
    
    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)


class Entity(object):
    def __init__(self):
        self._pos = (0, 0)
        self._size = (250, 200)
        self._source = "image/playerfr1.png"
        self._instruction = Rectangle(
            pos=self._pos, size=self._size, source=self._source)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self._instruction.pos = self._pos

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._instruction.size = self._size

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self._instruction.source = self._source

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.playerState = 0 
        self.source = "image/player.png"
        game.bind(on_frame=self.move_step)
        self.pos = (400, 0)

        self.keysPressed = set()
        Clock.schedule_interval(self.move_step,1/30)

    
    # Move
    def move_step(self,dt):
        currentpic = self.source
        currentx = self.pos[0]
        currenty = self.pos[1]

        step_size = 500 * dt

        if "w" in game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currenty += step_size
        if "s" in game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currenty -= step_size
        if "a" in game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currentx -= step_size
        if "d" in game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currentx += step_size

        self.pos = (currentx,currenty)
        self.source = currentpic

    



game = GameMain()
game.player = Player()
game.player.pos = (Window.width - Window.width/3, 0)
game.add_entity(game.player)

# enemy = Items((500,500))
# game.add_entity(enemy)





class MyApp(App):
    def build(self): #backGround
        return game


if __name__ == "__main__":
    app = MyApp()
    app.run()