from datetime import datetime

class VehicleModel:
    allowed_fuels = {"electric", "gaseous"}

    def __init__(self, data):
        self.vin = data.get("vin")
        self.fuelType = data.get("fuelType", "").lower()
        self.noOfAxles = data.get("noOfAxles")
        self.timestamp = data.get("timestamp") or datetime.utcnow().isoformat()
        self.errors = []

    def is_valid(self):
        if not self.vin:
            self.errors.append("Missing required field: vin")
        if not self.noOfAxles:
            self.errors.append("Missing required field: noOfAxles")
        else:
            try:
                self.noOfAxles = int(self.noOfAxles)
            except ValueError:
                self.errors.append("noOfAxles must be an integer")

        if not self.fuelType:
            self.errors.append("Missing required field: fuelType")
        else:
            self.fuelType = self.fuelType.lower()
            if self.fuelType not in ["electric", "gaseous"]:
                self.errors.append("fuelType must be 'electric' or 'gaseous'")

        return len(self.errors) == 0

    def to_dict(self):
        return {
            "vin": self.vin,
            "noOfAxles": self.noOfAxles,
            "fuelType": self.fuelType,
            "timestamp": self.timestamp,
        }