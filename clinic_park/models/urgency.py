from odoo import models, fields

class ClinicParkUrgency(models.Model):
    _name = 'clinic.park.urgency'
    _description = 'Atención de Urgencia'

    name = fields.Char(string='Identificación', default='N/N', help='Nombre o identificador temporal del paciente')
    edad_aproximada = fields.Char(string='Edad aproximada', help='Ejemplo: "30 años", "adulto joven", "niño"')
    genero_aparente = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('indeterminado', 'Indeterminado')
    ], string='Género aparente', default='indeterminado')

    motivo_urgencia = fields.Text(string='Motivo de urgencia')
    hallazgos_clinicos = fields.Text(string='Hallazgos clínicos preliminares')
    fecha_ingreso = fields.Datetime(string='Hora de ingreso', default=fields.Datetime.now)
