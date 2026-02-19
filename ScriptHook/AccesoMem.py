from json import load

oo_vv = None

try:
    #gestiona close
    with open('oo_vv.json', 'r') as f: oo_vv = load(f)

    print(oo_vv)

except Exception as e: print(f'e: {e}') # NO especifico. 4 casos
