from marshmallow import Schema, fields

class NotificationResponseSchema(Schema):
    id = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    booking_id = fields.Int(required=True)
    title = fields.Str(required=True)
    message = fields.Str(required=True)
    type = fields.Str(required=True)
    is_read = fields.Bool(required=True)
    created_at = fields.Raw(required=True)
    sent_at = fields.Raw(allow_none=True)