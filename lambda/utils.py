import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            if o % 1 == 0:
                return int(o)
            else:
                return float(o)
        return super().default(o)

def respond(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body, cls=DecimalEncoder)
    }

def parse_body(event):
    try:
        return json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {}