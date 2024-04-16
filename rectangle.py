from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Shape

class Rectangle(Shape):
    def __init__(self, is_regular: bool, vertices:list, edges:list, inner_angles:list):
        super().__init__(is_regular)
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

    def compute_area(self):
        width = edgeN.compute_lenght() or edgeP.compute_lenght()
        lenght = edgeM.compute_lenght() or edgeO.compute_lenght()
        return width * lenght
    
    def compute_perimeter(self):
        width = edgeN.compute_lenght() or edgeP.compute_lenght()
        lenght = edgeM.compute_lenght() or edgeO.compute_lenght()
        return (width * 2) + (lenght * 2)
    
    def compute_inner_angles(self):
        return angleM + angleN + angleO + angleP
    
verticeM = Point(0,0)
verticeN = Point(8,0)
verticeO= Point(8,4)
verticeP= Point(0,4)

edgeM = Line(verticeN,verticeO)
edgeN = Line(verticeO, verticeP)
edgeO = Line(verticeP, verticeM)
edgeP = Line(verticeM, verticeN)

angleM = 90
angleN = 90
angleO = 90
angleP = 90

vertices = [verticeM, verticeN, verticeO, verticeP]
edges = [edgeM, edgeN, edgeO, edgeP]
inner_angles = [angleM, angleN, angleO, angleP]

rectangle = Rectangle(False, vertices, edges, inner_angles)
print("Rectangle area: ", rectangle.compute_area())
print("Rectangle perimeter: ", rectangle.compute_perimeter())
print("Rectangle inner angles: ", rectangle.compute_inner_angles())
print("\n")