from json import dump

BLIPLIST, OBJECTPOOL, PEDPOOL, VEHICLEPOOL =['ADDRESS_'+o for o in (
    'BLIPLIST'   ,
    'OBJECTPOOL' ,
    'PEDPOOL'    ,
    'VEHICLEPOOL'
)]
vv = {
    int(1e3): {
        BLIPLIST   : 0        ,
        OBJECTPOOL : 0        ,
        PEDPOOL    : 0        ,
        VEHICLEPOOL: 0x13DE9D0
    }, 1010: {
        BLIPLIST   : 0xFB1AF0,
        OBJECTPOOL : 0x11E73E8,
        PEDPOOL    : 0x16EB9A0,
        VEHICLEPOOL: 0x11E1540
    }, 1020: {
        BLIPLIST   : 0xFAB470,
        OBJECTPOOL : 0x11D13C8,
        PEDPOOL    : 0x16E37E0,
        VEHICLEPOOL: 0x11CB520
    }, 1030: {
        BLIPLIST   : 0xFCA9D0,
        OBJECTPOOL : 0x11F5B38,
        PEDPOOL    : 0x17564D8,
        VEHICLEPOOL: 0x11EFC90
    }, 1040: {
        BLIPLIST   : 0xFCFC70,
        OBJECTPOOL : 0x11FADD8,
        PEDPOOL    : 0x175B77C,
        VEHICLEPOOL: 0x11F4F30
    }, 1050: {
        BLIPLIST   : 0x10D3AF0,
        OBJECTPOOL : 0x10EBD08,
        PEDPOOL    : 0x17DFCA8,
        VEHICLEPOOL: 0x10E8BD0
    }, 1060: {
        BLIPLIST   : 0x119DD50,
        OBJECTPOOL : 0x134FD00,
        PEDPOOL    : 0x18A72BC,
        VEHICLEPOOL: 0x1618260
    }, 1070: {
        BLIPLIST   : 0x119ED50,
        OBJECTPOOL : 0x1350CE0,
        PEDPOOL    : 0x18A82AC,
        VEHICLEPOOL: 0x1619240
    }, 1110: {
        BLIPLIST   : 0x1122E20,
        OBJECTPOOL : 0x1471440,
        PEDPOOL    : 0x18A3080,
        VEHICLEPOOL: 0x1621C10
    }, 1120: {
        BLIPLIST   : 0x10C3EA0,
        OBJECTPOOL : 0x118A660,
        PEDPOOL    : 0x18219EC,
        VEHICLEPOOL: 0x15C17B0
    },
}

def init(dir_base = 0, v = int(1e3)):
    dicc = {}

    if v in vv:dicc={d: dir_base + val for d,val in vv[v].items()}            

    return dicc

# PROBADOR
# gestiona close automatico
NOMBRE_JSON = 'oo_vv.json'
with open(NOMBRE_JSON, 'w') as f:\
     dump({f'{v}': init(v=v)for v in sorted(vv.keys())},f,indent=4)

print(f'{NOMBRE_JSON} exportado con éxito.')
    
# quito hex(dir_base), hex(val) para exportar a JSON
#[print(f'oo_db_{dir_base}_v{v}: {{\n'+'\n'.join(f'\t{o}: {val},'for o,val in init(dir_base,v).items())+'\n},',end=' ')for v in sorted(vv.keys()) for dir_base in (0,)]#range(0x1000000,0x1000000+1)]
