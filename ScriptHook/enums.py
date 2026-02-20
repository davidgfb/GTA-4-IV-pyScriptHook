from json import load

# GTAIV.exe (WinAPI GetFileVersionInfo, hash_a_v

vv = None

# PROBADOR
try:
    #gestiona close
    with open('obj/vv.json', 'r') as f: vv = load(f)

except Exception as e: print(f'e: {e}') # NO especifico. 4 casos

[print({f'{v}: {hex(h)}'}) for v, h in vv.items()]
