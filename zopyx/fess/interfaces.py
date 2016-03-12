# -*- coding: utf-8 -*-

################################################################
# xmldirector.plonecore
# (C) 2014,  Andreas Jung, www.zopyx.com, Tuebingen, Germany
################################################################

from zope import schema
from zope.interface import Interface


class IFESSSettings(Interface):
    """ Connector settings """

    fess_url = schema.TextLine(
        title=u'Fess URL',
        default=u'',
        required=True
    )
