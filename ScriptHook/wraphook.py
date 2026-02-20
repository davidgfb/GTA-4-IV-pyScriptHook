from win32api import GetFileVersionInfo, HIWORD, LOWORD

PLAN = 'FileVersion%sS' 
ms_file_version,ls_file_version=[
    GetFileVersionInfo('E:/Grand Theft Auto IV/GTAIV.exe',"\\")[e]
    for e in([PLAN % e for e in ('M','L')]
)]
vv = [str(f(v)) for v in (
    ms_file_version,
    ls_file_version
) for f in (
    HIWORD,
    LOWORD
)]

print(".".join(vv), '->', "".join(vv)) 
