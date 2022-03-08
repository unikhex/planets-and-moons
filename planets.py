#classes of planets
class Planet:
    def __init__(self, name,  size):
        self.name = name
        self.size = size
        self.moons = []
    
    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_moons(self):
        return self.moons
    
    def add_moon(self):
        self.moons.append()

class Moon:
    def __init__(self, name,  size):
        self.name = name
        self.size = size
        self.orbits = None
    
    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_orbit(self):
        return self.orbits
    
    def add_orbit(self, orbit):
        self.orbits = orbit
    



    

