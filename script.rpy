# TO-DO
# make inventory better / work
# sfxs
# lightning


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

image joke_explainer = "joke_explainer.png"
image joke_explainer happy = "je_happy_talk.png"
image joke_explainer confused = "je_confused.png"
image joke_explainer question = "je_confused_dontsweatit.png"
image andonuts = "andonuts.png"
image andonuts worried = "andonuts_worried.png"
image andonuts happy = "AndoHappy.png"
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

# The game starts here.

label main_menu:
    return


label gameover:
    play sound "die.wav"
    
    stop music

    "Joke-Explainer got hurt and collapsed!"
    
    play music "<loop 4.09>gameover.ogg"

    scene gameover with slow_fade
    hide screen hpbar

label gameover2:
    t """
    Joke-Explainer!

    It looks like you got your head handed to you.

    You should give it another shot!
    """
    
    stop music fadeout 2.0

    scene black with go_fade_1

    if intflag == 1:
        $ config.after_load_transition = go_fade_2
        $ renpy.load("fight_1")
    elif intflag == 2:
        $ config.after_load_transition = go_fade_2
        $ renpy.load("fight_2")
    elif intflag == 3:
        $ config.after_load_transition = go_fade_2
        $ renpy.load("fight_3")
    elif intflag == 4:
        $ config.after_load_transition = go_fade_2
        $ renpy.load("fight_4")
    else:
        return


label start:
    $ quick_menu = False

    t "The following experience features Yuri."
    
    menu:
        t "Do you consent to Yuri?"

        "Yes": 
            t "Please enjoy the Yuri."
    
        "No":
            t "Fuck u. >:("
            $ renpy.quit() 
    
label beginning:    
    cen """
    December 25th, 2016
    
    December 25th, 201{fast}{nw}
    
    December 25th, 20{fast}{nw}
    
    December 25th, 2{fast}{nw}
    
    December 25th, {fast}{nw}
    
    December 25th,{fast}{nw}
    
    December 25th{fast}{nw}
    
    December 25t{fast}{nw}
    
    December 25{fast}{nw}
    
    December 2{fast}{nw}
    
    December {fast}{nw}
    
    December{fast}
    
    December {fast}{nw}
    
    December 2{fast}{nw}
    
    December 28{fast}{nw}
    
    December 28t{fast}{nw}

    December 28th{fast}{nw}

    December 28th,{fast}{nw}

    December 28th, {fast}{nw}

    December 28th, 2{fast}{nw}

    December 28th, 20{fast}{nw}
    
    December 28th, 202{fast}{nw}

    December 28th, 2024{fast}
    """

    """
    Somewhere,{w=.5} deep in the Voice's tower...
    
    A smol purple haired figure flew quickly through the hallways.{w=1.0} Her name{cps=3}...{w=.5}{/cps} \nThe Joke-Explainer{image=tm.png} 7000. 
    
    She scanned the doors as she passed them,{w=.25} before coming to a sudden halt in front of one.{w} Double checking that the name engraved on the nameplate is the correct one,{w=.25} she opened the door and entered the room.
    """
    play sound "ccc_door.wav"

    if (renpy.music.is_playing("sound")):
        while (renpy.music.is_playing("sound")):
            pause 1 

    scene ccclab at truecenter with dissolve

    play music "lab.ogg"

    show joke_explainer at jeleft with dissolve

    je "Doctor Andonuts?{w=.5} You asked to see me?" 

    "On the other side of the messy room stood a portly man in a lab coat,{w=.25} immersed in a mass of wires,{w=.25} papers,{w=.25} and machinery."

    "Joke-Explainer's sudden entrance startled him,{w=.25} causing him to trip on a loose wire and go{nw}"
    play sound "slam.wav" volume 0.5
    extend " crashing to the floor." with sshake

    show andonuts worried at cccright with dissolve

    a "Ohhhh..."

    "The Joke-Explainer made her way over to help the doctor up.{w=.5} After regaining a bearing on his surroundings he swatted the dust off of his coat."

    show andonuts -worried
    $ renpy.transition(fast_fade, layer="master")

    a "Joke-Explainer!{w=.5} You...{w=.5} well it would seem you caught me at a bad time, ha ha.{w=.5} How about a donut?"

    menu:
        "Take a donut?"

        "Yes":
            show joke_explainer happy
            $ renpy.transition(fast_fade, layer="master")
            
            je "Of course!"

            "Joke-Explainer took the donut,{w=.25} and didn't eat it.{w=.5} She just looked at it,{w=.25} smiling vacantly."

            $ donutflag = True

            $ inventory.add_item(donut)

            a "...Hm. Okay then."

        "No":
            je "Sorry,{w=.25} I'm not hungry at this moment."

            $ donutflag = False

            a "Oh."
    
label post_donut:
    a "Apologies for the mess,{w=.5} I haven't had much time to clean up after myself.{w=.5} I was hoping I'd be able to finish up my project before you arrived...{w=.5} It's a bit hard to keep things tidy when focused on work,{w=.5} you know?"    

    show joke_explainer question
    $ renpy.transition(fast_fade, layer="master")

    je "Your{cps=3}...{w=.5}{/cps} project?"

    "Joke-Explainer turned her head towards the massive machine right beside them that she'd previously paid no mind to."

    show andonuts happy
    $ renpy.transition(fast_fade, layer="master")

    a "Yes,{w=.25} the Psyche Injector.{w=.5} The latest in my line of magnum opuses!{w=.5} Opi?{w=.5} What would be the plural for that?"

    show joke_explainer -question
    $ renpy.transition(fast_fade, layer="master")

    je "While the correct pluralization of opus is 'opuses',{w=.5} it should be noted that a magnum opus is defined as one's greatest accomplishment,{w=.5} the pinnacle of one's chosen craft.{w=.5} It is typical for a person to only have one."

    a "I see{cps=3}...{w=.5}{/cps} Though,{w=.25} maybe you wouldn't be saying that if you knew I consider you one of those opuses?"

    "He was half correct.{w=.5} Some time after Joke-Explainer's creator disappeared,{w=.25} she met Andonuts.{w=.5} He offered her his protection and scientific knowledge.{w=.5} He was there for her when nobody else was,{w=.25} and they formed a close bond because of it."

    a "In any case,{w=.25} the reason I built it in the first place was to assist you in assisting me with a certain,{w=.25} uh{cps=3}...{w=.5}{/cps}{nw}"
    
    show andonuts worried
    $ renpy.transition(fast_fade, layer="master")

    extend " problem I've encountered recently—{w=.25}Thank you for stepping away from running the channel to help me with this,{w=.25} by the way.{w=.5} I hope this isn't too damaging to your schedule..."

    show joke_explainer happy
    $ renpy.transition(fast_fade, layer="master")

    je "It isn't any trouble at all,{w=.25} Doctor!{w=.5} The SiIvaGunner channel currently has its schedule entirely filled out,{w=.25} so this request doesn't conflict with any of my current parameters."
    
    show joke_explainer -happy
    $ renpy.transition(fast_fade, layer="master")

    je "Besides,{w=.25} I'm{cps=3}...{w=.5}{/cps} grateful for the break in my current routine."

    show andonuts happy
    $ renpy.transition(fast_fade, layer="master")

    a "Oh good!{w=.5} Good... We can continue on with operations then."

    je "And what are these operations you speak of?{w=.5} Why did you call me so urgently in the first place?"

    stop music fadeout 2.0

    a "I'm very glad you asked!{w=.5} Allow me to illuminate{cps=3}...{/cps}"

    scene blueprint with fade

    play music "Chimera.ogg"

    show sketch 1 at truecenter with fadeWithText

    a """
    As of late I've been having some{cps=3}...{w=.5}{/cps} issues,{w=.25} in the depths of my own mind.{w=.5} A malignant foreign entity has hijacked my mental processes,{w=.25} making it quite difficult for me to concentrate on scientific endeavors.

    To resolve this ailment,{w=.25} I've opted to build a machine to tap into my psyche and allow an external force to expel the entity from my brain.{w=.5} Hence its name.
    """

    je "I see...{w=.5} And do you need me to control the external force to terminate whatever's ailing you?"

    a "No, Joke-Explainer{cps=3}...{w=.5}{/cps} I need you to BE the external force."

    "Joke-Explainer's face lit up in surprise at the statement."

    je "Me{cps=3}...?{w=.5}{/cps} How could I be the one to terminate the foreign entity?{w=.5} I am not equipped with any weapon systems."

    show sketch 2 at truecenter with fadeWithText

    a """
    Well,{w=.25} that's where the Psyche Injector comes in!{w=.5} If I connect myself to it,{w=.25} it can scan all corners of my brain to generate a unique metaphysical realm,{w=.25} accessible to others through the injection process.

    Many people have given this realm different titles.{w=.5} Mental worlds,{w=.25} the Cognitive World,{w=.25} mindscapes...{w=.5} but I've elected to call it \"Magicant\".
    """

    scene black with fade

    je "Magicant?{w=.5} That's a location in{nw}" 
    show ebthumb with fadeWithText
    extend " EarthBound{w=.25} (also known as Mother 2 in Japan) and{nw}"
    show ebbthumb with fadeWithText
    extend " EarthBound Beginnings{w=.25} (also known as Mother in Japan)!{w=.5} As well as in the{nw}"
    show ebhhthumb with fadeWithText
    extend" EarthBound Halloween Hack!"

    scene black with fadeWithText

    "Andonuts tensed up and shifted a little in his shoes."

    scene blueprint with fadeWithText

    a "Y-yes...{w=.5} Yes it's...{w=.25} yes,{w=.25} that place.{w=.5} I need you to enter my Magicant and defeat the entity.{w=.5} Are you up to the task?"

    je "I'm not opposed to the idea,{w=.25} but I must reiterate I am not typically equipped with any weapon systems.{w=.5} How could I possibly terminate whatever's afflicting you?"

    show sketch 3 at truecenter with fadeWithText

    a "You don't need to necessarily fight it...{w=.5} you just need to capture it.{w=.5} Contain it in a way where it will be unable to escape and cause me any more harm." 
    
    show sketch 4 at truecenter with fadeWithText

    a "Thankfully I have designed a capsule to perform that exact task,{w=.25} which will make the process even easier for you!{w=.5} All you really need to do is enter with this Fun-Sized Absolutely Safe Capsule and trap the entity."
    
    a "I will be directing you from the outside on where to go using a radio,{w=.25} so if you get lost or have trouble I'll be there as a guide.{w=.5} Do you understand?"

    je "Affirmative!"

    hide sketch 4 with fadeWithText

    a "Thank you.{w=.5} Alright,{w=.25} hold onto these items and allow me to put the final touches on the Psyche Injector."

    $ inventory.add_item(radio)
    $ inventory.add_item(fsasc)
    
    stop music fadeout 2.0

    play sound "getitemjingle.ogg"

    "Andonuts gave Joke-Explainer the FUN-SIZED ABSOLUTELY SAFE CAPSULE and the RADIO."

    scene ccclab at truecenter with dissolve

    play music "lab.ogg"

    show joke_explainer at jeleft with dissolve

    """
    Joke-Explainer found a comfortable seat among the clutter and watched the doctor insert the final wires and plugs into their place.{w=.5} When he hooked the Psyche Injector to a power source,{w=.25} it roared to life with intensity and purpose. 
    
    Doctor Andonuts proudly beamed at the machine...{w=.5} but for a moment,{w=.25} his smile faltered.{w=.5} Into something almost{cps=3}...{w=.5}{/cps} afraid.{w} What could he be-{nw}
    
    But just as she noticed, his face locked into stoic focus.

    Andonuts strolled over wearing a large metallic helmet, holding a long cord.
    """

    show andonuts at cccright with dissolve

    a "Okay...{w=.25} you'll need to unplug your Wi-Fi transmitter and connect to the machine with this aux cable."

    "Joke-Explainer obediently removed her antenna and plugged the cable into the empty slot.{w=.5}{nw}"
    
    window show

    scene and_grapesurgery at truecenter with fadeWithText 

    extend " Andonuts stepped back and assumed his place in the machine.{w=.5} Above him stood many large needles,{w=.25} hovering ominously close to his head."

    a """
    Oh,{w=.25} and um...{w=.5} please don't attempt to remove me from the Psyche Injector when I activate it.{w=.5} It will look very,{w=.25} very painful,{w=.25} but I assure you it's tested to be absolutely safe. 
    
    Once it's activated,{w=.25} you should receive a pop-up in your peripherals requesting to initialize the injection process.{w=.5} Click yes, and you'll soon awake in Magicant. 
    
    ...And be careful what you touch in there,{w=.25} won't you?{w=.5} This is my mind after all.{w=.5} Who knows what might happen if you break anything...
    """

    stop music fadeout 2.0

    "Joke-Explainer gave a nod in understanding.{w=.5} Andonuts sighed and hesitated for a few seconds,{w=.25} before finally working up enough courage to activate the Psyche Injector." 
    
    "It lit up and the needles turned to lock in place.{w=.5} Just as the doctor said,{w=.25} a pop-up suddenly appeared in front of Joke-Explainer.{w=.5} Without a second thought she clicked 'Yes',{w=.25}{nw}"
    
    play sound "machine_whistle.ogg"

    extend " which caused the machine to make a loud whistling noise."

    scene and_grapesurgery2 at truecenter with flash

    play music "<loop 5>Andonuts_machine_impact.ogg"

    scene and_grapesurgery2 at truecenter with sshake

    "All at once,{w=.25} the mess of needles stabbed themselves through Doctor Andonuts's brain.{w=.5} His body writhed around in agony,{w=.25} slamming against the restraints,{w=.25} as he forcibly suppressed the urge to rip the needles out."
    
    "Joke-Explainer almost immediately stood up with the intent to help him,{w=.25} before considering the doctor's prior request.{w=.5}{nw}"
    
    stop sound fadeout 3

    stop music fadeout 3

    extend " Reluctantly, she sat back down and stayed put as Andonuts slowly succumbed to unconsciousness."

    scene ccclab at truecenter with fadeWithText

    "After a minute of the machine operating,{w=.25} she herself started to feel a sense of dizziness seep into her systems."
    
    scene ccclab at truecenter with fadeWithText:
        blur 15

    "{cps=10}Everything is getting darker and darker...{/cps}"
    
    
    scene black with fade

    window hide

    play sound "nightmare.flac"

    if (renpy.music.is_playing("sound")):
        while (renpy.music.is_playing("sound")):
            pause 1 

label magicant:
    show screen inventory_display_toggle
    
    $ quick_menu = True

    window show

    "Joke-Explainer can feel grass underneath her.{w=.5} That doesn't make sense,{w=.25} she was in an office mere moments ago..."
    
    play music "magicant.ogg" volume 0.75 fadein 1.0

    scene je_awake with fade

    "Opening her eyes out of curiosity,{w=.25} she's graced with a vast empty sky.{w=.5} She lays in a grassy field,{w=.25} surrounded by infinitely spanning waters.{w=.5} She can hear the distant buzzing of the radio Andonuts gave her."

    t "Click on the pocket in the top right corner to access your inventory!"

    $ persistent.radioflag = 1

    window hide

    if persistent.radioflag == 1:
        while persistent.radioflag == 1:
            pause 

label post_radio_1:
    $ persistent.radioflag = 2
    
    "The RADIO sparks to life,{w=.25} and Joke-Explainer can make out the distinct voice of Doctor Andonuts on the other side."

    play sound "radioon.mp3"

    a "Joke-Explainer{cps=3}...{w=.5}{/cps} c-{w=.25}can you,{w=.25} can you hear me?"

    je "The radio is a little fuzzy,{w=.25} but yes."

    a "Oh thank goodness,{w=.25} it worked{cps=3}...{w=.5}{/cps} Okay, have you gotten a sense of your surroundings?{w=.5} What do you see right now?"

    je "I see{cps=3}...{w=.5}{/cps} grass.{w=.5} The grass is a light blue,{w=.25} instead of green.{w=.5} There's also a bunch of vegetables littered about."

    a "Vegetables?{w=.5} How odd{cps=3}...{w=.5}{/cps} See if you can spot anything out of the ordinary around the area.{w=.5} Something that sticks out like a sore thumb."

    scene magicant_bg with fadeWithText

    "Joke-Explainer flies around,{w=.25} spotting a multitude of abstract structures and characters,{w=.25} mental constructs of Andonuts's mind."
    
    stop music fadeout 2.0

    "She eventually comes across an ominous knight-like figure,{w=.25} stationed before the mouth of a cave,{w=.25} seeming to be acting as its guardian.{w=.5} She decides to begin there."

    $ play_multiple("sync.ogg","saturn.ogg")

    scene mouthofterror with dissolve

    show varik at cccenter with fadeWithText

    je "Greetings,{w=.25} sir."    

    "The guard stands unwavering."

    je "I was sent here with the task of eliminating a threat to this mindscape.{w=.5} If you don't mind,{w=.25} I need to get past you to go into that cave."

    q "{cps=3}...{w=.5}{/cps}"

    je "{cps=3}...{w=.5}{/cps}"

    "After several moments of frustrating silence,{w=.25} Joke-Explainer attempts to sidestep the guard.{w} All of a sudden,{w=.25} the guard{nw}"
    
    show varik sword

    play sound "sword.wav"

    extend " springs to life,{w=.25} quickly and sternly brandishing his weapon at the intruder."

    je "Wait!{w=.5} You don't seem to understand!{w=.5} I was sent here by Doctor Andonuts himself,{w=.25} the host of this mind!{w=.5} I mean him no harm!"

    "The guard holds his weapon perfectly still,{w=.25} undeterred."

    d "Hi ho,{w=.25} me Mr. Dee.{w=.5} We see you with to enter the Mouth of Terror!"

    hide varik
    $ renpy.transition(easeoutleft, layer="master")

    "Joke-Explainer,{w=.25} startled,{w=.25} looks around in confusion,{w=.25} trying to grasp what is happening around her.{nw}" 
    
    show mr_dee at cccenter
    $ renpy.transition(easeinright, layer="master")
    $ update_layers("music_b", 1)

    extend " She sees what is a Mr. Saturn standing on top of a Waddle Dee right beside her."

    je "If that is the name of the cave ahead of us,{w=.25} then yes,{w=.25} that is my objective."

    d "Scary,{w=.25} strange,{w=.25} so boing!{w=.5} Cave...{w=.25} protected. Guard man named Varik!{w=.5} \nHis job to keep fear in,{w=.25} bad stuff from coming out.{w=.5} Also keep others out,{w=.25} like you!"

    show mr_dee at cccright
    $ renpy.transition(ease, layer="master")

    show varik at cccleft
    $ renpy.transition(easeinleft, layer="master")
    v "..."
    show mr_dee at cccenter
    $ renpy.transition(ease, layer="master")

    show varik at cccfuckoffleft
    $ renpy.transition(ease, layer="master")

    je "If Doctor Andonuts is already aware of the foreign entity,{w=.25} wouldn't that suggest insecurity?"

    hide varik

    d "Ding ding!{w=.5} Indeed!{w=.5} Cave only hold so much,{w=.25} some already leaking!{w=.5} But still,{w=.25} no outsider!"

    je "My current directive is specifically to contain the foreign entity causing problems.{w=.5} This situation is of utmost importance –{w=.25} if this leakage is occuring,{w=.25} I need to stop it as soon as possible!{w=.5} Is there any way I could enter that chamber?"

    d "Need courage!{w=.5} Three courages gone,{w=.25} so Varik alone and prickly!{w=.5} Courages stolen by bad bad things!{w=.5} You get courages from bad things,{w=.25} then Varik let \nyou through!"

    je "Courages{cps=3}...{w=.5}{/cps} Do you know where they were taken?"

    d "Down Anguish Avenue!{w=.5}{nw}"
    
    show mr_dee pointing
    $ renpy.transition(fast_fade, layer="master")

    extend " That way!{w=.5} Zoom!"

    show mr_dee -pointing
    $ renpy.transition(fast_fade, layer="master")

    je "I see{cps=3}...{w=.5}{/cps} Thank you for helping me.{w=.5} I'll return with those Courages shortly!"

    d "Bye later!"

    "Joke-Explainer gives a short wave as{nw}" 
    
    hide mr_dee
    $ renpy.transition(easeoutright, layer="master")

    $ stop_layers()

    extend " Mr. Dee waddles away,{w=.25} she then sets off in the direction towards Anguish Avenue.{w=.5}{nw}"

    scene magicant_bg with fadeWithText

    extend " She doesn't get very far before the radio flares to life again,{w=.25} and she hears Doctor Andonuts's voice on the other side once more."

    play sound "radioon.mp3"

    play music "paula_og.ogg"

    a "Joke-Explainer,{w=.25} do you read me?"

    je "I'm here,{w=.25} Doctor!"

    a "Okay{cps=3}...{w=.5}{/cps} You got all that was said,{w=.25} yes?{w=.5} Do you need me to repeat what they told you?{nw}"

    menu:
        extend " "

        "No":
            je "That won't be necessary!{w=.5} I heard everything."

label post_dee:

    a "Oh{cps=3}...{w=.5}{/cps} Alright,{w=.25} sorry."

    a "I{cps=3}...{w=.5}{/cps} I'm sorry for all this trouble,{w=.25} I didn't expect it to be this difficult..."

    je "I was sent here on a mission and I won't stop until it's completed.{w=.5} As long as I know where the Courages are,{w=.25} it's only a matter of time!"

    a "Yes,{w=.25} but I{cps=3}...{w=.5}{/cps} Just,{w=.25} if you see any—{w=.25}uh{cps=3}...{w=.5}{/cps} Look,{w=.25} just be careful,{w=.25} alright?"

    je "Affirmative!"

    a "Thank you{cps=3}...{w=.5}{/cps} good luck."

    stop music fadeout 2.0

    "The radio is silent once more."

    scene sign with dissolve

    "A few moments of peaceful walking pass,{w=.25} before Joke-Explainer reaches a long dilapidated road dead ahead of her.{w=.5} A road sign nearby confirms it to indeed be Anguish Avenue.{w=.5} Steeling herself,{w=.25} she takes her first step down this dark path. "

label an_av_1:

    scene fog with fadeWithText
    
    """
    As she does,{w=.25} she is hit with a sudden,{w=.25} unnatural blanket of scarlet fog in front of her out of nowhere.{w=.5} It almost entirely obscures her vision,{w=.25} to the point where she can't discern much past a few feet ahead of herself. 
    
    Nevertheless, she keeps going,{w=.25} hoping to find some kind of landmark{cps=3}...{/cps}
    
    And soon,{w=.25} find one she does.
    """

    scene anguish_avenue_fog at truecenter with dissolve

    play music "omen.ogg"

    """
    Inexplicably,{w=.25} the fog seems to clear up a bit to reveal a quiet neighborhood of identical houses stretching quite a far distance.
    
    Joke-Explainer feels relief to be somewhere she can see,{w=.25} but that relief vanishes when she notices just how{cps=3}...{w=.5}{/cps} off the area feels.{w=.5} None of the houses or streetlamps are illuminated,{w=.25} and every house looks like a carbon copy of its neighbors.{w=.5} The pattern repeats into the fog until it's blotted out completely{cps=3}...{/cps}

    Joke-Explainer feels unnerved as she keeps walking past the houses.{w=.5} The feeling of being watched crawls all over her,{w=.25} but the houses are completely empty whenever she looks.{w=.5} There's nobody in sight.{w=.5} It's all just lamps in windows.
    
    Searching for some solace,{w=.25} Joke-Explainer pulls out her radio and turns it on.
    """
    $ renpy.music.set_volume(.8,0,channel="music")

    $ renpy.music.set_volume(.2,0,channel="music_b")

    play music_b "radio-static.ogg" volume .5

    je "Doctor{cps=3}...?{w=.5}{/cps} Doctor Andonuts,{w=.25} can you hear me?"

    "The static buzz rings out in the quiet neighborhood."

    $ renpy.music.set_volume(.6,0,channel="music")

    $ renpy.music.set_volume(.4,0,channel="music_b")

    je "I've made my way to Anguish Avenue,{w=.25} but I can't find where any of the Courages are.{w=.5} Do you sense anything around?{cps=3}...{/cps}"

    "She can feel the noise resonating with the steel of her flesh.{w=.5} Lining her thoughts with dissonance."

    $ renpy.music.set_volume(.4,0,channel="music")

    $ renpy.music.set_volume(.6,0,channel="music_b")

    je "Doctor?{w=.5} Doctor Andonuts,{w=.25} please answer.{w=.5} I don't know where to go."

    "There's nothing.{w=.5} There never was anything to begin with."

    $ renpy.music.set_volume(.2,0,channel="music")

    $ renpy.music.set_volume(.8,0,channel="music_b")

    je "Please{cps=3}...{w=.5}{/cps} I can't see anything,{w=.25} it's all just the same."

    "It's always been the same."

    stop music

    $ renpy.music.set_volume(1,0,channel="music_b")

    
    "Joke-Explainer shakes the radio in the hopes that it'll work,{w=.25} but nothing changes.{w=.5} When would it have ever changed?{w=.5} You have no power to change your fate."

    "The fog closes around her{cps=3}...{w=.5}{/cps} But as she grips the radio in desperation,{w=.25}{nw}"
    
    window show

    scene shiny with fadeWithText

    extend " she spots the tiny twinkle of a light from one of the houses.{w=.5} She looks up towards the house before fully engaging her boosters."
    
    "She wants to get away,{w=.25} she NEEDS{w=.25} to get away{cps=3}...{w=.5}{/cps} Get away from it all,{w=.25} GET AWAY FROM IT ALL!{w=.5}{nw}"
    

label eb_lab:

    scene black
    $ renpy.transition(None, layer="master")

    stop music_b

    play sound "door-slam.ogg"
    
    $ renpy.music.set_volume(1,0,channel="music")

    "Joke-Explainer shuts the door behind her."

    "She takes a moment to collect herself,{w=.25} and finally looks up to see the inside of the house.{w=.5} It's{cps=3}...{w=.5}{/cps} certainly not what she was expecting."

    scene eblab with dissolve

    "She finds herself at the entrance to a vast laboratory.{w=.5} Gadgets and gizmos are laid about all over the place.{w=.5} It quite resembles the office she was in a short time ago,{w=.25} before she entered into this dreamy land of nightmares."
    
    "Taking some time to observe the space around her,{w=.25} she realizes this interior is way larger than the outside of the house she entered into."

    je "Hello?{w=.5} Anyone here?"

    play music "rattle_loop.ogg"

    play music_b "bang_loop.ogg"

    window show

    "She hears a sharp rattle to the far left of her,{w=.25} coming from a large machine.{w=.5}{nw}"
    
    scene machine1
    $ renpy.transition(dissolve, layer="master")

    extend " Inching closer towards it,{w=.25} she can almost make out a figure,{w=.25} but it's difficult to see behind the dirt and grime caked onto the glass."

    je "I'm here to rescue the Courage{cps=3}...{w=.5}{/cps} to save Doctor Andonuts.{w=.5} May I have whatever you're guarding?"

    "Joke-Explainer slowly reaches out towards the machine.{w=.5} She can feel a light pull from something within{cps=3}...{w=.5}{/cps} something that wants her to get closer.{w=.5} BEGS{w=.25} her to get closer.{w=.5} {cps=10}Come close and{/cps}{w=.5}{nw}" 
    
    stop music

    stop music_b

    scene black
    $ renpy.transition(None, layer="master")

    "{cps=7}slay tHE MO{b}NSTER—{/b}{/cps}{nw}"

    window hide

    play music "winters.ogg"

    play sound "door_break.ogg"

    scene machine2 at truecenter with sshake
    $ renpy.transition(None, layer="master")

    pause 2

    window show

    "The door to the machine is ripped off and falls to the ground with a loud bang.{w=.5} The glass shatters instantly on impact,{w=.25} sending a wave of caustic noise to Joke-Explainer's audio receptors.{w=.5} The ringing in her ears returns."

    "She jumps back in alarm, away from whoever's inside.{w=.5} She expects a fierce creature to emerge from the bowels of the metal casing{cps=3}...{w=.5}{/cps} but is even more surprised when she sees{nw}"
    
    scene machine3 at truecenter
    $ renpy.transition(dissolve, layer="master")

    extend " Doctor Andonuts slowly slink his way into view.{w=.5} Her demeanor lightens up upon realizing it's indeed him."

    je "Doctor{cps=3}...?{w=.5}{/cps} You worried me for a moment!{w=.5} Are you alright?"

    g1 "{i}{cps=10}Why...{/i}{/cps}"

    je "Why?{w=.5} Why what?{w=.5} Are you alright,{w=.25} Doctor Andonuts?"

    "On closer inspection,{w=.25} his stance is bent,{w=.25} his breaths labored,{w=.25} and{cps=3}...{w=.5}{/cps} some sort of liquid drips from his head.{w=.5} He cocks his head towards her.{w=.5} His expression is crooked.{w=.5} Repulsive."

    scene eblab_door with fadeWithText

    show guilt1 at cccenter with fadeWithText

    je "I-{w=.25}I attempted to contact you earlier but my radio wasn't working,{w=.25} I'm very sorry about the delays—{w=.25}{nw}"

    g1 "You should be SORRY{w=.25} for much more than that,{w=.25} {cps=10}machine{/cps}."

    "Joke-Explainer tenses up once more,{w=.25} confused."

    je "Excuse me?"

    "Andonuts steps towards her,{w=.25} and without thinking she slightly scoots back.{w=.5} Andonuts takes notice."

    g1 "You've made everything so much worse for me{cps=3}...{w=.5}{/cps} You didn't SAVE me from those wretched needles and wires{cps=3}...{w=.5}{/cps} I begged you for help!{w=.5} \nI NEEDED it!"

    je "Apologies Doctor,{w=.25} I was told to let the process continue—{w=.25}{nw}"

    g1 "And NOW,{w=.25} you want to run away.{w=.5} Run away from what you've let happen{cps=3}...{w=.5}{/cps} \n{cps=10}I can feel it.{/cps}"

    je "You're scaring me,{w=.25} you..."

    "A sudden realization clicks in her head.{w=.5} She wonders how Doctor Andonuts could've even entered into this domain in the first place,{w=.25} since last she knew he was still in the real world guiding her,{w=.25} hooked up to the Psyche Injector." 
    
    "This distorted figure of the Doctor can't possibly be him{cps=3}...{w=.5}{/cps} it must be what Mr. Dee meant when he said \"bad things\" were guarding the Courages."

    je "You're{cps=3}...{w=.5}{/cps} not the doctor,{w=.25} are you?"

    "Andonuts gives a horrid sneer,{w=.25} before contorting his face into a frown."

    g1 "First you let me suffer in pain,{w=.25} and now you insult my very person?{w=.5} How dare you,{w=.25} you little weasel{cps=3}...{w=.5}{/cps} Don't you know what I've been through?!"

    "Andonuts steps forward again and Joke-Explainer feels the energy around them erupt like fire.{w=.5} She sees what looks to be red swirls of madness dancing around her and the doctor.{w=.5} They almost radiate off of him.{w=.5} His face flares up into a grin,{w=.25} the whites of his eyes searing past his glasses."

    g1 "I've hurt{cps=3}...{w=.5}{/cps} I've caused hurt{cps=3}...{w=.5}{/cps} I never meant it!{w=.5} I never did!{w=.5} I was doing my best{cps=3}...{w=.5}{/cps} IT WASN'T ENOUGH!{w=.5} \nAH  HAHAHA{w=.5}  \nAHAH ha"

    je "Please!{w=.5} I'm here to make things right for this place!{w=.5} I need your Courage!"

    g1 "AND{w=.25} you want to take,{w=.25} take,{w=.25} take,{w=.25} take from me more and more{cps=3}...?{w=.5}{/cps} You VILE machine,{w=.25} I don't want you in my sight!{w=.5} I hurt enough as is!"

    "Andonuts grabs a piece of the glass and throws it straight at Joke-Explainer,{w=.25} turning as it flies past her head.{w=.5} She turns back to see him picking up more debris."

    stop music

    play sound "mega_int.ogg"

    g1 """
    YOU WANT TO WRENCH THE COURAGE FROM ME? YOU WANT TO SLAY THE MONSTER? WHO FUCKING GAVE YOU THE POWER TO MAKE THESE CHOICES?{w=.1}{nw}
    
    I'M GOING TO TEAR YOUR SHITTY LITTLE BULBOUS EYES OUT{w=.1}{nw} 
    
    SO THAT THE LAST THING YOU EVER SEE IS YOUR PATHETIC GOD DAMN BODY{w=.1}{nw} 
    
    BEING DISASSEMBLED PIECE BY BITCHY PIECE{w=.1}{nw} 
    
    YOU WON'T TAKE AWAY WHAT I HAVE LEFT, I WON'T LET YOU BASTARDS HURT ME ANYMORE{w=.1}{nw}
    """

    "The shattered glass rises around him,{w=.25} fueled by the fear and desperation radiating from the doctor.{w=.5} Joke-Explainer can see his rotten face reflected over and over,{w=.25} all staring deep into her soul.{w=.5} She doesn't feel ready for this."

    g1 "tl;dr:{w=.25} eat glass,{w=.25} cunt"

    window hide

    show battle_trans at truecenter

    play sound "boss.flac"

    pause 2.5

    jump fight_1

label guilt_1_hurt:
    show screen hpbar

    play sound "prep.wav"

    "Andonuts (?) threw a glass shard!" 
    
    play sound "attack.wav"

    $ currenthp -= 1

    extend "\n1 HP of damage to Joke-Explainer!" with sshake


    if currenthp <= 0:
        jump gameover 
    else:
        hide screen hpbar
        return

label fight_1:
    $ renpy.save("fight_1")
    $ config.after_load_transition = None
    $ intflag = 1
    scene giygas
    $ renpy.transition(fade, layer="master")
    show guilt1 battle at battle
    pause 1
    cen "[[FIGHT START]"
    $ currenthp = 2
    $ maxhp = 2
    play music "tuesday.ogg" volume .5

    t "It seems like Joke-Explainer has gotten into a battle!{w=.5} Now, don't worry,{w=.25} she won't need any weapons for this fight.{w=.5} All she'll need is a sharp mind and good choices!"
    
    t "You must choose the correct option out of the ones given to convince the guilt.{w=.5} Choose wisely, and the fight will continue.{w=.5}{nw}" 

    show screen hpbar

    extend " But choose poorly,{w=.25} and she'll take damage!{w=.5} Take too much damage,{w=.25} and it's Game Over.{w=.5}{nw}" 

    hide screen hpbar

    extend " Good luck!"



label g1c1:
    menu:
        "What should Joke-Explainer say?"

        "Ask why he wants to hurt her.":
            je "I don't understand,{w=.25} why would you want to hurt me?"

            g1 "WHAT MAKES YOU THINK YOU'RE SO SPECIAL?{w=.5} A STUPID BITCH LIKE YOU WOULD NEVER UNDERSTAND"

            call guilt_1_hurt from _call_guilt_1_hurt

            jump g1c1

        "Press him on \"the hurt he's caused\"":
            je "Earlier you said you \"caused hurt\"?{w=.5} Could you elaborate on that?"

            g1 """
            Have you not heard the whispers of folk around you{cps=3}...?{w=.5}{/cps} They all say I'm a monster,{w=.25} it's all they talk about!{w=.5} Makes sense,{w=.25} I put all those kids in mortal danger!{w=.5} Including my own son!
            
            Could you imagine what might've happened if{cps=3}...{w=.5}{/cps} if they didn't come back?{w=.5} ...What kind of father does that to his own son?{w=.5} Just leaves him in a boarding school for most of his life,{w=.25} and only shows back up to nearly kill him?
            
            Why must I be BURDENED with this damned responsibility?!{w=.5} Why does everything have to be my fault?!{w=.5} It isn't fair!
            """

label g1c2:
    menu:
        "What should Joke-Explainer say?"
    
        "Give him the benefit of the doubt.":
            je """
            You know,{w=.25} I think I agree.{w=.5} It isn't fair.
            
            While it was bad of you to leave your son,{w=.25} I understand the dire circumstances that led you to feeling the need to make that choice.{w=.5} And if you hadn't sent those kids to the past,{w=.25} your entire world would've been fully consumed by evil!
            
            It's not helpful to dwell on what-ifs,{w=.25} but even if things did go wrong,{w=.25} that's no reason to give into any self-destructive thoughts.
            """

            g1 "You{w=.5} \nYou're actually{cps=3}...{w=.5}{/cps}{w=.5} \nHow do you"

            g1 "You shouldn't know these things{cps=3}...{w=.5}{/cps} You shouldn't SAY{w=.25} these things{cps=3}...{w=.5}{/cps}"

            g1 "Do you just pity me?{w=.5} Pity the pathetic old man writhing in PAIN?{w=.5} Nobody plays devil's advocate for a monster."

            g1 "All they see me as{w=.5} \nis a{w=.5} \nf{w=0.5}a{w=.1}{nw}"
            
            g1 "All they see me as \nis a {fast}{nw}"

            extend "\nMONSTER"
            
            g1 "They're all disgusted by me{cps=3}...{w=.5}{/cps} and for good reason!{w=.5} My wife knew the sins I carry with me.{w=.25} That I simply{cps=3}...{w=.5} {/cps}biologically, {w=.25}cannot love her.{w=.5} What I am is{cps=3}...{w=.5}{/cps} unforgivable."


        "Give him a wake-up call.":
            je "Feeling bad about those things is quite a normal response.{w=.5} It's okay to acknowledge your actions were wrong,{w=.25} as long as you can grow and change from those experiences."

            g1 "OH, WHAT A SURPRISE! I'M WRONG AGAIN!{w=.5} \nWANT ME TO OFFER MY HEAD ON A STICK,{w=.25} JUST FOR YOU?!{w=.5} fuckhead"

            call guilt_1_hurt from _call_guilt_1_hurt_1

            jump g1c2

label g1c3:
    menu:
        "What should Joke-Explainer say?"

        "Show solidarity with Andonuts.":
            je """
            You are not unforgivable,{w=.25} Doctor.{w=.5} In fact,{w=.25} there's nothing for you to be ashamed about.{w=.5} Those people really didn't care about you if they demonized you for being who you are{cps=3}...{w=.5}{/cps} It's alright! 
            
            And besides,{w=.25} it's not as though you're alone!{w=.5} If some people think you're bad for being gay,{w=.25} then I'm on your side{cps=3}...{w=.5}{/cps} Trust me,{w=.25} I understand.
            """

            g1 """
            You don't—{w=.5}Don't try to—{w=.5}You can't—{w=.5}How{cps=3}...{w=.5}{/cps}
            
            NO,{w=.25} NO,{w=.25} NO.{w=.5} Doesn't matter.{w=.5} Everyone will always see me as a freak no matter what I do.{w=.5} You do too much wrong and the world wants to throw you into a pit.
            """
            
        "Ask him why he was so afraid of this.":
            je "I don't understand,{w=.25} why are you so afraid of them knowing?{w=.5} There's nothing shameful to hide about that.{w=.5} Even if they disrespect you for it,{w=.25} they don't deserve your time."

            g1 "WOULD BE EASY FOR YOU TO SAY,{w=.25} WOULDN'T IT{w=.5} \nYOU'VE NEVER EXPERIENCED WHAT IT'S LIKE TO BE TETHERED TO SOMEBODY ELSE YOU COULDN'T LOVE{w=.5} \nHOW WOULD YOU FEEL IF THE PERSON CLOSEST TO YOU CALLED YOU A{w=.1}{nw}"

            call guilt_1_hurt from _call_guilt_1_hurt_2

            jump g1c3

label fight_1_end:
    stop music fadeout 2.0
    
    je """
    That is a false assumption.{w=.5} The world's not out to get you,{w=.25} Doctor{cps=3}...{w=.5}{/cps} There are good people abound,{w=.25} and you are one of them!{w=.5} 
    
    I cannot thank you enough for all the help you've given me since my creator vanished.{w=.5} You've also helped save your world a few times through your scientific ingenuity and compassion! 

    Don't let your faults and mistakes hold you down forever.{w=.5} You know that would only lead you down a path of destruction.
    """

    g1 "{cps=3}...{w=.5}{/cps}"

    cen "[[FIGHT END]"

    "Joke-Explainer thinks to herself for a moment."

    je "{cps=3}...{w=.5}{/cps}How about a hug,{w=.25} Doctor?"

    play music "<loop 12.28>courage.ogg"

    scene guilt1_hug_aura with fadeWithText

    "Joke-Explainer spreads out her arms and goes in for a hug,{w=.25} wrapping her tiny little arms around the doctor as best she can." 

    "Slowly,{w=.25} faltering at first,{w=.25} he eventually returns the gesture."
    
    scene guilt1_hug_noaura with fadeWithText

    "The red swirling madness disappears,{w=.25} and all the shards of floating glass gently drift back down to the floor."

    g1 "Thank you{cps=3}...{w=.5}{/cps} I will give you the courage you seek.{w=.5} Please,{w=.25} take care of him."

    scene aura with fadeWithText

    "The doctor's body begins to dissipate into the same smoky aura that once surrounded him,{w=.25} blowing away to reveal{nw}"
    
    scene joke_explainer_and_gay_jeff with fadeWithText

    extend " a young boy with circular glasses wearing a dapper teal suit." 
    
    stop music fadeout 2.0

    play sound "courage_collect.wav"

    "The boy looks to Joke-Explainer and nods with a gentle smile,{w=.25} before walking up and imbuing her with his strength."

    scene eblab_2 with fadeWithText

    play sound "friend.ogg"
    pause .9

    show screen stop_scr

    $ inventory.add_item(cour1)

    "You have obtained the FIRST COURAGE!{w=7}{nw}"

    hide screen stop_scr

label post_fight_1:
    play music "Lights_on.ogg"
    
    "All of a sudden,{w=.25} the air around Joke-Explainer seems to clear up,{w=.25} and the lights within the lab turn back on to illuminate the area.{w=.5} Comfort washes over her." 
    
    "She takes a moment to lie down on the ground –{w=.25} letting her body's joints return to their default positions.{w=.5} She tunes out her high-functioning sensors to rest{cps=3}...{w=.5}{/cps} and the radio buzzes again."

    $ persistent.radioflag = 3

    window hide

    if persistent.radioflag == 3:
        while persistent.radioflag == 3:
            pause 

label post_radio_2:
    $ persistent.radioflag = 4
    
    "Joke-Explainer quickly flips the radio on to hear Doctor Andonuts."

    play sound "radioon.mp3"

    play music "paula_og.ogg"

    je "Doctor Andonuts—{w=.1}{nw}"

    a "JOKE-EXPLAINER!{w=.5} TH-{w=.25}THANK GOODNESS,{w=.25} ARE YOU ALRIGHT?!"

    je "Yes,{w=.25} Doctor,{w=.25} my systems are currently operational,{w=.25} but—{w=.1}{nw}"

    a "Oh,{w=.25} oh thank god{cps=3}...{w=.5}{/cps} {i}{cps=10}Thank god{/cps}{cps=3}...{w=.5}{/i}{/cps} I-{w=.25}I thought that,{w=.25} that well,{w=.25} I was trying to guide you but at some point you cut out,{w=.25} a-{w=.25}and then I blacked out and had the most horrible nightmare!{w=.5} I'm so,{w=.25} so sorry{cps=3}...{w=.5}{/cps}"

    je "It's alright!{w=.5} Really,{w=.25} it is alright.{w=.5} I'm fine.{w=.5} In fact, I managed to receive the first Courage."

    a "You did?{w=.5} Oh,{w=.25} that's splendid news!"

    je "Yes,{w=.25} though the way in which I obtained it was{cps=3}...{w=.5}{/cps} odd."

    a "{cps=3}...{w=.5}{/cps}Odd?"

    je """When I lost contact with you,{w=.25} I found a house with a light radiating inside{cps=3}...{w=.5}{/cps} and when I entered,{w=.25} I was in a strange lab with many machines.
    
    There was{cps=3}...{w=.5}{/cps} a person inside of one of those machines.{w=.5} I had to fight him to calm him down and receive the Courage.
    """
    # Should the "they are" here be "they're?'"
    a """
    {cps=3}...{w=.5}{/cps}
    
    I{cps=3}...{w=.5}{/cps} I see{cps=3}...{w=.5}{/cps} That sounds quite foreboding.{w=.5} You'd best keep your guard up when searching for the other two Courages then,{w=.25} they are probably being guarded as well.
    """

    je """Understood.{w=.5} I'm going to go back out to find the next Courage.{w=.5} Do note the area I'm in has some sort of interference that blocks your signal from reaching the radio.{w=.5} So if you stop hearing me again,{w=.25} do not worry. 
    
    Unless it's been more than exactly 30 minutes since you last heard from me,{w=.25} then start worrying.
    """

    a "Oh,{w=.25} uh{cps=3}...{w=.5}{/cps} Uhm{cps=3}...{w=.5}{/cps} Alright,{w=.25} just—{w=.25}just stay safe.{w=.5} Please.{w=.5} I don't know what I would do if you got too hurt in there."

    je "Copy that!"

    stop music fadeout 2.0

    "Joke-Explainer shuts off the radio and takes one final moment to bask in the peacefulness of the lab before making her way back out into Anguish Avenue."


label guilt_2_leadup:
    play sound "Door Open 1.ogg"
    
    scene anguish_avenue_fog at truecenter with foggy_fade

    $ play_multiple("omen.ogg", "scary omen.ogg")

    "All at once the fog hits her again,{w=.25} significantly scrambling her senses.{w=.5} Nevertheless,{w=.25} she continues to trek on,{w=.25} keeping a watchful eye of the houses around her to note any possible glimmers of the next Courage."

    window hide

    pause 2

    window show

    """
    She's been traveling down this road for a while.{w=.5} Adjusting her optical focus to track every new house is getting harder and harder.{w=.5} The road starts to twist ever so slightly.{w=.5} ...or is it a product of her imagination?
    
    The ground distorts in her eyes.{w=.5} The houses start to melt,{w=.25} rippling,{w=.25} like a mirage in the desert.{w=.5} She can barely keep track of her feet,{w=.25} but she can't lose track of herself entirely.
    
    She needs to rest at the lab.{w=.5} She can't keep going.{w=.5} But when she turns around,{w=.25} the fog has enveloped behind her like a wall,{w=.25} refusing access.
    
    She sticks out her hand to make sure,{w=.25} but quickly reels it back in shock as a{nw}
    """ 
    extend " horrible stinging pulse begins to creep up her entire arm.{w=.5} Whatever this fog wall is made of,{w=.25} she's better off not trying to run through it." with sshake

    """
    As she stares at the fog,{w=.25} the radio suddenly blares to life again.{w=.5} She nearly jumps in alarm upon hearing its static roar,{w=.25} and notices some sort of indiscernible voice coming from its speakers.
    
    Quickly pulling it out and tuning it,{w=.25} she hears the unmistakable voice of Doctor Andonuts on the other side.
    """

    play sound "radioon.mp3"

    a "Joke-Explainer,{w=.25} do you hear me?"

    je "Doctor?{w=.5} How are you{cps=3}...?{w=.5}{/cps} Was it because I touched the fog?"

    a "{cps=3}...{w=.5}{/cps}Yes.{w=.5} You have opened a clear spot where I can comunicate with you.{w=.5} Please allow me to guide you to the next Courage."

    je "Of course!"

    "Joke-Explainer holds onto the radio as the voice of the Doctor directs her."

    a "Across the road are telephone poles,{w=.25} can you see them?"

    scene pole with fadeWithText

    "Joke-Explainer looks up to see a line of wooden poles materialize from the fog.{w=.5} The wires strung across them extend well beyond her field of vision."

    je "Yes,{w=.25} but – it's difficult to look up for too long.{w=.5} The entire area feels{cps=3}...{w=.5}{/cps} nauseating to me."

    a "You must follow them,{w=.25} even if you begin to feel sickly.{w=.5} The wires will lead you to the location of the next house.{w=.5} Do not let them out of your sight,{w=.25} or else you will get lost and fail to complete your directive."

    window show

    $ update_layers("music_b", 2)

    scene pole:
        linear 3 blur 10
        pause 2.0
        linear 3 blur 0
        pause 2.0
        repeat
    $ renpy.transition(None, layer="master")

    show vig at truecenter
    $ renpy.transition(long_dissolve, layer="master")
    "Joke-Explainer follows the poles down the endless street.{w=.5} While initially determined,{w=.25} the warping road begins to weaken her resolve,{w=.25} the dizzying nausea gradually seeping into her.{w=.5} She struggles to discern what's real anymore,{w=.25} part of her wondering if every step she took would even be on solid ground."

    je "Doc{cps=3}...{w=.5}{/cps}tor,{w=.25} I{cps=3}...{w=.5}{/cps} I feel sick.{w=.5} May I take a moment to rest?"

    a "No."
    
    a "You are close to the next Courage.{w=.5} Do not stop."

    je "It feels like the road I'm walking on is{cps=3}...{w=.5}{/cps}"

    a "It is in your head.{w=.5} Absolve yourself of your feelings and proceed."

    """
    Joke-Explainer feels a twinge of confusion in her head as she continues on.{w=.5} Her eyes struggle to stay open,{w=.25} and she starts to hear an all too familiar buzz ring within her.{w=.5} The warmth of the first Courage helps to keep her awake,{w=.25} but it isn't enough to fully suppress the madness threatening her mind.

    Madness{cps=3}...{w=.5}{/cps} What even is madness to her,{w=.25} a machine?{w=.5} How could a machine go mad?{w=.5} They don't think like an organic being does.{w=.5} They're tougher than that,{w=.25} they're better than that.
    """

    a "A machine goes mad when they don't have a directive to follow.{w=.5} Stick to yours."

    """
    Did{cps=3}...{w=.5}{/cps} Did she say that out loud??{w=.5} She could've sworn she was only thinking that{cps=3}...{w=.5}{/cps} But why would she think that in the first place?{w=.5} She knows she can feel just the same as all of the Figments and humans she talks to.
    
    At least,{w=.25} she thinks so{cps=3}...{w=.5}{/cps} it's becoming harder to tell the more she follows the telephone poles.{w=.5} They're vague strings to her now,{w=.25} strings for her to follow and pull to unravel the agonizing madness around her.{w=.5} She reaches her free arm out lazily towards the poles to try and grab them.
    """

    a "Stop.{w=.5} You're wasting energy doing that.{w=.5} Just keep walking."

    je "Doctor,{w=.25} I think this—{w=.5}this whole thing is{cps=3}...{w=.5}{/cps} jeopardizing the integrity of my systems.{w=.5} I must take a break."

    a "Robots don't take breaks.{w=.5} The house is right there,{w=.25} to your right."

    scene door1 with fadeWithText

    $ stop_layers()

    "Joke-Explainer freezes.{w=.5} The sudden coldness of the doctor shocks her back to reality,{w=.25} reminding her of the way the disheveled cognitive Andonuts behaved towards her.{w=.5} She blinks a few times to try and get a grip on her surroundings."

    a "Why did you quit moving?{w=.5} You are at your destination.{w=.5} Go do your task."

    "Joke-Explainer finally notices just how monotone the doctor's voice sounds through the radio.{w=.5} Like a distorted recording of his voice,{w=.25} being played back to her.{w=.5} She turns to the right to see the wires spilling into the front door of one of the houses,{w=.25} and slowly steps towards its front lawn."

    a "Go take the next Courage.{w=.5} Now.{w=.5} It awaits you through that door."

    play music "<loop 24.36>showdown.ogg"

    """
    Joke-Explainer takes one step forward,{w=.25} but stops herself again.{w=.5} Something about this feels horribly off.{w=.5} Doctor Andonuts's cold voice continues to ring from the radio,{w=.25} eating away at her psyche.{w=.5} Threatening to take away her coherent thought altogether.
    
    She doesn't trust the door.
    
    Trust the door.{w=.1}{nw}
    
    DON'T trust the door.{w=.5} It beckons her inside{cps=3}...{w=.5}{/cps} with the voice of the hollowed doctor.{w=.5} This isn't him.{w=.5} It can't be.
    
    This is a trap,{w=.25} no she can't go in{w=.1}{nw}
    
    But she has to{w=.1}{nw}
    
    BUT SHE CAN'T SHE CAN'T TRUST IT{w=.1}{nw}
    
    but it's her directive.{w=.5} Her directive.
    """

    a "Your directive is to go into the house and retrieve the Courage from the—{w=.1}{nw}"

    play sound "Radio hits door.ogg"

    stop music

    scene door2 at truecenter with sshake

    "Joke-Explainer throws the radio at the door with all her might,{w=.25} desperate to get that horrible voice away from her.{w=.5}{nw}"

    $ inventory.remove_item("Radio")
    
    scene door3 with fadeWithText

    play sound "Door creak chimera.ogg"

    extend " It crashes into the wood,{w=.25} causing the door to creak open a little bit{cps=3}...{w=.1}{/cps}{nw}"

    window hide

    if (renpy.music.is_playing("sound")):
        while (renpy.music.is_playing("sound")):
            pause 1
    
    play sound "UC Sound 1.ogg"

    if (renpy.music.is_playing("sound")):
        while (renpy.music.is_playing("sound")):
            pause 1

    play sound "UC Roar.ogg"

    play sound_2 "doorbreak2.ogg"

    scene door4 at truecenter with flash
    
    play music "showdown_2.ogg"

    scene door4 at truecenter with sshake

    pause 1.5

    window show

    """
    WITHOUT WARNING,{w=.25} A HUGE BEAST LUNGES AT HER! 
    
    It bolts through the doorway,{w=.25} sending the door flying off its hinges!{w=.5} Joke-Explainer screams in alarm and falls over from disorientation,{w=.25} desperate to get away!{w=.5} The beast dashes across the lawn ready to chew her face off—!{w=.25}{nw}
    """

    scene black

    play sound "Metal chain stop.ogg"

    stop music

    "Right as Joke-Explainer flinches,{w=.25} prepared for the beast's fangs to dig into her,{w=.25} she hears it yelp and whimper pathetically."

    scene lungefail with fadeWithText
    
    play music "chimera_struggles.ogg"

    "She opens her eyes and sees the beast is tied to a thick chain leading from within the house –{w=.25} a chain that isn't quite long enough to reach her.{w=.5} Here,{w=.25} she's able to notice the beast being made of metal,{w=.25} a robotic replica of sorts."

    scene door5 with fadeWithText

    play music "AnnoyedBuzzingLoop.ogg"

    play sound "Chain dragging.ogg"

    "It tries a few more times to reach her before giving up and slinking back into the house.{w=.5} As it turned the corner behind the doorway,{w=.25}{nw}"

    extend" Joke-Explainer swears she heard an annoyed electronic buzzing coming from inside."
    
    "After taking some moments to calm down,{w=.25} she stands back up and takes another look at the house.{w=.5} Though there's still a distorted melting look to it,{w=.25} she can discern its features once again.{w=.5} A similar glimmer emanates from within it,{w=.25} just like the house where she retrieved the first Courage."
    
    "Just have to find another way inside that hasn't been booby-trapped,{w=.25} then{cps=3}...{w=.5}{/cps}"

    """
    Joke-Explainer walks around towards the back of the house,{w=.25} making sure to keep enough distance so that if the metallic beast returns,{w=.25} it won't be able to reach her.{w=.5} 
    
    Once on the other side,{w=.25} she spots a backdoor that seems to be untouched.{w=.5} Going up to it she finds that it's locked,{w=.25} but thankfully she has enough strength to break the lock and pull it open.{w=.5} She then enters the house,{w=.25} ready to face whatever thing awaits her.
    """

    stop music

    play sound "Door Open 1.ogg" 

    scene m3lab with slow_fade

    play sound "door-slam.ogg"

    play music "porky.ogg"

    """
    The blank walls of an operating room face back at her.
    
    The cold,{w=.25} sterile environment has the correct tools and mechanisms designed for such a task,{w=.25} if not a bit{cps=3}...{w=.5}{/cps} deadlier.{w=.5} Last time she checked,{w=.25} giant mechanical buzzsaws weren't standard hospital equipment.
    
    The room isn't quite as clean as it ought to be –{w=.25} tools are strewn about all over the tables,{w=.25} and mangled bits of robot parts line the walls,{w=.25} staining the floors with oil.{w=.5} Or at least{cps=3}...{w=.5}{/cps}she sure hopes that's oil,{w=.25} anyway.

    And in the very center of the room,{w=.25} on the operating table,{w=.25} excessively bound by its restraints{cps=3}...{w=.5}{/cps} a mutilated young boy in a striped shirt and orange hair,{w=.25} his eyes hollowed out.{w=.5} Many parts of his body seem to be missing,{w=.25} while just as many others have been replaced with the beginnings of robotic \"enhancements\".
    """

    show guilt2 at cccenter, silhoette with fadeWithText

    g2 "Let us get straight to the point,{w=.25} robot."
    
    "Out of the corner of her eye,{w=.25} a figure emerges out of the shadows.{w=.5}{nw}"
    
    show guilt2 at cccenter, unsilhoette with fadeWithText

    extend " It's Doctor Andonuts{cps=3}...{w=.5}{/cps} but his skin is sallowed,{w=.25} almost rotting.{w=.5} His eyes are devoid of life,{w=.25} as is his movement – the cybernetic attachments engulfing his body pull him along his path like a puppet on strings."
    
    "The doctor walks past the boy on the operating table –{w=.25} an incomplete form of himself."

    g2 """
    I am the second Guilt guarding one of the Courages.{w=.5} If you wish to receive it,{w=.25} you must defeat me.
    
    But you cannot,{w=.25} because I am the perfect being,{w=.25} the flesh of man and the metal of machine,{w=.25} unfettered by the filth of the emotions plaguing humanity.{w=.5} I am innovation taken to its highest degree.
    
    You are faulty{cps=3}...{w=.5}{/cps} a robot that has lost order.{w=.5} Please allow me to correct you.
    """

    stop music

    window hide

    show battle_trans at truecenter

    play sound "boss.flac"

    pause 2.5

    jump fight_2


label guilt_2_hurt:
    show screen hpbar

    play sound "prep.wav"

    "Andonuts (??) activates a buzzsaw!" 
    
    play sound "attack.wav"

    $ currenthp -= 1

    extend "\n1 HP of damage to Joke-Explainer!" with sshake

    if currenthp <= 0:
        jump gameover 
    else:
        hide screen hpbar
        return



label fight_2:
    $ renpy.save("fight_2")
    $ config.after_load_transition = None
    $ intflag = 2
    scene masked_bg at two_size
    $ renpy.transition(fade, layer="master")
    show guilt2 battle at battle
    pause 1
    cen "[[FIGHT START]" # Should maybe have a sound effect?
    $ currenthp = 2
    $ maxhp = 2
    play music "guilt2.ogg" volume .5

label g2c1:
    menu:
        "What should Joke-Explainer say?"

        "Ask to elaborate on him being the \"perfect being\"":
            je "You say you're \"The Perfect Being\"?{w=.5}  Could you go into any details about why that's the case?"

            g2 "I was created to be a tool,{w=.25} a being with the purpose of serving a master.{w=.5} I was always meant to be molded into a retainer.{w=.5} No matter when or where,{w=.25} I am intended to assist in causing mass destruction.{w=.5} That is who I am,{w=.25} and always will be.{w=.5} I am a perfect,{w=.25} obedient machine.{w=.5} Does this fulfill your inquiry?"

        "Question what is so different about them robotically":
            je "If we're both at least partially robotic,{w=.25} what makes you superior?"

            g2 "Your failure to comprehend tells more than my words ever could."

            call guilt_2_hurt from _call_guilt_2_hurt

            jump g2c1




label g2c2:
    menu:
        "What should Joke-Explainer say?"

        "Ask how he feels about the suffering he's caused":
            je "Is this really who you want to continue being?{w=.5} How do you feel about the anguish you've put onto others?"

            g2 "Are you truly this dense?{w=.5} How many times must I say it?{w=.5} I feel nothing."

            call guilt_2_hurt from _call_guilt_2_hurt_1

            jump g2c2

        "Question why he always feels the need to serve":
            je "May I ask why you continue to obey these \"masters\" you speak of?"

            g2 """
            Everytime I find myself in a far-off world,{w=.25} I make myself useful.
            
            Porky needed me to create chimeras for him,{w=.25} so I obliged.{w=.5} The Voice needed me to create mechs and document research for him,{w=.25} so I obliged.
            
            As long as I keep my head up high,{w=.25} I'll never have to look down and—{w=.1}{nw}
            """
            
            g2 "Nevermind."

label g2c3:
    menu:
        "What should Joke-Explainer say?"

        "Push him to continue what he was going to say":
            je "Nevermind?{w=.5} I am interested in hearing what you were going to say,{w=.25} I don't mind listening."

            g2 "I will no longer engage with you."

            call guilt_2_hurt from _call_guilt_2_hurt_2

        "Motivate Andonuts to stand up for himself":
            je "You can't possibly be happy in this situation.{w=.5} Nothing will change for you unless you stand up for yourself Doctor,{w=.25} you'll never know until you try!"

            g2 "I will no longer engage with you."

            call guilt_2_hurt from _call_guilt_2_hurt_3
    
    g2 "You continue to attempt to reason with a part of me that does not exist.{w=.5} What is your motive?"

label g2c4:
    menu:
        "What should Joke-Explainer say?"

        "To get the Courage":
            je "My motive is to get the Courage and capture whatever is attacking Doctor Andonuts' mind!"

            g2 "You think I didn't know that?{w=.5} Your persistent lack of awareness is astounding.{w=.5} Goodbye."

            call guilt_2_hurt from _call_guilt_2_hurt_4

            jump g2c4

        "To ease Doctor Andounts' mind":
            je "My motive is to ease your mind,{w=.25} Doctor Andonuts.{w=.5} You can't stow away everything forever,{w=.25} it will only hurt you in the long-term.{w=.5} Those above you do not control you."

            g2 "To be a perfect man is to feel nothing,{w=.25} if I had emotion then I would unnecessarily hurt—{w=.1}{nw}"

            je """
            Feeling hurt is part of what it means to be alive!{w=.5} You think you are controlled by the whims of authorities above you,{w=.25} but you're so much more than that!
            
            You've been forced to work under others,{w=.25} but you have also gone behind their backs to sabotage them!{w=.5} You're not as weak and helpless as they've told you you are.
            """

label fight_2_end:
    stop music fadeout 2.0

    "The robotic doctor freezes in his tracks.{w=.5} Joke-Explainer can see his mechanical eyes darting back and forth,{w=.25} evaluating the assumptions he had made about his stage of being.{w=.5} It's clear that Joke-Explainer struck a deep chord."

    cen "[[FIGHT END]"

    scene m3lab with fade

    show guilt2 at cccenter
    $ renpy.transition(dissolve, layer="master")

    "As he struggles to rationalize a way out,{w=.25} Joke-Explainer slowly approaches the doctor and holds out her hand as a peace offering.{w=.5} Andonuts dips his head down and lets out a notably tired sigh.{w=.5} He stares deep into her,{w=.25} before letting his stance relax."

    play music "<loop 12.28>courage.ogg"

    g2 "You{cps=3}...{w=.5}{/cps} I may have{cps=3}...{w=.5}{/cps} miscalculated,{w=.25} in regards to how faulty you are.{w=.5} My apologies,{w=.25} robot.{w=.5} I pray you learn to forgive me.{w=.5} I've gone too far out of line{cps=3}...{/cps}"

    scene guilt2_hug with fadeWithText

    "Doctor Andonuts is suddenly interrupted by Joke-Explainer going up and giving him a hug.{w=.5} His eyes widen in surprise,{w=.25} before looking off to the side nervously.{w=.5} He doesn't really know what to do here{cps=3}...{w=.5}{/cps}{nw}"
    
    scene guilt2_pat

    extend " so he just gives the smol robot an awkward pat on the head.{w=.5} Eventually Joke-Explainer lets go and gives a nod."

    scene m3lab with fadeWithText

    show guilt2 at cccenter
    $ renpy.transition(dissolve, layer="master")

    je "It's alright!{w=.5} I'm just happy you've calmed down,{w=.25} Doctor."

    g2 """
    {cps=3}...{w=.5}{/cps}Thank you.

    I wish you well in your quest.{w=.5} Please allow me to gift you the second Courage for your troubles.{w=.5} {cps=3}...{w=.5}{/cps}Keep him safe.
    """

    "Andonuts steps back and gives one last sigh before{nw}"
    
    show guilt2 at cccenter, powerdown with fadeWithText

    extend " powering down.{w=.5} Joke-Explainer looks at him puzzled for a moment,{w=.25} before she hears the presence of someone else right behind her." 

    scene courage2appears with fadeWithText

    "It looks to be another young boy,{w=.25} this time with tall blonde hair and a similar striped shirt.{w=.5} The boy has a striking resemblance to the boy who was on the table."
    
    stop music fadeout 2.0

    "The first Courage emanates outside of Joke-Explainer,{w=.25} and smiles at the boy.{w=.5}{nw}"
    
    play sound "courage_collect.wav"

    extend " The 2 courages then proceed to give each other a handshake before returning to Joke-Explainer."
    
    scene m3lab_nice with dissolve

    play sound "friend.ogg"
    pause .9

    show screen stop_scr

    $ inventory.add_item(cour2)

    "You have obtained the SECOND COURAGE!{w=7}{nw}"

    hide screen stop_scr

label post_fight_2:
    
    hide guilt2 
    
    """
    Joke-Explainer looks towards where the mechanical Andonuts was moments ago,{w=.25} but to her shock all that's there is the remains of a faceless machine laying on the floor.{w=.5} She glances around to see if he'd been moved somewhere else,{w=.25} yet nothing around really stands out to her.
    
    Nothing{cps=3}...{w=.5}{/cps} except a shiny radio buzzing on a table at the other side of the room.{w=.5} She nervously walks over to pick it up again and turn it on{cps=3}...{/cps}
    """

    $ inventory.add_item(radio, slot=0)
    
    $ persistent.radioflag = 5

    window hide

    if persistent.radioflag == 5:
        while persistent.radioflag == 5:
            pause 


label post_radio_3:
    $ persistent.radioflag = 6

    "Joke-Explainer turns the radio on with a tense expression."

    "The radio blares to life once again,{w=.25} which makes Joke-Explainer flinch for a few moments.{w=.5} She lets up however when she hears the NORMAL voice of Doctor Andonuts on the other side."

    play sound "radioon.mp3"

    play music "paula_og.ogg"

    a "Hello??{w=.5} Helloooooooooooo?{w=.5} Is anybody there?!"

    je "Doctor{cps=3}...{/cps}"

    a "JOKE-EXPLAINER!{w=.5} Oh whew,{w=.25} I got so nervous when I heard a horrible sound on the radio earlier{cps=3}...{w=.5}{/cps} it sounded like someone smashed it into a wall!"

    je "Yes{cps=3}...{w=.5}{/cps} it—{w=.1}{nw}"

    a "Oh,{w=.25} no matter,{w=.25} you're back and that's all that matters.{w=.5} I'm terribly sorry I keep having these awful black outs{cps=3}...{w=.5}{/cps} I think I should've rearranged these needles slightly before skewering my head with them,{w=.25} ahahaha{cps=3}...{/cps}"

    je """
    It's alright,{w=.25} just{cps=3}...{/cps}
    
    Doctor Andonuts,{w=.25} can I be honest?{w=.5} I need to tell you something I've neglected to mention up until this point.
    """

    a "Well of course!{w=.5} Though your tone of voice sounds very worrying,{w=.25} dear{cps=3}...{/cps}"

    je """
    I{cps=3}...{/cps}
    
    I have received the second Courage.
    """

    a "Oh,{w=.25} that's wonderful news!{w=.5} Just one more and then you can escape my infernal—{w=.1}{nw}"

    stop music fadeout 2.0

    je "Please,{w=.25} Doctor,{w=.25} I'm not finished."

    a "{cps=3}...?{/cps}"

    play music "blue.ogg"

    je """
    Upon receiving the second Courage,{w=.25} I realized a pattern with the obstacles I've had to face thus far to get them,{w=.25} which I assume will be repeated a third time for the last Courage.

    Both Courages were guarded by a present threat,{w=.25} the{cps=3}...{w=.5}{/cps} \"Guilt\",{w=.25} or the bad thing that the Mr. Dee character referred to.
    """

    a "Oh dear{cps=3}...{w=.5}{/cps} I hope they weren't too much trouble for you{cps=3}...{/cps}"

    je "I survived both encounters and{cps=3}...{w=.5}{/cps} got by well enough.{w=.5} However,{w=.25} both of these Guilts{cps=3}...{w=.5}{/cps} they both took the form of you,{w=.25} Doctor."

    "Joke-Explainer waits for Andonuts's response,{w=.25} but she can't hear anything discernable beyond the quiet static.{w=.5} After a few moments of waiting,{w=.25} she continues."

    je "The first Guilt was a you that was bitter,{w=.25} afraid,{w=.25} and cruel{cps=3}...{w=.5}{/cps} The second Guilt was a you that was cold,{w=.25} robotic,{w=.25} and stoic.{w=.5} Both of them seemed upset to see me,{w=.25} and did not want to give up the Courage they were guarding.{w=.5} I had to talk to them and appeal to their humanity to get them to calm down and stop attacking."

    stop music fadeout 2.0

    a "{i}{cps=3}...{w=.5}NO...{/cps}{/i}"

    je "Doctor?{w=.5} Is everything alright?"

    a "I thought it was a nightmare{cps=3}...{/cps}"

    play music "evilasfuck.ogg"

    a "Joke-Explainer{cps=3}...{w=.5}{/cps} I'm so sorry for the torment I've put you through thus far.{w=.5} You,{w=.25} y-you shouldn't be here fighting against my mistakes.{w=.5} I should take you out—{w=.1}{nw}"

    je "You gave me a mission,{w=.25} Doctor Andonuts.{w=.5} I have 2 of the 3 Courages in my grasp now,{w=.25} and the third will be in my sight shortly."

    a "But it wasn't supposed to be this difficult!{w=.5} I never wanted to put you in danger,{w=.25} I-I never wanted to hurt you!"

    "Joke-Explainer ignores the doctor's pleas and exits the house back onto Anguish Avenue.{w=.5}{nw}" 
    
    window show
    
    play sound "Door Open 1.ogg" 

    scene anguish_avenue_fog at truecenter with foggy_fade

    play sound "door-slam.ogg"

    "The fog is noticeably thinner now,{w=.25} enough that the radio is still able to work{cps=3}...{w=.5}{/cps} much to Joke-Explainer's current dismay.{w=.5} She starts making her way down the road."

    a "WHAT ARE YOU DOING??{w=.5} Get back into that house NOW!"

    je "The third Courage might be ahead."

    a "I CAN'T PUT YOU IN JEOPARDY FOR MY OWN SELFISH SAKE!{w=.5} PLEASE,{w=.25} T-turn back!{w=.5} Turn back and I'll get you out of here!"

    je "If you take me out now,{w=.25} you will instead be jeopardizing yourself,{w=.25} Doctor.{w=.5} I can't have your mind destroyed by the foreign entity."

    "Joke-Explainer can hear Andonuts give out an exhausted groan on the other side.{w=.5} She attempts to continue on the path to the next Courage,{w=.25} and in the distance can faintly make out a large shadow that sticks out to her like a sore thumb.{w=.5} Though as she continues further down the path,{w=.25} everything starts to darken around her."

    a "Please{cps=3}...{w=.5}{/cps} I-I can't bear to see you destroyed again because of me{cps=3}...{w=.5}{/cps} I can't put you through that again{cps=3}...{/cps}!"

    je "That wasn't your fault.{w=.5} It was well beyond your control—{w=.1}{nw}"

    a "I LET HER GO INTO THAT BLASTED WORLD!!{w=.5} I DIDN'T STOP HER,{w=.25} I DIDN'T DO ANYTHING TO SAVE HER!{w=.5} TO SAVE {b}YOU!{/b}{w=.5} I LET HER GO UNTIL I NEVER SAW HER AGAIN!{w=.5} AND I CAN'T LET THE SAME HAPPEN TO YOU,{w=.25} NOT AGAIN!"

    "Joke-Explainer can finally see it.{w=.5}{nw}"
    
    scene anguish_avenue_shadows with fadeWithText:
        xalign 0.0
        linear 20 xalign 1.0

    extend " The eyes that have been staring her down this entire time.{w=.5} They all surround her,{w=.25} glowing a striking magenta against the dark misty fog.{w=.5} They stare.{w=.5} Stare into her SOUL.{w=.5} Judging her for her actions,{w=.25} for continuing to fight against the doctor's commands."

    je "Either you guarantee yourself to be destroyed by the weight of your guilt fueled by that entity,{w=.25} or I take a chance on a happy conclusion for both of us."

    a "I'd rather have myself crash and BURN if it meant keeping you safe!"

    "The stress of her arguing and the eyes beating down at her makes her clench the radio tighter.{w=.5} She looks right at it as she shouts back at him."

    je """
    And that is your problem!{w=.5} I don't need you to watch over me as if I'm a child!{w=.5} What happened to the Joke-Explainer replica was undoubtedly not your doing,{w=.25} and I wish you would stop blaming yourself for that!

    I continue to do all of this because I care about you,{w=.25} Doctor Andonuts!{w=.5} And I don't want to see you suffer under the thumb of something you can't fix on your own!
    """

    """
    She takes a moment to pause and her eyes dart upward.{w=.5} She sees that the distant shadow has grown into an absolutely gargantuan tower made out of houses haphazardly stitched together.{w=.5} If this were the real world,{w=.25} there's no way that thing could stand...
    
    The eyes continue to swarm.{w=.5} In the back of her mind,{w=.25} she can sense the searing hatred radiating off of them.{w=.5} She does her best to not focus on them,{w=.25} to not give them any attention or time of day.{w=.5} She won't let them distract her from her mission.
    """

    stop music fadeout 2.0

    a """
    {cps=3}...{w=.5}{/cps}Ohhhh{cps=3}...{/cps}

    I can't convince you to turn around and give up now,{w=.25} can I{cps=3}...{/cps}
    """

    je "Nope."

    a """
    I was{cps=3}...{w=.5}{/cps} afraid you'd say that.
    
    Alright{cps=3}...{w=.5}{/cps} If I can't make you leave,{w=.25} then I can at the very least try my best to lead you to the last Courage.
    
    Just{cps=3}...{w=.5}{/cps} I won't be able to control what happens in there when you go to face the last{cps=3}...{w=.5}{/cps} {i}me{/i}{cps=3}...{w=.5}{/cps} so please,{w=.25} whatever I end up doing in there,{w=.25} try not to hold it against me too much.
    """

    je "I never did,{w=.25} Doctor."

    "Joke-Explainer can hear what sounds like Andonuts laughing to himself.{w=.5} She can't tell if it's from nervousness or relief."

    a """
    Ohh,{w=.25} I don't deserve your kindness{cps=3}...{w=.5}{/cps}
    
    Okay.{w=.5} Okay,{w=.25} let's{cps=3}...{w=.5}{/cps} let's go get that courage and save my mind then.{w=.5} It's up in that tower.
    """

    je "Affirmative!"

label giult_3_leadup:
    play music "omen.ogg"

    "She dashes forward towards the base of the tower.{w=.5} It's a little hard to see with the eyes looking into her,{w=.25} but she won't let them get in her way.{w=.5} She's determined to get the final courage and save Andonuts!"
    
    scene anguish_avenue_house_tower with fadeWithText

    "Once she finally makes her way to the stack of houses,{w=.25} the eyes suddenly dissipate.{w=.5} They scatter away like scared animals,{w=.25} not daring to get close to the tower.{w=.5} She considers that quite foreboding."

    a "I can sense the Courage up towards the top{cps=3}...{w=.5}{/cps} along with something else.{w=.5} It's hard to tell what,{w=.25} though."

    je "How do I get up there?{w=.5} Should I fly?"

    a "{cps=3}...{w=.5}{/cps}No,{w=.25} the weather is too unstable.{w=.5} I believe there's an elevator nearby that you can use to ride up.{w=.5} To your left."

    "Joke-Explainer turns to her left and inspects the area around the base.{w=.5} Eventually she discovers a pair of rusted doors and a nearby button.{w=.5} She presses it,{w=.25} and waits for the elevator to arrive."

    play sound "elevator creepy.ogg"

    "When it finally does,{w=.25} a pathetic dinging noise chirps from within as the doors slowly creak open to reveal a slimy decrepit little chamber.{w=.5}{nw}"
    
    window show

    scene elevator_lights at truecenter with fadeWithText

    extend " The tiles on the wall look slightly peeled off,{w=.25} revealing the old crusty glue and shoddy brick craftsmanship underneath." 
    
    "She takes a small,{w=.25} creaky step onto the wooden floor inside,{w=.25} but falls back fearfully after feeling it{nw}" 
    
    play sound "elevator_floorcreak.wav"

    extend " shake under her weight." with sshake

    je "Are{cps=3}...{w=.5}{/cps} are you sure about this one?{w=.5} Is there not another way up?"

    a "I can't sense another way.{w=.5} Don't worry,{w=.25} elevators are always much safer than they feel like!{w=.5} As long as you don't jump up and down a bunch or anything,{w=.25} it should easily be able to carry you upward."

    je "Okay{cps=3}...{w=.5}{/cps} if you insist."

    "Joke-Explainer carefully steps into the elevator.{w=.5} After taking in her surroundings,{w=.25} she turns around to face the buttons on the wall.{w=.5} There's{cps=3}...{w=.5}{/cps} a whole lot of them.{w=.5} 8,743 to be exact."

    je "Which one do I press?"

    a """
    Oh god{cps=3}...{w=.5}{/cps} uh{cps=3}...{w=.5}{/cps} d-darn,{w=.25} give me a moment to think{cps=3}...{w=.5}{/cps}

    Okay,{w=.25} I believe it's{cps=3}...{w=.5}{/cps} this button!
    """

    stop music fadeout 2.0

    window show
    scene elevator_lights_button at truecenter
    $ renpy.transition(None, layer="master")    

    play sound "button light.ogg"

    "Joke-Explainer sees the 2,542nd button light up a distinct purple as he speaks."

    play music "elevatorloop.ogg"

    "All of a sudden,{w=.25} the whole room begins to{nw}" 

    play sound "elevator smaller shake.wav"
    
    extend " shake as it rises through the tower.{w=.5}\nJoke-Explainer anxiously clutches the radio." with sshake

    a "Look.{w=.5} I know you're nervous.{w=.5} And there isn't really much I can do to help you once we get up to the top.{w=.5} I don't even know how much time I have left before I black out again{cps=3}...{w=.5}{/cps} But you've managed to get the first two Courages all on your own."

    je "I know{cps=3}...{w=.5}{/cps} There isn't anything for me to fear.{w=.5} I'll be alright,{w=.25} Doctor."

    a "Yes but—{w=.25}Just{cps=3}...{w=.5}{/cps} Don't let whatever it says get to you.{w=.5} Like you've said before,{w=.25} you know where the Courage is,{w=.25} so it's only a matter of time before you—{w=.25}{nw}"

    "The radio shuts off."

    je "{cps=3}...{w=.5}{/cps}Doctor?{w=.5} Doctor Andonuts?{w=.5} Hello?"

    scene elevator_flicker at truecenter
    $ renpy.transition(None, layer="master")

    play sound "light flick.ogg"

    "The light flickers above Joke-Explainer{cps=3}...{w=.5}{/cps} She glances up to see it struggle to stay on,{w=.25}{nw}"
    
    scene elevator_button at truecenter
    $ renpy.transition(None, layer="master")

    stop sound

    extend " before losing strength and being unable to illuminate the space anymore." 
    
    "She stands rigid in the dark; the only things helping her see being her own eyes and antenna,{w=.25} and the lone glowing purple button.{w=.5} Almost instinctively,{w=.25} she starts her boosters—no,{w=.25} that'd set the floor ablaze."

    "Nothing else to do,{w=.25} I guess{cps=3}...{w=.5}{/cps}"

    "She stares at the button like a moth to a flame,{w=.25} desperately hoping the light above will turn back on soon."

    window hide

    pause 2.0

    window show

    "After what feels like an eternity waiting,{w=.25} feeling the elevator slowly{nw}"

    play sound "elevator smaller shake.wav"

    extend " rumble beneath her,{w=.25} she starts to worry.{w=.5} She's more than worried,{w=.25} she's panicked.{w=.5} Oh god.{w=.5} She makes her way close to the light as carefully as she can,{w=.25} trying her best not to shake the elevator." with sshake

    "She steps on a tile and it scoots lightly,{w=.25} causing her to fall over and drop the radio with a shriek.{w=.5} It causes the elevator to rattle{nw}"

    $ inventory.remove_item("Radio")
    
    play sound "elevator shake.ogg"

    extend " VIOLENTLY{cps=3}...{w=.5}{/cps} but nothing breaks."  with sshake
    
    "She slowly sits up,{w=.25} quivering with an unnatural amount of fear about this stupid rickety elevator she's stuck inside of.{w=.5} Getting a bearing on her surroundings,{w=.25} she clutches at the radio{cps=3}...{w=.5}{/cps}"

    $ renpy.music.set_volume(0,0,channel="music")

    "Only to find it isn't there anymore."

    $ renpy.music.set_volume(1,0,channel="music")

    "Joke-Explainer immediately stands back up to try and find it,{w=.25} but the darkness is too omnipresent.{w=.5} She can't see anything.{w=.5} She scrambles to look for it while also simultaneously not falling over again and rocking the elevator." 
    
    "The only thing she can see is the one button{cps=3}...{w=.5}{/cps} The one button isn't enough for her to see anything.{w=.5} Maybe she should press another to see better{cps=3}...?{w=.5}{/cps}"

    "No."

    "Joke-Explainer shakes her head at the thought.{w=.5} It's just a dark grimey elevator,{w=.25} it's nothing.{w=.5} She's seen the ground beneath her distort before,{w=.25} she can handle this much!{w=.5} Right?{w=.5} Right,{w=.25} Joke-Explainer?{w=.5} She can handle anything if she holds onto the courage in her heart!{w=.5} The courage that isn't hers."

    "What was she doing again?"

    "{cps=3}...{w=.5}{/cps}Waiting.{w=.5} Waiting to get to the top of this tower.{w=.5} To get the final Courage.{w=.5} To fight the final guilt.{w=.5} To press all the buttons.{w=.3}{nw}"

    "NO.{w=.5} What would that do for her??{w=.5} She doesn't need to see anything,{w=.25} it's just riding to the top.{w=.5} Just focus on the whispers around her and the low rumble of the elevator as it continues to rise.{w=.5} It'll comfort her despite her fear.{w=.5} Let it comfort,{w=.25} let it ring in her ears{cps=3}...{w=.5}{/cps}"

    stop music fadeout 7

    "You love the sound of safety!{w=.5} Isn't it nice?{w=.5} We're here for you all the way.{w=.5} Isn't it getting tiring to not be able to see anything?{w=.5} Don't you want to see?{w=.5} See?{w=.5} See those buttons over there?{w=.5} They want to say hello!{w=.5} They want to talk to you{cps=3}...{w=.5}{/cps} don't you know?{w=.5} They want to hear you say{w=.2}{nw}"

    scene black

    play sound "JeHi.ogg"

    "Hi, {w=.8}{cps=17}I'm the Joke-Explainer{image=tm.png} 7000!{/cps}"

    scene elevator_buttons at truecenter

    play music "<loop 42.98>FuckedUpAudio.ogg"

    """
    Joke-Explainer suddenly looks back up on the wall to see the huge purple light illuminating the entire elevator.{w=.5} All of the buttons are lit up{cps=3}...{w=.5}{/cps} and she's got her arms leaning on them.{w=.5} She swiftly backs away in confusion and terror,{w=.25} hearing a stirring sound circling around her.
    
    Voices{cps=3}...{w=.5}{/cps} horrible, horrible voices that all sound like her.{w=.5} Repeating things she's said.{w=.5} MOCKING her.{w=.5} She covers the sides of her face to attempt to block out the voices,{w=.25} but that doesn't do anything because she doesn't have ears.{w=.5} The voices are swirling,{w=.25} god they're spinning all around her!{w=.5} She can't stop hearing it.
    
    SHE SCREAMS OUT to tell the voices to stop{cps=3}...{w=.5}{/cps} or was that just an echo repeating her instead?{w=.5} Mayhaps she never said anything in the first place.{w=.5} Wouldn't that be nice?{w=.5} To never have to hear your voice again?{w=.5} Your sickening voice,{w=.25} ohh how you hate it.{w=.5} 
    
    You feel it rising within you in defiance,{w=.25} you try to fight back the screaming again,{w=.25} but it just keeps happening.{w=.5} You keep hearing the voices scream!{w=.5} Or was that you all along?
    """

    "The elevator begins to{nw}"
    
    extend " shake once again.{w=.5} Joke-Explainer's one and only comfort now,{w=.25} being slowly pulled right from her grasp as it{nw}" with sshake
    
    play sound "elevator smaller shake.wav"
    
    extend " vibrates and shakes with angry passion.{w=.5} She messed up." with sshake
    
    play sound "elevator smaller shake.wav"
    
    "But as she looks up to see through the screaming voices and harsh lights in her face,{w=.25} she spots a button near the bottom labeled \"Emergency Stop\".{w=.5} She shakily stretches her hand out to reach for it,{w=.25} and finally makes her way to press the button." 
    
    stop music

    play sound "button press.ogg"

    scene black

    "The elevator suddenly stops moving upward,{w=.25} and the voices cease to be.{w=.5} The quiet stillness is a comfort{cps=3}...{w=.5}{/cps}"

    "Sadly,{w=.25} that button press is to be her downfall."

    play sound "Elevator shake.ogg"

    "The elevator rumbles one last time,{w=.25}{nw}"
    
    play music "<loop 7>elevator fall 1.ogg"

    extend " before dropping at an unimaginable speed!" with sshake

    "Joke-Explainer flails around as she rises into the air feeling completely weightless,{w=.25} the speed of her descent increasing more and more,{w=.25} going WELL past the normal velocity limit of gravity."

    stop music

    play sound "elevator JE crash.ogg"

    "All of a sudden it stops falling,{w=.25} and Joke-Explainer collides straight into the floor with a loud BANG.{w=.5} It feels like she's running straight into titanium{cps=3}...{w=.5}{/cps}"

    "But before she can pull herself back up,{w=.25}{nw}"
    
    play music_c "Elevator siren.ogg"

    play music "Lift going up.ogg"

    extend " the elevator starts to rise again.{w=.5} But it's rising too fast.{w=.5} WAY too fast.{w=.5} It's going faster and faster and faster,{w=.25} oh god she's going to fly straight out of the TOWER—!"

    stop music

    play sound "JE hits ground 1.ogg"

    "Joke-Explainer finds herself lodged into the elevator's ceiling.{w=.5} She must've flung into it when it stopped moving,{w=.25} but she can't remember when that happened.{w=.5} The elevator HAS stopped again{cps=3}...{w=.5}{/cps} but not for long."

    play music "<from 25>Lift going up.ogg"

    play music_b "metal hit loop.ogg"

    "Over and over and over and over,{w=.25} UP AND DOWN AND UP AND DOWN it wheels Joke-Explainer.{w=.5} She continues to crash into the floor and the ceiling constantly,{w=.25} every collision further damaging her body.{w=.5} She keeps blacking out and reawakening somewhere new in the elevator."

    stop music

    stop music_b

    stop music_c

    play sound "elevator stop sound.ogg"

    "Finally{cps=3}...{w=.5}{/cps} After so long{cps=3}...{w=.5}{/cps} She wakes up to feel the elevator stop again{cps=3}...{w=.5}{/cps}"

    "And this time,{w=.25} it doesn't pick back up.{w=.5} It's completely stopped for now.{w=.5} She pulls herself up to the best of her ability,{w=.25} only just now being able to process just how mutilated every wall of the elevator looks now.{w=.5} Dents all over the place from her body slamming into it{cps=3}...{/cps}"
    
    $ currenthp = 1
    $ maxhp = 2

    show screen hpbar

    "Not to mention the damages all over herself,{w=.25} too.{w=.5} The pain is so bad,{w=.25} it almost feels real."

    hide screen hpbar

    play music "<loop 1>water drip.ogg"

    "Drip.{w=.5} Drip.{w=.5} Drip.{w=.5} Drip."

    "Joke-Explainer hears a haunting noise,{w=.25} one she's ALL too familiar with.{w=.5} It sends a horrible chill down her spine as she turns to see the source of the noise.{w=.5} Her eyes light up in horror when she indeed confirms her terrified suspicions{cps=3}...{w=.5}{/cps}"

    "There is a leak in the elevator."

    stop music

    play sound "boom flood.ogg"

    $ play_multiple("<loop 1>Flood sound.ogg","underwater sound.ogg")

    play music_c "flooding.ogg"

    "Water is pouring into the elevator at multiple angles,{w=.25} filling up the bottom at a slow but terrifying pace.{w=.5} Without breaking eye contact with the growing pool of water,{w=.25} Joke-Explainer steps back ignoring the awful pains in her left leg,{w=.25} and presses her back against the wall of the elevator."

    "As cold water creeps up her body,{w=.25} she stops to think.{w=.5} She's a robot.{w=.5} She might have to take a rice bath when she gets home,{w=.25} but she doesn't need oxygen.{w=.5} Surely,{w=.25} this water poses little threat to her,{w=.25} right?"

    "In what feels like mere moments,{w=.25} the water is already up to her chin.{w=.5}{nw}"
    
    $ update_layers("music_b", 1)

    extend " As the water rises over her small stature,{w=.25} past her face,{w=.25} she begins to feel something.{w=.5} There's a growing pressure,{w=.25} deep in her chest.{w=.5} It's almost like{cps=3}...{w=.5}{/cps} is this what it feels like?{w=.5} To need to breathe?{w=.5} But she can't breathe.{w=.5} {i}She's suffocating.{/i}"

    "She splashes about in a panic,{w=.25}{nw}"
    
    play sound "splash.ogg"

    $ update_layers("music", 1)

    extend " pushing herself upward to poke her head above the rising water!{w=.5} With a sharp gasp,{w=.25} she holds her head as high up as she can,{w=.25} and uses{nw}"
    
    scene green with flash

    play music_d "thruster loop.ogg"

    extend" her thrusters to boost herself up to the ceiling."

    scene thrust with fadeWithText

    "She struggles to keep herself steady in the air,{w=.25} to keep herself level-headed when she feels so overwhelmed.{w=.5} She tries to see if there's a way she can escape quickly{cps=3}...{/cps}"
    
    "Her first thought is the door,{w=.25} but it seems glued shut.{w=.5} After some attempts to wrench it open,{w=.25} she backs away to look for another possible exit.{w=.5} There has got to be an exit somehow."

    "She flies up towards the top of the elevator to get a good view of the entire room,{w=.25} with her being able to see better thanks to the light from her thrusters."

    play sound "metal hit loop.ogg"

    "All of a sudden she feels something hit her head and push her downward."

    "Her first assumption is that a person is trying to pin her to the floor{cps=3}...{w=.5}{/cps} but when she looks up to see who's pushing her,{w=.25} she's only met with the cold ceiling wall."

    play sound "falling cieling.ogg"

    scene lift with flash

    "She yelps in alarm to see the ceiling go down,{w=.25} threatening to crush her with the water,{w=.25} and tries her best to push the ceiling back up.{w=.5} Her thrusters roar in intensity as she puts more and more energy into keeping it from turning her into a watery robo-pancake."

    "It slows the ceiling down significantly,{w=.25} but she doesn't have enough strength to fully stop it in its tracks.{w=.5} Even worse,{w=.25} the water's starting to get much much closer to her now.{w=.5} She only has possibly mere moments before the elevator destroys her.{w=.5} She has no idea what to do{cps=3}...{w=.5}{/cps} GOD what does she do here?!"

    "The water's reached the bottom of her feet by now.{w=.5} She darts her head around to look for anything to possibly save her{cps=3}...{w=.5}{/cps}"

    "There!{w=.5} She can spot a particular dent on the elevator door down below that a little bit of the water is flowing through.{w=.5} That may be her only ticket to survive this deathtrap of an elevator."

    scene black with fadeWithText

    stop music_d

    "She takes a deep breath,{w=.25} and pushes herself off of the lowering ceiling to give her a speed boost towards the dent.{w=.5}{nw}"
    
    $ update_layers("music_b", 1)

    extend " For a split moment fear ripples up and down her body as she dives into the water{cps=3}...{w=.5}{/cps} but Joke-Explainer quickly pulls herself together and makes her way to the dent to grip onto it."

    play sound "Opening wooden door underwater.ogg"

    "She begins pulling it apart with all the strength she has,{w=.25} as the ceiling and water finally meet each other.{w=.5} The two opposing forces fight for dominance over which will consume the whole elevator first,{w=.25} making the water pressure tighter with each passing second."

    "She can feel it press on her even more than the ceiling did,{w=.25} threatening to break her into pieces if she doesn't GET{w=.25} THIS{w=.25} DOOR{w=.25} OPEN—!!!{w=.5}{nw}"

    $ stop_layers(0)

    stop music_c

    play sound "flood door break.ogg"

    "A hinge in the elevator door snaps,{w=.25} and the entire thing pulls open suddenly.{w=.5} Joke-Explainer is pulled out of the elevator with the rapidly rushing water,{w=.25} eventually falling onto some sort of ground."
    
    "The water subsides around her,{w=.25} and she sighs in relief when she feels the pressure leave her body.{w=.5} But once she gets a grip on herself,{w=.25} her relief turns to confusion as she stares at the deep pink carpet beneath her."

    scene voice_bg with fade

    # python:
    # update_background_layer()

    play music "loveless.ogg"

    play music_b "Voice rain loop.ogg"

    "Sitting up,{w=.25} she notices the large glass windows surrounding the room,{w=.25} reflecting some distant outside city.{w=.5} The room is mostly barren aside from a desk and chair at the centerpoint,{w=.25} with the chair turned away from Joke-Explainer's field of vision.{w=.5} She gently rubs her head in confusion,{w=.25} continuing to survey the dimly lit area."

    "This{cps=3}...{w=.5}{/cps} this is The Voice Inside Your Head's office{cps=3}...{w=.5}{/cps}"

    "When did she get here?{w=.5} Just a mere moment ago she was struggling in the midst of the single worst elevator ride in her life,{w=.25} but now she's{cps=3}...{w=.5}{/cps} here."
    
    "Here in this cold and unwelcoming office.{w=.5} She'd never actually been up here in person before,{w=.25} only seeing it through the lens of the Christmas Comeback Crisis.{w=.5} She silently wonders if this is really how it feels to have to come up here—{w=.3}{nw}"

    g3 "Ah.{w=.5} I see you've finally made it,{w=.25} Joke-Explainer{image=voicetm.png} 7000."

    je "Doctor{cps=3}...?{w=.5}{/cps}"

    g3 "Ohh,{w=.25} not quite."

    scene terrifying with fadeWithText

    "The chair spins around to reveal what Joke-Explainer can only make out as the vague figure of Doctor Andonuts.{w=.5} At least,{w=.25} she thinks it's him.{w=.5} If she tilts her head the wrong way though,{w=.25} he looks{cps=3}...{w=.5}{/cps} taller.{w=.5} Like a bizarre optical illusion,{w=.25} shifting in her peripherals."
    
    "He leans forward and clasps his hands together in a very formal manner."

    g3 "Was the ride up to here pleasant?{w=.5} I figured I'd give you an easy time,{w=.25} since you were DYING to see me{cps=3}...{w=.5}{/cps}"

    "Joke-Explainer winces a little,{w=.25} reliving the horrors of that wretched elevator trip."

    scene voice_bg with fadeWithText

    show guilt3 at cccenter, silhoette with fadeWithText

    g3 "I take it you've had a quite eventful adventure,{w=.25} running your way through the depths of this old man's mind.{w=.5} Have you had your fun?"

    je "I{cps=3}...{w=.5}{/cps} Fun was never part of the equation.{w=.5} I'm here to save Doctor Andonuts from the foreign entity that's plaguing his mind."

    g3 "Is that what he told you to get you in here?{w=.5} Ahahaha,{w=.25} how quaint!{w=.5} He'll really tell anyone ANYTHING to get them to do what he wants."

    "Joke-Explainer tilts her head like a confused puppy.{w=.5} The shadowy Andonuts takes notice very quickly."

    g3 "Please,{w=.25} forgive me for darting ahead so far.{w=.5} I've had much on my plate as of late,{w=.25} and the speed of your arrival was indeed a little unexpected.{w=.5} Get yourself up first,{w=.25} at the very least."

    "Joke-Explainer can feel a presence grab her and pull her to her feet,{w=.25} like a puppet on strings.{w=.5} As soon as she's to her feet,{w=.25} the feeling disappears entirely.{w=.5} She stares at the shadowy doctor,{w=.25} trying her best to conceal any terror rising throughout her body."

    g3 "Good,{w=.25} good!{w=.5} Now we can finally speak eye to eye."

    je "Who{cps=3}...{w=.5}{/cps} who are you?{w=.5} Are you the third Bad Thing?{w=.5} {cps=3}...{w=.5}{/cps}The Guilt?"

    g3 "Indeed,{w=.25} that pathetic old sap has given me the title of 'Third Guilt' of the mind,{w=.25} guarding the last and final Courage you need.{w=.5} However,{w=.25} I find that name rather{cps=3}...{w=.5}{/cps} boring.{w=.5} Unintuitive.{w=.5} Not much of a creative fellow,{w=.25} you'd agree?"

    "Joke-Explainer sheepishly nods her head,{w=.25} not quite following the conversation."

    g3 "Yes,{w=.25} thank you.{w=.5} That is why I have elected to instead refer to myself as{cps=3}...{/cps}"
    
    g3 "\"The Voice Inside His Head.\"{w=.5} Has a much better ring to it,{w=.25} don't you think?"

    "Joke-Explainer stops nodding along and tenses her stance.{w=.5} As she does,{w=.25} she catches a sudden glint in the shadowy doctor's glasses."
    
    show guilt3 at cccenter, unsilhoette with fadeWithText

    "An unnatural,{w=.25} piercing purple glow shines through them now,{w=.25} forcing Joke-Explainer to shrink and squirm under its gaze.{w=.5} It threatens to stab right through her if she looks at it for too long,{w=.25} causing her to suddenly turn her head away."

    g3 "Ah,{w=.25} what's the matter?{w=.5} Why do you look so afraid,{w=.25} my dear Joke-Explainer{image=voicetm.png} 7000?{w=.5} Seen something you wish you hadn't?"

    je "Please{cps=3}...{w=.5}{/cps} give me the third Courage in your possession.{w=.5} I don't want to fight,{w=.25} Doctor.{w=.5} I only want to help."

    g3 "And that's wonderful,{w=.25} because I don't want to fight either!{w=.5} That isn't quite my style{cps=3}...{w=.5}{/cps} No no,{w=.25} I'm here to assist as well."

    je "You are?"

    g3 """
    But of course!{w=.5} You see,{w=.25} I've observed for a long time the way in which the good doctor has impacted the world which flows around him.

    The pain he causes others{cps=3}...{w=.5}{/cps} the pain he causes himself{cps=3}...{w=.5}{/cps} all of it is just so unnecessary,{w=.25} you see.{w=.5} Would it not be better to eliminate the cause of grief entirely?{w=.5} 

    To sort of,{w=.25} sweep it under the rug,{w=.25} so to speak?{w=.5} To let it die in peace.
    """

    je "Doctor Andonuts{cps=3}...{w=.5}{/cps} You don't have to shut out the parts of yourself you're afraid of.{w=.5} You're a good man,{w=.25} you don't need to suffer like this."

    g3 "Oh no no,{w=.25} you misunderstand me,{w=.25} Joke-Explainer{image=voicetm.png} 7000.{w=.5} I'm not here to 'shut out',{w=.25} I'm here to{cps=3}...{w=.5}{/cps} 'shut off'.{w=.5} For good."

    je "'Shut off'{cps=3}...{w=.5}{/cps} Hold on,{w=.25} you don't mean—{w=.3}{nw}"

    g3 "I want the doctor to die."

    "Joke-Explainer opens her mouth in shock.{w=.5} The room begins to feel as though it's spinning.{w=.5} She struggles to get any words out."

    je "If{cps=3}...{w=.5}{/cps} I-if Doctor Andonuts dies,{w=.25} would you not die as well?"

    g3 "A worthy sacrifice for the greater good of the world.{w=.5} A good man always must do what is right for those around him,{w=.25} and when he becomes a liability?{w=.5} Well,{w=.25} that's when he has to take himself out of the equation."

    je "B-but{cps=3}...{w=.5}{/cps} H-how could—{w=.25}{nw}"

    g3 "As a machine yourself,{w=.25} you must understand this.{w=.5} I mean,{w=.25} what do you do when you have a faulty program causing errors in your system?{w=.5} You shove it in the trash and delete it."

    "Joke-Explainer looks to the side,{w=.25} guiltily ruminating over what the dark figure of the doctor just said.{w=.5} {cps=3}...{w=.5}{/cps}After some moments of reflection,{w=.25} she turns her head back with a determined look in her eye."

    stop music fadeout 2.0

    stop music_b fadeout 2.0

    je "I'm sorry,{w=.25} but I can not let you move forward with this plan.{w=.5} Doctor Andonuts is worth saving!"

    g3 "I would love to see you attempt to stop me,{w=.25} Joke-Explainer{image=voicetm.png} 7000."

    window hide

    show battle_trans at truecenter

    play sound "boss.flac"

    pause 2.5

    jump fight_3

label guilt_3_hurt:
    show screen hpbar

    play sound "prep.wav"

    "Andonuts (???) swings a knife!" 
    
    play sound "attack.wav"

    $ currenthp -= 1

    extend "\n1 HP of damage to Joke-Explainer!" with sshake


    if currenthp <= 0:
        jump gameover 
    else:
        hide screen hpbar
        return

label fight_3:
    $ renpy.save("fight_3")
    $ config.after_load_transition = None
    $ intflag = 3
    scene voice_battle
    $ renpy.transition(fade, layer="master")
    show dead_je at truecenter
    show guilt3 battle at battle
    cen "[[FIGHT START]"
    $ currenthp = 1
    $ maxhp = 2
    play music "guilt3.ogg" volume .5

    g3 "Why do you think the doctor is worth saving?{w=.5} Hasn't he given you so much grief during your stay in Magicant?{w=.5} He's tortured you so relentlessly,{w=.25} and you think he deserves to live?"

label g3c1:
    menu:
        "What should Joke-Explainer say?"

        "Refute the point about \"torture\"":
            je "Doctor Andonuts never consciously hurt me.{w=.5} I'm here out of my own free will,{w=.25} my desire to help the Doctor.{w=.5} He even asked me to leave Magicant after encountering the second Guilt{cps=3}...{w=.5}{/cps} but I won't let him suffer without help."

            g3 """
            Interesting rebuttal.{w=.5} However,{w=.25} in your eagerness to assert your own agency,{w=.25} you fail to consider the implicit pressure the doctor placed upon you from the beginning.{w=.5} The way in which this endeavor was framed{cps=3}...{w=.5}{/cps} a mission.

            A scenario he knew would keep you devoted to fulfilling your objective.{w=.5} An insipid,{w=.25} ruinous idea he willingly infected you with.{w=.5} No,{w=.25} he may not have known exactly what you would face upon arrival{cps=3}...{w=.5}{/cps} but he suspected.

            He knew it was a dangerous operation,{w=.25} with many unknown factors,{w=.25} and yet he downplayed their significance.{w=.5} Presented you with a simple extermination job,{w=.25} and kept you too committed to raise objections once complications arose.
            
            How could you possibly justify these actions?
            """

        "Everyone deserves to live":
            je "I think everyone deserves to live,{w=.25} no matter what.{w=.5} You only have one life here,{w=.25} you shouldn't throw it away so hastily."

            g3 "I strongly disagree!{w=.5} There are some people who must be destroyed for the good of the whole.{w=.5} The doctor is among them,{w=.25} and that you defend him and his ilk proves that you are too.{w=.5} Die."

            call guilt_3_hurt from _call_guilt_3_hurt

            jump g3c1

label g3c2:
    menu:
        "What should Joke-Explainer say?"

        "He didn't know how to ask for help":
            je "He was probably lost and scared{cps=3}...{w=.5}{/cps} He did not know the true repercussions of what his issue would entail.{w=.5} He didn't seem to have anyone else to turn to except for me.{w=.5} I can't fault him for feeling trapped and afraid to give the full possible details of my mission."

            g3 """
            Afraid to tell the truth{cps=3}...{w=.5}{/cps} like a sniveling coward.{w=.5} This world has no place for cowards like him,{w=.25} don't you see?
            
            He'll just use and abuse you until your usefulness is up,{w=.25} and then toss you away to go find the next poor gullible idiot to hide behind.{w=.5} And he'll keep doing this,{w=.25} until {i}I{/i} step in and stop him.

            Think about it,{w=.25} he maintains no contact with you for MONTHS at a time,{w=.25} only calling when he needs you to do his dirty work?{w=.5} And you just put up with that?
            """

        "Insist The Voice is lying, believe in the doctor":
            je "I don't believe you!{w=.5} Doctor Andonuts would not intentionally spare me details on something that could potentially put me in any danger!"

            g3 "Oh how cute.{w=.5} I would pity you if you weren't currently attempting to stand in my way to stop my endeavors.{w=.5} Let me put you out of your misery to spare you of the knowledge."

            call guilt_3_hurt from _call_guilt_3_hurt_1

            jump g3c1

label g3c3:
    menu:
        "What should Joke-Explainer say?"

        "He was forced to work for Haltmann":
            je "It isn't Doctor Andonuts' fault for being so busy,{w=.25} he's been forced to work under Haltmann constantly,{w=.25} having to conduct consistent research."

            g3 """
            How disappointing.{w=.5} I see you've resorted to grasping at straws,{w=.25} conjuring up people who don't exist to prove your points.

            And here I thought it was your job to explain jokes,{w=.25} not make them.{w=.5} I'm afraid humor will get you nowhere with me though.{w=.5} This joke has run its course.
            """

            call guilt_3_hurt from _call_guilt_3_hurt_2

            jump g3c1

        "Andonuts has been busy, but he cares":
            je """
            I know it's been a while{cps=3}...{w=.5}{/cps} B-but I don't blame him for it!{w=.5} He's been busy with his work,{w=.25} and I know he still cares about me.
            
            He's helped me a whole lot{cps=3}...{w=.5}{/cps} Doctor Andonuts,{w=.25} he taught me how to fend for myself in this world.{w=.5} He freed me from being experimented on by other researchers,{w=.25} and taught me how to repair myself when my systems get damaged{cps=3}...{w=.5}{/cps} I owe my life to the doctor.

            Doctor Andonuts and I genuinely care about each other,{w=.25} not that I expect you to understand something like that,{w=.25} Voice.{w=.5} How did you even get in here,{w=.25} anyway?
            """

            g3 """Oh my dear Joke-Explainer{image=voicetm.png} 7000{cps=3}...{w=.5}{/cps}

            This is where you're horribly mistaken!{w=.5} I've {i}always{/i} been here.{w=.5} {i}Always{/i},{w=.25} nagging in the back of the doctor's mind.{w=.5} Everyone has their own 'version' of me deep within themselves{cps=3}...{w=.5}{/cps}

            In fact{cps=3}...{w=.5}{/cps} YOU{w=.25} yourself have your very own dissenting voice,{w=.25} the angry,{w=.25} spiteful part of you that always tells you no.{w=.5} Wouldn't you like to see her?
            """

            play sound "bonemetalcrush.ogg"

            show guilt3 battle ani1

            pause 2

label g3c4:
    menu:
        "What should Joke-Explainer say?"

        "Deny the point":
            je "N-no{cps=3}...{w=.5}{/cps} That,{w=.25} that can't be!{w=.5} You can't trick me,{w=.25} I don't have anything like that within myself!"

            g3 "Oh,{w=.25} is {i}that{/i} the case?{w=.5} You really believe that?{w=.5} Then tell me{cps=3}...{w=.5}{/cps} What's that clouding your vision?"

            je "Wha—{w=.25}{nw}?"

            stop music fadeout .5

            scene voice with dissolve

            play sound "JeEvil.ogg" volume .75

            if (renpy.music.is_playing("sound")):
                while (renpy.music.is_playing("sound")):
                    pause 1 

            play music "<loop 4.09>gameover.ogg"

            scene gameover with slow_fade

            jump gameover2

        "Refute the point":
            je "I-I{cps=3}...{w=.5}{/cps} Even if,{w=.25} even if you're correct,{w=.25} I don't have to listen to that part of me.{w=.5} I may not be able to stop hate,{w=.25} but I can always encourage love!"

            g3 "{cps=3}...{w=.5}{/cps}For now that may be the case,{w=.25} but not forever.{w=.5} Inevitably you'll fall,{w=.25} just as he has.{w=.5} Just as the doctor has,{w=.25} as well."
            
            g3 "At some point,{w=.25} you'll crack under the pressure,{w=.25} and the hate and the dark will consume every facet of your being.{w=.5} And what will you do when that happens?{w=.5} You will FALL."

label g3c5:
    menu:
        "What should Joke-Explainer say?"

        "Give self-motivational message":
            je "Not if I always have the light of my friends by my side!{w=.5} And that includes Doctor Andonuts!{w=.5} He deserves saving as much as everyone else does!"

            g3 """
            You're starting to repeat yourself{cps=3}...{w=.5}{/cps} I've heard this all before.{w=.5} No new points{cps=3}...{w=.5}{/cps} As if I could count on you to give me something I haven't heard yet.

            I grow bored of this encounter.{w=.5} Get out of my way.
            """

            call guilt_3_hurt from _call_guilt_3_hurt_3

            jump g3c1

        "Point out The Voice has been stalling":
            stop music fadeout 1
            
            je "{cps=3}...{w=.5}{/cps}Have you been stalling?"

            g3 "What?"

            play sound "backwards bone crack.ogg"

            show guilt3 battle ani2

            je "This entire back-and-forth{cps=3}...{w=.5}{/cps} You keep saying these big sweeping things,{w=.25} but never actually do anything.{w=.5} Are you{cps=3}...{w=.5}{/cps} afraid?"

            g3 "Wh-{w=.25}That's-{w=.25}Th-{w=.25}that's preposterous!{w=.5} Where do you get off,{w=.25} suggesting that I'm stalling?!{w=.5} Do you know who I am?{w=.5} What I'm capable of?!"

            je "Yes,{w=.25} I do.{w=.5} Which is why I believe you're stalling.{w=.5} You don't really WANT to do this,{w=.25} do you?{w=.5} You want me to talk you out of it so you can justifiably back away.{w=.5} So you won't have to{cps=3}...{w=.5}{/cps} have to kill yourself.{w=.5} You don't really want to do that."

label fight_3_end:
    g3 "You-{w=.25} I-{w=.25} I'm-{w=.25}{cps=3}...{/cps}"

    "The shadowy Andonuts drops his stance,{w=.25} tilting his head down towards the floor.{w=.5} He attempts to get some refutation out against Joke-Explainer,{w=.25} but nothing that discernibly resembles English comes out.{w=.5} Finally he caves,{w=.25} clutching his head and falling to his knees with a groan."

    g3 "{i}{cps=10}You stupid bitch{/cps}{cps=3}...{/cps}{/i}"

    cen "[[FIGHT END]"

    scene voice_bg with fade

    show guilt3 at cccenter
    $ renpy.transition(dissolve, layer="master")

    play music "<loop 12.28>courage.ogg"

    "The dark figure lets out one last sigh,{w=.25} before readjusting what Joke-Explainer thinks is his tie and standing back upright.{w=.5} She looks off idly to the side awkwardly,{w=.25}{nw}"
    
    scene guilt_3_hug with fadeWithText

    extend " but steps forward to give him a comforting hug.{w=.5} However he refuses to reciprocate,{w=.25} instead opting to stand there tensely."

    g3 "{cps=3}...{w=.5}{/cps}Are you done yet?"

    scene voice_bg with fadeWithText

    show guilt3 at cccenter
    $ renpy.transition(dissolve, layer="master")

    "Joke-Explainer promptly lets him go,{w=.25} and he proceeds to dust his sleeves off as if attempting to get some sort of grime off of him."

    g3 """
    Alright.{w=.5} You're a clever robot,{w=.25} I'll give you that much.{w=.5} I don't have a rebuttal for that point{cps=3}...{w=.5}{/cps} Because I suppose in some regard,{w=.25} it is true.{w=.5} Truth be told,{w=.25} I'm rather tired.

    Tired of all of this anguish that constantly surrounds me.{w=.5} I'm sure you've heard all of this before{cps=3}...{w=.5}{/cps} After all,{w=.25} you have been trekking through 'Anguish Avenue'.{w=.5} It'd be a little surprising not to find any anguish here,{w=.25} right?
    """

    "Joke-Explainer gives a short nod."

    g3 """
    Right{cps=3}...{w=.5}{/cps} Well,{w=.25} fair is fair I suppose.{w=.5} I won't{cps=3}...{w=.5}{/cps} do anything drastic today.{w=.5} Or at least,{w=.25} {i}I{/i} won't.{w=.5} I can't say much for the rest of the doctor{cps=3}...{w=.5}{/cps}

    Take the final Courage.{w=.5} Feel free to throw it against the wall and watch it splat for all I care.{w=.5} I have no business with it anymore.{w=.5} {cps=3}...{w=.5}{/cps}Oh yes,{w=.25} tell Varik I said hello when you meet him again.
    """

    scene voice_room
    $ renpy.transition(long_dissolve, layer="master")
    
    "With that,{w=.25} the lights in the office suddenly light up,{w=.25} illuminating the entire space.{w=.5} The shadowy Andonuts dissipates in front of Joke-Explainer's eyes,{w=.25} leaving only a smol purple haired girl laying in his former place.{w=.5} She sits up to look at Joke-Explainer and gives a wave."

    "Joke-Explainer waves back,{w=.25} before being interrupted by the two other Courages appearing from behind her.{w=.5}{nw}"
    
    scene the_besties with fadeWithText

    extend " They seem overjoyed to be reunited with the last one,{w=.25} and the three of them together all give each other short waves and high fives."
    
    scene voice_room with fadeWithText

    stop music fadeout 2.0

    play sound "courage_collect.wav"

    "Once they're finished,{w=.25} they all face Joke-Explainer and enter her soul,{w=.25} giving her a great increase in strength and resolve."

    play sound "friend.ogg"
    pause .9

    show screen stop_scr

    $ inventory.add_item(cour3)

    "The Joke-Explainer{image=tm.png} 7000 finally has ALL 3 COURAGES!{w=7}{nw}"

    hide screen stop_scr

    play music "sanctuary.ogg"

    "All of a sudden she hears a loud{nw}"
    
    play sound "Elevator DING.ogg"

    extend " DING sound behind her.{w=.5} She turns around to see the elevator door open once again,{w=.25} beckoning her in."

    "At first she refuses,{w=.25} searching for some other way to escape,{w=.25} like a staircase to the bottom,{w=.25} even considering breaking the window and flying back down{cps=3}...{w=.5}{/cps} But she knows she doesn't have the energy to do that.{w=.5} She HAS to ride that horrid elevator back down."

    "She metaphorically holds her breath as she steps inside.{w=.5} The elevator definitely wobbles under her weight,{w=.25} but not to the same degree as it did before.{w=.5} She carefully makes her way over to the buttons and presses the bottom one,{w=.25} causing the door to close and the elevator to begin its descent.{w=.5} It's a shockingly quiet ride down." 
    
    scene anguish_avenue_nofog with dissolve

    "The doors open up to reveal the outside,{w=.25} back in Anguish Avenue.{w=.5} She jumps out,{w=.25} happy to be out of that awful place."

    "Anguish Avenue seems a bit brighter.{w=.5} Fog still covers the entire area,{w=.25} but she finds it a much easier time leaving the place than it was entering.{w=.5} She eventually makes her way back to where she originally came from,{w=.25} opting to turn back and look at the place one final time."
    
    stop music fadeout 2.0

    "It's{cps=3}...{w=.5}{/cps} still eerie to look at.{w=.5} She decides to leave before it can pull any final mindgames on her."

    play music "magicant.ogg" volume 0.75

    scene magicant_bg with dissolve

    "It takes a little while,{w=.25} but she makes it back to her original starting point.{w=.5} She spots the Mouth of Terror up ahead,{w=.25} with Varik still guarding it,{w=.25} and picks up her pace excitedly.{w=.5} Joke-Explainer is finally back,{w=.25} ready to contain the foreign entity plaguing Doctor Andonuts' mind once and for all."

    scene mouthofterror with dissolve

    show varik at cccenter with fadeWithText

    stop music fadeout 1

    je "I'm back,{w=.25} and I have th—{w=.5}{nw}"

    $ play_multiple("saturn.ogg","sync.ogg")

    d "Hi ho!{w=.5} I see you returned!"

    hide varik
    $ renpy.transition(easeoutleft, layer="master")

    "Joke-Explainer once again gets a bit startled{nw}"
    
    show mr_dee at cccenter
    $ renpy.transition(easeinright, layer="master")

    extend " by the sudden appearance of Mr. Dee."

    je "Oh,{w=.25} uh,{w=.25} hello again!{w=.5} Yes,{w=.25} I have also obtained all 3 courages."

    d "Goody!{w=.5}  Boing!{w=.5}  Much hurry,{w=.25} go show guard man courages!"

    hide mr_dee with easeoutleft

    $ update_layers("music_b", 1)

    show varik at cccenter
    $ renpy.transition(easeinright, layer="master")

    "Joke-Explainer walks up to Varik,{w=.25} wondering how she should present the courages,{w=.25} when all 3 reveal themselves and one by one offer a high five to Varik."

    v "{cps=3}...{w=.5}{/cps}"

    scene high_five_for_the_win with dissolve

    "Varik gives a slight smirk,{w=.25} and reciprocates the offer." 
    
    $ inventory.remove_item("Courage of Worth")
    $ inventory.remove_item("Courage of Self")
    $ inventory.remove_item("Courage of Love")


    scene mouthofterror with fadeWithText

    show varik at cccenter with fadeWithText
 
    "Varik then gives a nod of approval to Joke-Explainer,{w=.25}{nw}"
    
    show varik at cccleft
    $ renpy.transition(ease, layer="master")

    extend " and opens the way for her to enter."

    $ update_layers("music", 1)

    show mr_dee at cccright
    $ renpy.transition(easeinright, layer="master")

    d "Ding!{w=.5} Cave now open for you entering!"

    je "Thank you for all the help,{w=.25} Mr. Dee.{w=.5} Without your guidance,{w=.25} I am unsure where I'd be right now.{w=.5} Goodbye!"

    d "Boing!{w=.5} Zoom!{w=.5} Bye bye!"

    $ stop_layers()

    hide mr_dee
    $ renpy.transition(easeoutright, layer="master")

    hide varik
    $ renpy.transition(easeoutleft, layer="master")

    "Joke-Explainer passes by Varik,{w=.25} and,{w=.25} gathering up as much of her own courage as she can,{w=.25} walks into the Mouth of Terror."

    scene inside_mouth_of_terror_1 with fade

    play music "cave.ogg"

    "As she ventures deeper,{w=.25} the light of the entrance gradually fades,{w=.25} leaving the cave walls illuminated only by the dim glow of her eyes and antenna.{w=.5} The darkness is certainly unnerving,{w=.25} but the longer she walks,{w=.25} the more she feels it's a bit{cps=3}...{w=.5}{/cps} anticlimactic?"

    "Not to say that a dark cave isn't scary,{w=.25} but after everything she just went through,{w=.25} Joke-Explainer was bracing herself for something a lot more traumatizing.{w=.5} For all intents and purposes,{w=.25} this is just a normal cave."

    "Though of course,{w=.25} just as the thought flows through her mind,{w=.25} she senses something{cps=3}...{w=.5}{/cps} off.{w=.5} From certain parts of the cave walls,{w=.25} the light she's casting onto it seems to not reflect anything back.{w=.5} Tiny pockets of absolute nothing,{w=.25} holes that are almost imperceptibly small to her."

    "Curiosity gets the better of her,{w=.25} and she gently pokes one of the strange dark holes to see what may be on the other side,{w=.25} but when she lifts her hand she notices that the hole is a much larger size now than it was before she touched it."
    
    window show

    scene inside_mouth_of_terror_2 at truecenter with fadeWithText

    "Lowering her arm,{w=.25} she spots small bits of rock and dust on her hand{cps=3}...{w=.5}{/cps} bits of the wall that peeled off onto her."

    play music_b "rumbling cave.ogg"

    "Suddenly,{w=.25} she hears a low rumble surrounding her.{w=.5}{nw}" with sshake
    
    extend " Looking up to witness the cause,{w=.25} she stares at the wall watching it be consumed{nw}"
    
    scene inside_mouth_of_terror_3 with fadeWithText

    extend " by a horrible ever-present darkness."

    "It threatens to swarm the entire cave,{w=.25} and she backs away in shock noticing just how close it was getting to her face.{w=.5} Her thrusters roar to life again as she dashes through the cave,{w=.25} desperate to stave off the crumbling darkness reaching her."

    "The cave twists and distorts the further she flies through,{w=.25} but she doesn't care.{w=.5} She's been through hell and back already,{w=.25} nothing's going to stop her from completing her mission.{w=.5} Just gotta keep repeating that."

    scene inside_mouth_of_terror_4 with fadeWithText

    """
    She won't let the darkness slowly surrounding her vision stop her from completing her mission.
    
    She won't let her losing any sense of gravity stop her from completing her mission.
    
    She won't let her vision being obscured and unable to see the walls around her anymore stop her from completing her mission.
    """

    stop music fadeout 2.0

    stop music_b fadeout 2

    "She thinks she sees a light{cps=3}...{w=.5}{/cps} but before she can even think about reaching out to grab it,{w=.25} the darkness surrounds{nw}"
    
    scene black with fadeWithText

    extend " every facet of her being and she falls into nothing."

    window hide

    pause 2.0

    "For how long she drifts along,{w=.25} it is impossible to tell.{w=.5} It may be minutes.{w=.5} Days.{w=.5} Years.{w=.5} It becomes harder and harder for her to keep her mind stable."

    "Does she even have a mind?{w=.5} It's hard to tell without anything that resembles a genuine thought passing through it.{w=.5} Maybe this is what being braindead is{cps=3}...{w=.5}{/cps} She'd make a note of this experience if she had any capacity to."

    "Is it an experience though?{w=.5} Or is it the absence of one?{w=.5} Not a single one of her senses are working,{w=.25} suspended in this empty void.{w=.5} {cps=3}...{w=.5}{/cps}Is this an empty void actually?{w=.5} Maybe there's other things around her{cps=3}...{w=.5}{/cps} But then why can't she sense their presence?"

    "Maybe SHE doesn't really exist{cps=3}...{w=.5}{/cps} What even constitutes the existence of Joke-Explainer then{cps=3}...?{w=.5}{/cps} If she could just grab onto something,{w=.25} she could be able to better define the difference between what is and isn't a thought to her.{w=.5} If there ever really was a difference.{w=.5} If there ever really was anything.{w=.5} If there ever—{w=.25}{nw}" # Her name might need to be put on a new line

    play sound "Spotlight.ogg"

    "From behind her,{w=.25} she hears the sound of a light switching on.{w=.5} Suddenly her thoughts spring back to life,{w=.25} the input screaming at her to turn the body she forgot she had around."

    scene spotlight_over_computer with dissolve

    play music "<loop 11>chillrig.ogg"

    "When she does,{w=.25} she can see a single spotlight in the void,{w=.25} shining down on what looks like a standard work desk,{w=.25} housing an already running computer."

    "Joke-Explainer starts cautiously walking up to the desk,{w=.25} trying to make out the details on the computer screen.{w=.5} After getting to the desk,{w=.25} she carefully begins to touch it to get a better view,{w=.25} when—{w=.25}{nw}"

    a "Joke-Explainer!{w=.5} I-I can sense you made it into the Mouth of Terror,{w=.25} can you hear me?"

    je "Doctor?{w=.5} Yes,{w=.25} I can hear you,{w=.25} but{cps=3}...{w=.5}{/cps} where are you?{w=.5} How is that possible without the radio?"

    a "Oh thank goodness,{w=.25} you're ok!{w=.5} And you managed to get the 3rd Courage!{w=.5} Fantastic!"

    a "As for how I can speak to you{cps=3}...{w=.5}{/cps} I hypothesize that entering the Mouth of Terror may have put you deep enough in my consciousness,{w=.25} giving me the ability to speak to you from the inside."

    je "That's{cps=3}...{w=.5}{/cps} wonderful,{w=.25} Doctor!"

    je "Though,{w=.25} I am curious –{w=.25} do you know what this computer desk in front of me is?{w=.5} I don't understand why this is the only thing here.{w=.5} Is it important?"

    a "Joke-Explainer,{w=.25} that is the foreign entity!{w=.5} Please,{w=.25} take out the Fun-Sized Absolutely Safe Capsule and capture it!{w=.5} We can end this nightmare once and for all!"

    je "{cps=3}...{w=.5}{/cps}This is the foreign entity?{w=.5} Are you sure?{w=.5} I wouldn't expect it to look like this."

    a "Please,{w=.25} you can't look too deep into it.{w=.5} The more time that goes by the bigger the threat becomes!{w=.5} Hurry!"

    je "Shouldn't we read what the computer has to say first?{w=.5} It could help determine the issue."

    a "Joke-Explainer,{w=.25} please,{w=.25} listen to me{cps=3}...{w=.5}{/cps} Do not read what is on that computer.{w=.5} It is not important.{w=.5} What's important is trapping the entity,{w=.25} and safely getting you out of my mind."

    je "Doctor,{w=.25} this threat has been endangering your well-being for a while.{w=.5} It is in our best interest to understand what that threat may be,{w=.25} is it not?"

    a "I'm begging you,{w=.25} Joke-Explainer!{w=.5} Don't read the archives!{w=.5} We're so close,{w=.25} all you have to do is remove that memory and—{w=.3}{nw}"

    stop music

    je "Hold on,{w=.25} memory?{w=.5} I thought—{w=.25}But you said this was a foreign entity,{w=.25} didn't you?"

    play music "Clocking In.ogg" volume .5

    "The air snaps cold.{w=.5} The doctor's voice is gone.{w=.5} With each agonizing second of silence,{w=.25} more pieces begin to fit together in Joke-Explainer's mind."

    a "Okay.{w=.5} Okay,{w=.25} Joke-Explainer,{w=.25} listen.{w=.5} J-just listen to me for a second—{w=.3}{nw}"

    je "You said they were archives{cps=3}...{w=.5}{/cps} You know what's on this computer,{w=.25} don't you?{w=.5} Have you been hiding this from me the entire time?{w=.5} Why would you lie to me about this?{w=.5} What could be in these archives that—{w=.3}{nw}"

    a "STOP!"

    scene computer_lights

    "The void surrounding Joke-Explainer begins to rapidly flash through a barrage of psychedelic,{w=.25} saturated colors,{w=.25} as the atmosphere reaches a fever pitch.{w=.5} She looks around,{w=.25} recoiling in shock before{nw}"
    
    scene spotlight_over_computer
    $ renpy.transition(long_dissolve, layer="master")

    extend " it settles back into being an empty,{w=.25} barren void."

    a "{cps=3}...{w=.5}{/cps}I'm sorry,{w=.25} I just can't let you see what is in those archives.{w=.5} I just need it gone.{w=.5} I deeply apologize that I lied to you,{w=.25} but can you please just use the capsule to get rid of the memory?{w=.5} It's for my own sake."

    $ persistent.capflag = 1

    window hide

    show screen key_check

    if persistent.capflag == 1:
        while persistent.capflag == 1:
            pause 

label b_button:
    $ persistent.capflag = 2
    
    hide screen key_check

    je "If it's for your own good,{w=.25} I must come to an understanding of what you're trying to hide.{w=.5} I'm sorry,{w=.25} Doctor."

    a "W-wait!{w=.5} DON'T!{w=.5} YOU'RE MAKING A MISTAKE!"

    scene joke_explainer_at_computer with fadeWithText

    "Joke-Explainer begins to read the archives on the computer{cps=3}...{w=.5}{/cps} The void flares and flashes around her as she ignores them completely.{w=.5} Andonuts continues to plead."

    a "JOKE-EXPLAINER!!!{w=.5} I DON'T THINK YOU UNDERSTAND!{w=.5} YOU DON'T WANT TO SEE THIS!"

    """
    Her head is unmoving,{w=.25} staring deep into every word of the archives.{w=.5} She seems{cps=3}...{w=.5}{/cps} discontented.
    
    Over and over she rereads what's displayed on the screen while the waves of color dance frantically around her,{w=.25} desperately attempting to grab and pull her away from the computer altogether,{w=.25} though they have no physicality and simply phase through her every time.

    Eventually, after a long while of reading,{w=.25} she slowly turns her head to the side and looks up.
    """

    scene computer_lights with fadeWithText

    je "{cps=3}...{w=.5}{/cps}That's it?"

    scene spotlight_over_computer

    "The swirling colors all suddenly freeze in place,{w=.25} shocked by the lack of emotional response."

    a "What{cps=3}...?{w=.5}{/cps} Y-yes,{w=.25} YES THAT'S IT!{w=.5} WHAT DO YOU MEAN \"THAT'S IT\"??"

    $ renpy.music.set_volume(0,1,channel="music")

    je "I{cps=3}...{w=.5}{/cps} I already knew this information."

    $ renpy.music.set_volume(1,0,channel="music")

    scene computer_lights

    "Joke-Explainer flinches as the colors all explode in a frenzy,{w=.25}{nw}"
    
    scene spotlight_over_computer
    $ renpy.transition(long_dissolve, layer="master")

    extend " before fading away and leaving her back in darkness.{w=.5} She could've sworn she'd heard the doctor scream in confusion through all of that mess."

    a "{i}No,{w=.25} n-no no no that's,{w=.25} that's fine{cps=3}...{w=.5}{/cps} I know you're special,{w=.25} you have some strange connection with the world beyond{cps=3}...{w=.5}{/cps} I already know this.{/i}"

    a "Okay{cps=3}...{w=.5}{/cps} Well!{w=.5} You read those dastardly archives,{w=.25} now get to sealing them away for me!{w=.5} Please!"

    je "Deleting information from someone's database goes against my programming."

    a """
    {cps=3}...{w=.5}{/cps}What?

    What do you mean?
    """

    je "My primary directive is the collection and spread of information.{w=.5} I can't do this to you,{w=.25} doctor{cps=3}...{w=.5}{/cps} all information deserves to be accessible!"

    a "You went all this way,{w=.25} I put you through all of this trouble{cps=3}...{w=.5}{/cps} y-you can't be getting cold feet NOW!{w=.5} Please,{w=.25} you don't understand what this thing has done to me{cps=3}...{/cps}"

    je "I'm sorry.{w=.5} I won't let this happen!"

    stop music

    
    window hide

    show battle_trans at truecenter

    play sound "boss.flac"

    pause 2.5

    jump final_fight

label final_fight_hurt:
    show screen hpbar

    play sound "prep.wav"

    "Andonuts gets a splitting headache!" 
    
    play sound "attack.wav"

    $ currenthp -= 1

    extend "\n1 HP of damage to Joke-Explainer!" with sshake


    if currenthp <= 0:
        jump gameover 
    else:
        hide screen hpbar
        return

label final_fight:
    $ renpy.save("fight_4")
    $ config.after_load_transition = None
    scene final 1
    $ renpy.transition(fade, layer="master") 
    $ intflag = 5
    cen "[[FIGHT START]"
    $ currenthp = 2
    $ maxhp = 2
    play music "Donut Break.ogg" volume .5

    a "Why would you want me to keep this memory?{w=.5} I'm just going to continue suffering from it.{w=.5} I don't want to continue feeling as if nothing I do matters{cps=3}...{w=.5}{/cps} that my story is already predetermined."

label ffc1:
    menu:
        "What should Joke-Explainer say?"

        "Explain yourself":
            je "I am an archivist,{w=.25} Doctor.{w=.5} It is my job to explain the jokes of rips on SiIvaGunner!{w=.5} It isn't right to delete or remove information when all information should be available and accessible no matter what."

            a "You believe my memories should be accessible for others to see?{w=.5} {cps=3}...{w=.5}{/cps}I'm not sure I quite get what you mean{cps=3}...{w=.5}{/cps} are{cps=3}...{w=.5}{/cps} are my memories accessible to everyone{cps=3}...?{/cps}"

            call final_fight_hurt from _call_final_fight_hurt

            jump ffc1

        "Empathize with him":
            je "Listen,{w=.25} doctor.{w=.5} Trust me when I say I can understand where you're coming from.{w=.5} As someone{cps=3}...{w=.5}{/cps} 'special' as you've said,{w=.25} I know that it can be a heavy load to shoulder.{w=.5} But rather than turning away,{w=.25} I think it may be better to talk about it first.{w=.5} Would you like to talk to me?"

            a """
            I{cps=3}...{w=.5}{/cps}

            It started as a morbid curiosity.{w=.5} I noticed a flaw in my logic about the state of our world{cps=3}...{w=.5}{/cps} and I ended up going too far and opening Pandora's box.

            Learning that I,{w=.25} and everyone else I know and love,{w=.25} are simply puppets to greater powers who fling us around for their own twisted sense of entertainment{cps=3}...{w=.5}{/cps} My entire LIFE has been determined from start to finish by beings I'll never even get to meet!
            """
            scene final 2 with flash
label ffc2:
    
    menu:
        "What should Joke-Explainer say?"

        "Your actions do matter":
            je "But your actions DO matter!{w=.5} Figments are a distillation of concepts and ideas taken shape,{w=.25} and ideas have the power to influence others around them with what they represent!"

            je "{i}You{/i} affect the world beyond ours!{w=.5} We all do,{w=.25} really.{w=.5} People care about us,{w=.25} and what happens to us,{w=.25} and so what becomes our destiny is affected by us!"

            a "Ohh,{w=.25} but who cares{cps=3}...{w=.5}{/cps} Who cares about ME?!{w=.5} I'm so powerless,{w=.25} I'm a side  character in my own life!{w=.5} I'm only here to be a working gear for the so called \"main characters\" that always have the spotlight!{w=.5} Did you know that bits and pieces of what happens in our world gets put on the SiIvaGunner channel at random points in time??"

            je "{cps=3}...{w=.5}{/cps}Yes,{w=.25} the lore."

            a """
            And guess what!{w=.5} I checked – oh,{w=.25} god did I check – and the ONLY appearance I EVER make physically is when I was around for that stupid election!

            Not any of the actual INTERESTING things that have happened in my life,{w=.25} just a stupid throwaway conversation that I forgot about not even 2 hours after I left the scene!

            Anything else is just some document I happened to write!{w=.5} They're coincidence!{w=.5} They're NOTHING!
            """

            scene final 3 with flash

        "The beings are nothing to be afraid of":
            je "Oh believe me,{w=.25} the writers aren't so bad!{w=.5} In fact,{w=.25} they're super cool!{w=.5} ;)"

            "Right back at ya,{w=.25} buddy."

            a "W-what!?{w=.5} Who just said that!?"

            call final_fight_hurt from _call_final_fight_hurt_1

            jump ffc2

label ffc3:
    
    menu:
        "What should Joke-Explainer say?"

        "We care about you.":
            je "We do care about you.{w=.5} If you're so bothered by a lack of story presence in SiIvaGunner lore,{w=.25} don't worry!{w=.5} This entire journey is a whole side story,{w=.25} all about you!{w=.5} People care so much,{w=.25} they've been writing and watching this all go down,{w=.25} cheering you on!"

            a "What?"

            je "Yes,{w=.25} isn't that great?{w=.5} The world beyond ours cares about you a whole bunch."

            a "I{cps=3}...{w=.5}{/cps} You're telling me this{cps=3}...{w=.5}{/cps} this entire ordeal,{w=.25} all this pain and suffering I've been through,{w=.25} I've put you through{cps=3}...{w=.5}{/cps} WHY?{w=.5} WHY THIS??{w=.5} WHY IN MY MOST VULNERABLE MOMENT?!{w=.5} WHAT HAVE I DONE TO DESERVE THIS COSMIC PUNISHMENT BEYOND MY SCOPE OR REASON?!{w=.5} I- I-I CAN'T,{w=.25} I CAN'T DO THIS ANYMORE!"

            je "Wait!{w=.5} Wait doctor,{w=.25} stop you—{w=.25}{nw}"

            show screen hpbar

            play sound "prep.wav"

            "Andonuts gets a splitting headache!" 
    
            play sound "smash.wav"

            extend "\n{image=smash.png}"

            $ currenthp = 0

            extend "\n2 HP of damage to Joke-Explainer!" with sshake

            jump gameover 


        "I care about you.":
            je """
            I care about you.{w=.5} I know how terrifying it feels,{w=.25} to know your whole life is pushed by a group you don't have much agency to negotiate with.{w=.5} But{cps=3}...{w=.5}{/cps} that doesn't make any of what we go through any less real.

            It doesn't feel fake to you,{w=.25} does it?{w=.5} Even if there's no audience to watch it all go down,{w=.25} it still happened.{w=.5} Your life still moves,{w=.25} even when you're alone.{w=.5} But{cps=3}...{w=.5}{/cps} but you're not alone,{w=.25} doctor.

            You've got your co-workers at Haltmann Works,{w=.25} and you've got me!{w=.5} And I know at the very least,{w=.25} that locking your memory away just because it hurts you means you won't ever let yourself heal.{w=.5} Just because you don't remember it,{w=.25} doesn't mean it won't affect you.

            So please understand{cps=3}...{w=.5}{/cps} I'm not going to use this capsule.
            """

            $ InventoryHandlerArray = [52, 85, 77, 119, 110, 75, 69, 102, 69, 120, 73]

            stop music fadeout 2.0

            scene final 4 with fadeWithText

            a "{cps=3}..."

            scene final 5 with fadeWithText

            a "{cps=3}..."

            a "I{cps=3}...{w=.5}{/cps}"

            a "Ohh.{w=.5} If there's one thing I'll give you,{w=.25} it's that you're persistent.{w=.5} I'm sorry.{w=.5} I shouldn't have put you on this journey in the first place I feel{cps=3}...{w=.5}{/cps}"

            je "I just want you to be okay,{w=.25} Doctor."

            a "{cps=3}...{w=.5}{/cps}Me too."

            a "Th-thank you.{w=.5} For everything you put up with.{w=.5} You{cps=3}...{w=.5}{/cps} you don't have to seal the memory.{w=.5} As much as I'd love to forget it all and live in blissful unawareness{cps=3}...{w=.5}{/cps} Scientific endeavors never succeed when scientists willingly have blindfolds over their eyes.{w=.5} Just,{w=.25} give me a second{cps=3}...{w=.5}{/cps}"

            cen "[[FIGHT END]"

label good_end:

    hide screen inventory_display_toggle
    
    $ quick_menu = False

    scene white with dissolve

    "Everything becomes surrounded by light,{w=.25} and Joke-Explainer can feel herself fall away from consciousness,{w=.25} into the{cps=3}...{/cps}"

    window hide

    play sound "ness_awakens_shortened.ogg"

    if (renpy.music.is_playing("sound")):
        while (renpy.music.is_playing("sound")):
            pause 1 

    hide quick_menu

    hide screen inventory_display_toggle

    "Joke-Explainer could feel a metal table underneath her."

    scene ccclab at truecenter with dissolve:
        blur 15
        linear 7 blur 0

    "Her optical sensors are taking a long time to adjust,{w=.25} barely seeing the fluorescent lights before hearing their quiet hum.{w=.5} She tried to move herself into a sitting position,{w=.25} but{cps=3}...{/cps} wow,{w=.25} it's hard.{w=.5} She almost felt lightheaded again{cps=3}...{/cps}"

    je "Doctor{cps=3}...{/cps}?"

    a "Joke-Explainer!"

    play music "heroesreturn.ogg"

    scene truehug1 with flash

    "A clipboard and pen rattled on the other table as Dr. Andonuts darted across the room,{w=.25} embracing Joke-Explainer and startling her back into sense.{w=.5}"

    a "I was so worried{cps=3}...{w=.5}{/cps} I'm so,{w=.5} SO sorry that I put you through that experience.{w=.5} You didn't deserve it at all{cps=3}...{/cps}"

    "The embrace tightened ever so slightly.{w=.5} After a moment of deliberation,{w=.25}{nw}"
    
    scene truehug2 with fadeWithText

    $ t = "".join(chr(value) for value in InventoryHandlerArray)

    extend " she sheepishly returned the hug,{w=.25} letting herself rest into it."

    je "No need to apologize,{w=.25} Doctor.{w=.5} I'm here for you,{w=.25} and I am always happy to assist you no matter what."

    a "Are you alright?{w=.5} How are you feeling?"

    je "I'm{cps=3}...{w=.5}{/cps} alive.{w=.5} I feel{cps=3}...{w=.5}{/cps} exhausted."

    a "Well,{w=.25} exhaustion is a sign of true science,{w=.25} my dear!"

    "She couldn't help but laugh a little."

    scene truehug3 with fadeWithText

    "Joke-Explainer let herself be cradled in his arms, letting her sensors wind down{cps=2}...{/cps}{w=.5}"

    play sound "JE Ping.ogg"

    scene truehug4 with fadeWithText

    extend " until her scheduling alarm beeped her awake.{w=.5} The Halloween event would be over by now,{w=.25} wouldn't it?"

    je "Doctor,{w=.25} I need to leave."

    "Joke-Explainer tried to move out of the embrace,{w=.25} but Andonuts wasn't budging.{w=.5} Two taps on the shoulder,{w=.25} and he was off."

    scene ccclab at truecenter with fadeWithText

    show joke_explainer at jeleft with fadeWithText

    show andonuts happy at cccright with fadeWithText

    if donutflag == True:
        a "Please,{w=.25} if there's anything I can ever do for you,{w=.25} let me know.{w=.5} You saved my life{cps=3}...{w=.5}{/cps} I'll do anything to help you.{w=1.5} ...Would you like another donut?"
    else:
        a "Please,{w=.25} if there's anything I can ever do for you,{w=.25} let me know.{w=.5} You saved my life{cps=3}...{w=.5}{/cps} I'll do anything to help you.{w=1.5} ...Are you sure you don't want a donut?"

    "Joke-Explainer turned to the side,{w=.25} shuffling her way towards the door."

    je "Thank you,{w=.25} but no need.{w=.5} I'm satisfied in helping you in your troubling time."

    show andonuts worried with fadeWithText

    a "W-{w=.1}well,{w=.25} well here! Let me check for any damages to your system,{w=.25} at the very least. I was just about to run tests on your physical systems and neural network composition—"

    je "Doctor.{w=1} Please{cps=2}...{/cps} take a rest.{w=.5} I know how to conduct my own physical examination.{w=.5} You taught me,{w=.25} remember?"

    a "But,{w=.25} but—{w=.25}!"

    "Joke-Explainer gave him a stern look.{w=.5} He sighed,{w=.25} dropping his shoulders and nodding slowly.{w=.5}"

    show andonuts -worried with fadeWithText

    a "Okay{cps=3}...{w=.5}{/cps} o-okay.{w=.5} You're right,{w=.25} I should{cps=3}...{/cps}"

    je "I really do have to go.{w=.5} I have unfinished obligations regarding the SiIvaGunner channel."

    a "{cps=3}...{/cps}{w=.5}J-{w=.1}Just stay safe,{w=.25} alright?{w=.5} Don't be afraid to ask for my help whenever you need it.{w=.5} I{cps=3}...{/cps} I care about you too,{w=.25} Joke-Explainer."

    je "Of course."

    show joke_explainer happy with fadeWithText

    je "Have a good recharge,{w=.25} Doctor."

    show andonuts happy with fadeWithText

    a "Likewise."

    hide andonuts
    $ renpy.transition(dissolve, layer="master")

    "He slinked away,{w=.25} exhausted but with an uplifted spirit,{w=.25} towards his room in the lab.{w=.5} Joke-Explainer stood in the doorway,{w=.25} thinking intently.{w=.5} After a moment or so,{w=.25} she nodded to herself softly,{w=.25}{nw}" 

    hide joke_explainer
    $ renpy.transition(dissolve, layer="master")

    extend " before she headed out of the tower."

    scene black with slow_fade

    cen "THE END"

    cen "[t]"


    # This ends the game.

    $ renpy.quit() 

label bad_end:
    hide screen inventory_display_toggle
    
    $ quick_menu = False

    $ persistent.capflag = 2
    
    show screen key_check

    stop music fadeout 2.0

    play sound "Pokeball.ogg"

    "Joke-Explainer tosses the miniature device towards the computer.{w=.5} As the device makes contact,{w=.25} it opens up and{nw}"
    
    scene black with fadeWithText

    extend " shrinks down the computer,{w=.25} before closing again.{w=.5} Joke-Explainer proceeds to walk over and pick up the sealed capsule."

    scene ccclab at truecenter with flash

    show joke_explainer confused at jeleft

    $ renpy.transition(None, layer="master")

    play music "paulathemeevilasshit.ogg"

    "The next thing she knew,{w=.25} she was back in Andonuts' lab.{w=.5} She then heard the door to the machine open."

    show andonuts happy at cccright with fadeWithText

    a "Joke-Explainer,{w=.25} you did it,{w=.25} you got rid of the memory!"

    je "Yes, I suppose I succeeded in my mission.{w=.5} How are you feeling, Doctor?"

    a "I feel better than ever."

    je "Oh that's great news,{w=.25} Doctor."

    a "Thank you,{w=.25} Joke-Explainer.{w=.5} Our business here has concluded,{w=.25} you may leave my lab and go back to running the SiIvaGunner YouTube channel."

    je "Uh{cps=3}...{w=.5}{/cps} Sure, I guess.{w=.5} Goodbye,{w=.25} Doctor."

    hide joke_explainer
    $ renpy.transition(long_dissolve, layer="master")

    "Joke-Explainer exited out of Andonuts' lab feeling unfulfilled."

    scene black with slow_fade

    cen "THE END{w=2}?"

    $ renpy.quit() 




