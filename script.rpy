# TO-DO
# make inventory better / work
# sfxs
# lightning

# The game starts here.

label main_menu:
    return

label start:
    $ quick_menu = False

    t "The following experience features yuri."
    
    menu:
        t "Do you consent to yuri?"

        "Yes": 
            t "Please enjoy the yuri."
    
        "No":
            t "fuck u, saying u don't consent to yuri is not nice >:\["
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
    
    December 22{fast}{nw}
    
    December 22n{fast}{nw}
        
    December 22nd{fast}{nw}
        
    December 22nd,{fast}{nw}
    
    December 22nd, {fast}{nw}

    December 22nd, 2{fast}{nw}
    
    December 22nd, 20{fast}{nw}
    
    December 22nd, 202{fast}{nw}

    December 22nd, 2024{fast}
    """

    "On the outskirts of Grandiose City…"
    "two robots were huddled together, trying to survive the harsh cold."
    "That is until…"

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
    
    "Meanwhile, lower in the tower, in Dr. Andonuts' lab..."

    scene ccclab at truecenter with dissolve
    
    play music snowblind
    
    t "andonuts@HWCdesk4012:/$ exutils get stat CYP-XPL-001\nPOWER RESERVES: 100\%\nCONDITION: STABLE"
    t "andonuts@HWCdesk4012:/$ exutils get stat n919-XPL-001\nPOWER RESERVES: 100\%\nCONDITION: STABLE"
    
    show andonuts worried at flip, cccleft with dissolve
    "The doctor read over the pair's logs closely.\nThey had clearly been worn out from their time away from the laboratory, but at least they were fine now -{w=.5} and safely resting."

    scene black at truecenter with Dissolve(2.0)
    #TODO: show spheric flashback art
    "It had been approximately a few days since the Spherics had raided the lab.\n"
    extend "The attack was sudden and unprompted,{w=.5} but clearly intentional."
    "Was the attack caused by Andonuts’ research into the SilvaGunner albums?"
    extend "\nAll signs seemed to point to that being the case."
    #TODO: show JE and andonuts escape flashback art
    "Whatever the cause was, Andonuts and Joke-Explainer had quickly rushed out of the lab to avoid injury." 
    "The other two - ARG-Explainer and Cipher-Explainer - were pursued by the Spherics and forced to evacuate farther, ending up lost in the tundra outside of Grandiose City." 
    extend " Furthermore, they were seperated - only being able to communicate over wireless transmission."

    q "CogDis hardcodes which side a character's title is on.\n(left for joke explainer and right for andonuts respectively)" (window_background=cl) # use contents between the parenthesis for characters on the left
    q "This fix is.. bad and ugly, but it gets around said hardcoding" (window_background=cr, who_xalign=1.0, who_xpos=1720) # use contents between the parenthesis for characters on the right

    # remove when editing script further, this ends the script early and returns it to the disclaimer
    return