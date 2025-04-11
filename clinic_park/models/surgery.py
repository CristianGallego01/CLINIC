from odoo import models, fields

class ClinicParkCirugia(models.Model):
    _name = 'clinic.park.surgery'
    _description = 'Cirugía'

    triage_id = fields.Many2one('clinic.park.triage', string='Triage', required=True, ondelete='cascade')
    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    name= fields.Char(string='Nombre', related='patient_id.name', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)
    procedimiento = fields.Text(string='Procedimiento')
    fecha_cirugia = fields.Datetime(string='Fecha de Cirugía')