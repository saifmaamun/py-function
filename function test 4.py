# planet

planets = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"
}

def planetFinder(id):
    if len(planets)<id:
        return "no Planet found"
    else:
        return planets[id]

x= planetFinder(1)
print(x)