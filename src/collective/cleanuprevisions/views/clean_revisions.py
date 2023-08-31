# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class ICleanRevisions(Interface):
    """Marker Interface for ICleanRevisions"""


@implementer(ICleanRevisions)
class CleanRevisions(BrowserView):
    def __call__(self):
        template = """<li class="heading" i18n:translate="">
          Sample View
        </li>"""
        return template
