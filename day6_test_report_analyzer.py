from pprint import pprint
def reportAnalyzer(report:dict):
    build_info ={
        "build_version": report["build_version"],
        "execution_date": report["execution_date"],
        "build_health" : "INVESTIGATION REQUIRED"
    }
    module_results = {}
    execution_status={}
    long_running_test_cases = []
    for data in report["test_results"]:
        module = data["module"]
        test_case_id = data["testcase_id"]
        status = data["status"]
        execution_time = data["execution_time"]
        if module not in module_results:
            module_results[module]={}
        if status not in module_results[module]:
            module_results[module][status] =[]
        module_results[module][status].append(test_case_id)
        if status not in execution_status:
            execution_status[status] = 0
        execution_status[status] +=1
        
        if execution_time > 30:
            long_running_test_cases.append(test_case_id)
        
    return {
        "build_info": build_info,
        "module_results": module_results,
        "execution_status": execution_status,
        "long_running_test_cases": long_running_test_cases
    }
            
        
report = {
    "build_version": "v2.5.1",
    "execution_date": "2026-05-14",
    "test_results": [
        {
            "module": "Bluetooth",
            "testcase_id": "TC201",
            "status": "PASS",
            "execution_time": 12
        },
        {
            "module": "Bluetooth",
            "testcase_id": "TC202",
            "status": "FAIL",
            "execution_time": 35
        },
        {
            "module": "Navigation",
            "testcase_id": "TC330",
            "status": "BLOCKED",
            "execution_time": 0
        },
        {
            "module": "HMI",
            "testcase_id": "TC101",
            "status": "PASS",
            "execution_time": 8
        },
        {
            "module": "HMI",
            "testcase_id": "TC102",
            "status": "FAIL",
            "execution_time": 40
        }
    ]
}

result = reportAnalyzer(report)
pprint(result)