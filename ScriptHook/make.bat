@echo off
set "ACCION=%1"
if "%ACCION%"=="" set "ACCION=run"

if "%ACCION%"=="clean" (
    if exist obj rmdir /s /q obj
    echo obj borrado.
) else if "%ACCION%"=="all" (
    if not exist obj mkdir obj
    if not exist obj\vv.json cd Exportadores && py "Exportador vv json.py" && cd ..
    if not exist obj\oo_vv.json cd Exportadores && py "Exportador json oo vv.py" && cd ..
) else if "%ACCION%"=="run" (
    call %0 all
    py enums.py
    py "Acceso Mem.py"
) else if "%ACCION%"=="rebuild" (
    call %0 clean
    call %0 run
)
