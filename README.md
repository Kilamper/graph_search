# graph_search
This document provides relevant information about Search Algorithms

<p>Contributors: Kilian Armas Pérez and Echeyde Ramos Caballero</p>
<p>Tags: python, search_algorithms, breadth_first_search, branch&bound,
branch&bound_with_subestimation</p>

## Requirements 
Previous installation of Python 3.0+

## Installation and Execution
Download the compressed folder with the 3 modules.
Open and execute module named "run".

## Description
<p>Starting from a code base that had an algorithm to determine a route
between nodes using either breadth first or depth first search, we modified the
existing function "graph_search()" to also determine and
return the number of generated and expanded nodes in the process. We added 2
variables.</p>
<p>Each time that a node was popped in the algorithm we increase 
the variable that represents the number of visited nodes, and after each time the 
function called the method "fringe.extend()" the number of generated nodes would
be also increased.</p>

![image1](https://github.com/Kilamper/practica1/assets/73082382/d78b59f2-a703-4f1d-aa08-32f6f9225c2b)

<p>Also, as you can see in the image, we add a time counter using the "perf_counter()" 
function included in the "time" library.</p>

<p>In addition to the given algorithms we implement two other powerful search algorithms, 
such as Branch and Bound and its alternative with underestimation. In order to implement 
this algorithms we add two new boolean variables to the "graph_search" method.</p>
<ol>
  <li>The first variable ("branch") is to identify if the search is being done with Branch and 
Bound or not, in case its value is True, the "fringe" FIFOQueue will be sorted by the path 
cost of the nodes.</li>

  <li>While the second one is to detect if the Branch and Bound search is with 
underestimation or not, and if its value is True, the sort will be done by the sum of the path 
cost and the heuristic result of the nodes.</li>
</ol>

![image2](https://github.com/Kilamper/practica1/assets/73082382/6b8b2369-b35e-440e-a584-0d439fcf6a48)

<p>We also created a new "sort()" method in the FIFOQueue class to sort the fringe depending on
whether it is Branch and Bound with or without underestimation.</p>

![image3](https://github.com/Kilamper/practica1/assets/73082382/0e848b2c-69b1-44ba-8231-15ab84a4e3db)

<p>We use all modified options and algorithms in the module "run" so you can watch
the results.</p>
