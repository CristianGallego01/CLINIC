from odoo import models, fields

class ClinicParkCirugia(models.Model):
    _name = 'clinic.park.surgery'
    _description = 'Cirugía'

    triage_id = fields.Many2one('clinic.park.triage', string='Triage', required=True, ondelete='cascade')
    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    procedimiento = fields.Text(string='Procedimiento')
    fecha_cirugia = fields.Datetime(string='Fecha de Cirugía')