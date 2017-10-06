@ECHO OFF
CLS
:A
CALL "robot.py"
ECHO Restarting..
timeout 3
GOTO A