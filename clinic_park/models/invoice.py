from odoo import models, fields
from odoo.exceptions import UserError

class ClinicParkInvoice(models.Model):
    _name = 'clinic.park.invoice'
    _description = 'Alta clínica con facturación'

    name = fields.Char(string="Nombre del Procedimiento", required=True)
    patient_id = fields.Many2one('clinic.park.patient', string='Paciente', required=True)
    description = fields.Text(string="Detalle / Insumos / Observaciones")
    total_amount = fields.Float(string="Total a Facturar", required=True)
    invoice_id = fields.Many2one('account.move', string="Factura Generada", readonly=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('invoiced', 'Facturado')
    ], default='draft', string='Estado')

    def action_create_invoice(self):
        if not self.total_amount or self.total_amount <= 0:
            raise UserError("El total debe ser mayor que cero.")

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.patient_id.id,
            'invoice_line_ids': [(0, 0, {
                'name': self.name + ' - ' + (self.description or ''),
                'quantity': 1,
                'price_unit': self.total_amount,
            })],
        })

        self.invoice_id = invoice.id
        self.state = 'invoiced'

    def action_view_invoice(self):
        if not self.invoice_id:
            raise UserError("No se ha generado ninguna factura aún.")
        return {
            'type': 'ir.actions.act_window',
            'name': 'Factura',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
