import math

class RightTriangle:
    def __init__(self, a=0.0, b=0.0, c=0.0, A=0.0, B=0.0):
        self.a = a  # side a
        self.b = b  # side b
        self.c = c  # hypotenuse c
        self.A = A  # angle A (non-right angle)
        self.B = B  # angle B (non-right angle)
        self.C = 90.0  # angle B (non-right angle, automatically 90 - A)
    
    # Convert degrees to radians
    def degrees_to_radians(self, degrees):
        return degrees * math.pi / 180

    # Convert radians to degrees
    def radians_to_degrees(self, radians):
        return radians * 180 / math.pi
    
    # Pythagorean Theorem to find the missing side (hypotenuse or leg)
    def pythagorean_theorem(self):
        return math.sqrt(self.a**2 + self.b**2)

    # Method to print the sides and angles of the triangle
    def print_triangle_details(self):
        print("\nTriangle Details:")
        print(f"Sides: a = {self.a:.2f}, b = {self.b:.2f}, c = {self.c:.2f}")
        print(f"Angles: A = {self.A:.2f}°, B = {self.B:.2f}°, C = 90.00° (right angle)")
    
    # Method to solve the right triangle based on given inputs
    def solve(self):
        if self.a != 0 and self.b != 0:
            # Calculate the angles based on the sides using inverse trig functions
            angle_A_rad = math.atan(self.b / self.a)  # Angle A: opposite b, adjacent a
            angle_B_rad = math.atan(self.a / self.b)  # Angle B: opposite a, adjacent b

            self.A = self.radians_to_degrees(angle_A_rad)
            self.B = self.radians_to_degrees(angle_B_rad)

            self.c = self.pythagorean_theorem()
            self.print_triangle_details()

        elif self.c != 0 and self.a != 0 and self.b == 0:
            self.b = math.sqrt(self.c**2 - self.a**2)
            angle_A_rad = math.atan(self.b / self.a)
            angle_B_rad = math.atan(self.a / self.b)
            self.A = self.radians_to_degrees(angle_A_rad)
            self.B = self.radians_to_degrees(angle_B_rad)

            self.print_triangle_details()

        elif self.c != 0 and self.b != 0 and self.a == 0:
            self.a = math.sqrt(self.c**2 - self.b**2)
            angle_A_rad = math.atan(self.b / self.a)
            angle_B_rad = math.atan(self.a / self.b)
            self.A = self.radians_to_degrees(angle_A_rad)
            self.B = self.radians_to_degrees(angle_B_rad)

            self.print_triangle_details()

        elif self.c != 0 and self.b != 0 and self.a == 0:
            self.a = math.sqrt(self.c**2 - self.b**2)
            angle_A_rad = math.atan(self.b / self.a)
            angle_B_rad = math.atan(self.a / self.b)
            self.A = self.radians_to_degrees(angle_A_rad)
            self.B = self.radians_to_degrees(angle_B_rad)

            self.print_triangle_details()

        elif self.a != 0 and self.A != 0:
            self.B = 90 - self.A
            self.c = self.a / math.cos(self.degrees_to_radians(self.A))
            self.b = math.sqrt(self.c**2 - self.a**2)
            self.print_triangle_details()

        elif self.b != 0 and self.A != 0:
            self.B = 90 - self.A
            self.c = self.b / math.sin(self.degrees_to_radians(self.A))
            self.a = math.sqrt(self.c**2 - self.b**2)
            self.print_triangle_details()

        elif self.a != 0 and self.B != 0:
            self.A = 90 - self.B
            self.c = self.a / math.sin(self.degrees_to_radians(self.B))
            self.b = math.sqrt(self.c**2 - self.a**2)
            self.print_triangle_details()

        elif self.b != 0 and self.B != 0:
            self.A = 90 - self.B
            self.c = self.b / math.cos(self.degrees_to_radians(self.B))
            self.a = math.sqrt(self.c**2 - self.b**2)
            self.print_triangle_details()

        else:
            print("Insufficient or invalid data. Please make sure to provide enough information.")

def main():
    print("Enter the sides and angles of the right triangle in the format:")
    print("a,b,c,A (side a, side b, side c, angle A in degrees where A is one of the non-90° angles)")
    user_input = input("Enter the values: ").strip()
    
    args = list(map(float, user_input.split(",")))
    if len(args) < 2:
        print("Invalid input format.")
        return
    
    # Initialize the triangle object with the input values
    a, b, c, A, B = args[0], args[1], 0.0, 0.0, 0.0
    if len(args) >= 3:
        c = args[2]
    if len(args) >= 4:
        A = args[3]
    if len(args) == 5:
        B = args[4]
    
    # Create a RightTriangle instance
    triangle = RightTriangle(a, b, c, A, B)
    
    # Solve and print the triangle details
    triangle.solve()

# Run the program
if __name__ == "__main__":
    main()
