@ECHO OFF

REM Command file for MKDocs documentation

if "%RUNAPP%" == "" (
	set RUNAPP=mkdocs
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  new + name   create new websites
	echo.  serve        start website server
	echo.  build        build md to html
	goto end
)

if "%1" == "new" (
	%RUNAPP% new %2
	goto end
)

if "%1" == "serve" (
	%RUNAPP% serve
	goto end
)

if "%1" == "serve" (
	%RUNAPP% build --clean
	goto end
)

:end
