class Device:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    def __str__(self):
        return f"{self.name} ({self.device_type})"

class SmartHome:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def __iter__(self):
        # TODO: Return a SmartHomeIterator instance
        pass

class SmartHomeIterator:
    def __init__(self, devices):
        # TODO: Initialize the iterator
        pass

    def __next__(self):
        # TODO: Return the next device or raise StopIteration
        pass
