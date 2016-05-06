#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    reusable UIModules for Toronado
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    reusable UIModules for Toronado.

    :copyright: (c) 2016 by Lix Xu.
    :license: BSD, see LICENSE for more details
"""

from __future__ import unicode_literals
import tornado.web

__version__ = '0.0.1'


class BaseUIModule(tornado.web.UIModule):
    def render(self, **kwargs):
        kw = {}
        for kls in self.__class__.__mro__:
            if kls.__name__ == 'UIModule':
                break

            for k, v in kls.__dict__.items():
                if not k.startswith('_'):
                    kw.setdefault(k, kwargs.pop(k, v))

        kw.update(kwargs)
        gtp = self.handler.get_template_path
        self.handler.get_template_path = self.get_template_path
        ui_text_ = self.render_string(self.__class__.template, **kw)
        self.handler.get_template_path = gtp
        return ui_text_

    def get_template_path(self):
        return None
