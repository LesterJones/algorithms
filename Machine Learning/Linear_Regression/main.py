import random


# Function should take to equal length lists of x & y.
def linear_regression(x, y):
    n = len(x)

    # Create two lists corresponding to x**2 and x*y.
    i = 0
    x2 = []
    xy = []
    while i < n:
        x2.append(x[i] * x[i])
        xy.append(x[i] * y[i])
        i = i + 1

    # Create the needed sums from our 4 lists
    sum_of_x = sum(x)
    sum_of_y = sum(y)
    sum_of_x2 = sum(x2)
    sum_of_xy = sum(xy)

    # Use the sums to calculate the y_intercept and slope of our line
    y_int = ((sum_of_x2 * sum_of_y) - (sum_of_x * sum_of_xy)) / ((n * sum_of_x2) - (sum_of_x ** 2))
    slope = ((n * sum_of_xy) - (sum_of_x * sum_of_y)) / ((n * sum_of_x2) - (sum_of_x ** 2))

    return slope, y_int


# Create some data for x
x_data = list(range(1000))
our_slope = random.randint(1, 10) / random.randint(1, 10)
our_intercept = random.randint(0, 10)
# Create some y-data & add some random variance.
y_data = [our_slope * num + our_intercept + random.randint(-10, 10) for num in x_data]
est_slope, est_int = linear_regression(x_data, y_data)
# Check the real vs predicted.
print('real', our_slope, our_intercept)
print('prediction', est_slope, est_int)
