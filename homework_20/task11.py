def make_logger(level):
    def logger(message):
        print(f"[{level}] {message}")
    return logger

info_logger = make_logger("INFO")
error_logger = make_logger("ERROR")

info_logger("This is an informational message")
error_logger("This is an error message")
