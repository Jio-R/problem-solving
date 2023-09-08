import math

#Starting Triangle
polygonSides = 6
polygonSideLength = 1
apothem = math.sqrt(1 - (polygonSideLength/2)**2)
pi = polygonSides * polygonSideLength / 2

#New triangle(s)
for i in range(int(input("Polygon to have 6 * 2^n sides: "))):
    polygonSideLength = math.sqrt((polygonSideLength/2)**2 + (1-apothem)**2)
    apothem = math.sqrt(1-(polygonSideLength/2)**2)

    polygonSides *= 2
    pi = polygonSides * polygonSideLength / 2

print("A " + str(polygonSides) + "-sided polygon with a radius of 1 has a perimeter of " + str(pi))
