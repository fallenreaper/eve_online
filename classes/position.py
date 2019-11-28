

class Position:
    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_json(cls, js):
        x = js["x"] if "x" in js else None
        y = js["y"] if "y" in js else None
        z = js["z"] if "z" in js else None
        return cls(x,y,z)