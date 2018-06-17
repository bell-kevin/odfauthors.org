# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from odfauthors.theme.testing import ODFAUTHORS_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that odfauthors.theme is properly installed."""

    layer = ODFAUTHORS_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if odfauthors.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'odfauthors.theme'))

    def test_browserlayer(self):
        """Test that IOdfAuthorsthemeLayer is registered."""
        from odfauthors.theme.interfaces import (
            IOdfAuthorsthemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IOdfAuthorsthemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ODFAUTHORS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['odfauthors.theme'])

    def test_product_uninstalled(self):
        """Test if odfauthors.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'odfauthors.theme'))

    def test_browserlayer_removed(self):
        """Test that IOdfAuthorsthemeLayer is removed."""
        from odfauthors.theme.interfaces import IOdfAuthorsthemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IOdfAuthorsthemeLayer, utils.registered_layers())
