for %%I in (.) do set cudi=%%~nxI
cd installer
move /Y HTGi.exe HTG-V%cudi%.exe
"%PROGRAMFILES%\7-Zip\7z.exe" a HTG-V%cudi%.7z -t7z -mx=9 -myx=7 -ms=on -m0=LZMA2 -md=1536m -mmf=hc4 -mmc=1000000 -mfb=273 HTG-V%cudi%.exe -pstronglystressed -mhe
cd %~dp0
xcopy "installer\HTG-V%cudi%.7z" "%HOMEPATH%\OneDrive\Desktop\"
gdrive-windows-x64 upload -p 1z8JKv6c32doFdaFqPOe_PsbHo_4oOGu1 "%HOMEPATH%\OneDrive\Desktop\HTG-V%cudi%.7z"
rd __pycache__ /S /Q
rd comp /S /Q
del %HOMEPATH%\OneDrive\Desktop\HTG.exe
del %HOMEPATH%\OneDrive\Desktop\HTG-V%cudi%.7z