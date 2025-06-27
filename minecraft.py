from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina() # basic instinx(creation of window)
window.exit_button._visible=False 
player = FirstPersonController()
Sky()
# Entity can be shape,button,sound
car=Entity(
    model='car',
    color=color.red,
    position=(0,1),
    scale=(1,1),
    z=-3,
    speed=8
)
def update():
    car.rotation_x+=(
        (held_keys['l']-held_keys['j'])
        *time.dt
        *100
    )
    car.position +=(
        (held_keys['o']-held_keys['k'])
        * car.speed * time.dt 
        *car.forward

    )
boxes = []
for i in range (50):
    for j in range(50):
        box = Button(color = color.green, model = "cube", position = (j,0,i), 
                     texture = "grass.png", parent = scene, origin_y = 0.5 )
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                new = Button(color = color.brown, model = "cube", position = box.position + mouse.normal, 
                     texture = "grass.png", parent = scene, origin_y = 0.5 )
                boxes.append(new)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)

app.run()

