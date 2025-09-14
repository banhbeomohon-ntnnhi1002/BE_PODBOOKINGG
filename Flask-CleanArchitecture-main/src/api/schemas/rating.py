from marshmallow import Schema, fields, validate

class RatingRequestSchema(Schema):
    booking_id = fields.Integer(required=True)
    customer_id = fields.Integer(required=True)
    pod_id = fields.Integer(required=True)
    stars = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    comment = fields.String(allow_none=True)

class RatingResponseSchema(Schema):
    id = fields.Integer()
    booking_id = fields.Integer()
    customer_id = fields.Integer()
    pod_id = fields.Integer()
    stars = fields.Integer()
    comment = fields.String()
    created_at = fields.DateTime()