def info_logs(logs: list):

    module_dict ={}
    for log in logs:
        timestamp , module, status, test_id = log.split("|")
        timestamp = timestamp.strip()
        module = module.strip()
        status = status.strip()
        test_id = test_id.strip()
        if module not in module_dict:
            module_dict[module] ={}
        if status not in module_dict[module]:
            module_dict[module][status] = []
        module_dict[module][status].append(test_id)
            
    max_fail = 0
    max_module = []
    for module in module_dict:
        fail_count = len(module_dict[module].get("FAIL",[]))
        if fail_count >max_fail:
            max_fail = fail_count
            max_module = [module]
        elif fail_count == max_fail:
            max_module.append(module)
                                
    return{
        "ModuleReuslt": module_dict,

        "MostfailedModule": {
            "HighestFauledModule": max_module,
            "Count": max_fail
        }
    }

logs = [
    "2026-05-12 10:10:00 | HMI | PASS | TC101",
    "2026-05-12 10:15:00 | Bluetooth | FAIL | TC205",
    "2026-05-12 10:20:00 | HMI | PASS | TC102",
    "2026-05-12 10:25:00 | Navigation | FAIL | TC330",
    "2026-05-12 10:30:00 | Bluetooth | PASS | TC206",
    "2026-05-12 10:35:00 | HMI | FAIL | TC103"
]

print(info_logs(logs))