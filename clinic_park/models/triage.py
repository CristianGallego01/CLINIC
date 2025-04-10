from odoo import models, fields

class ClinicParkTriage(models.Model):
    _name = 'clinic.park.triage'
    _description = 'Triage'
    _inherit = ['mail.thread']

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True, ondelete='cascade')
    current_date= fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    reason = fields.Text(string='Motivo de Consulta', required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    age = fields.Integer(string='Edad', related='patient_id.age', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)
    # signos vitales
    temperatura = fields.Float(string='Temperatura', required=True)
    pulso = fields.Integer(string='Pulso', required=True)
    presion = fields.Char(string='Presion', required=True)
    # clasificacion
    atencion = fields.Selection([  
        ('consulta', 'Consulta'),
        ('preparacion', 'Preparación Quirúrgica'),
        ('cirugia', 'Cirugía'),
        ('recuperacion', 'Recuperación y Hospitalización'),
        ('facturacion', 'Facturación'),
    ],string="clasificacion",copy=False,required=True)