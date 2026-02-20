from win32api import GetFileVersionInfo, HIWORD, LOWORD

PLAN = 'FileVersion%sS' 
ms_file_version,ls_file_version=[
    GetFileVersionInfo('E:/Grand Theft Auto IV/GTAIV.exe',"\\")[e]
    for e in([PLAN % e for e in ('M','L')]
)]
vv_num = [f(v) for v in (
    ms_file_version,
    ls_file_version
) for f in (
    HIWORD,
    LOWORD
)]
major, minor, patch, build = vv_num

vv_str = list(map(str, vv_num))

hash_v = int.from_bytes(vv_num, 'big')

print(f'{".".join(vv_str)} -> {"".join(vv_str)}\n\
s/ build: {hex(hash_v & 0xFFFFFF00)} (\
c/ build: {hex(hash_v)})') # ID_hash_v
