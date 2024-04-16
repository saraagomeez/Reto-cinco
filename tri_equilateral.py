from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Triangle

class Equilateral(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        lenght_edgeE = edgeE.compute_lenght()
        lenght_edgeF = edgeF.compute_lenght()
        base = edgeF.compute_lenght()
        height = verticeF.compute_distance(point_height)
        return (base * height) / 2
    
    def compute_perimeter(self):
        lenght_edgeD = edgeD.compute_lenght()
        lenght_edgeE = edgeE.compute_lenght()
        lenght_edgeF = edgeF.compute_lenght()
        return lenght_edgeD + lenght_edgeE + lenght_edgeF
    
    def compute_inner_angles(self):
        return angleD + angleE + angleF
    
verticeD = Point(0,0)
verticeE = Point(6,0)
verticeF= Point(3, 5.1961)
point_height = Point(3,0)

edgeD = Line(verticeE,verticeF)
edgeE = Line(verticeF, verticeD)
edgeF = Line(verticeD, verticeE)

angleD = 60
angleE = 60
angleF = 60

vertices = [verticeD, verticeE, verticeF]
edges = [edgeD, edgeE, edgeF]
inner_angles = [angleD, angleE, angleF]

equilateral_triangle = Equilateral(True, vertices, edges, inner_angles)
print("Equilateral area: ", equilateral_triangle.compute_area())
print("Equilateral perimeter: ", equilateral_triangle.compute_perimeter())
print("Equilateral inner angles: ", equilateral_triangle.compute_inner_angles())
print("\n")