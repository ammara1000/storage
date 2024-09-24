echo off
set /a num=0
:start
set /a num=%num%+1
start /max
if %num% == 50 (goto end)
goto start
:end