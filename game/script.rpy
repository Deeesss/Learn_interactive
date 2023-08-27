# Script hry funguje v tomto súboru.

# Set up LayeredImage Sprites
layeredimage petra:
    group base auto:
        attribute casual default

    if casual:
        pos (0, 40)
        "petra_headband"
        
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


    scene room

    # Toto zobrazí charakter/osobu
    show petra happy at right:
        # Toto umiestňuje charakter
        yoffset 250
        xoffset 300
    # Toto stmavuje obrazovku alebo rozjasnuje 
    with fade

    # Toto púšťa hudbu, fadein od ticha do plnej hlasitosti na začiatku prehrávania, fadeout určuje ako 
    # dlho bude hudba postupné stíchať z plnej hlasitosti do ticha
    $ play_music(garden, fadein=2.0, fadeout=2.0)

    # Toto zobrazuje achievementy, neni to úplny kod ale ako základ zatial stačí
    $ achievement.grant("Beginning")

 

    # Toto zobrazuje text.

    Petra "AAAAAH, dobré ráno všetkým"
    show petra neutral with dissolve

    Petra "Toto je moj príbeh Game testerky"

    Petra "Začínam novú etapu, potrebujem vylepšiť svoje znalosti testera a programátora"

    Petra "Momentálne mám v hlave Python."

    # Toto zobrazuje výrazy v tvári
    show petra happy with dissolve

    Petra "Všetko je v podstate o tom nastavení a motivácii"

    Petra "A moja motivácia je hlavne mať velmi dobrý život"

    Petra "A najbližšie roky to vidím na nové auto, byt, výlety po svete"

    Petra "Žijem s mojou veľmi dobrou kamarátkou Zuzkou, Zuzka sa je velmi úspešná osoba narozdiel odomňa, krásna, múdra, úspešná"

    Petra "A ja ?"
    show petra upset with dissolve

    Petra "Mám čo doháňať a učiť sa od nej"

    Petra "Pred nedávnom si práve kúpila byt a chystá sa školou postupne zlepšovať svoje znalosti až kým sa nestane manažerkou"

    Petra "To ja som trošku stará škola, mám iba nejaké vzdelanie a všetko sa učím sama alebo s pomocou kamarátov alebo kolegou"

    Petra "Mám pred sebou ešte zaujímavú cestu, myslím si že to zvládnem bez problémov"

    Petra "Lenže predomňou stojí rozhodnutie s ktorým sa musím popasovať"
    
    Petra "Čo mi hovorí dokým sa my rozprávame tak ona už je hore a určite niečo robí produktívne"
    show petra happy with dissolve

    Petra "Pokial teda nepozerá Shorts"

    Petra "To sú krátke videa ktoré su v dnešnej dobe populárne a ludia s tým dokážu zabiť kopec času"

    Petra "Toto je jej občas úchylka, sama je ako sa tomu hovorí Bloger/Influencer a toto jej záluba"

    Petra "Niekedy premýšlam čo všetko stíha, ona má práve povahu čo nikdy neni spokojná pokial nemá celkovo využitého svojho času"

    Petra "Oproti mne čo rada oddychuje a maká hlavne keď je chuť tak to je rozdiel, ale je pravda že svoju prácu robím poctivo a snažím sa"

    Petra "Ja ale viem čo chcem a keď to dosiahnem tak to bude genialne"

    Petra "Ona je vždy skorej hore ako ja pokial náhodou nemá homeoffice čo vždy spí dokedy chce"

    Petra "Mám ju velice rada, hovorím jej baleno"

    Petra "Nepýtajte sa ako to vzniklo sama neviem"

    show petra smile with dissolve

    show zuzka smile at left:
        yoffset 250
        xoffset -300

    Petra "Ahoj, už som hore..."

    show zuzka smile with dissolve
    
    Zuzka "Ahoj, Petra ako sa spalo"

    Petra "Ale velmi dobre, pojdeme sa najesť?"

    Zuzka "Počkaj odošlem niečo.."
    show zuzka angry with dissolve

    Zuzka "No kam by si chcela ísť?"

    Petra "Do mekáču"

    Zuzka "Samozrejme mohla som si myslieť"

    Zuzka "Pozri na seba jak vyzeráš, takýmto tempom pribereš"

    Petra "Ďakujem ďakujem"

    Zuzka "Ech šoferujem teda, aj tak ťa musím vyhodiť u práce"

    Petra "Takže toto je moje žrút..."

    Petra "Mám rada túto E90"

    Zuzka "Mne tiež ale toto hobby je finančne náročne"

    Petra "Ja viem, preto musím zárabať viac"

    Petra "aaaaaaaaaaaaaah"

    Zuzka "Čo zas robíš ??? Ech nevyjadrujem sa"

    Petra "Kludne šoferuj, dneska toho mám viac v hlave a na práci  tak by som rada začala pracovať už teraz"

    Zuzka "Ty si s toho auta robíš kancelář"

    Petra "Nemožem strácať čas, musím sa rozhodnúť"

    Petra "Musím sa rozhodnúť čo si zvolím"

    Zuzka "Jaaj toto máš namysli, skús to premýslieť čo najskor a vyber si to najlepšie čo sa ti bude lubiť"
  
    Petra  "Takže naštartujem.."



    

   

   



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

            $ achievement.grant("Completionist")

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