class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
        
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    
hoth = Planet('Hoth', 20000, 5.5, 'Hoth Sytem')
print(f'Names is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')
print(hoth.orbit())