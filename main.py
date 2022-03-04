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

        self._score_label = CoreLabel(text="Score: 0", font_size=20)
        self._score_label.refresh()
        self._score = 0

        self.item_type = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','BOMB','CLEAR']
        self._get_items = ""

        self.register_event_type("on_frame")

        with self.canvas:
            Rectangle(source="image/background.png", pos=(0, 0),
                      size=(Window.width, Window.height))
            self._score_instruction = Rectangle(texture=self._score_label.texture, pos=(
                0, Window.height - 50), size=self._score_label.texture.size)

        self.keysPressed = set()
        self._entities = set()

        Clock.schedule_interval(self._on_frame, 1/40)

        # Sound
        self.sound = SoundLoader.load('audio/sound.mp3')
        self.sound.loop = True
        self.sound.play()

        Clock.schedule_interval(self.spawn_items, 2)

    def spawn_items(self, dt):
        # print(Window.width)
        random_item_type = random.choice(self.item_type)
        random_x = random.randint(0, Window.width)
        y = Window.height - 80
        random_speed = random.randint(50, 200)
        self.add_entity(Items((random_x, y), random_speed, random_item_type))
    
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
        
    @property
    def get_items(self):
        return self._get_items

    def add_items(self, value):
        self._get_items += value
    
    def clear_items(self):
        self._get_items = ""



class Entity(object):
    def __init__(self):
        self._pos = (0, 0)
        self._size = (0, 0)
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
        self.size = (150,160)
        # self.source = "image/player.png"
        game.bind(on_frame=self.move_step)
        self.pos = (400, 0)


    def stop_callbacks(self):
        game.unbind(on_frame=self.move_step)

    # Move
    def move_step(self, sender, dt):
        currentpic = self.source
        currentx = self.pos[0]
        currenty = self.pos[1]

        step_size = 500 * (dt)

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

        self.pos = (currentx, currenty)
        self.source = currentpic


class Items(Entity):
    def __init__(self, pos, speed, item_type):
        super().__init__()
        self._speed = speed
        self.item_type = item_type
        self.size = (50, 50)
        self.pos = pos
        self.source = "image/A_test.png"
        game.bind(on_frame=self.move_step)

    def stop_callbacks(self):
        game.unbind(on_frame=self.move_step)

    def move_step(self, sender, dt):
        for e in game.colliding_entities(self):
            if e == game.player:
                self.stop_callbacks()
                game.remove_entity(self)
                print(F"collide! {self.item_type}")
                if self.item_type == "BOMB":
                    print("BOMB")
                elif self.item_type == "CLEAR":
                    game.clear_items()
                else:
                    game.add_items(self.item_type)
                print(game.get_items)
                return
        step_size = self._speed * dt
        new_x = self.pos[0]
        new_y = self.pos[1] - step_size
        self.pos = (new_x, new_y)


game = GameMain()
game.player = Player()
game.player.pos = (Window.width - Window.width/3, 0)
game.add_entity(game.player)

# enemy = Items((500,500))
# game.add_entity(enemy)


class MyApp(App):
    def build(self):
        return game


if __name__ == "__main__":
    app = MyApp()
    app.run()
