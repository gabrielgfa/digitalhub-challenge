import json
from services import VehicleService
from utils import respond, parse_body

service = VehicleService()

def lambda_handler(event, context):
    method = event.get('httpMethod', '').upper()

    if method == 'POST':
        data = parse_body(event)
        return service.create_vehicle(data)

    elif method == 'GET':
        return service.list_vehicles()

    elif method == 'DELETE':
        data = parse_body(event)
        return service.delete_vehicle(data)

    else:
        return respond(405, {"error": "Method not allowed"})