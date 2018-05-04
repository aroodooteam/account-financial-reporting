# -*- encoding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi, Guewen Baconnier
#    Copyright Camptocamp SA 2011
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
import time

from openerp import api, exceptions, fields, models, _
import logging
logger = logging.getLogger(__name__)


class AccountReportPartnersLedgerWiz(models.TransientModel):
    _inherit = "partners.ledger.webkit"

    result_selection = fields.Selection(selection_add=[('other', 'Normal')])
    acc_ids = fields.Many2many(comodel_name='account.account', string='Filter on Account')

    def pre_print_report(self, cr, uid, ids, data, context=None):
        data = super(AccountReportPartnersLedgerWiz, self).pre_print_report(
            cr, uid, ids, data, context=context)
        if context is None:
            context = {}
        # will be used to attach the report on the main account
        data['ids'] = [data['form']['chart_account_id']]
        vals = self.read(cr, uid, ids,
                         ['acc_ids'],
                         context=context)[0]
        data['form'].update(vals)
        logger.info('\n=== ppr_new = %s' % data)
        return data
