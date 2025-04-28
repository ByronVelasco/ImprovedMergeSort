# Experiment Engine: Sorting Algorithm Machines

This module provides the experimental engine used to evaluate and compare the time complexity of sorting algorithms. It includes functions for testing algorithms across various scenarios and visualizing the results.

## Machine Overview

- A set of sizes of lists is defined in the variable `sizes`.
- For each size, the sorting operation is repeated `reps` times to compute an **average execution time**. This reduces the impact of random system processes affecting timing.
- The algorithms to be tested are listed in `algorithm`.
- The input configurations (e.g., ascending, descending, and random lists) are stored in `scenarios`.

The execution times are stored in a list called `total_times`, where each entry corresponds to the average time for a specific size and scenario.

---

## Types of Machines

There are two experimental machines in the project:

- `ComplexityMachine`:

  Validates the **theoretical time complexity** of a single algorithm across multiple scenarios (random, ascending, descending).

- `ComparisonMachine`:

  Compares the **execution speed** of multiple algorithms under a **single scenario**.

---

## Graphs and Visualization

The plots generated in this project are **line plots**, each titled according to the algorithm or scenario used. All graphs are saved in the `img/` folder of the project, and also displayed within the notebook.

### Plotting Functions

- `ComplexityGraph`:

  Used to plot the results obtained from `ComplexityMachine`. Compares one algorithm across different list types.

- `ComparisonGraph`:  

  Used to plot the results from `ComparisonMachine`. Compares multiple algorithms in one scenario.

---

## MachineCall Utility

The function `MachineCall` acts as a controller. Based on the input data, it decides whether to use `ComplexityMachine` or `ComparisonMachine`, ensuring that the appropriate logic and graphing function is triggered.

---

This experimental engine is designed for academic and educational use, to help visualize how sorting algorithms behave in practical conditions.