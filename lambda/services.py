from models import VehicleModel
from utils import respond
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('vehicle-demo')


class VehicleService:

    def create_vehicle(self, data):
        vehicle = VehicleModel(data)
        if not vehicle.is_valid():
            return respond(400, {"error": vehicle.errors})

        table.put_item(Item=vehicle.to_dict())
        return respond(201, {"message": "Vehicle created", "timestamp": vehicle.timestamp})

    def list_vehicles(self):
        response = table.scan()
        items = [VehicleModel(item).to_dict() for item in response.get('Items', [])]
        return respond(200, items)

    def delete_vehicle(self, data):
        vin = data.get('vin')
        if not vin:
            return respond(400, {"error": "Missing required field: vin"})
        table.delete_item(Key={"vin": vin})
        return respond(200, {"message": "Vehicle deleted"})