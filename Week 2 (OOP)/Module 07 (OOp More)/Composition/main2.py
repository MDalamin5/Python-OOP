class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size
        

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        pass


class Computer:
    def __init__(self, cores, size, capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(size)
        self.capacity = HardDrive(capacity)
        pass
            