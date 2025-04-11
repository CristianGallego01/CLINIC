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
    checklist_consent = fields.Boolean(string='Consentimiento informado firmado')
    checklist_exams = fields.Boolean(string='Exámenes preoperatorios revisados')
    checklist_equipment = fields.Boolean(string='Equipo quirúrgico preparado')
    checklist_allergies = fields.Boolean(string='Alergias conocidas verificadas')
    checklist_documents = fields.Boolean(string='Documentación completa')

    preparation_date = fields.Datetime(string='Fecha de Preparación', required=True)
    patient_signature = fields.Binary(string='Firma del Paciente' required=True)

    @fields.depends('checklist_consent', 'checklist_exams', 'checklist_equipment', 'checklist_allergies', 'checklist_documents')
    def _compute_checklist_verified(self):
        for rec in self:
            rec.checklist_verified = all([
                rec.checklist_consent,
                rec.checklist_exams,
                rec.checklist_equipment,
                rec.checklist_allergies,
                rec.checklist_documents
            ])