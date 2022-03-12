from kivy.graphics import Rectangle

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
    def __init__(self,game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.playerState = 0
        self.size = (150,160)
        # self.source = "image/player.png"
        self.game.bind(on_frame=self.move_step)


    def stop_callbacks(self):
        self.game.unbind(on_frame=self.move_step)

    # Move
    def move_step(self, sender, dt):
        currentpic = self.source
        currentx = self.pos[0]
        currenty = self.pos[1]

        step_size = 500 * (dt)

        if "w" in self.game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                print("w")
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currenty += step_size
        if "s" in self.game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                print("s")
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currenty -= step_size
        if "a" in self.game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                print("a")
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currentx -= step_size
        if "d" in self.game.keysPressed:
            if self.playerState < 7:
                currentpic = F"image/playerfr{self.playerState + 1}.png"
                print("d")
                self.playerState += 1
            else:
                self.playerState = 0
                currentpic = F"image/playerfr{self.playerState + 1}.png"
            currentx += step_size

        self.pos = (currentx, currenty)
        self.source = currentpic


class Items(Entity):
    def __init__(self, pos, speed, item_type, game):
        super().__init__()
        self.game = game
        self._speed = speed
        self.item_type = item_type
        self.size = (50, 50)
        self.pos = pos
        self.source = F"image/asset/{item_type}.jpg"
        self.game.bind(on_frame=self.move_step)

    def stop_callbacks(self):
        self.game.unbind(on_frame=self.move_step)

    def move_step(self, sender, dt):
        for e in self.game.colliding_entities(self):
            if e == self.game.player:
                self.stop_callbacks()
                self.game.remove_entity(self)
                print(F"collide! {self.item_type}")
                if self.item_type == "Bomb":
                    self.game.half_score()
                    print("BOMB")
                    is_alpha = False
                elif self.item_type == "Eraser":
                    self.game.clear_items()
                    is_alpha = False
                else:
                    self.game.add_items(self.item_type)
                    is_alpha = True
                self.game.refresh_word(is_alpha)
                print(self.game.get_items)
                return
        step_size = self._speed * dt
        new_x = self.pos[0]
        new_y = self.pos[1] - step_size
        self.pos = (new_x, new_y)         