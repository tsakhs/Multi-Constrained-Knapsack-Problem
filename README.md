# 🧬 Multi-Constrained Knapsack Problem Solver (Genetic Algorithm)

This project presents a solution to the **Multi-Constrained Knapsack Problem (MCKP)** using a Genetic Algorithm. It was developed for educational and research purposes, demonstrating how evolutionary techniques can solve complex combinatorial optimization problems.

## 📦 Problem Statement

The goal is to maximize the total value of selected items without exceeding three separate capacity constraints (`W1`, `W2`, `W3`). Each item has a value and three corresponding weights. This is a generalization of the classic knapsack problem with multiple constraints.

## 💡 Approach

A **Genetic Algorithm (GA)** is implemented, consisting of:
- **Population Initialization** with randomly valid individuals
- **Fitness Evaluation** based on total value while meeting constraints
- **Selection** via tournament-style competition
- **Crossover** to combine parent genes
- **Mutation** with repair to ensure feasibility
- **Elitism** to retain the best individuals
- **Repair Function** to fix invalid solutions exceeding constraints

## 🧪 Dataset

The dataset includes:
- `weights1.npy`, `weights2.npy`, `weights3.npy`: 3 arrays representing item weights for each constraint
- `values.npy`: Array of item values

Each `.npy` file contains 10,000 entries, and the capacity constraints are:
- `W1` ≤ 500
- `W2` ≤ 750
- `W3` ≤ 1000

## 🚀 Running the Project

Ensure the `.npy` files (`weights1.npy`, `weights2.npy`, `weights3.npy`, `values.npy`) are in the same directory.

```bash
python Genetics_Random_Init.py
