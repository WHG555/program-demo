@ECHO OFF

REM Command file for MKDocs documentation

if "%RUNAPP%" == "" (
	set RUNAPP=mkdocs
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  install      install mkdocs
	echo.  new + name   create new websites
	echo.  serve        start website server
	echo.  build        build md to html
	goto end
)

if "%1" == "install" (
	pip install -r requirements.txt
	goto end
)

if "%1" == "new" (
    cd docs
	%RUNAPP% new %2
	goto end
)

if "%1" == "serve" (
    cd docs
	%RUNAPP% serve
	goto end
)

if "%1" == "build" (
    cd docs
	%RUNAPP% build --clean
	goto end
)

if "%1" == "pack" (
	cd code
    pyinstaller -D -w --icon=logo.ico --add-data aishow.ui;aishow.ui main.py wlcmd.py base.py
	goto end
)

:end
