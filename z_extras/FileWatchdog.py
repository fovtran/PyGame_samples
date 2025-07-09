from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

import os
import hashlib
import time

def calculate_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

if __name__ == "__main__":
    file_to_watch = "example.txt"
    last_hash = calculate_file_hash(file_to_watch)

    while True:
        time.sleep(1)
        if os.path.exists(file_to_watch):
            current_hash = calculate_file_hash(file_to_watch)
            if current_hash != last_hash:
                print(f"File changed: {file_to_watch}")
                last_hash = current_hash
        else:
            print(f"File deleted: {file_to_watch}")
            break


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    path_to_watch = "."  # Monitor the current directory
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
