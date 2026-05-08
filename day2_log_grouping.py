# from collections import defaultdict

def log_grouping(logs: list):
    grouped_logs = {}

    for log in logs:
        level,message = log.split("|")   #split the strings
        level = level.strip()   #remove the extra spaces from the string
        message = message.strip()
        if level not in grouped_logs:
            grouped_logs[level] = [message]
        else:
            grouped_logs[level].append(message)
            
    max_level = None
    max_count = 0
    for key,val in grouped_logs.items():
        key_length = len(val)
        if key_length > max_count:
            max_count = key_length
            max_level = key
    
    
    return {
    "grouped_logs": grouped_logs,
    "max_level": max_level,
    "max_count": max_count
    }

logs = [
    "INFO | User logged in",
    "ERROR | Payment failed",
    "INFO | Page loaded",
    "WARNING | Low battery",
    "INFO | User logout",
    "ERROR | Timeout error"
]
print(log_grouping(logs))
