# Cover image

image cover = "images/cover.png"

# Characters
define S = Character( "Screenshot_37" )
define b = Character( "Bugman" )
define m = Character( "Moroa" )
define p = Character( "Pablo" )
image Screenshot_37 = "images/characters/Screenshot_37.png"
image bugman = "images/characters/bugman.png"
image moroa = "images/characters/moroa.png"
image pablo = "images/characters/pablo.png"

# NPCs
image Screenshot_37 = "images/npcs/Screenshot_37.png"
image _empty = "images/npcs/_empty.png"
image _empty2 = "images/npcs/_empty2.png"
image beba_morki_pas = "images/npcs/beba_morki_pas.png"
image cuvar_bruno = "images/npcs/cuvar_bruno.png"
image cuvar_luka = "images/npcs/cuvar_luka.png"
image gospodin_rakovica = "images/npcs/gospodin_rakovica.png"
image gusar = "images/npcs/gusar.png"
image konjusar_sarko = "images/npcs/konjusar_sarko.png"
image konobar_kalamarko_krakovic = "images/npcs/konobar_kalamarko_krakovic.png"
image kralj_dante = "images/npcs/kralj_dante.png"
image kraljica_marie = "images/npcs/kraljica_marie.png"
image kuhar_branko_skockani = "images/npcs/kuhar_branko_skockani.png"
image mag_iz_dubina = "images/npcs/mag_iz_dubina.png"
image marina = "images/npcs/marina.png"
image marina_mala = "images/npcs/marina_mala.png"
image princ_salvadore = "images/npcs/princ_salvadore.png"
image princeza_frida = "images/npcs/princeza_frida.png"
image princeza_rakova = "images/npcs/princeza_rakova.png"
image profesor_sipa_tintic = "images/npcs/profesor_sipa_tintic.png"
image puz_kadrinalac = "images/npcs/puz_kadrinalac.png"
image snorkijevac_joja = "images/npcs/snorkijevac_joja.png"
image snorkijevac_ratko = "images/npcs/snorkijevac_ratko.png"
image snorkijevac_zarko = "images/npcs/snorkijevac_zarko.png"
image snorkijevac_zivko = "images/npcs/snorkijevac_zivko.png"
image vegimal1 = "images/npcs/vegimal1.png"
image vegimal2 = "images/npcs/vegimal2.png"
image vegimal3 = "images/npcs/vegimal3.png"
image vegimal4 = "images/npcs/vegimal4.png"
image vegimals13 = "images/npcs/vegimals13.png"
image vegimals24 = "images/npcs/vegimals24.png"
image zig = "images/npcs/zig.png"
image zig_mali = "images/npcs/zig_mali.png"

# Backgrounds
image brod = "images/locations/brod.png"
image dvor = "images/locations/dvor.png"
image fridina_soba = "images/locations/fridina_soba.png"
image glavni_trg = "images/locations/glavni_trg.png"
image grad_topla_vodica = "images/locations/grad_topla_vodica.png"
image hram = "images/locations/hram.png"
image knjiznica = "images/locations/knjiznica.png"
image konjusnice = "images/locations/konjusnice.png"
image krcma = "images/locations/krcma.png"
image nastamba_maga = "images/locations/nastamba_maga.png"
image pablova_soba = "images/locations/pablova_soba.png"
image pecina_hobotnice = "images/locations/pecina_hobotnice.png"
image prokleti_gusari = "images/locations/prokleti_gusari.png"
image unutar_puza = "images/locations/unutar_puza.png"
image vatreno_gorje = "images/locations/vatreno_gorje.png"
image vijecnica = "images/locations/vijecnica.png"
image vodoskok_snorkijevci = "images/locations/vodoskok_snorkijevci.png"
image zeljezarija = "images/locations/zeljezarija.png"
image zemlja_rakova = "images/locations/zemlja_rakova.png"

# Sound effects
define snd = ""

init python:
    def play_sound_effect():
        renpy.sound.play( snd )

screen custom_listener():
    key "K_z" action [ Function( play_sound_effect ) ]

label start:
    show screen custom_listener
    python:
        import json
        cscn = " "
        cshw = [ "", "", "" ]
        pos = 0
    jump next

label next:
    python:
        import json

        with renpy.open_file( 'next.json' ) as file:
            data = json.load( file )

        # Set the variables based on the JSON data
        scn = data[ "scene" ]
        shw = data[ "show" ]
        bgm = "audio/bcgsound/" + data[ "bgm" ] + ".mp3"
        snd = "audio/soundeffects/" + data[ "sound" ] + ".mp3"

    # SOUND
    play music bgm if_changed
    # SCENES

    if scn == "brod" and cscn != "brod":
        jump brod
    if scn == "dvor" and cscn != "dvor":
        jump dvor
    if scn == "fridina_soba" and cscn != "fridina_soba":
        jump fridina_soba
    if scn == "glavni_trg" and cscn != "glavni_trg":
        jump glavni_trg
    if scn == "grad_topla_vodica" and cscn != "grad_topla_vodica":
        jump grad_topla_vodica
    if scn == "hram" and cscn != "hram":
        jump hram
    if scn == "knjiznica" and cscn != "knjiznica":
        jump knjiznica
    if scn == "konjusnice" and cscn != "konjusnice":
        jump konjusnice
    if scn == "krcma" and cscn != "krcma":
        jump krcma
    if scn == "nastamba_maga" and cscn != "nastamba_maga":
        jump nastamba_maga
    if scn == "pablova_soba" and cscn != "pablova_soba":
        jump pablova_soba
    if scn == "pecina_hobotnice" and cscn != "pecina_hobotnice":
        jump pecina_hobotnice
    if scn == "prokleti_gusari" and cscn != "prokleti_gusari":
        jump prokleti_gusari
    if scn == "unutar_puza" and cscn != "unutar_puza":
        jump unutar_puza
    if scn == "vatreno_gorje" and cscn != "vatreno_gorje":
        jump vatreno_gorje
    if scn == "vijecnica" and cscn != "vijecnica":
        jump vijecnica
    if scn == "vodoskok_snorkijevci" and cscn != "vodoskok_snorkijevci":
        jump vodoskok_snorkijevci
    if scn == "zeljezarija" and cscn != "zeljezarija":
        jump zeljezarija
    if scn == "zemlja_rakova" and cscn != "zemlja_rakova":
        jump zemlja_rakova

    if "Screenshot_37" in shw and "Screenshot_37" not in cshw:
        jump Screenshot_37
    if "bugman" in shw and "bugman" not in cshw:
        jump bugman
    if "moroa" in shw and "moroa" not in cshw:
        jump moroa
    if "pablo" in shw and "pablo" not in cshw:
        jump pablo
    if "Screenshot_37" in shw and "Screenshot_37" not in cshw:
        jump Screenshot_37
    if "_empty" in shw and "_empty" not in cshw:
        jump _empty
    if "_empty2" in shw and "_empty2" not in cshw:
        jump _empty2
    if "beba_morki_pas" in shw and "beba_morki_pas" not in cshw:
        jump beba_morki_pas
    if "cuvar_bruno" in shw and "cuvar_bruno" not in cshw:
        jump cuvar_bruno
    if "cuvar_luka" in shw and "cuvar_luka" not in cshw:
        jump cuvar_luka
    if "gospodin_rakovica" in shw and "gospodin_rakovica" not in cshw:
        jump gospodin_rakovica
    if "gusar" in shw and "gusar" not in cshw:
        jump gusar
    if "konjusar_sarko" in shw and "konjusar_sarko" not in cshw:
        jump konjusar_sarko
    if "konobar_kalamarko_krakovic" in shw and "konobar_kalamarko_krakovic" not in cshw:
        jump konobar_kalamarko_krakovic
    if "kralj_dante" in shw and "kralj_dante" not in cshw:
        jump kralj_dante
    if "kraljica_marie" in shw and "kraljica_marie" not in cshw:
        jump kraljica_marie
    if "kuhar_branko_skockani" in shw and "kuhar_branko_skockani" not in cshw:
        jump kuhar_branko_skockani
    if "mag_iz_dubina" in shw and "mag_iz_dubina" not in cshw:
        jump mag_iz_dubina
    if "marina" in shw and "marina" not in cshw:
        jump marina
    if "marina_mala" in shw and "marina_mala" not in cshw:
        jump marina_mala
    if "princ_salvadore" in shw and "princ_salvadore" not in cshw:
        jump princ_salvadore
    if "princeza_frida" in shw and "princeza_frida" not in cshw:
        jump princeza_frida
    if "princeza_rakova" in shw and "princeza_rakova" not in cshw:
        jump princeza_rakova
    if "profesor_sipa_tintic" in shw and "profesor_sipa_tintic" not in cshw:
        jump profesor_sipa_tintic
    if "puz_kadrinalac" in shw and "puz_kadrinalac" not in cshw:
        jump puz_kadrinalac
    if "snorkijevac_joja" in shw and "snorkijevac_joja" not in cshw:
        jump snorkijevac_joja
    if "snorkijevac_ratko" in shw and "snorkijevac_ratko" not in cshw:
        jump snorkijevac_ratko
    if "snorkijevac_zarko" in shw and "snorkijevac_zarko" not in cshw:
        jump snorkijevac_zarko
    if "snorkijevac_zivko" in shw and "snorkijevac_zivko" not in cshw:
        jump snorkijevac_zivko
    if "vegimal1" in shw and "vegimal1" not in cshw:
        jump vegimal1
    if "vegimal2" in shw and "vegimal2" not in cshw:
        jump vegimal2
    if "vegimal3" in shw and "vegimal3" not in cshw:
        jump vegimal3
    if "vegimal4" in shw and "vegimal4" not in cshw:
        jump vegimal4
    if "vegimals13" in shw and "vegimals13" not in cshw:
        jump vegimals13
    if "vegimals24" in shw and "vegimals24" not in cshw:
        jump vegimals24
    if "zig" in shw and "zig" not in cshw:
        jump zig
    if "zig_mali" in shw and "zig_mali" not in cshw:
        jump zig_mali

    $ renpy.pause ()


# SCENE LABELS

label brod:
    $ cscn = "brod"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene brod
    jump next

label dvor:
    $ cscn = "dvor"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene dvor
    jump next

label fridina_soba:
    $ cscn = "fridina_soba"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene fridina_soba
    jump next

label glavni_trg:
    $ cscn = "glavni_trg"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene glavni_trg
    jump next

label grad_topla_vodica:
    $ cscn = "grad_topla_vodica"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene grad_topla_vodica
    jump next

label hram:
    $ cscn = "hram"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene hram
    jump next

label knjiznica:
    $ cscn = "knjiznica"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene knjiznica
    jump next

label konjusnice:
    $ cscn = "konjusnice"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene konjusnice
    jump next

label krcma:
    $ cscn = "krcma"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene krcma
    jump next

label nastamba_maga:
    $ cscn = "nastamba_maga"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene nastamba_maga
    jump next

label pablova_soba:
    $ cscn = "pablova_soba"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene pablova_soba
    jump next

label pecina_hobotnice:
    $ cscn = "pecina_hobotnice"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene pecina_hobotnice
    jump next

label prokleti_gusari:
    $ cscn = "prokleti_gusari"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene prokleti_gusari
    jump next

label unutar_puza:
    $ cscn = "unutar_puza"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene unutar_puza
    jump next

label vatreno_gorje:
    $ cscn = "vatreno_gorje"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene vatreno_gorje
    jump next

label vijecnica:
    $ cscn = "vijecnica"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene vijecnica
    jump next

label vodoskok_snorkijevci:
    $ cscn = "vodoskok_snorkijevci"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene vodoskok_snorkijevci
    jump next

label zeljezarija:
    $ cscn = "zeljezarija"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene zeljezarija
    jump next

label zemlja_rakova:
    $ cscn = "zemlja_rakova"
    $ pos = 0
    $ cshw = [ "", "", "" ]
    scene zemlja_rakova
    jump next


# CHARACTER AND NPC LABELS

label Screenshot_37:
    $ cshw[ pos ] = "Screenshot_37"
    if pos == 0:
        show Screenshot_37 with dissolve 
    elif pos == 2:
        show Screenshot_37 at left with moveinleft
    elif pos == 1:
        show Screenshot_37 at right with moveinright
    
    $ pos += 1
    jump next

label bugman:
    $ cshw[ pos ] = "bugman"
    if pos == 0:
        show bugman with dissolve 
    elif pos == 2:
        show bugman at left with moveinleft
    elif pos == 1:
        show bugman at right with moveinright
    
    $ pos += 1
    jump next

label moroa:
    $ cshw[ pos ] = "moroa"
    if pos == 0:
        show moroa with dissolve 
    elif pos == 2:
        show moroa at left with moveinleft
    elif pos == 1:
        show moroa at right with moveinright
    
    $ pos += 1
    jump next

label pablo:
    $ cshw[ pos ] = "pablo"
    if pos == 0:
        show pablo with dissolve 
    elif pos == 2:
        show pablo at left with moveinleft
    elif pos == 1:
        show pablo at right with moveinright
    
    $ pos += 1
    jump next

label Screenshot_37:
    $ cshw[ pos ] = "Screenshot_37"
    if pos == 0:
        show Screenshot_37 with dissolve 
    elif pos == 2:
        show Screenshot_37 at left with moveinleft
    elif pos == 1:
        show Screenshot_37 at right with moveinright
    
    $ pos += 1
    jump next

label _empty:
    $ cshw[ pos ] = "_empty"
    if pos == 0:
        show _empty with dissolve 
    elif pos == 2:
        show _empty at left with moveinleft
    elif pos == 1:
        show _empty at right with moveinright
    
    $ pos += 1
    jump next

label _empty2:
    $ cshw[ pos ] = "_empty2"
    if pos == 0:
        show _empty2 with dissolve 
    elif pos == 2:
        show _empty2 at left with moveinleft
    elif pos == 1:
        show _empty2 at right with moveinright
    
    $ pos += 1
    jump next

label beba_morki_pas:
    $ cshw[ pos ] = "beba_morki_pas"
    if pos == 0:
        show beba_morki_pas with dissolve 
    elif pos == 2:
        show beba_morki_pas at left with moveinleft
    elif pos == 1:
        show beba_morki_pas at right with moveinright
    
    $ pos += 1
    jump next

label cuvar_bruno:
    $ cshw[ pos ] = "cuvar_bruno"
    if pos == 0:
        show cuvar_bruno with dissolve 
    elif pos == 2:
        show cuvar_bruno at left with moveinleft
    elif pos == 1:
        show cuvar_bruno at right with moveinright
    
    $ pos += 1
    jump next

label cuvar_luka:
    $ cshw[ pos ] = "cuvar_luka"
    if pos == 0:
        show cuvar_luka with dissolve 
    elif pos == 2:
        show cuvar_luka at left with moveinleft
    elif pos == 1:
        show cuvar_luka at right with moveinright
    
    $ pos += 1
    jump next

label gospodin_rakovica:
    $ cshw[ pos ] = "gospodin_rakovica"
    if pos == 0:
        show gospodin_rakovica with dissolve 
    elif pos == 2:
        show gospodin_rakovica at left with moveinleft
    elif pos == 1:
        show gospodin_rakovica at right with moveinright
    
    $ pos += 1
    jump next

label gusar:
    $ cshw[ pos ] = "gusar"
    if pos == 0:
        show gusar with dissolve 
    elif pos == 2:
        show gusar at left with moveinleft
    elif pos == 1:
        show gusar at right with moveinright
    
    $ pos += 1
    jump next

label konjusar_sarko:
    $ cshw[ pos ] = "konjusar_sarko"
    if pos == 0:
        show konjusar_sarko with dissolve 
    elif pos == 2:
        show konjusar_sarko at left with moveinleft
    elif pos == 1:
        show konjusar_sarko at right with moveinright
    
    $ pos += 1
    jump next

label konobar_kalamarko_krakovic:
    $ cshw[ pos ] = "konobar_kalamarko_krakovic"
    if pos == 0:
        show konobar_kalamarko_krakovic with dissolve 
    elif pos == 2:
        show konobar_kalamarko_krakovic at left with moveinleft
    elif pos == 1:
        show konobar_kalamarko_krakovic at right with moveinright
    
    $ pos += 1
    jump next

label kralj_dante:
    $ cshw[ pos ] = "kralj_dante"
    if pos == 0:
        show kralj_dante with dissolve 
    elif pos == 2:
        show kralj_dante at left with moveinleft
    elif pos == 1:
        show kralj_dante at right with moveinright
    
    $ pos += 1
    jump next

label kraljica_marie:
    $ cshw[ pos ] = "kraljica_marie"
    if pos == 0:
        show kraljica_marie with dissolve 
    elif pos == 2:
        show kraljica_marie at left with moveinleft
    elif pos == 1:
        show kraljica_marie at right with moveinright
    
    $ pos += 1
    jump next

label kuhar_branko_skockani:
    $ cshw[ pos ] = "kuhar_branko_skockani"
    if pos == 0:
        show kuhar_branko_skockani with dissolve 
    elif pos == 2:
        show kuhar_branko_skockani at left with moveinleft
    elif pos == 1:
        show kuhar_branko_skockani at right with moveinright
    
    $ pos += 1
    jump next

label mag_iz_dubina:
    $ cshw[ pos ] = "mag_iz_dubina"
    if pos == 0:
        show mag_iz_dubina with dissolve 
    elif pos == 2:
        show mag_iz_dubina at left with moveinleft
    elif pos == 1:
        show mag_iz_dubina at right with moveinright
    
    $ pos += 1
    jump next

label marina:
    $ cshw[ pos ] = "marina"
    if pos == 0:
        show marina with dissolve 
    elif pos == 2:
        show marina at left with moveinleft
    elif pos == 1:
        show marina at right with moveinright
    
    $ pos += 1
    jump next

label marina_mala:
    $ cshw[ pos ] = "marina_mala"
    if pos == 0:
        show marina_mala with dissolve 
    elif pos == 2:
        show marina_mala at left with moveinleft
    elif pos == 1:
        show marina_mala at right with moveinright
    
    $ pos += 1
    jump next

label princ_salvadore:
    $ cshw[ pos ] = "princ_salvadore"
    if pos == 0:
        show princ_salvadore with dissolve 
    elif pos == 2:
        show princ_salvadore at left with moveinleft
    elif pos == 1:
        show princ_salvadore at right with moveinright
    
    $ pos += 1
    jump next

label princeza_frida:
    $ cshw[ pos ] = "princeza_frida"
    if pos == 0:
        show princeza_frida with dissolve 
    elif pos == 2:
        show princeza_frida at left with moveinleft
    elif pos == 1:
        show princeza_frida at right with moveinright
    
    $ pos += 1
    jump next

label princeza_rakova:
    $ cshw[ pos ] = "princeza_rakova"
    if pos == 0:
        show princeza_rakova with dissolve 
    elif pos == 2:
        show princeza_rakova at left with moveinleft
    elif pos == 1:
        show princeza_rakova at right with moveinright
    
    $ pos += 1
    jump next

label profesor_sipa_tintic:
    $ cshw[ pos ] = "profesor_sipa_tintic"
    if pos == 0:
        show profesor_sipa_tintic with dissolve 
    elif pos == 2:
        show profesor_sipa_tintic at left with moveinleft
    elif pos == 1:
        show profesor_sipa_tintic at right with moveinright
    
    $ pos += 1
    jump next

label puz_kadrinalac:
    $ cshw[ pos ] = "puz_kadrinalac"
    if pos == 0:
        show puz_kadrinalac with dissolve 
    elif pos == 2:
        show puz_kadrinalac at left with moveinleft
    elif pos == 1:
        show puz_kadrinalac at right with moveinright
    
    $ pos += 1
    jump next

label snorkijevac_joja:
    $ cshw[ pos ] = "snorkijevac_joja"
    if pos == 0:
        show snorkijevac_joja with dissolve 
    elif pos == 2:
        show snorkijevac_joja at left with moveinleft
    elif pos == 1:
        show snorkijevac_joja at right with moveinright
    
    $ pos += 1
    jump next

label snorkijevac_ratko:
    $ cshw[ pos ] = "snorkijevac_ratko"
    if pos == 0:
        show snorkijevac_ratko with dissolve 
    elif pos == 2:
        show snorkijevac_ratko at left with moveinleft
    elif pos == 1:
        show snorkijevac_ratko at right with moveinright
    
    $ pos += 1
    jump next

label snorkijevac_zarko:
    $ cshw[ pos ] = "snorkijevac_zarko"
    if pos == 0:
        show snorkijevac_zarko with dissolve 
    elif pos == 2:
        show snorkijevac_zarko at left with moveinleft
    elif pos == 1:
        show snorkijevac_zarko at right with moveinright
    
    $ pos += 1
    jump next

label snorkijevac_zivko:
    $ cshw[ pos ] = "snorkijevac_zivko"
    if pos == 0:
        show snorkijevac_zivko with dissolve 
    elif pos == 2:
        show snorkijevac_zivko at left with moveinleft
    elif pos == 1:
        show snorkijevac_zivko at right with moveinright
    
    $ pos += 1
    jump next

label vegimal1:
    $ cshw[ pos ] = "vegimal1"
    if pos == 0:
        show vegimal1 with dissolve 
    elif pos == 2:
        show vegimal1 at left with moveinleft
    elif pos == 1:
        show vegimal1 at right with moveinright
    
    $ pos += 1
    jump next

label vegimal2:
    $ cshw[ pos ] = "vegimal2"
    if pos == 0:
        show vegimal2 with dissolve 
    elif pos == 2:
        show vegimal2 at left with moveinleft
    elif pos == 1:
        show vegimal2 at right with moveinright
    
    $ pos += 1
    jump next

label vegimal3:
    $ cshw[ pos ] = "vegimal3"
    if pos == 0:
        show vegimal3 with dissolve 
    elif pos == 2:
        show vegimal3 at left with moveinleft
    elif pos == 1:
        show vegimal3 at right with moveinright
    
    $ pos += 1
    jump next

label vegimal4:
    $ cshw[ pos ] = "vegimal4"
    if pos == 0:
        show vegimal4 with dissolve 
    elif pos == 2:
        show vegimal4 at left with moveinleft
    elif pos == 1:
        show vegimal4 at right with moveinright
    
    $ pos += 1
    jump next

label vegimals13:
    $ cshw[ pos ] = "vegimals13"
    if pos == 0:
        show vegimals13 with dissolve 
    elif pos == 2:
        show vegimals13 at left with moveinleft
    elif pos == 1:
        show vegimals13 at right with moveinright
    
    $ pos += 1
    jump next

label vegimals24:
    $ cshw[ pos ] = "vegimals24"
    if pos == 0:
        show vegimals24 with dissolve 
    elif pos == 2:
        show vegimals24 at left with moveinleft
    elif pos == 1:
        show vegimals24 at right with moveinright
    
    $ pos += 1
    jump next

label zig:
    $ cshw[ pos ] = "zig"
    if pos == 0:
        show zig with dissolve 
    elif pos == 2:
        show zig at left with moveinleft
    elif pos == 1:
        show zig at right with moveinright
    
    $ pos += 1
    jump next

label zig_mali:
    $ cshw[ pos ] = "zig_mali"
    if pos == 0:
        show zig_mali with dissolve 
    elif pos == 2:
        show zig_mali at left with moveinleft
    elif pos == 1:
        show zig_mali at right with moveinright
    
    $ pos += 1
    jump next


# END LABEL

label end:
    return