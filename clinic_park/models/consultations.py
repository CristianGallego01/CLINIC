from odoo import models, fields,api

class ClinicParkConsultation(models.Model):
    _name = 'clinic.park.consultation'
    _description = 'Consulta'

    triage_id = fields.Many2one('clinic.park.triage', string='Triage', required=True, ondelete='cascade')
    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)

    # Prescripciones
    tratamiento = fields.Text(string='Tratamiento Prescrito')
    procedimientos = fields.Text(string='Procedimientos Recomendados')

    def action_ir_a_cirugia(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cirugía',
            'res_model': 'clinic.park.cirugia',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_triage_id': self.triage_id.id,
            }
        }

    def action_ir_a_procedimientos(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Procedimientos',
            'res_model': 'clinic.park.procedimiento',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_patient_id': self.patient_id.id,
                'default_triage_id': self.triage_id.id,
            }
        }
