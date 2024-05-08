from tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, arr):
        self.arr = arr
        pass

    def need_service(self):
        s = 0
        for i in self.arr:
            s+= i
            
        if s >= 3:
            return True
            
        return False