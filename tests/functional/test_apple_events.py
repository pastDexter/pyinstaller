#-----------------------------------------------------------------------------
# Copyright (c) 2005-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

"""
OSX-specific test to check handling AppleEvents by bootloader
"""

# Library imports
# ---------------
import os
import subprocess
import sys
import time

# Third-party imports
# -------------------
import pytest

# Local imports
# -------------
from PyInstaller.utils.tests import skipif_notosx


@skipif_notosx
def test_osx_custom_protocol_handler(tmpdir, pyi_builder_spec):
    app_path = os.path.join(tmpdir, 'dist', 'pyi_osx_custom_protocol_handler.app')
    logfile_path = os.path.join(tmpdir, 'dist', 'args.log')

    # Generate new URL scheme to avoid collisions
    custom_url_scheme = "pyi-test-{}".format(int(time.time()))
    os.environ["PYI_CUSTOM_URL_SCHEME"] = custom_url_scheme

    pyi_builder_spec.test_spec('pyi_osx_custom_protocol_handler.spec')

    # First run using 'open' registers custom protocol handler
    subprocess.check_call(['open', app_path])
    # 'open' starts program in a different process, so we need to wait for it to finish
    time.sleep(2)

    # Call custom protocol handler
    url = custom_url_scheme + "://url-args"
    subprocess.check_call(['open', url])
    # Wait for the program to finish
    time.sleep(2)
    assert os.path.exists(logfile_path) == 1, 'Missing args logfile'
    logfile_lines = open(logfile_path, 'r').readlines()
    assert len(logfile_lines) > 0 and logfile_lines[-1] == url, 'Invalid arg appended'
