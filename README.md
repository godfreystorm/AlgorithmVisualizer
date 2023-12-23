# AlgorithmVisualizer
This Algorithm Visualizer project is an interactive tool I created using **Python** and **Pygame**. It was developed with the intention of visually representing the algorithms I had recently learned in my Design of Algorithms course, aiding both my understanding and that of others interested in these concepts. The visualizer allows users to see the algorithms in action in real-time, offering features such as the option to sort in either descending or ascending order, and the ability to pause mid-sort — even during an ascending order sort — and then switch to descending order or even a different sorting algorithm. Upon resuming, the visualization completes the sort, effectively demonstrating the program's and algorithm’s adaptability and providing a comprehensive understanding of the selected algorithms' behavior with different data sets.


Thanks to this self-driven project, I was able to deepen my understanding of various algorithms while also honing my skills in Python and gaining practical experience with Pygame. I warmly invite you to explore the visualizations, experiment with the code, and provide any feedback or suggestions. Whether you're a student seeking to understand sorting algorithms or an educator looking for classroom resources, I hope this tool enhances your learning and teaching experience.


**Algorithms currently visualized are listed below in order of creation of visualizations.**
## Algorithms:
* **Bubble Sort:** A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent pairs, and swaps them if they are in the wrong order.
* **Insertion Sort:** A straightforward algorithm that builds the final sorted array one item at a time by comparing each new element to the already-sorted elements and inserting it into the correct position.

## Getting Started
To get a copy of this project up and running on your local machine for development and testing purposes, follow these steps:

1. **Clone the Repository**: Clone this repo to your local machine using `https://github.com/yourusername/AlgorithmVisualizer.git`.
2. **Navigate to the Directory**: Change into the project directory: '***cd AlgorithmVisualizer***'
3. **Install Python:** Download and install Python from https://python.org.
4. **Install Pygame:** Install the Pygame library using pip (Python's package installer): '***pip3 install pygame***'
5. **Running the Visualizer:** To run the visualizer, execute the main.py script from your command line or terminal: '***python main.py***'

## Dependencies:
* **Python:** The core language used for the project. Make sure you have Python 3.x installed.
* **Pygame:** A set of Python modules designed for writing video games, used here to create the visualizations.


# Instructions
## Key presses:
* **R = Reset.** This will reset the graph to be sorted and also pick new random numbers/graph items to be sorted.
* **Space Bar = Start sorting.** This will begin the sorting process.
* **A = Ascending.** Sort in ascending order.
* **D = Descending.** Sort in descending order.


## Solved Issues:
* Preventing overlapping pixels.
* Descending order for Insertion sort not working. 
* Cant pause sorting process, dosent stop till completed once begun.
* Sorting should stop and reset if reset is hit during sorting.

## Planned Improvements:
* Put algorithms in files seperate from the main to allow for easier maintenance and readability.
* put algorithm selection in drop down menu to allow for better UI when more are added.

# Contact Information
* **Email Address:** Godfreystorm@gmail.com