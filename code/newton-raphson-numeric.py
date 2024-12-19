import matplotlib.pyplot as plt
import math


def f(x):  # Insert function here
    return x**3 - 2 * x + 1


iterationCount = 10  # Amount of iteration
firstGuess = -2  # First guess
derivativeStep = 0.01  # For calculating the method of increments


approximationList = [float(firstGuess)]  # List of approximations
for i in range(iterationCount):
    diff = (
        f(approximationList[i] + derivativeStep) - f(approximationList[i])
    ) / derivativeStep  # Finding the derivative at a certain point
    nextGuess = (
        approximationList[i] - f(approximationList[i]) / diff
    )  # Newton-Raphson's method
    approximationList.append(nextGuess)  # Add next guess to the list of approximations

print(approximationList)  # Print out the list of approximations
fig, axes = plt.subplots()  # Initiate plot
axes.plot(list(range(iterationCount + 1)), approximationList)  # Plotting
axes.set_xlabel("Iteration")  # Setting the x-axis label
axes.set_ylabel("Guess")  # Setting the y-axis label
plt.show()  # Showing the plot
