from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Rectangle

class Square(Rectangle):
    def __init__(self, is_regular: bool, vertices: list, edges: list, inner_angles: list):
        super().__init__(is_regular, vertices, edges, inner_angles)

    def compute_area(self):
        side = edgeQ.compute_lenght() or edgeR.compute_lenght() or edgeT.compute_lenght() or edgeU.compute_lenght()
        return side**2
    
    def compute_perimeter(self):
        side = edgeQ.compute_lenght() or edgeR.compute_lenght() or edgeT.compute_lenght() or edgeU.compute_lenght()
        return side * 4
    
    def compute_inner_angles(self):
        return angleQ + angleR + angleT + angleU
    
verticeQ = Point(0,0)
verticeR = Point(5,0)
verticeT= Point(5,5)
verticeU= Point(0,5)

edgeQ = Line(verticeR,verticeT)
edgeR = Line(verticeT, verticeU)
edgeT = Line(verticeU, verticeQ)
edgeU = Line(verticeQ, verticeR)

angleQ = 90
angleR = 90
angleT = 90
angleU = 90

vertices = [verticeQ, verticeR, verticeT, verticeU]
edges = [edgeQ, edgeR, edgeT, edgeU]
inner_angles = [angleQ, angleR, angleT, angleU]

square = Square(True, vertices, edges, inner_angles)
print("Square area: ", square.compute_area())
print("Square perimeter: ", square.compute_perimeter())
print("Square inner angles: ", square.compute_inner_angles())
print("\n")