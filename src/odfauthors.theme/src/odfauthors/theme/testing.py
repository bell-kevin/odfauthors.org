# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import odfauthors.theme


class OdfAuthorsthemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=odfauthors.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'odfauthors.theme:default')


ODFAUTHORS_THEME_FIXTURE = OdfAuthorsthemeLayer()


ODFAUTHORS_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ODFAUTHORS_THEME_FIXTURE,),
    name='OdfAuthorsthemeLayer:IntegrationTesting'
)


ODFAUTHORS_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ODFAUTHORS_THEME_FIXTURE,),
    name='OdfAuthorsthemeLayer:FunctionalTesting'
)


ODFAUTHORS_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ODFAUTHORS_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='OdfAuthorsthemeLayer:AcceptanceTesting'
)
