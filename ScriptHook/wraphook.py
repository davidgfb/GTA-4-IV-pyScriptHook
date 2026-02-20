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

vv_familia_str = list(map(str, (major, minor, patch, 0)))

vv_build_str = list(map(str, vv_num))

familia = int.from_bytes((major, minor, patch), 'big') << 8

hex_fam = hex(familia)

print(f'familia: {".".join(vv_familia_str)} -> {"".join(vv_familia_str)} \
(c/ build: {".".join(vv_build_str)} -> {"".join(vv_build_str)})\n\
familia: {hex_fam} (c/ build: {hex_fam} + {hex(build)} = \
{hex(familia | build)})') # ID_hash_v
