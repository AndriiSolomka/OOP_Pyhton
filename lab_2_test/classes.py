from abc import ABC, abstractmethod


class ShapeObjectsEditor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.all_shapes = []

    def clear_bindings(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def redraw_all_shapes(self):
        self.canvas.delete("all")
        for shape in self.all_shapes:
            print(shape)
            shape.show()

    def StartPointEditor(self):
        self.point_editor = PointEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", self.point_editor.on_button_press)

    def StartLineEditor(self):
        self.line_editor = LineEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", self.line_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", self.line_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.line_editor.on_button_release)

    def StartSquareEditor(self):
        self.square_editor = SquareEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", self.square_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", self.square_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.square_editor.on_button_release)

    def StartEllipseEditor(self):
        self.ellipse_editor = EllipseEditor(self.canvas, self.all_shapes, self)
        self.canvas.bind("<Button-1>", self.ellipse_editor.on_button_press)
        self.canvas.bind("<B1-Motion>", self.ellipse_editor.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.ellipse_editor.on_button_release)


class Shape(ABC):
    def __init__(self, canvas, x1=None, y1=None, x2=None, y2=None):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @abstractmethod
    def show(self):
        pass


class PointShape(Shape):
    def show(self):
        self.canvas.create_oval(
            self.x1 - 2, self.y1 - 2, self.x1 + 2, self.y1 + 2, fill="black"
        )


class LineShape(Shape):
    def show(self):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")


class SquareShape(Shape):
    def show(self):
        self.canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, outline="black"
        )


class EllipseShape(Shape):
    def show(self):
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black")


class ShapeEditor(ABC):
    def __init__(self, canvas, all_shapes, shape_objects_editor):
        self.canvas = canvas
        self.all_shapes = all_shapes
        self.shape_objects_editor = shape_objects_editor
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.temp_item = None

    def on_button_press(self, event):
        self.x1, self.y1 = event.x, event.y

    def on_mouse_drag(self, event):
        if self.temp_item:
            self.canvas.delete(self.temp_item)
        self.temp_item = self.draw_temp_shape(event)

    def on_button_release(self, event):
        if self.temp_item:
            self.canvas.delete(self.temp_item)
        self.x2, self.y2 = event.x, event.y
        self.draw_shape()

    @abstractmethod
    def draw_temp_shape(self, event):
        pass

    @abstractmethod
    def draw_shape(self):
        pass


class PointEditor(ShapeEditor):
    def on_button_press(self, event):
        point = PointShape(self.canvas, event.x, event.y)
        self.all_shapes.append(point)
        self.shape_objects_editor.redraw_all_shapes()

    def draw_temp_shape(self):
        pass

    def draw_shape(self):
        pass


class LineEditor(ShapeEditor):
    def draw_temp_shape(self, event):
        return self.canvas.create_line(
            self.x1, self.y1, event.x, event.y, fill="grey", dash=(4, 2)
        )

    def draw_shape(self):
        line = LineShape(self.canvas, self.x1, self.y1, self.x2, self.y2)
        self.all_shapes.append(line)
        self.shape_objects_editor.redraw_all_shapes()


class SquareEditor(ShapeEditor):
    def draw_temp_shape(self, event):
        return self.canvas.create_rectangle(
            self.x1, self.y1, event.x, event.y, outline="grey", dash=(4, 2)
        )

    def draw_shape(self):
        square = SquareShape(self.canvas, self.x1, self.y1, self.x2, self.y2)
        self.all_shapes.append(square)
        self.shape_objects_editor.redraw_all_shapes()


class EllipseEditor(ShapeEditor):
    def draw_temp_shape(self, event):
        dx = abs(self.x1 - event.x)
        dy = abs(self.y1 - event.y)
        return self.canvas.create_oval(
            self.x1 - dx,
            self.y1 - dy,
            self.x1 + dx,
            self.y1 + dy,
            outline="grey",
            dash=(4, 2),
        )

    def draw_shape(self):
        dx = abs(self.x1 - self.x2)
        dy = abs(self.y1 - self.y2)
        ellipse = EllipseShape(
            self.canvas, self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy
        )
        self.all_shapes.append(ellipse)  # Добавляем эллипс в список
        self.shape_objects_editor.redraw_all_shapes()  # Перерисовываем все фигуры на холсте
