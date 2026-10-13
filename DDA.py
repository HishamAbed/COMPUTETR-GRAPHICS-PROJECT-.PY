import matplotlib.pyplot as plt

# 1. Input: starting and ending points
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# 2. Calculate the difference
dx = x2 - x1
dy = y2 - y1

# 3. Determine the number of steps
steps = max(abs(dx), abs(dy))

# Handle the case where both points are identical
if steps == 0:
    plt.scatter(x1, y1, color="red")
    plt.title("DDA Line Drawing Algorithm")
    plt.grid(True)
    plt.show()
else:
    # 4. Calculate increments
    x_increment = dx / steps
    y_increment = dy / steps

    # 5. Initialize starting point
    x = x1
    y = y1

    points_x = []
    points_y = []

    # 6. Generate points along the line
    for i in range(steps + 1):
        rounded_x = round(x)
        rounded_y = round(y)

        points_x.append(rounded_x)
        points_y.append(rounded_y)

        print(f"Point {i}: ({rounded_x}, {rounded_y})")

        x += x_increment
        y += y_increment

    # 7. Plot the line
    plt.plot(points_x, points_y, "bo-", label="DDA Line")
    plt.scatter(points_x, points_y, color="red")

    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()