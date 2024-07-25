import datetime


def log_messages(severity, *messages, **metadata):
    log = [f"Severity: {severity}"]
    log.extend(f"{key.capitalize()}: {value}" for key, value in metadata.items())
    log.append("Messages:")
    log.extend(f"- {message}" for message in messages)
    return "\n".join(log)

severity = "ERROR"
messages = ["Failed to connect to database", "Timeout occured while fetching data"]
metadata = {
    "timestamp": datetime.datetime.now().isoformat(),
    "user": "admin"
}

log = log_messages(severity, *messages, **metadata)
print(log)
