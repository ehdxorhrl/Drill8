from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(20, 780), 599
        self.dy = random.randint(4, 15)
        if (self.x % 2) != 0:
            self.image = load_image('ball41x41.png')
        else:
            self.image = load_image('ball21x21.png')
    def update(self):
        if (self.x % 2) != 0:
            if self.y > 75:
                self.y -= self.dy
            else:
                self.y = 75
        else:
            if self.y > 65:
                self.y -= self.dy
            else:
                self.y = 65
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world
    global balls

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    world += team
    balls = [Ball() for i in range(20)]
    world += balls


def update_world():
    for o in world:
        o.update()

    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

running = True

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.03)

close_canvas()
