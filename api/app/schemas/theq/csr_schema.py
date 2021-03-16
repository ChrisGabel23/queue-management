'''Copyright 2018 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

import toastedmarshmallow
from marshmallow import fields
from app.models.theq import CSR
from app.schemas.theq import CSRStateSchema, OfficeSchema, RoleSchema
from qsystem import ma


class CSRSchema(ma.SQLAlchemySchema):

    class Meta:
        model = CSR
        include_relationships = True
        load_instance = True
        jit = toastedmarshmallow.Jit

    csr_id = fields.Int()
    username = fields.Str()
    office_id = fields.Int()
    role_id = fields.Int()
    receptionist_ind = fields.Int()
    deleted = fields.DateTime()
    csr_state_id = fields.Int()
    counter_id = fields.Int()
    counter = fields.Int(attribute="counter_id")
    csr_state = fields.Nested(CSRStateSchema(exclude=('csrs',)))
    office = fields.Nested(OfficeSchema())
    role = fields.Nested(RoleSchema(exclude=('roles',)))
    office_manager = fields.Int()
    pesticide_designate = fields.Int()
    qt_xn_csr_ind = fields.Int()
    finance_designate = fields.Int()
    ita2_designate = fields.Int()
