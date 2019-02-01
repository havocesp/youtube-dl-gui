# -*- mode: python -*-

block_cipher = None

appData=[
    ('youtube_dl_gui/data', 'youtube_dl_gui/data'),
    ('youtube_dl_gui/locale', 'youtube_dl_gui/locale')
]

appAllPath=[
    'C:\\Python\\lib\\site-packages',
    'C:\\workspace\\youtube-dl-package\\youtube_dl_gui',
    'C:\\workspace\\youtube-dl-package'
]


a = Analysis(['MyApp.py'],
             pathex=appAllPath,
             binaries=[],
             datas = appData,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MyApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
