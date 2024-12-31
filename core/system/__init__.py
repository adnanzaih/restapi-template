import platform
import psutil


class ClassSystem:
    def __init__(self):
        self.info = {}

    def get_system_info(self):
        self.info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "OS Release": platform.release(),
            "Architecture": platform.architecture()[0],
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "CPU Cores": psutil.cpu_count(logical=False),
            "Logical CPUs": psutil.cpu_count(logical=True),
            "Total RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
        }
        return self.info
