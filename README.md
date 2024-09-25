# Overview
This Python program predicts the allele combinations formed when crossing gene traits of two parents, whether for monohybrid or dihybrid crosses. The program helps to understand dominant, recessive, homozygous, and heterozygous traits and their possible gene combinations based on user input.

**Features**

Monohybrid Cross: For crosses involving a single trait.
Dihybrid Cross: For crosses involving two traits.
Predicts allele combinations based on user-provided genotype information.
Supports dominant/recessive and homozygous/heterozygous configurations.
Generates gene combinations in Punnett square format.
How to Use
Run the Program: Execute the Python code in any Python 3 environment.

**Input Type:**

The program first asks if you're solving a monohybrid (y) or dihybrid (n) cross.
Follow the prompts to provide:
Trait names (and optionally, their symbols).
Whether the trait follows conventional naming methods.
Whether the trait is homozygous or heterozygous.
Whether it is dominant or recessive.

Monohybrid Cross:


Input gene symbols for two parent traits.
The program will output possible allele combinations in a Punnett square format.
Dihybrid Cross:


Provide genotypes for two traits of both parents.
The program will compute and display 16 possible combinations (Punnett square) of the dihybrid cross.
Code Breakdown
di_arrangement(x, y): Function to determine the correct order of alleles in a gene pair based on alphabetical order.

User Inputs: The program prompts for traits, dominance, and zygosity to determine parent genotypes.

Monohybrid Crossing: Computes 4 possible gene combinations using Punnett square logic.

Dihybrid Crossing: Computes 16 possible gene combinations by combining the two traits from each parent.
