# **Improved MergeSort**

## **Summary**

This project focuses on optimizing the classic Merge Sort algorithm by introducing a hybrid approach that uses Insertion Sort for sorting small sublists. Through experimental testing, the impact of different sublist size thresholds (`k`) on overall performance was analyzed and compared against standard Merge Sort and Quick Sort implementations.

## **Objectives**

- Implement an Improved Merge Sort algorithm that uses Insertion Sort for sublists smaller than a defined threshold.
- Analyze the effect of varying the threshold (`k`) on execution time.
- Compare the performance of the Improved Merge Sort against standard Merge Sort and Quick Sort.
- Validate the empirical complexity of the algorithm and confirm its correctness across multiple test cases.

## **Conclusion**

This project explored the optimization of the classic Merge Sort algorithm by introducing a hybrid approach that uses Insertion Sort for small sublists.

Through experimental analysis, it was demonstrated that:
- Dividing the list into sublists of approximately 16 elements significantly improves execution time.
- The Improved MergeSort consistently outperforms both standard Merge Sort and Quick Sort across various input sizes.
- The optimization becomes increasingly effective as the list size grows, confirming better scalability.

These results validate the strategy of combining simple sorting algorithms for small data blocks with more complex algorithms for larger merges, achieving a balance between overhead and sorting efficiency.  
Future work could focus on fine-tuning the threshold dynamically based on system performance or dataset characteristics.

## **Project Structure**

The repository is organized into the following components:

- `1 Finding optimal k` Folder:

   This folder contains the implementation of the `improved_merge_sort` algorithm, along with experiments to determine the optimal threshold (`k`) for switching to Insertion Sort. It includes code, analysis, and results related to finding the most effective value of `k` for maximizing sorting performance.

- `2 Improved Merge Sort` Folder:

   This folder contains the implementation of algorithms `merge_sort`, `improved_merge_sort` and `quick_sort` and their performance comparison with each other. It includes an experiment measuring and analyzing their execution times.

- `img` Folder:

   Stores the output images generated during experimentation.

- `project_functions.py` Python Script:

   This Python script includes all the sorting algorithms developed specifically for this project.

- `requirements.txt` Text File:

   This file lists all the dependencies required to run the project.

## **Final Note**

The system developed for this project was created solely for academic purposes. It is not designed to be an optimal or production-grade benchmarking tool.

## **Reference**

This project follows the structure and theoretical foundations presented in the following textbook:

> Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.  
> *Introduction to Algorithms*. Fourth Edition.  
> Cambridge, Massachusetts; London, England: The MIT Press, 2022.  
> ISBN: 9780262046305  
> LCCN: 2021037260  
> Available at: [https://lccn.loc.gov/2021037260](https://lccn.loc.gov/2021037260)

> Byron Velasco, 2025.  
> *Sorting Algorithms* (GitHub Repository).  
> Available at: [https://github.com/ByronVelasco/SortingAlgorithms](https://github.com/ByronVelasco/SortingAlgorithms)

## **License**

- The **source code** of this project is licensed under the [MIT License](./LICENSE).  
  You are free to use, modify, and distribute the code with proper attribution.

- The **educational content** (including explanations, diagrams, and documentation) is shared under the  
  [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
  You may reuse and adapt it for non-commercial purposes with attribution.

---

© 2025 Byron Velasco