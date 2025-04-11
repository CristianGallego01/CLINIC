from odoo import models, fields

class ClinicParkProcedure(models.Model):
    _name = 'clinic.park.procedure'
    _description = 'Procedimiento'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    procedure_name = fields.Char(string='Nombre del Procedimiento', required=True)
    procedure_date = fields.Datetime(string='Fecha del Procedimiento', required=True)
    descripcion = fields.Text(string='Descripción del Procedimiento')