from tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, arr):
        self.arr = arr
        pass

    def need_service(self):
        for i in self.arr:
            if i >= 0.9:
                return True
            
        return False