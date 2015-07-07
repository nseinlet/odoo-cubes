# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.odoo.com>
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

{
    'name' : 'Odoo BI wizard',
    'version': '0.1',
    'summary': 'A small wizard to create custom BI views',
    'sequence': '19',
    'category': 'Tools',
    'complexity': 'medium',
    'description':
        """
Odoo BI wizard
==============

Create new views for BI analysis
        """,
    'data': [
             'models/cube.xml',
             'models/model.xml',
             'models/link.xml',
             'models/field.xml',
             'models/computedfield.xml',
             'models/rule.xml',
             'models/o2m.xml',
             'views/computedfields.xml',
             'views/cubes.xml',
             'views/rules.xml',
             'views/menu.xml',
             'views/cubemodel.xml',
             'views/cubelink.xml',
             'security/biwizard_groups.xml',
             'security/ir.model.access.csv',
             ],
    'depends' : ['base_action_rule'],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
