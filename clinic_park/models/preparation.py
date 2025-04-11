from odoo import models, fields

class ClinicParkPreparation(models.Model):
    _name = 'clinic.park.preparation'
    _description = 'Preparación Quirúrgica'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    triage_id = fields.Many2one('clinic.park.triage', string='Triage')
    consultation_id = fields.Many2one('clinic.park.consultations', string='Consulta')

    preoperative_form = fields.Text(string='Formulario Preoperatorio', required=True)
    supplies = fields.Text(string='Insumos Utilizados', required=True)
    nurse_signature = fields.Char(string='Firma de Enfermería', required=True)
    checklist_verified = fields.Boolean(string='Lista de Chequeo Verificada', default=False)

    preparation_date = fields.Datetime(string='Fecha de Preparación', required=True)