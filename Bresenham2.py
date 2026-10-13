import matplotlib.pyplot as plt


def bresenham_line(x1, y1, x2, y2):
    # Calculate differences
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the direction of movement
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Initialize the decision error
    p = dx - dy

    x, y = x1, y1
    points = []

    while True:
        # Store the current pixel
        points.append((x, y))

        # Stop when the endpoint is reached
        if x == x2 and y == y2:
            break

        p2 = 2 * p

        # Update x
        if p2 > -dy:
            p -= dy
            x += sx

        # Update y
        if p2 < dx:
            p += dx
            y += sy

    return points


# Input starting and ending coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Apply Bresenham algorithm
points = bresenham_line(x1, y1, x2, y2)

# Print the pixels
print("\nPixels on the line:")
for point in points:
    print(point)

# Extract x and y coordinates
xs = [point[0] for point in points]
ys = [point[1] for point in points]

# Plot the line using Matplotlib
plt.figure(figsize=(8, 6))

# Draw the ideal line
plt.plot(
    [x1, x2], [y1, y2],
    color="blue",
    linestyle="--",
    label="Ideal line"
)

# Draw the selected pixels
plt.scatter(
    xs, ys,
    color="red",
    s=100,
    label="Bresenham pixels",
    zorder=3
)

# Display pixel coordinates
for x, y in points:
    plt.annotate(
        f"({x},{y})",
        (x, y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9
    )

# Configure the grid
plt.xticks(range(min(x1, x2) - 1, max(x1, x2) + 2))
plt.yticks(range(min(y1, y2) - 1, max(y1, y2) + 2))
plt.grid(True, linestyle="-", alpha=0.5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bresenham Line Drawing Algorithm")
plt.legend()
plt.axis("equal")
plt.show()

