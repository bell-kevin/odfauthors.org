# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'odfauthors.policy:uninstall',
        ]


def post_install(context):
    """Post install script"""
    if context.readDataFile('odfauthorspolicy_default.txt') is None:
        return

    portal = context.getSite()
    portal.setLayout('frontpageview')
    if getattr(portal, 'front-page', False):
        api.content.delete(portal['front-page'])


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('odfauthorspolicy_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
