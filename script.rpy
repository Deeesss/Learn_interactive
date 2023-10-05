init python:
    # My def smooth move character
    def smooth_move_character(character, target_x, target_y, duration):
        pass
    # My def shake screen
    def shake_screen(intensity, duration):

        pass



# Script hry funguje v tomto súboru.


# Set up LayeredImage Sprites
layeredimage petra:
    group base auto:
        attribute casual default

    if casual:
        pos (0, 40)
        "petra_surprise"
        
    group face auto:
        attribute neutral default
    
layeredimage zuzka:
    group base auto:
        attribute smile default

    if casual:
        pos (0, 40)
        "zuzka_smile" 
     

    group face auto:
        attribute smile default



default casual = True

define Petra = Character("Petra", color="#f88787", image="petra")
define Petra_nvl = Character("Petra", color="#f88787", kind=nvl, image="petra")
define Zuzka = Character("Zuzka", color="#f88781", image="zuzka") 
define nar_nvl = nvl_narrator


image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 0.5 zoom 0.5

default persistent.firstlaunch = False

label splashscreen:

    scene black

# The first time the game is launched, players can set their accessibility settings.
    if not persistent.firstlaunch:


        call screen splash_settings
# This screen will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.firstlaunch = True
# Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=60} No pressure":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0

    # The first time the game is launched, players cannot skip the animation
    if not persistent.seen_splash:

    # No input will be detected for the set time stated.
    # Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)

        $ persistent.seen_splash = True

    # Players can skip the animation in subsequent launches of the game.
    else:

        if renpy.pause(8.5):

            jump skip_splash

    scene black
    with fade

    label skip_splash:

        pass

    return

## Tuto začína hra.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene nice_place

    # Toto zobrazí charakter/osobu
    show petra happy at center:
        # Toto umiestňuje charakter
        yoffset 200
        xoffset 100
    # Toto stmavuje obrazovku alebo rozjasnuje 
    with fade

    # Toto púšťa hudbu, fadein od ticha do plnej hlasitosti na začiatku prehrávania, fadeout určuje ako 
    # dlho bude hudba postupné stíchať z plnej hlasitosti do ticha
    $ play_music(garden, fadein=2.0, fadeout=2.0)

    # Toto zobrazuje achievementy, neni to úplny kod ale ako základ zatial stačí
    $ achievement.grant("Beginning")

    
 

    # Toto zobrazuje text.
    Petra "Greetings everyone."
    show petra neutral with dissolve
    $ smooth_move_character(Petra, 800, 400, 2.0)


    
    


    Petra "I would like to show a small sample of what they have for this character, Petra."
    # Toto zobrazuje výrazy v tvári
    show petra happy with dissolve
    Petra "This character is a sample from an author who gave me the opportunity to use this character."

    
    show petra upset with dissolve
    Petra "The music and images were composed by AI, but it's still a new approach that may have copyright issues; you never know."
    show petra happy with dissolve
    Petra "Behind every change are expressions and animations with Python language commands and the possibility of using LayeredImage, which is utilized by Renpy itself."

    menu: 
        # menu: Blok menu v Ren'Py slúži na definovanie možností výberu pre hráča. V tomto bloku môžete uviesť rôzne textové možnosti, ktoré hráč môže vybrať. Napríklad:
        "You like this edit":
            jump  you_like_that_really
    
            # jump: Príkaz jump sa používa na presmerovanie priebehu príbehu na určené návestie (label). Napríklad:
        "No i dont like this edit":
            
            jump  needs_much_work
    label you_like_that_really:
        show petra happy at center, Shake(None, 1.0, dist=5) with dissolve
            
        Petra "Thank you very much, but I want to try harder."
        $ sshake = Shake((5, 20, 0.5, 0.3), 1.0, dist=15)
        Petra "I think its not about python, its code what i need understand"
        Petra "This choice give me another function in Renpy"
        jump continuation
        # label: label sa používa na definovanie určitého bodu v príbehu, kde sa môžete vrátiť pomocou jump. Label je ako označený bod v príbehu. Napríklad:
    pass
    


        
    label needs_much_work:
        show petra upset with dissolve
        Petra "Yes, I need to work more on my project."
        Petra "I do more code in future"
        show petra happy with dissolve
        Petra "Its not easy, but its fun"
        Petra "This choice give me another function in Renpy"
        jump continuation
    pass           

    
    label continuation:
         

        pass

    Petra "You can Learn with Renpy Python, thats why i try this novel framework"
    Petra "It's relatively straightforward, but problems may arise when layering, which can be a challenge with file naming and Python code entry."
    Petra "It's such a simple way to learn Python, with this."
    Petra "Thank you very much for the opportunity and for watching this game to the end."



    

   

   



    ## "This is done with the special {color=#32CD32}{i}ic{/i}{/color} speaker tag we defined in {color=#32CD32}{i}accessibility.rpy{/i}{/color}."This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

   

## End Credits
label credits:

    ## We hide the quickmenu for the last part of the game so they don't
    ## appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits(15.0)

    $ persistent.credits_seen = True

    scene black
    with fade

    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:

        pass

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results

    centered "Fin"

    hide screen results

    if persistent.game_clear:

        pass

    ## Do you want to leave some author's notes or a hidden message for your dedicated fans?
    ## This will check if they've seen all that the game has to offer.
    else:

        if readtotal == 100:

            $ achievement.grant("Try")

            ## Due to the way that $ percent() works, we need to make this a text displayable
            ## or else it'll try to count it too.
            show text "{size=60}{color=#ffffff}You've unlocked a special message.\nAccess it through the Extras Menu.{/color}{/s}":
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 1.0 alpha 1.0

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## We re-enable the quickscreen as the credits are over.
    $ quick_menu = True

    # This ends the game.
    return