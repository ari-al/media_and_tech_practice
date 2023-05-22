#sun and moon
x_center = 0
y_center = 0

sun_px=0
sun_py=0

moon_px=0
moon_py=0
 
r=800

sun_deg=180
moon_deg=0

button_x=200
button_y=200

speed = 0.5

PLAY='PLAY';
PAUSE='PAUSE';
button_action=PLAY;

def setup():
    global x_center, y_center
    x_center=width/2
    y_center=height
    size(1600,900)
    
def draw():
    background(0)
    draw_sun()
    draw_moon()
    house_image=loadImage("house.png");
    image(house_image,0, 500);


def draw_sun():
    global x_center, y_center, inc, r, sun_deg, speed, sun_px, sun_py
    global button_action, PAUSE, button_x, button_y
    sun_image=loadImage("sun.png");

    angle=radians(sun_deg)
    px=x_center + r * cos(angle)
    py=y_center + r * sin(angle)
    sun_px=px
    sun_py=py
    fill(0x00000000)
    ellipse(px+110,py+110, button_x, button_y)
    image(sun_image,px,py); # 223*223 
    if button_action != PAUSE:
        if sun_deg < 360:
            sun_deg=sun_deg+speed
        else:
            sun_deg=0


def draw_moon():
    global x_center, y_center, inc, r, moon_deg, speed, moon_px, moon_py
    global button_action, PAUSE, button_x, button_y
    moon_image=loadImage("moon.png");
    angle=radians(moon_deg)
    px=x_center + r*cos(angle)
    py=y_center + r*sin(angle)
    moon_px=px
    moon_py=py
    fill(0x00000000)
    ellipse(px+110,py+110, button_x, button_y)
    image(moon_image, px,py)
    if button_action != PAUSE:
        if moon_deg < 360:
            moon_deg=moon_deg+speed
        else:
            moon_deg=0
            

def mousePressed():
    global sun_px, sun_py, moon_px, moon_py
    global button_action, PAUSE, PLAY
    if clickButton(sun_px, sun_py) or clickButton(moon_px, moon_py):
        button_action=PAUSE
    else:
        button_action=PLAY
        
def mouseDragged():
    global button_action
    global moon_deg, sun_deg, speed
    if sun_deg < 360:
        sun_deg=sun_deg+speed
    else:
        sun_deg=0
    if moon_deg < 360:
        moon_deg=moon_deg+speed
    else:
        moon_deg=0
    
def mouseReleased():
    global button_action, PLAY
    button_action=PLAY
    

def clickButton(x,y):
    correction = 115
    if dist(mouseX,mouseY,x+correction,y+correction) < 100:
        return True
    else:
        return False
