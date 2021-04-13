@echo off                          
:loop                             
start "terminal.exe" "C:\Program Files (x86)\RoboForex - MetaTrader 4\terminal.exe"  
timeout /t 20 >null              
taskkill /f /im "terminal.exe" >nul  
timeout /t 7 >null                 
goto loop   