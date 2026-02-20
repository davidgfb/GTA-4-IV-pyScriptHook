clean: @if exist obj rmdir /s /q obj

all: 
  @if not exist obj mkdir obj
  @if not exist obj\vv.json cd Exportadores && py "Exportador vv json.py"
  @if not exist obj\oo_vv.json cd Exportadores && py "Exportador json oo vv.py"

run: all
  py enums.py
  py "Acceso Mem.py"

rebuild: clean run
