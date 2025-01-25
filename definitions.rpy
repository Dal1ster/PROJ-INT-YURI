init:

    python:
        
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
    #

#

define cl = "gui/textbox-cl.png"
define cr = "gui/textbox-cr.png"
define je = Character("JK-EX-7000")
define a = Character("Dr. Andonuts")
define q = Character("???")
define t = Character(None, what_color='#15D114')
define cen = Character(None, what_xalign=0.5, what_text_align=0.5)
define flash = Fade(.1, 0.0, .25, color="#fff")
transform two_size:
    zoom 2

image battle_trans:
    "transition/CDTransition_000001.png"
    pause .03
    "transition/CDTransition_000002.png"
    pause .03
    "transition/CDTransition_000003.png"
    pause .03
    "transition/CDTransition_000004.png"
    pause .03
    "transition/CDTransition_000005.png"
    pause .03
    "transition/CDTransition_000006.png"
    pause .03
    "transition/CDTransition_000007.png"
    pause .03
    "transition/CDTransition_000008.png"
    pause .03
    "transition/CDTransition_000009.png"
    pause .03
    "transition/CDTransition_000010.png"
    pause .03
    "transition/CDTransition_000011.png"
    pause .03
    "transition/CDTransition_000012.png"
    pause .03
    "transition/CDTransition_000013.png"
    pause .03
    "transition/CDTransition_000014.png"
    pause .03
    "transition/CDTransition_000015.png"
    pause .03
    "transition/CDTransition_000016.png"
    pause .03
    "transition/CDTransition_000017.png"
    pause .03
    "transition/CDTransition_000018.png"
    pause .03
    "transition/CDTransition_000019.png"
    pause .03
    "transition/CDTransition_000020.png"
    pause .03
    "transition/CDTransition_000021.png"
    pause .03
    "transition/CDTransition_000022.png"
    pause .03
    "transition/CDTransition_000023.png"
    pause .03
    "transition/CDTransition_000024.png"
    pause .03
    "transition/CDTransition_000025.png"
    pause .03
    "transition/CDTransition_000026.png"
    pause .03
    "transition/CDTransition_000027.png"
    pause .03
    "transition/CDTransition_000028.png"
    pause .03
    "transition/CDTransition_000029.png"
    pause .03
    "transition/CDTransition_000030.png"
    pause .03
    "transition/CDTransition_000031.png"
    pause .03
    "transition/CDTransition_000032.png"
    pause .03
    "transition/CDTransition_000033.png"
    pause .03
    "transition/CDTransition_000034.png"
    pause .03
    "transition/CDTransition_000035.png"
    pause .03
    "transition/CDTransition_000036.png"
    pause .03
    "transition/CDTransition_000037.png"
    pause .03
    "transition/CDTransition_000038.png"
    pause .03
    "transition/CDTransition_000039.png" 

image dead_je = WaveImage("doomfes_je.png",amp=40, freq=50, speed=50, strip_height=10,)
init python:
    renpy.music.register_channel("sound_2", "sfx", loop=False)
    renpy.music.register_channel("music_c", "music", loop=True)
    renpy.music.register_channel("music_d", "music", loop=True)
style say_vbox xfill True
define fadeWithText = { "master" : Dissolve(0.5) }
image black = 'black.png'
image fog = '#B87C99'
image aura = '#9471E7'
image voice = '#FF00E8'
image white =  '#ffffff'
image green = '#33F3A6'
define slow_fade = Fade(1,1,1)
define go_fade_1 = Fade(2,0,0)
define go_fade_2 = Fade(0,0,1)
define foggy_fade = Fade(.5, 1, .5, color='#B87C99')
define long_dissolve = Dissolve(2.0)
define fast_fade = Dissolve(.25)

transform silhoette:
    matrixcolor Matrix([ 0, 0, 0, 0,
                        0, 0, 0, 0,
                        0, 0, 0, 0,
                        0, 0, 0, 1, ])
transform unsilhoette:
    matrixcolor Matrix([ 1, 0, 0, 0,
                        0, 1, 0, 0,
                        0, 0, 1, 0,
                        0, 0, 0, 1, ])
transform powerdown:
    matrixcolor Matrix([ .5, 0, 0, 0,
                        0, .5, 0, 0,
                        0, 0, .5, 0,
                        0, 0, 0, 1, ])


init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

transform hp_trans:
    on show:
        easein .5
    on hide:
        easeout .5

transform jeleft:
    xpos 100
    ypos 100
transform jeright:
    xpos 1350
    ypos 100
transform cccleft:
    xpos 200
    ypos 100
transform cccright:
    xpos 1250
    ypos 100
transform cccenter:
    xalign 0.5
    ypos 100
transform cccfuckoffleft:
    xpos -1000
    ypos 100
transform battle:
    xalign .5
    yalign .05
transform flip: # Used for flipping. Taken from: https://www.reddit.com/r/RenPy/comments/je2pzw/comment/g9fk1n3/
    xzoom -1.0
    
    
################################################################
#      HERE STARTS DECODER YURI VISUAL NOVEL DEFINITIONS       #
################################################################

# IMAGES
image voice_tower_explode = "images/bg/voice_tower_explode.png"

image andonuts = "andonuts/andonuts.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake
image andonuts worried = "andonuts/andonuts_worried.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake
image andonuts happy = "andonuts/andonuts_happy.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake

image joke_explainer = "jkex7000/joke_explainer.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake
image joke_explainer happy = "jkex7000/je_happy_talk.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake
image joke_explainer confused = "jkex7000/je_confused.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake
image joke_explainer question = "jkex7000/je_confused_dontsweatit.png" # changed from CogDis to be in an Andonuts folder, for convenience's sake

# MUSIC
define audio.snowblind = "<loop 8.726>audio/bgm/snowblind.ogg"

# SOUND EFFECTS

# TRANSITIONS
define dissolve_2sec_wtext = { "master" : Dissolve(2.0) }

# CHARACTERS