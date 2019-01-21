# -*- mode: python -*-

block_cipher = None

appData=[
    ('youtube_dl_gui/data', 'youtube_dl_gui/data'),
    ('youtube_dl_gui/locale', 'youtube_dl_gui/locale')
]

appAllPath=[
    'C:\\Python\\lib\\site-packages',
    'C:\\workspace\\youtube-dl-package\\youtube_dl_gui',
    'C:\\workspace\\youtube-dl-package',
	'C:\\Python\\Lib\\site-packages\\wx-3.0-msw\\wx\\lib\\pubsub\\core\\kwargs'
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
          [],
          exclude_binaries=True,
          name='MyApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='MyApp')

app = BUNDLE(coll,
            name='MyApp.app',
            icon=None,
            bundle_identifier=None)
