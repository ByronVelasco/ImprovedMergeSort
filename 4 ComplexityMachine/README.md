# **Experiment Engine: Sorting Algorithm Machines**

This module provides the experimental engine used to evaluate and compare the time complexity of sorting algorithms. It includes functions for testing algorithms across various scenarios and visualizing the results.

## **Machine Overview**

- A set of sizes of lists is defined in the variable `sizes`.
- For each size, the sorting operation is repeated `reps` times to compute an **average execution time**. This reduces the impact of random system processes affecting timing.
- The algorithms to be tested are listed in `algorithm`.
- For the improved MergeSort complexity, some scenarios are given in `k_sizes`.

The execution times are stored in a list called `total_times`, where each entry corresponds to the average time for a specific size.

---

## **Types of Machines**

There are two experimental machines in the project:

- `ComplexityMachine`:

  Validates the **theoretical time complexity** of `ImprovedMergeSort` algorithm through different `k_sizes`.

- `ComparisonMachine`:

  Compares the **execution speed** of multiple algorithms.

---

## **Graphs and Visualization**

The plots generated in this project are **line plots**.. All graphs are saved in the `img/` folder of the project, and also displayed within the notebook.

### **Plotting Functions**

- `ComplexityGraph`:

  Used to plot the results obtained from `ComplexityMachine`. Compares `ImprovedMergeSort` algorithm through many `k_sizes`.

- `ComparisonGraph`:  

  Used to plot the results from `ComparisonMachine`. Compares multiple algorithms.

---

## **MachineCall Utility**

The function `MachineCall` acts as a controller. Based on the input data, it decides whether to use `ComplexityMachine` or `ComparisonMachine`, ensuring that the appropriate logic and graphing function is triggered.

---

This experimental engine is designed for academic and educational use, to help visualize how sorting algorithms behave in practical conditions.