from pprint import pprint
def vehicle_log_analyzer(vehicle_response:dict) :
    validation_error = []
    for index, response in enumerate(vehicle_response["vehicles"],start =1):
        key_fields = {
            "record_index": index,
            "failed_fields":[]
        }
        vin = response["vin"]
        model = response["model"]
        software_version = response["software_version"]
        status =  response["status"]
        last_sync_days = response["last_sync_days"]
        if not vin:
            key_fields["failed_fields"].append("vin")
        if not model:
            key_fields["failed_fields"].append("model")
        if not software_version:
            key_fields["failed_fields"].append("software_version")
        if key_fields["failed_fields"]:
            validation_error.append(key_fields)
        
        
    return validation_error



vehicle_response = {
    "api_version": "v3.2.1",
    "region": "NA",
    "vehicles": [

        {
            "vin": "1HGCM82633A123456",
            "model": "Honda Accord",
            "software_version": "v2.1.0",
            "status": "ACTIVE",
            "last_sync_days": 2
        },

        {
            "vin": "",
            "model": "Toyota Camry",
            "software_version": "v2.0.1",
            "status": "ACTIVE",
            "last_sync_days": 5
        },

        {
            "vin": "1HGCM82633A123457",
            "model": "",
            "software_version": "v1.0.0",
            "status": "INACTIVE",
            "last_sync_days": 45
        },

        {
            "vin": "1HGCM82633A123456",
            "model": "Honda Civic",
            "software_version": "v2.1.0",
            "status": "ACTIVE",
            "last_sync_days": 1
        },

        {
            "vin": "",
            "model": "",
            "software_version": "",
            "status": "ERROR",
            "last_sync_days": 90
        }
    ]
}
result = vehicle_log_analyzer(vehicle_response)
pprint(result)