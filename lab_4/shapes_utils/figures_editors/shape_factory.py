from lab_4.shapes_utils.figure_shapes.cube_shape import CubeShape
from lab_4.shapes_utils.figure_shapes.ellipseLine_shape import EllipseLineShape
from lab_4.shapes_utils.figure_shapes.ellipse_shape import EllipseShape
from lab_4.shapes_utils.figure_shapes.line_shape import LineShape
from lab_4.shapes_utils.figure_shapes.point_shape import PointShape
from lab_4.shapes_utils.figure_shapes.square_shape import SquareShape
from lab_4.shapes_utils.temp_shapes.temp_cube import TempCube
from lab_4.shapes_utils.temp_shapes.temp_ellipse import TempEllipse
from lab_4.shapes_utils.temp_shapes.temp_ellipseLine import TempEllipseLine
from lab_4.shapes_utils.temp_shapes.temp_line import TempLine
from lab_4.shapes_utils.temp_shapes.temp_square import TempSquare


class ShapeFactory:
    _temp_shape_classes = {
        'Line': TempLine,
        'Square': TempSquare,
        'Ellipse': TempEllipse,
        'EllipseLine': TempEllipseLine,
        'Cube': TempCube,
    }

    _shape_classes = {
        'Point': PointShape,
        'Line': LineShape,
        'Square': SquareShape,
        'Ellipse': EllipseShape,
        'EllipseLine': EllipseLineShape,
        'Cube': CubeShape,
    }

    @classmethod
    def get_temp_shape_class(cls, shape_type):
        return cls._temp_shape_classes.get(shape_type)

    @classmethod
    def get_shape_class(cls, shape_type):
        return cls._shape_classes.get(shape_type)
