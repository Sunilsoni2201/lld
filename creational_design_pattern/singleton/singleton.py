import concurrent.futures
import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                cls._instance = super().__new__(cls)
        return cls._instance


def get_instance():
    instance = Singleton()
    print(f'Instance ID: {id(instance)}')
