from shapes_utils.shape.shape import Shape


class PointShape(Shape):
    def show(self):
        self.canvas.create_oval(
            self.x1 - 2, self.y1 - 2, self.x1 + 2, self.y1 + 2, fill="black"
        )
