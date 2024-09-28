# Hardy-Weinberg Equilibrium Calculator

This script calculates allele and genotype frequencies in a population using the Hardy-Weinberg principle. It prompts the user for the population sizes of dominant and recessive individuals and allows the user to input known allele frequencies (if available). The script calculates:

- `p`: Frequency of the dominant allele in the population
- `q`: Frequency of the recessive allele in the population
- `p²`: Percentage of homozygous dominant individuals
- `q²`: Percentage of homozygous recessive individuals
- `2pq`: Percentage of heterozygous individuals

## Features
- Calculates allele frequencies from known or estimated values.
- Computes the percentages of homozygous dominant, homozygous recessive, and heterozygous individuals.
- Ensures that the Hardy-Weinberg equilibrium condition (`p + q = 1`) is satisfied using assertions.

## How It Works
1. The user is prompted to enter the population of dominant and recessive individuals.
2. The script asks whether the frequency of the dominant allele (`p`) is known. If so, the frequency can be entered; otherwise, the script will estimate it from the population data.
3. If the dominant allele frequency is not known, the script will use the frequency of the recessive allele (`q`) instead and calculate the rest.
4. The script calculates the percentages of homozygous dominant (`p²`), homozygous recessive (`q²`), and heterozygous (`2pq`) individuals in the population.
5. It verifies that the sum of `p` and `q` equals 1, and that the sum of genotype percentages equals 100%.

## Usage
To use the script, run it in any Python environment:

```bash
python hardy_weinberg_calculator.py
