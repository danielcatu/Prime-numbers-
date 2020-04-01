@echo off
:ARGUMENTS_LOOP
if "%~1"==""  ( goto SETVARIABLES) 
    :: Help switches
    if /I "%~1" == "-n" (set n=%~2& goto SHIFT)
:SHIFT
Shift
goto ARGUMENTS_LOOP

:SETVARIABLES
FOR /l %%N in (1,1,%n%) DO ( 
    echo Con %%N nucleos
     FOR /l %%K in (100000,100000,1000000) DO mpiexec -n %%N python primos.py %%K
    )

pause