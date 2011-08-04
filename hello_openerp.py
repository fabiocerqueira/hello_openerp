#-*- coding: utf-8 -*-
from osv import fields, osv

class hello(osv.osv):
    """
    Simple object with one field
    """
    _name = 'ho.hello'
    _description = 'hello'
    _columns = {
        'text':fields.char('text', size=256, required=True, readonly=False),
    }
hello()
