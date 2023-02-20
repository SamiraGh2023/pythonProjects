import random
import sys
import matplotlib.pyplot as plt
from math import factorial


# Represents individuals in the population
class Individual:
    ind_id = 0

    # age is a number, genotype is a list containing two strings
    def __init__(self, age, genotype):
        self.age = age
        self.genotype = genotype
        self.id = Individual.ind_id

        # Change the class variable, not the instance variable
        Individual.ind_id += 1

    # less than operator
    def __lt__(self, other):
        return self.age < other.age

    # equal operator
    def __eq__(self, other):
        return self.id == other.id

    # not equal operator
    def __ne__(self, other):
        return self.id != other.id


def estimate_genotype_distribution(population):
    n, AA, Aa, aa = (0, 0, 0, 0)

    for individual in population:
        n += 1

        if (individual.genotype == ['A', 'A']):
            AA += 1
        elif (individual.genotype == ['A', 'a']):
            Aa += 1
        else:
            aa += 1

    return (AA / n, Aa / n, aa / n)


def estimate_allele_frequency(population):
    n, A, a = (0, 0, 0)

    for individual in population:
        n += 2
        for allele in individual.genotype:
            if (allele == 'A'):
                A += 1
            else:
                a += 1

    return (A / n, a / n)


def first_gen():
    population = []

    # Assign random age and given genotype distribution to first generation
    for i in range(0, 30):
        population.append(Individual(random.randint(0, 80),
                                     ['A', 'A']))

    for i in range(0, 5):
        population.append(Individual(random.randint(0, 80),
                                     ['A', 'a']))

    for i in range(0, 65):
        population.append(Individual(random.randint(0, 80),
                                     ['a', 'a']))

    # Sort the list after age (through less than operator)
    population.sort()

    return population


def next_gen(population):
    parent1 = random.choice(population)
    parent2 = random.choice([x for x in population if x != parent1])

    # Choose the new alleles randomly from the parents
    # according to Mendelian laws of inheritance
    genotype = [random.choice(parent1.genotype), random.choice(parent2.genotype)]

    # ['A', 'a'] should be the same as ['a', 'A']
    genotype.sort()

    # create and insert new offspring into the population
    offspring = Individual(0, genotype)
    population.insert(0, offspring)

    # Ageing takes place here. Delete oldest member and increment everyone's age
    population.pop()
    for individual in population:
        individual.age += 1


# Computes the exact test for Hardy Weinberg Equilibrium
# and returns the p-value
# Put in the absolute frequencies, not the probabilities!
def test_HWE(AA, Aa, aa):
    # Compute allele frequencies
    a_freq = int(2 * aa + Aa)
    A_freq = int(2 * AA + Aa)

    # subprocedure, which returns the propability of getting a genotype distribution
    # of n_AA, n_Aa and n_aa.
    def P(n_AA, n_Aa, n_aa):

        # Compute allele frequencies
        n_A = 2 * n_AA + n_Aa
        n_a = 2 * n_aa + n_Aa

        n = (n_A + n_a) / 2

        # Formula from Uni lecture 2
        return (factorial(n) * factorial(n_A)
                * factorial(n_a) * pow(2, n_Aa)
                / (factorial(n_AA) * factorial(n_Aa)
                   * factorial(n_aa) * factorial(2 * n)
                   )
                )

    props = [((P(x, y, z)), (x, y, z))
             for x in range(A_freq // 2 + 1)
             for z in range(a_freq // 2 + 1)
             if x + min(A_freq - 2 * x, a_freq - 2 * z) + z == (A_freq + a_freq) // 2
             for y in [min(A_freq - 2 * x, a_freq - 2 * z)]]

    list.sort(props)

    p_val = 0
    for (propability, (x, y, z)) in props:

        p_val += propability

        if ((x, y, z) == (AA, Aa, aa)):
            break

    return p_val


if (__name__ == '__main__'):

    # Parsing command line input
    try:
        maxgens = int(sys.argv[1])
    except (ValueError, IndexError):
        print("usage: ", sys.argv[0], "gen",
              "\n------------------"
              "\narguments:",
              "\ngen : number of generations")

        sys.exit(2)

    # Generate beginning population and initialize data lists
    population = first_gen()
    allele_freqs = [estimate_allele_frequency(population)]
    genotype_dist = [estimate_genotype_distribution(population)]
    to_test = (int(genotype_dist[0][0] * len(population)),
               int(genotype_dist[0][1] * len(population)),
               int(genotype_dist[0][2] * len(population)))
    p_values = [test_HWE(to_test[0], to_test[1], to_test[2])]

    # Iterates over all generations
    for i in range(0, maxgens):
        # compute the next generation
        next_gen(population)

        # Save the genotype distribution and allele frequencies for plotting
        genotype_dist.append(estimate_genotype_distribution(population))
        allele_freqs.append(estimate_allele_frequency(population))

        to_test = (int(genotype_dist[-1][0] * len(population)),
                   int(genotype_dist[-1][1] * len(population)),
                   int(genotype_dist[-1][2] * len(population)))
        p_values.append(test_HWE(to_test[0], to_test[1], to_test[2]))

    # Plotting with matplotlib
    plt.figure(1)

    # Plot for genotype distribution
    plt.subplot(211)

    # Input the different values with different colors as line graph
    plt.plot([x for (x, y, z) in genotype_dist], 'r-', label='AA')
    plt.plot([y for (x, y, z) in genotype_dist], 'g-', label='Aa')
    plt.plot([z for (x, y, z) in genotype_dist], 'b-', label='aa')

    # Adjust the plot axis
    plt.axis([0, maxgens, 0, 1])
    plt.legend()

    # Plot for allele frequencies
    plt.subplot(212)

    # Input the different values with different colors as line graph
    plt.plot([x for (x, y) in allele_freqs], 'r-', label='A')
    plt.plot([y for (x, y) in allele_freqs], 'g-', label='a')

    # label the plotted graphs
    plt.text(0, allele_freqs[0][0] + 0.02, 'A', color='r')
    plt.text(0, allele_freqs[0][1] + 0.02, 'a', color='g')

    # Adjust the plot axis
    plt.axis([0, maxgens, 0, 1])
    plt.legend()

    plt.figure(2)

    plt.plot(p_values, 'r-',
             [0.05 for i in range(0, maxgens + 1)], 'g-')
    plt.show()
