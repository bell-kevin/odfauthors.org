# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from tdf.exttempsitepolicy import _
from Acquisition import aq_inner



class frontpageView(BrowserView):

    """ The view of the ODFAuthors frontpage
    """


