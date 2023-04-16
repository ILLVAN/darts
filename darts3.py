# DARTS by iLLVAN
import simpleaudio as sa
import sys
import time

aud_whut = sa.WaveObject.from_wave_file("whut.wav")
aud_lo11 = sa.WaveObject.from_wave_file("Loop11.wav")
aud_loop = sa.WaveObject.from_wave_file("Loop.wav")
aud_loo2 = sa.WaveObject.from_wave_file("Loop2.wav")
aud_loo3 = sa.WaveObject.from_wave_file("Loop3.wav")
aud_loo8 = sa.WaveObject.from_wave_file("Loop8.wav")
aud_rhod = sa.WaveObject.from_wave_file("Rhodes1.wav")
aud_sati = sa.WaveObject.from_wave_file("satie2.wav")
aud_trom = sa.WaveObject.from_wave_file("tromb.wav")
aud_yeah = sa.WaveObject.from_wave_file("yea.wav")
aud_hhs1 = sa.WaveObject.from_wave_file("HHS1.wav")
aud_meta = sa.WaveObject.from_wave_file("metallic.wav")
aud_bott = sa.WaveObject.from_wave_file("BOTTTLEZZ.wav")
aud_craz = sa.WaveObject.from_wave_file("CRAZYBAZZ.wav")
aud_dx200 = sa.WaveObject.from_wave_file("DX200.wav")
aud_fall = sa.WaveObject.from_wave_file("FALL.wav")
aud_hatz = sa.WaveObject.from_wave_file("HATZZZ.wav")
aud_lun1 = sa.WaveObject.from_wave_file("luny_tunes_LOOP1.wav")
aud_lun2 = sa.WaveObject.from_wave_file("luny_tunes_LOOP2.wav")
aud_risi = sa.WaveObject.from_wave_file("RISIN .wav")
aud_sads = sa.WaveObject.from_wave_file("SADSYNTH.wav")
aud_sick = sa.WaveObject.from_wave_file("SICKDRUMZZ .wav")
aud_subm = sa.WaveObject.from_wave_file("SUBMARINEZZZzz .wav")
aud_whae = sa.WaveObject.from_wave_file("WHA EVER BAZZ .wav")
aud_xoxo = sa.WaveObject.from_wave_file("XOX OFFBEAT.wav")
aud_scra = sa.WaveObject.from_wave_file("scrapple.wav")

while True:
    try:
        print('\n')
        print('\n')
        numpla = int(input('number of players: '))
        numpli = range(numpla)
        break
    except:
        continue

# creating results-dict and asking no of players and game (301 / 501 / ... )
res = {}
for i in numpli:
    name = input('enter player: ')
    name = name.upper()
    res[name] = []
print('\n')
print('players:',res)
while True:
    try:
        hint= int(input('enter game: '))
        break
    except:
        print('integers please')
        continue

# input loop
i = 1
delete = False
while True: 
    for name in res:
        if delete is True:
            i = i - 1
            delete = False
            break
        n = hint - sum(res[name])
        while True: 
            print('\n')
            if delete is False:
                print(name, '- your turn:', n)
            try:
                scor = int(input('score: '))
            except:
                play_obj = aud_whut.play()
                print('integers please')
                continue
            if scor == 1312:
                sys.exit()    
            if scor == 666:
                for name in res:   
                    res[name] = res[name][:i-2]
                i = i - 1
                delete = True
                break
            if scor > n:
                scor = 0
            if scor >= 0:
                res[name].append(scor)
                if scor > 99:
                    play_obj = aud_lo11.play()
                elif scor > 95:
                    play_obj = aud_fall.play()
                elif scor > 90:
                    play_obj = aud_yeah.play()
                elif scor > 82:
                    play_obj = aud_rhod.play()
                elif scor > 77:
                    play_obj = aud_risi.play()
                elif scor > 73:
                    play_obj = aud_trom.play()
                elif scor > 66:
                    play_obj = aud_dx200.play()
                elif scor == 63:
                    play_obj = aud_lun1.play()
                elif scor > 60:
                    play_obj = aud_loo3.play()
                elif scor > 51:
                    play_obj = aud_meta.play()
                elif scor > 47:
                    play_obj = aud_xoxo.play()
                elif scor == 42:
                    play_obj = aud_lun2.play()
                elif scor > 39:
                    play_obj = aud_hhs1.play()
                elif scor > 35:
                    play_obj = aud_sick.play()   
                elif scor == 32:
                    play_obj = aud_subm.play()
                elif scor > 30:
                    play_obj = aud_loo8.play()
                elif scor == 25:
                    play_obj = aud_whae.play()
                elif scor == 27:
                    play_obj = aud_hatz.play()
                elif scor > 20:
                    play_obj = aud_loo2.play()
                elif scor > 16:
                    play_obj = aud_bott.play()
                elif scor > 13:
                    play_obj = aud_craz.play()
                elif scor > 10:
                    play_obj = aud_loop.play()
                elif scor > 7:
                    play_obj = aud_sads.play()                
                elif scor > 0:
                    play_obj = aud_sati.play()
                elif scor == 0:
                    play_obj = aud_whut.play()
            # play_obj.wait_done()
            break
        n = hint - sum(res[name])
        if n == 0:
            time.sleep(5)
            play_obj = aud_scra.play()
            print('\n')
            print('\n')
            print('*************', name, 'WON THE GAME *************')
            print('\n')
            print('\n')
            exit = input('press enter to exit game ')
            sys.exit()
        name = name + 's'
        print(name,'new score:', n)
    print('\n________________________________________________')
    print('\nNEW SCORE AFTER ROUND', i)
    print('\n')
    for name in res:
        print('***', name)
        if i != 0:
            avg = int(sum(res[name]) / i)
        else:
            avg = 0
        print('***',hint - sum(res[name]),'            avg', avg, res[name])
        print()
    print('________________________________________________')
    i = i + 1


