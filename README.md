# Reto-cinco

1. Para la primera parte de este reto lo que hice fue crear un paquete con un único modulo dentro de este, para luego hacer un llamado a cada función desde un archivo "main.py".

```
Reto cinco/
├── Paquete/
│   ├── __init__.py
│   ├── shape.py
└── main.py
```

**Shape module**

```
import math
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x
    
    def set_x(self, x):
        self._x = x
    
    def get_y(self):
        return self._y
    
    def set_y(self, y):
        self._y = y
    

    def compute_distance(self, other_point):
        distance = ((self._x - other_point.get_x())**2 + (self._y - other_point.get_y())**2)**0.5
        return distance
    
class Line:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def compute_lenght(self):
        lenght = ((self._end._x - self._start.get_x())**2 + (self._end._y - self._start.get_y())**2)**0.5
        return lenght
    
class Shape:
    def __init__(self, is_regular: bool):
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []
        self._inner_angles = []

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

class Triangle(Shape):
    def __init__(self, is_regular: bool):
        super().__init__(is_regular)

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
```

**Main module**

```
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
```

2. Para la segunda parte de este reto cree un archivo con un modulo distinto para cada figura.

```
├── Paquete/
│   ├── __init__.py
│   ├── shape.py
└── main.py
├── tri_equilateral.py
├── tri_isosceles.py
├── tri_rectangle.py
├── rectangle.py
├── tri_scalene.py
├── square.py
└── triangle.py
```
**Triangle module**

```
from Paquete.shape import Shape

class Triangle(Shape):
    def __init__(self, is_regular: bool):
        super().__init__(is_regular)
```

**tri_isosceles module**

```
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
```

**tri_equilateral module**

```
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
```

**tri_scalene module**

```
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
```

**tri_rectangle module**

```
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
```

**rectangle module**

```
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
```

**square module**

```
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
```
