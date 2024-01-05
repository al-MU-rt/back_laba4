from marshmallow import Schema, fields, validate

class Us_Sch(Schema):
    id = fields.Int()
    u_name = fields.String(required=True)
    default_curr_id = fields.Int(required=False)
    password = fields.String(required=True)
class Categ_Sch(Schema):
    name = fields.String(required=True)

class Rec_Sch(Schema):
    categ_id = fields.Integer(required=True, validate=validate.Range(min=0))
    u_id = fields.Integer(required=True, validate=validate.Range(min=0))
    am = fields.Float(required=True, validate=validate.Range(min=0.0))
    curr_id = fields.Int(required=False)

class Curr_Sch(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    symb = fields.Str(required=True)
