# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['./scripts/OttoHub.py','./scripts/OttoInput.py','./scripts/OttoList.py','./scripts/OttoMath.py','./scripts/OttoNote.py','./scripts/OttoOverwrite.py','./scripts/OttoRemind.py','./scripts/OttoSort.py'],
    pathex=['./scripts'],
    binaries=[],
    datas=[('hourpass.mp3','.')],
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
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    [a.scripts[0]], #Only first entry in list of scripts
    a.binaries,
    a.datas,
    [],
    name='OttoWorkOptimizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='Otto Work Optimizer'
)