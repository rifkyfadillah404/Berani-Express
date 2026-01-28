from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CourierCustomer(models.Model):
    _name = 'courier.customer'
    _description = 'Courier Customer'

    name = fields.Char(string='Nama Pelanggan', required=True)


class CourierShipment(models.Model):
    _name = 'courier.shipment'
    _description = 'Courier Shipment'

    name = fields.Char(string='No. Resi', required=True)
    customer_id = fields.Many2one('courier.customer', string='Pelanggan')


class CourierIncident(models.Model):
    _name = 'courier.incident'
    _description = 'Courier Incident'

    name = fields.Char(
        string='Judul Insiden',
        required=True,
    )
    customer_id = fields.Many2one(
        'courier.customer',
        string='Pelanggan',
        required=True,
    )
    shipment_id = fields.Many2one(
        'courier.shipment',
        string='No. Resi',
    )
    incident_type = fields.Selection(
        selection=[
            ('health', 'Health'),
            ('lost_item', 'Lost Item'),
            ('delay', 'Delay'),
            ('other', 'Other'),
        ],
        string='Tipe',
        default='other',
    )
    incident_datetime = fields.Datetime(
        string='Waktu',
        required=True,
        default=fields.Datetime.now,
    )
    severity = fields.Selection(
        selection=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        string='Urgensi',
        default='low',
    )
    description = fields.Text(string='Kronologi')
    followup_note = fields.Text(string='Catatan')
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('followup', 'Follow Up'),
            ('done', 'Done'),
        ],
        string='Status',
        default='draft',
    )
    resolved_at = fields.Datetime(
        string='Selesai pada',
        readonly=True,
    )

    _sql_constraints = [
        (
            'unique_customer_type_datetime',
            'UNIQUE(customer_id, incident_type, incident_datetime)',
            'Incident with same customer, type, and datetime already exists!'
        ),
    ]

    def action_followup(self):
        """Mark incident as follow-up"""
        self.write({'state': 'followup'})

    def action_resolve(self):
        """Mark incident as resolved"""
        self.write({
            'state': 'done',
            'resolved_at': fields.Datetime.now(),
        })

    @api.constrains('state', 'followup_note')
    def _check_followup_note(self):
        for record in self:
            if record.state == 'done' and not record.followup_note:
                raise ValidationError('Catatan wajib diisi sebelum menyelesaikan insiden!')
