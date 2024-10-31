import threading
import time
import queue


log_queue = queue.Queue()

def log_reader():

    with open(log_file_path, 'r') as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if line:
                log_queue.put(line)
            else:
                time.sleep(0.5)

def log_analyzer():
    while True:
        line = log_queue.get()
        if "ERROR" in line:
            print(line.strip())
        log_queue.task_done()

if __name__ == '__main__':
    log_file_path = 'server_log.txt'

    read_thread = threading.Thread(target=log_reader)
    analyze_thread = threading.Thread(target=log_analyzer)

    read_thread.start()
    analyze_thread.start()

    read_thread.join()
    analyze_thread.join()

