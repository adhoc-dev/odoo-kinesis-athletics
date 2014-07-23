# -*- coding: utf-8 -*-

from openerp import netsvc
from openerp.osv import osv, fields


class evaluation_in_person_wizard(osv.osv_memory):

    _name = 'kinesis_athletics.evaluation.person.wizard'
    _description = 'Wizard'

    def EvaluationsPersonWizard(self, cr, uid, ids, context=None):

        wizard = self.browse(cr, uid, ids[0], context=context)
        active_ids=context.get('active_ids', False)

        person_obj = self.pool['res.partner']

        evaluation_obj = self.pool['kinesis_athletics.evaluation']

        evaluation_ids = []
        for person in person_obj.browse(cr, uid, active_ids, context=context):

            default = {
                'date': wizard.date,
                'partner_id': person.id,
                'group_id': person.actual_group_id.id,
                'company_id': person.company_id.id,
                'template_id': wizard.evaluation_id.id,
                'is_template':False,
                }
            evaluation_id = evaluation_obj.copy(cr, uid, wizard.evaluation_id.id, default = default, context=context)

            evaluation_ids.append(evaluation_id)

        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        action_evaluation = mod_obj.get_object_reference(cr, uid, 'kinesis_athletics', 'action_kinesis_athletics_evaluation_evaluations')
        action_evaluation_id = action_evaluation and action_evaluation[1] or False
        action_evaluation = act_obj.read(cr, uid, [action_evaluation_id], context=context)[0]
        action_evaluation['domain'] = [('id','in',evaluation_ids)]

        return action_evaluation


    _columns = {
        'date': fields.date(string='Date'),
        'evaluation_id': fields.many2one('kinesis_athletics.evaluation', string='Evaluation Template', domain=[('is_template', '=', True)], required=True),
    }

    _defaults = {
        'date':fields.date.context_today,
    }
