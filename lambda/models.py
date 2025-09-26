class VehicleModel:
    allowed_fuels = {"electric", "gaseous"}

    def __init__(self, data):
        self.vin = data.get("vin")
        self.fuelType = data.get("fuelType", "").lower()
        self.noOfAxles = data.get("noOfAxles")
        self.errors = []

    def is_valid(self):
        if not self.vin:
            self.errors.append("Missing vin")
        if not self.noOfAxles:
            self.errors.append("Missing noOfAxles")
        else:
            try:
                self.noOfAxles = int(self.noOfAxles)
            except (ValueError, TypeError):
                self.errors.append("noOfAxles must be an integer")

        if self.fuelType not in self.allowed_fuels:
            self.errors.append("fuelType must be 'electric' or 'gaseous'")

        return not self.errors

    def to_dict(self):
        return {
            "vin": self.vin,
            "noOfAxles": self.noOfAxles,
            "fuelType": self.fuelType
        }