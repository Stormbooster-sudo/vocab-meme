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

class Charactor(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        
        # Sound
        self.sound = SoundLoader.load('audio/sound.mp3')
        self.sound.play()

        #Charactor animate State
        self.playerState = 0 
        with self.canvas:
            self.player = Rectangle(source="image/playerfr1.png",pos=(700,500),size=(240,200))

        self.keysPressed = set()

        Clock.schedule_interval(self.move_step,1/30)

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

    def move_step(self,dt):
        currentpic = self.player.source
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        step_size = 500 * dt

        if "w" in self.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currenty += step_size
        if "s" in self.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currenty -= step_size
        if "a" in self.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currentx -= step_size
        if "d" in self.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currentx += step_size

        self.player.pos = (currentx,currenty)
        self.player.source = currentpic

class GameMain(Widget):
    player = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)





class MyApp(App):
    def build(self): #backGround
        Window.clearcolor = (1,1,1,1)
        # sound = SoundLoader.load('audio/sound.mp3')
        # if sound:
        #     print("Sound found at %s" % sound.source)
        #     print("Sound is %.3f seconds" % sound.length)
        #     sound.play()

        return Charactor()


if __name__ == "__main__":
    app = MyApp()
    app.run()