from odoo import models, fields

class ClinicParkProcedure(models.Model):
    _name = 'clinic.park.procedure'
    _description = 'Procedimiento'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    consultations_id = fields.Many2one('clinic.park.consultations', string='Consulta', required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)
    procedimiento = fields.Text(string='Procedimiento',related="consultations_id.procedimientos", required=True)
    procedure_date = fields.Datetime(string='Fecha del Procedimiento', required=True)
    descripcion = fields.Text(string='Descripción del Procedimiento')
    costo = fields.Float(string='Costo', required=True)