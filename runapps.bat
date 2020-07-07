@echo off

set LOGFILE=ipconfiglog(pleaseDoNotModifyThisFiel).log
call :LOG > %LOGFILE%
node server.js

:LOG
ipconfig

