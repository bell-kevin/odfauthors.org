# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces.controlpanel import IMailSchema
from odfauthors.policy.testing import ODFAUTHORS_POLICY_INTEGRATION_TESTING
from zope.component import getUtility
from zope.event import notify
from zope.interface import Invalid
from zope.lifecycleevent import ObjectModifiedEvent
from zope.lifecycleevent import ObjectRemovedEvent

import unittest


class TestOdfauthorsValidators(unittest.TestCase):
    """Test that odfauthors.policy is properly installed."""

    layer = ODFAUTHORS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        registry = getUtility(IRegistry)
        mail_settings = registry.forInterface(
            IMailSchema, prefix='plone', check=False)
        mail_settings.smtp_host = u'localhost'
        mail_settings.email_from_address = 'whatever'

