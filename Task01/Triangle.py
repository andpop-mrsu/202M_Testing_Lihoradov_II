from triangle_func import IncorrectTriangleSides


class Triangle:
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

        if (first_side + second_side <= third_side
                or first_side + third_side <= second_side
                or second_side + third_side <= first_side):
            raise IncorrectTriangleSides('Sides set incorrectly')

    def triangle_type(self) -> str:
        if self.first_side != self.second_side != self.third_side:
            return "nonequilateral"
        elif self.first_side == self.second_side == self.third_side:
            return "equilateral"
        else:
            return "isosceles"

    def perimeter(self) -> int:
        return self.first_side + self.second_side + self.third_side
