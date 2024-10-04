from shapes_utils.shape.shape import Shape


class LineShape(Shape):
    def show(self):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")
