**Genetic Drift Simulation**

This script simulates a population undergoing genetic drift. Genetic
drift is the random fluctuation of the frequency of alleles in a
population due to chance events. The script models the process of
genetic drift by creating a population of individuals and randomly
selecting individuals to produce offspring in each generation.

**Usage**

<img width="634" alt="1p" src="https://user-images.githubusercontent.com/125828094/219978303-cafaa79a-9919-437e-93de-4c7e2aaffc94.png">

-   gen : Number of generations to simulate.

**Classes**

**Individual**

Represents individuals in the population. Each individual has a unique
ID, age, and genotype.

**Functions**

**estimate_genotype_distributaion:**

Calculates the proportion of individuals in a population with each of
the three possible genotypes:

AA, Aa, and aa.

**estimate_allele_frequency:**

Calculates the frequency of the two alleles A and a in a population.

**first_gen**

Generates the first generation of the population. Assigns random age and
given genotype distribution to individuals in the first generation.

**next_gen**

Creates the next generation of the population. Selects two individuals
at random to the parents and randomly chooses alleles from the parents
according to the Mendelian laws of inheritance.

**test_HWE**

Computes the exact test for Hardy Weinberg Equilibrium and returns the
p-value.

**Example**
<img width="638" alt="2p" src="https://user-images.githubusercontent.com/125828094/219978378-1f9c4c68-9bcf-47d3-9fa6-19cbddb837ad.png">


!["2p"](https://raw.githubusercontent.com/samiraGh2023/pythonProjects/main/Users/samira/Desktop/2p.png)

