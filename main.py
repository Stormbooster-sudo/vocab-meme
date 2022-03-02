from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        with self.canvas:
            self.player = Rectangle(source="image/player.png",pos=(700,500),size=(120,100))

        self.keysPressed = set()

        Clock.schedule_interval(self.move_step,0)

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

        step_size = 1000 * dt

        if "w" in self.keysPressed:
            currenty += step_size
        if "s" in self.keysPressed:
            currenty -= step_size
        if "a" in self.keysPressed:
            currentx -= step_size
            currentpic = "image/player.png"
        if "d" in self.keysPressed:
            currentx += step_size
            currentpic = "image/player-right.png"

        self.player.pos = (currentx,currenty)
        self.player.source = currentpic



class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == "__main__":
    app = MyApp()
    app.run()