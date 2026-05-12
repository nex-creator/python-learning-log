
def middleware_log_parser(response:dict):
    grouped_module ={}
    resp_times = {}
    for record in response["data"]:
        module = record["module"]
        testcase_id = record["testcase_id"]
        result = record["result"]
        resp_time_ms = record["response_time_ms"]
        if module not in grouped_module:
            grouped_module[module]={}
        if result not in grouped_module[module]:
            grouped_module[module][result] =[]
        grouped_module[module][result].append(testcase_id)
        if module not in resp_times:
            resp_times[module] =[]  
        resp_times[module].append(resp_time_ms)
        
    avg_resp_time ={} 
    for module in resp_times:
        values = resp_times[module]
        avg = sum(values) / len(values)
        avg_resp_time[module] = avg
        
    # Threshold 
    slow_modules =[]    
    for module in avg_resp_time:
        val = avg_resp_time[module]
        if val > 300:
            slow_modules.append(module)
        
        
    
    return {
        "functional": grouped_module,
        "timingLogs": resp_times,
        "metrics": {
            "avg_resp_time": avg_resp_time,
            "slow_module": slow_modules
        }
    } 
          

response = {
    "status": "success",
    "data": [
        {
            "module": "Bluetooth",
            "testcase_id": "TC201",
            "result": "PASS",
            "response_time_ms": 120
        },
        {
            "module": "Navigation",
            "testcase_id": "TC330",
            "result": "FAIL",
            "response_time_ms": 350
        },
        {
            "module": "Bluetooth",
            "testcase_id": "TC202",
            "result": "FAIL",
            "response_time_ms": 500
        },
        {
            "module": "HMI",
            "testcase_id": "TC101",
            "result": "PASS",
            "response_time_ms": 90
        }
    ]
}

print(middleware_log_parser(response))