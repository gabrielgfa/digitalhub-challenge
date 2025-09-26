from datetime import datetime
from typing import Dict, Any, List


class VehicleModel:
    REQUIRED_FIELDS = {"vin", "noOfAxles", "fuelType"}
    ALLOWED_FUELS = {"electric", "gaseous"}

    def __init__(self, data: Dict[str, Any]):
        self.raw_data = data
        self.vin: str | None = data.get("vin")
        self.no_of_axles: int | None = None
        self.fuel_type: str | None = None
        self.timestamp: str = data.get("timestamp") or datetime.utcnow().isoformat()
        self.errors: List[str] = []
        self._validate()

    def _validate(self):
        if not self.vin:
            self.errors.append("Missing required field: vin")

        no_of_axles = self.raw_data.get("noOfAxles")
        if no_of_axles is None:
            self.errors.append("Missing required field: noOfAxles")
        else:
            try:
                self.no_of_axles = int(no_of_axles)
            except (ValueError, TypeError):
                self.errors.append("noOfAxles must be an integer")

        fuel_type = self.raw_data.get("fuelType")
        if not fuel_type:
            self.errors.append("Missing required field: fuelType")
        else:
            fuel_type = str(fuel_type).lower()
            if fuel_type not in self.ALLOWED_FUELS:
                self.errors.append(f"fuelType must be one of {', '.join(self.ALLOWED_FUELS)}")
            else:
                self.fuel_type = fuel_type

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "vin": self.vin,
            "noOfAxles": self.no_of_axles,
            "fuelType": self.fuel_type,
            "timestamp": self.timestamp,
        }