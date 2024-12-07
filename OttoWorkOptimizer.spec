# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['OttoHub.py','OttoInput.py','OttoList.py','OttoMath.py','OttoNote.py','OttoOverwrite.py','OttoRemind.py','OttoSort.py'],
    pathex=[''],
    binaries=[],
    datas=['hourpass.mp3'],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
    optimize=0
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='OttoHub.py',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Otto Work Optimizer'
)