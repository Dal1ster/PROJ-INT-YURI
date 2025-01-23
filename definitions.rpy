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



define intflag = 0
define donutflag = False
define je = Character("JK-EX-7000", window_background="gui/textbox-cl.png")
define a = Character("Dr. Andonuts", window_background="gui/textbox-cr.png", who_xalign=1.0, who_xpos=1720)
define q = Character("???", window_background="gui/textbox-cl.png")
define d = Character("Mr. Dee", window_background="gui/textbox-cl.png", what_style="boing", what_size=49)
define v = Character("Varik", window_background="gui/textbox-cl.png")
define t = Character(None, what_color='#15D114') 
define g1 = Character("Andonuts (?)", window_background="gui/textbox-cr.png", who_xalign=1.0, who_xpos=1720)
define g2 = Character("Andonuts (??)", window_background="gui/textbox-cr.png", who_xalign=1.0, who_xpos=1720)
define g3 = Character("Andonuts (???)", window_background="gui/textbox-cr.png", what_font="Perfect DOS VGA 437 Win.ttf", what_size=46, who_xalign=1.0, who_xpos=1720)
define cen = Character(None, what_xalign=0.5, what_text_align=0.5)
define flash = Fade(.1, 0.0, .25, color="#fff")
transform two_size:
    zoom 2

image varik = "varik.png"
image varik sword = "varik_sword.png"
image mr_dee = "mr_dee.png"
image mr_dee pointing = "mr_dee_pointing.png"
image guilt1 = "guilt1_neutral.png"
image guilt1 battle = "guilt1_battle.png"
image guilt2 = "guilt2_neutral.png"
image guilt2 battle = "guilt2_battle.png"
image guilt2_pat:
    "guilt2_hug_pat1"
    pause .5
    "guilt2_hug_pat2"
    pause .5
    repeat
image voice_bg = Movie(play="images/Thunder_background.webm")
image terrifying = Movie(play="images/Terrifiing.webm")
image voice_battle = Movie(play="images/voicedonuts bg.webm")
image guilt3 = "guilt3_neutral.png"
image guilt3 battle = "vandonuts/guilt3_battle_0000.png"
image guilt3 battle ani1:
    "vandonuts/guilt3_battle_0000.png"
    pause .075
    "vandonuts/guilt3_battle_0001.png"
    pause .075
    "vandonuts/guilt3_battle_0002.png"
    pause .075
    "vandonuts/guilt3_battle_0003.png"
    pause .075
    "vandonuts/guilt3_battle_0004.png"
    pause .075
    "vandonuts/guilt3_battle_0005.png"
    pause .075
    "vandonuts/guilt3_battle_0006.png"
    pause .075
    "vandonuts/guilt3_battle_0007.png"
    pause .075
    "vandonuts/guilt3_battle_0008.png"
    pause .075
    "vandonuts/guilt3_battle_0009.png"
    pause .075
    "vandonuts/guilt3_battle_0010.png"
    pause .075
    "vandonuts/guilt3_battle_0011.png"
image guilt3 battle ani2:
    "vandonuts/guilt3_battle_0012.png"
    pause .075
    "vandonuts/guilt3_battle_0013.png"
    pause .075
    "vandonuts/guilt3_battle_0014.png"
    pause .075
    "vandonuts/guilt3_battle_0015.png"
    pause .075
    "vandonuts/guilt3_battle_0016.png"
    pause .075
    "vandonuts/guilt3_battle_0017.png"
    pause .075
    "vandonuts/guilt3_battle_0018.png"
    pause .075
    "vandonuts/guilt3_battle_0019.png"
    pause .075
    "vandonuts/guilt3_battle_0020.png"
    pause .075
    "vandonuts/guilt3_battle_0021.png"
image sketch 1:
    "blueprint_sketch/a1.png"
    pause .25
    "blueprint_sketch/a2.png"
    pause .25
    repeat
image sketch 2:
    "blueprint_sketch/b1.png"
    pause .25
    "blueprint_sketch/b2.png"
    pause .25
    repeat
image sketch 3:
    "blueprint_sketch/c1.png"
    pause .25
    "blueprint_sketch/c2.png"
    pause .25
    repeat
image sketch 4:
    "blueprint_sketch/d1.png"
    pause .25
    "blueprint_sketch/d2.png"
    pause .25
    repeat
image elevator_flicker:
    "elevator_lights_button.png"
    pause .25
    "elevator_button.png"
    pause .1
    "elevator_lights_button.png"
    pause .5
    "elevator_button.png"
    pause .1
    "elevator_lights_button.png"
    pause .1
    "elevator_button.png"
    pause .1
    "elevator_lights_button.png"
    pause .75
    "elevator_button.png"
    pause .1
    repeat
image computer_lights:
    "comp_light/computer_color1.png"
    pause .5
    "comp_light/computer_color2.png"
    pause .5
    "comp_light/computer_color3.png"
    pause .5
    "comp_light/computer_color4.png"
    pause .5
    "comp_light/computer_color5.png"
    pause .5
    "comp_light/computer_color6.png"
    pause .5
    "comp_light/computer_color7.png"
    pause .5
    "comp_light/computer_color8.png"
    pause .5
    repeat

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

image giygas = TranslateImage(WaveImage("guilt1_bg.png",amp=20, freq=50, speed=50, strip_height=5, double="interleaved"))
image masked_bg = WaveImage(PaletteCycler("images/Guilt2BG/MMBG", ".png", ['#0D8382', '#0B5E5C', '#09494A', '#0B5150', '#0A302F', '#0A302F', '#0D8382', '#0B5E5C', '#09494A', '#0B5150', '#0A302F', '#0A302F']), freq=3, amp=3, strip_height=10, double=True)
image dead_je = WaveImage("doomfes_je.png",amp=40, freq=50, speed=50, strip_height=10,)
image final 1 = WaveImage("andonot0.png", amp=100, freq=10, damp=2, speed=50, strip_height=5, double=True)
image final 2 = WaveImage("andonot02.png", amp=50, freq=10, damp=2, speed=50, strip_height=5, double=True)
image final 3 = WaveImage("andonot.png", amp=20, freq=15, damp=2, speed=50, strip_height=5, double=True)
image final 4 = WaveImage("andonot.png", amp=10, freq=20, damp=2, speed=50, strip_height=5, double=True)
image final 5 = WaveImage("andonot2.png", amp=10, freq=20, damp=2, speed=50, strip_height=5, double=True)
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
image thrust = 'water_in_da_elevator.png' # previously #33F3A6
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

# MADINSTANCE CODE SECTION HIIIIII
# MR. DEE MUSIC CODE

init python:
    renpy.music.register_channel("music_b", "music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    # feel free to tweak this function to fit your needs or add more arguments just make sure to not fw the channels
    def play_multiple(song, song2, delay = 2):
        renpy.music.play(song,"music",True,delay,True,0,None,False,1.0)
        renpy.music.play(song2,"music_b",True,delay,True,delay,None,False,1.0)
        renpy.music.set_volume(0, delay = 0, channel="music_b")

    def stop_layers(delay = 2):
        renpy.music.stop(channel="music", fadeout = delay)
        renpy.music.stop(channel="music_b", fadeout = delay)
        renpy.music.set_volume(1,0,channel="music")
        renpy.music.set_volume(1,0,channel="music_b")

    # fadeout is multiplied by 3 to reduce dead air as much as possible
    def update_layers(dir, delay = 2):
        if dir == "music_b":
            renpy.music.set_volume(0, delay = (delay * 3), channel="music")
            renpy.music.set_volume(1, delay = delay, channel="music_b")
        elif dir == "music":
            renpy.music.set_volume(1, delay = delay, channel="music")
            renpy.music.set_volume(0, delay = (delay * 3), channel="music_b")

# LIGHTNING BACKGROUND CODE
init python:
    # Define a preset array of images for the thunder layer
    BACKGROUND_IMAGES = [
        "lightning_frames/cogdis_voiceoffice_2.png",
        "lightning_frames/cogdis_voiceoffice_3.png",
        "lightning_frames/cogdis_voiceoffice_4.png"
    ]

    # Function to set a random timer between 1 and 5 seconds
    def random_timer():
        return renpy.random.randint(1, 5)

    def initizalize_thunder():
        renpy.add_layer("thunder_layer",above="master")
        while True:
            renpy.pause(random_timer())
            


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