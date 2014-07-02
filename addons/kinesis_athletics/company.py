# -*- coding: utf-8 -*-
##############################################################################
#
#    Kinesis Athletics
#    Copyright (C) 2014 Ingenieria Adhoc
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class company(osv.osv):
    """"""
    
    _name = 'res.company'
    _inherits = {  }
    _inherit = [ 'res.company' ]

    _columns = {
        'has_group': fields.boolean(string='Has Group'),
        'company_type_id': fields.many2one('kinesis_athletics.company_type', string='Company Type'), 
        'groups_ids': fields.one2many('kinesis_athletics.group', 'company_id', string='Groups'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




company()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
