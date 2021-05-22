#excubefinder
def cube_finder(l):
    cube = [ ]
    for i in l:
        cube.append(i**3)
    return cube
number = list(range(1,4))
print(cube_finder(number))