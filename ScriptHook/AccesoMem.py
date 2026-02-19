from json import load

oo_vv = None

def init(oo_vv, dir_base = 0, v = int(1e3)):
    dicc = {}

    if v in oo_vv:dicc={d: dir_base + val for d,val in oo_vv[v].items()}            

    return dicc

# PROBADOR
try:
    #gestiona close
    with open('obj/oo_vv.json', 'r') as f: oo_vv = load(f)

except Exception as e: print(f'e: {e}') # NO especifico. 4 casos

[print(f'oo_db_{hex(dir_base)}_v{v}: {{\n'+'\n'.join(f'\t{o}: {hex(val)},'for o,val in init(oo_vv,dir_base,v).items())+'\n},',end=' ')for v in sorted(oo_vv.keys()) for dir_base in (0,)]#range(0x1000000,0x1000000+1)]
