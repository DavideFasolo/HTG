pyinstaller.exe --workpath=comp --distpath="comp" --clean --specpath=comp --onefile -w --icon="Configurazione\icns\icona.ico" HTG.py
pyinstaller.exe --workpath=comp --distpath="comp" --clean --specpath=comp --onefile -w --icon="Configurazione\icns\icona.ico" splash.py
xcopy /Y comp\HTG.exe %HOMEPATH%\OneDrive\Desktop\
