from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Triangle

class Isosceles(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
    
    def compute_area(self):
        lenght_edgeB = edgeB.compute_lenght()
        lenght_edgeC = edgeC.compute_lenght()
        base = edgeC.compute_lenght()
        height = ((lenght_edgeB)**2 - (lenght_edgeC/2)**2)**0.5
        return (base * height) / 2
    
    def compute_perimeter(self):
        lenght_edgeA = edgeA.compute_lenght()
        lenght_edgeB = edgeB.compute_lenght()
        lenght_edgeC = edgeC.compute_lenght()
        return lenght_edgeA + lenght_edgeB + lenght_edgeC
    
    def compute_inner_angles(self):
        return angleA + angleB + angleC
    
verticeA = Point(0,0)
verticeB = Point(4,0)
verticeC = Point(2,4)

edgeA = Line(verticeB,verticeC)
edgeB = Line(verticeC, verticeA)
edgeC = Line(verticeA, verticeB)

angleA = 63.4
angleB = 63.4
angleC = 53.1

vertices = [verticeA, verticeB, verticeC]
edges = [edgeA, edgeB, edgeC]
inner_angles = [angleA, angleB, angleC]

isosceles_triangle = Isosceles(False, vertices, edges, inner_angles)
print("Isoceles area: ", isosceles_triangle.compute_area())
print("Isosceles perimeter: ", isosceles_triangle.compute_perimeter())
print("Isosceles inner angles: ", isosceles_triangle.compute_inner_angles())
print("\n")