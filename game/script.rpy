# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

###########################################################################
############# styles ######################################################



style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True
    
style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72
    
style choice_button_text:
    color "0000FF"
    font "courbd.ttf"
    
################CHARACTERS########################

define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)


#this is just to show you what a default character would look like. the colo*Ur is the text colour of the box, not of the textbox ^-^
define p = Character("PLACEH", color='#FFFFFF', image="placeh", window_background="gui/textbox_cobalt.png", who_outlines=[ (4, "#005682") ],)
define o = Character("OLDERE", color='#FFFFFF', image="oldere", window_background="gui/textbox_jade.png", who_outlines=[ (4, "#008141") ],)
#you need to edit the outlines depending on blood colour!

############IMAGES AND SHIT#################
image placeh = Image("images/game_bro.png", ypos=730)
image oldere = Image("images/s.png", ypos=730)
#i'd advise you keep ypos the same for the important characters!
#also, i've left an ardata sprite in there just to help you to keep everything in proportion

image bg alternia = "images/background1.png"

## COMMON TRANSFORMS ##
#these are all transforms to make your sprite bounce around a little! it's super useful for making your game more dynamic

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    
transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    
transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640
    
transform shudder:
    
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4
    
transform lowered:
    ypos 730
    linear 0.75 ypos 765
    
transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat
    
transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat
    
transform shuddering:
    
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat
    
transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

#Quickly push sprite to side of screen    
transform shoveright:
    
    linear 0.1 xpos 960
    
transform shoveleft:
    
    xpos 640
    linear 0.1 xpos 320
    
transform shoveoffleft:
    
    linear 0.1 xpos -320
    
#Quickly push sprite to default position, from offscreen bottom
transform shoveup:
    
    xpos 640 ypos 1440
    linear 0.1 ypos 730

# The game starts here.
label start:
    
    # This is used to easily add a formatted '>' to the start of choices in menus.
    $ pick = "{color=#000000}>{/color}"
    
    $ quick_menu = True
    
    $ volume1 = True

    jump start2
            
label start2:
    
    # Stop main menu music, or any other music playing, and transition to volume select.
    stop music fadeout 1.5
    
    show image "gui/main_menu.png"
    
    window hide
    
    scene black with Dissolve(1.5)
    
    $ main_menu = True
    
    call screen vol_select()
    
    stop music fadeout 1.5
    
label volumeone:
    
    $ renpy.block_rollback()
    
    $ main_menu = False
    
    show image "gui/game_menu.png"
    
    window hide
    
    scene black with Dissolve(1.5)
    
    op "You have just crash landed on a planet called Alternia, and staggered from the smouldering wreckage of your ship."
    
    op "You are now completely alone in a strange world."
    
    op "Desperate for information, for provisions, and possibily a bit of medical attention."
    
    op "But most of all, you are desperate for..."
    
    op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"
    
    op "Won't someone on this godforsaken rock be your buddy?"
    
    op "Any weirdo will do. You're not that picky."
    
    op "Hang on... What's this now? Is someone approaching...?"
    
    call screen troll_select1
    
    with Pause(0.25)
    
    return
    
#note: to edit the starting labels, you have to go into screens, under trollselect1. there might be some old gunk in there btw.
label placeh:
    
    $ renpy.block_rollback()

    scene black with Dissolve(1.0)
    
    scene bg alternia with dissolve
    
    $ quick_menu = True
    
    "Yes, someone is approaching! A strange, grey-skinned alien, with some other modifier that I don't really want to come up with right now. Who could it be????????"

    window hide
    
    play music "music/ASSGORE.mp3" loop

    show placeh with moveinbottom
    
    p "Wow, this sure is some sample text!"
    
    show placeh at twitch
    
    p "wow"
    
    show placeh at nod
    
    p "yeah"
    
    show placeh at shoveoffleft
    
    p "And those were sure some transforms!"
    
    #this is where it ends. OOF.
    
    $ renpy.pause(0.5)
            
    $ quick_menu = False
            
    play music "music/game_over.mp3" fadeout 1.0
            
    scene weegee with Dissolve(1.0)
            
    $ renpy.pause()
                
    stop music fadeout 1.0
            
    scene black with Dissolve(1.0)
            
    return
    
label oldere:
    
    show oldere with moveinbottom
                
    o "Kung pow penis."            
                
    $ renpy.pause()
                
    stop music fadeout 1.0
            
    scene black with Dissolve(1.0)            
            
            
    
    
    
    


return
