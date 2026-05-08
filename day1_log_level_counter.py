def log_analyzer(logs: list) -> dict:
    output ={}
    for log in logs:
        level,message = log.split("|")
        level = level.strip()
        message = message.strip()
        if level not in output:
            output[level] = 1
        else:
            output[level] +=1
    return output
        






logs = [
    "INFO | User logged in",
    "ERROR | Payment failed",
    "INFO | Page loaded",
    "WARNING | Low battery",
    "INFO | User logout"
]
print(log_analyzer(logs))