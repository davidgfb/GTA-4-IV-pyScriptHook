from win32api import GetFileVersionInfo, HIWORD, LOWORD

PLAN = 'FileVersion%sS' 
ms_file_version,ls_file_version=[
    GetFileVersionInfo('E:/Grand Theft Auto IV/GTAIV.exe',"\\")[e]
    for e in([PLAN % e for e in ('M','L')]
)]

print(f'{HIWORD(ms_file_version)}.{LOWORD(ms_file_version)}.{HIWORD(ls_file_version)}.{LOWORD(ls_file_version)}')
