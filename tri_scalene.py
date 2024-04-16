from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Triangle

class Scalene(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        base = edgeI.compute_lenght()
        height = verticeI.compute_distance(point_height)
        return (base * height) / 2
    
    def compute_perimeter(self):
        lenght_edgeG = edgeG.compute_lenght()
        lenght_edgeH = edgeH.compute_lenght()
        lenght_edgeI = edgeI.compute_lenght()
        return lenght_edgeG + lenght_edgeH + lenght_edgeI
    
    def compute_inner_angles(self):
        return angleG + angleH + angleI
    
verticeG = Point(0,0)
verticeH = Point(9,0)
verticeI= Point(3,5)
point_height = Point(3,0)

edgeG = Line(verticeH,verticeI)
edgeH = Line(verticeI, verticeG)
edgeI = Line(verticeG, verticeH)

angleG = 59.03
angleH = 39.80
angleI = 81.15

vertices = [verticeG, verticeH, verticeI]
edges = [edgeG, edgeH, edgeI]
inner_angles = [angleG, angleH, angleI]

scalene_triangle = Scalene(False, vertices, edges, inner_angles)
print("Scalene area: ", scalene_triangle.compute_area())
print("Scalene perimeter: ", scalene_triangle.compute_perimeter())
print("Scalene inner angles: ", scalene_triangle.compute_inner_angles())
print("\n")