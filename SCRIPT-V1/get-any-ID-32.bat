@echo off
for /f "delims=" %%i in ('"C:\Program Files\AnyDesk\AnyDesk.exe" --get-id') do set CID=%%i
echo %CID% >> %COMPUTERNAME%-especificaciones.txt
exit