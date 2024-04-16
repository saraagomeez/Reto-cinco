from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Triangle

class TriRectangle(Triangle):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        base = edgeL.compute_lenght()
        height = edgeK.compute_lenght()
        return (base * height) / 2
    
    def compute_perimeter(self):
        lenght_edgeJ = edgeJ.compute_lenght()
        lenght_edgeK = edgeK.compute_lenght()
        lenght_edgeL = edgeL.compute_lenght()
        return lenght_edgeJ + lenght_edgeK + lenght_edgeL
    
    def compute_inner_angles(self):
        return angleJ + angleK + angleL
    
verticeJ = Point(0,0)
verticeK = Point(4,0)
verticeL= Point(0,6)

edgeJ = Line(verticeK,verticeL)
edgeK = Line(verticeL, verticeJ)
edgeL = Line(verticeJ, verticeK)

angleJ = 90
angleK = 45
angleL = 45

vertices = [verticeJ, verticeK, verticeL]
edges = [edgeJ, edgeK, edgeL]
inner_angles = [angleJ, angleK, angleL]

tri_rectangle_triangle = TriRectangle(False, vertices, edges, inner_angles)
print("Triangle rectangle area: ", tri_rectangle_triangle.compute_area())
print("Triangle rectangle perimeter: ", tri_rectangle_triangle.compute_perimeter())
print("Triangle rectangle inner angles: ", tri_rectangle_triangle.compute_inner_angles())
print("\n")