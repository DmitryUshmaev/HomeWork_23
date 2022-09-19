from typing import Dict, Any

from marshmallow import fields, Schema, validates_schema, ValidationError

VALID_CMD_PARAMS: tuple = ('filter', 'sort', 'map', 'unique', 'limit', 'regex')


# Схема запроса

class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError("'cmd' contains invalid value")

        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
