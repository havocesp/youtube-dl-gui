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


a = Analysis(['VideoDownloader.py'],
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
          name='VideoDownloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='VideoDownloader')

app = BUNDLE(coll,
            name='VideoDownloader.app',
            icon='C:\\workspace\\youtube-dl-gui\\youtube_dl_gui\\data\\pixmaps\\onlinedownload88.ico',
            bundle_identifier=None)
