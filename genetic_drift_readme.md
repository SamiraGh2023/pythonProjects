**[Genetic Drift Simulation]{.underline}**

This script simulates a population undergoing genetic drift. Genetic
drift is the random fluctuation of the frequency of alleles in a
population due to chance events. The script models the process of
genetic drift by creating a population of individuals and randomly
selecting individuals to produce offspring in each generation.

**Usage**

!["1p"](https://raw.githubusercontent.com/username/repo-name/branch-name/Users/samira/Desktop/1p.png)

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

![import matplotlib. pyplot PI t as \# generate population and
initialize data lists population = first_gen() allele_freqs = AA---freq
= CO\]\] Aa_freq = C 1\]\] aa_freq = \# simulate genetic drift for 50
generations for i in range(5Ø) next_gen(population) al lele_freqs.
AA_freq. st ri but ion(populati on) ) Aa_freq. st ri but ion(populati
on) \[1\] ) aa_freq. st ri but ion(populati on) \[2\] ) allele_freqs\] ,
allele_freqs\] , \# plot allele frequencies plt.p10t(CXC 0 for in x
plt.p10t(CXC 1 for in x plt. legend() plt. showO \# test for
Hardy-Weinberg Equilibrium label= label= test_HWE(AA_freqC-1\],
Aa_freqC-1\], aa_freqC- ](media/image2.png){width="5.541666666666667in"
height="4.847222222222222in"}
