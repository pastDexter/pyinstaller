# -*- mode: python -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2005-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

import os

block_cipher = None
app_name = 'pyi_osx_custom_protocol_handler'
custom_url_scheme = os.environ.get('PYI_CUSTOM_URL_SCHEME', 'pyi-test-app')


a = Analysis(['../scripts/pyi_log_args.py'],
             pathex=[],
             binaries=None,
             datas=None,
             hiddenimports=[],
            hookspath=[],
             runtime_hooks=None,
             excludes=None,
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
          name=app_name,
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name=app_name + '.app',
             icon=None,
             bundle_identifier=None,
             # Register custom protocol handler
             info_plist={
                'CFBundleURLTypes': [{
                    'CFBundleURLName': 'PYITestApp',
                    'CFBundleTypeRole': 'Viewer',
                    'CFBundleURLSchemes': [custom_url_scheme]
                }]
             })
