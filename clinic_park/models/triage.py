from odoo import models, fields,api

class ClinicParkTriage(models.Model):
    _name = 'clinic.park.triage'
    _description = 'Triage'

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True, ondelete='cascade')
    current_date= fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    reason = fields.Text(string='Motivo de Consulta', related ="patient_id.reason",required=True)
    name = fields.Char(string='Nombre', related='patient_id.name', store=True)
    age = fields.Integer(string='Edad', related='patient_id.age', store=True)
    dni = fields.Char(string='Cedula', related='patient_id.dni', store=True)
    # signos vitales
    temperatura = fields.Float(string='Temperatura', required=True)
    pulso = fields.Integer(string='Pulso', required=True)
    presion = fields.Char(string='Presion', required=True)
    # clasificacion
    atencion = fields.Selection([ 
        ('por clasificar', 'Por Clasificar'),
        ('consulta', 'Consulta'),
        ('preparacion', 'Preparación Quirúrgica'),
        ('cirugia', 'Cirugía'),
        ('recuperacion', 'Recuperación y Hospitalización'),
        ('facturacion', 'Facturación'),
    ],default="por clasificar",string="clasificacion",copy=False,required=True)

    patient_id = fields.Many2one('clinic.park.patient', string='Paciente')

    # @api.model
    # def create(self, vals):
    #     record = super().create(vals)
    #     if vals.get('atencion') == 'consulta':
    #         record._crear_consulta_si_aplica()
    #     return record

    # def write(self, vals):
    #     anterior_clasificacion = self.mapped('atencion')
    #     res = super().write(vals)

    #     for record, anterior in zip(self, anterior_clasificacion):
    #         nueva = vals.get('atencion', record.atencion)

    #         # Si cambió de 'consulta' a otra → eliminar consulta
    #         if anterior == 'consulta' and nueva != 'consulta':
    #             consulta = self.env['clinic.park.consultations'].search([('triage_id', '=', record.id)])
    #             consulta.unlink()

    #         # Si cambió a 'consulta' → crear consulta
    #         if anterior != 'consulta' and nueva == 'consulta':
    #             record._crear_consulta_si_aplica()

    #     return res

    # def _crear_consulta_si_aplica(self):
    #     self.ensure_one()
    #     Consulta = self.env['clinic.park.consultations']
    #     ya_existe = Consulta.search([('triage_id', '=', self.id)], limit=1)
    #     if not ya_existe:
    #         Consulta.create({
    #             'triage_id': self.id,
    #             'patient_id': self.patient_id.id,
    #         })
    
    @api.model
    def create(self, vals):
        record = super().create(vals)
        if vals.get('atencion') == 'consulta':
            record._crear_consulta_si_aplica()
        elif vals.get('atencion') == 'preparacion':
            record._crear_preparacion_si_aplica()
        return record

    def write(self, vals):
        anterior_clasificacion = self.mapped('atencion')
        res = super().write(vals)

        for record, anterior in zip(self, anterior_clasificacion):
            nueva = vals.get('atencion', record.atencion)

            # Si se cambia de consulta a otra
            if anterior == 'consulta' and nueva != 'consulta':
                consulta = self.env['clinic.park.consultations'].search([('triage_id', '=', record.id)])
                consulta.unlink()

            # Si se cambia a consulta
            if anterior != 'consulta' and nueva == 'consulta':
                record._crear_consulta_si_aplica()

            # Si se cambia de preparación a otra
            if anterior == 'preparacion' and nueva != 'preparacion':
                preparacion = self.env['clinic.park.prepared'].search([('triage_id', '=', record.id)])
                preparacion.unlink()

            # Si se cambia a preparación
            if anterior != 'preparacion' and nueva == 'preparacion':
                record._crear_preparacion_si_aplica()

        return res

    def _crear_consulta_si_aplica(self):
        self.ensure_one()
        Consulta = self.env['clinic.park.consultations']
        ya_existe = Consulta.search([('triage_id', '=', self.id)], limit=1)
        if not ya_existe:
            Consulta.create({
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            })

    def _crear_preparacion_si_aplica(self):
        self.ensure_one()
        Preparacion = self.env['clinic.park.prepared']
        ya_existe = Preparacion.search([('triage_id', '=', self.id)], limit=1)
        if not ya_existe:
            Preparacion.create({
                'triage_id': self.id,
                'patient_id': self.patient_id.id,
            })