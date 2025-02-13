# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (c) 2005-2019, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


def test_six_moves(pyi_builder):
    pyi_builder.test_source(
        """
        from six.moves import UserList
        UserList
        """)

# Run the same test a second time to trigger errors like
#   Target module "six.moves.urllib" already imported as "AliasNode(…)"
# caused by PyiModuleGraph being cahced in a insufficient way.
test_six_moves_2nd_run = test_six_moves
