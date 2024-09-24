Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "installer.bat", 0
Set WShell = Nothing