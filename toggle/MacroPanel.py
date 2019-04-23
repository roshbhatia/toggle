# MacroPanel

import collections

from gi.repository import Clutter, Mx, Mash
import logging

_MacroAttributes = collections.namedtuple(
        '_MacroAttributes',
        ['macro_name', 'payload', 'button_id', 'icon_path']
)

""" Yield key, value pairs of macros specified in config file.
Macros are specified as options in the config file under a [Macros] section. The
option name defines the name of the macro.
"""
def _load_macros(config):
    #XXX
    for name, payload in macros.items():
        yield name, _MacroAttributes(
                payload=payload,
                button_id='temp-button-{}'.format(name)
        )


class MacroPanel:
    def __init__(self, config=None):
        self._config = config
        self._macros = dict(_load_macros(config))

    def _run_macro(self, macro_id):
        #XXX

