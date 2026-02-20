# GTAIV.exe (WinAPI GetFileVersionInfo, hash_a_v
vv = {
    'UnknownVersion': 0,
    1000: 0x1000000,
    1010: 0x1000100,
    1020: 0x1000200,
    1030: 0x1000300,
    1040: 0x1000400,
    1050: 0x1000004,
    1060: 0x1000600,
    1070: 0x1000700,
    1110: 0x1010100, # EFLC
    1120: 0x1010200, # EFLC
}

# PROBADOR
[print({v: hex(h)}) for v, h in vv.items()]
