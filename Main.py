from Paquete.shape import Point
from Paquete.shape import Line
from Paquete.shape import Rectangle
from Paquete.shape import Square
from Paquete.shape import Isosceles
from Paquete.shape import Equilateral
from Paquete.shape import Scalene
from Paquete.shape import TriRectangle

if __name__ == "__main__":
    def Tri_Isosceles():
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

    def Tri_Equilateral():
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

    def Tri_Scalene():
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

    def Tri_Rectangle():
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

    def Rect():
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

    def Sqr():
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

    Tri_Isosceles()
    Tri_Equilateral()
    Tri_Scalene()
    Tri_Rectangle()
    Rect()
    Sqr()