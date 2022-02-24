# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, template = "Hello, <name>!"):
    greet_string = template.replace("<name>", name)

    return greet_string

def force(mass, body = "earth"):
    planets = {
        "sun"       : 274.0, 
        "jupiter"   : 24.9, 
        "neptune"   : 11.2, 
        "saturn"    : 10.4, 
        "earth"     : 9.8, 
        "uranus"    : 8.9, 
        "venus"     : 8.9, 
        "mars"      : 3.7, 
        "mercury"   : 3.7, 
        "moon"      : 1.6, 
        "pluto"     : 0.6, 
        }
    amnt_force = round((mass * planets[body]), 1)

    return(amnt_force)

def pull(m1, m2, d):
    # G = gravitational_constant
    gravitational_constant = (6.674 * (10 ** -11))
    # F = force
    force = (gravitational_constant * ((m1 * m2)/(d ** 2)))
    return force

print(greet("Bob"))
print(greet("Bob", "What's up, <name>!"))
print(force(1.5))
print(pull(0.1, (5.972 * (10 ** 24)), (6.371 *(10 ** 6))))
