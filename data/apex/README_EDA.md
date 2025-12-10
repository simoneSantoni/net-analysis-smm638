# Exploratory Data Analysis (EDA) for Burt (2004) Structural Holes Dataset

## Overview

This directory contains a comprehensive exploratory data analysis (EDA) for the synthetic companion dataset based on:

**Burt, Ronald S. 2004. "Structural Holes and Good Ideas." _American Journal of Sociology_ 110(2):349-399.**

## Files

### Data Files

- `nodes.csv` - 673 supply-chain managers with attributes and performance metrics
- `edges.csv` - 1,218 discussion network ties with weights
- `DATASET_OVERVIEW.md` - Comprehensive documentation of the dataset

### Analysis Script

- `eda_apex.py` - Complete EDA script using pandas, matplotlib, and networkx

### Output Directory

- `eda_output/` - Contains all generated visualizations and summary report

## Running the EDA

To run the exploratory data analysis:

```bash
cd /home/simon/githubRepos/net-analysis-smm638/data/apex
python eda_apex.py
```

The script will:

1. Load and inspect the data
2. Calculate descriptive statistics
3. Analyze network structure
4. Generate 7 comprehensive visualizations
5. Create a summary report

## Generated Visualizations

The EDA generates the following visualizations (saved to `eda_output/`):

1. **fig1_demographics.png** - Demographic distributions
   - Age, education, job rank, role, business unit, isolate status

2. **fig2_network_metrics.png** - Network position metrics
   - Degree, weighted degree, log constraint, betweenness, clustering
   - Degree vs constraint scatter plot

3. **fig3_performance.png** - Performance and outcome variables
   - Salary residual, evaluation, promotion rates
   - Idea value, dismissal rates, response funnel

4. **fig4_correlation_heatmap.png** - Correlation matrix
   - Key variables including network metrics and outcomes

5. **fig5_edge_analysis.png** - Edge/tie analysis
   - Tie type and weight distributions
   - Within vs cross-BU ties
   - Degree rank distribution

6. **fig6_structural_holes_theory.png** - Key theoretical relationships
   - Constraint vs idea value
   - Constraint vs salary residual
   - Constraint by evaluation category
   - Promotion rate by constraint quartile

7. **fig7_network_visualization.png** - Network structure
   - Colored by business unit
   - Node size by structural holes (low constraint)

## Summary Report

The script generates `eda_summary_report.txt` with:

- Dataset overview statistics
- Demographic summary
- Network metrics
- Key findings replicating Burt (2004)
- List of all visualizations

## Key Findings

The EDA confirms the core theoretical predictions of Burt (2004):

### 1. Brokerage and Performance

- **Degree ↔ Log Constraint**: r = -0.965 (more contacts → lower constraint)
- **Log Constraint ↔ Salary**: Negative association (structural holes → higher salary)

### 2. Brokerage and Good Ideas

- **Log Constraint ↔ Idea Value**: r = -0.473 (strong negative)
  - Managers with networks spanning structural holes generate better ideas
- **Idea Dismissal Rate**: 64.8% overall, but lower for those with low constraint

### 3. Network Structure

- **Social Isolates**: 28.7% of the population (193/673)
- **Cross-BU Ties**: Only 0.6% of ties bridge business units
- **Tie Strength Distribution**:
  - Often: 38.3%
  - Frequent: 34.0%
  - Sometimes: 18.9%
  - Idea only: 8.9%

## Requirements

The EDA script requires:

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- networkx

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn networkx
```

## Usage Examples

### Load and Inspect Data

```python
import pandas as pd
import networkx as nx

# Load datasets
nodes = pd.read_csv('nodes.csv')
edges = pd.read_csv('edges.csv')

# Create network
G = nx.from_pandas_edgelist(edges, 'source', 'target', edge_attr='weight')

# Basic network stats
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Density: {nx.density(G):.4f}")
```

### Analyze Structural Holes and Performance

```python
import matplotlib.pyplot as plt

# Scatter plot: Constraint vs Idea Value
ideas = nodes[nodes['idea_expressed'] == True]
plt.scatter(ideas['log_constraint'], ideas['idea_value'])
plt.xlabel('Log Constraint (Higher = More Constrained)')
plt.ylabel('Idea Value (1-5)')
plt.title('Structural Holes and Good Ideas')
plt.show()
```

### Calculate Network Metrics

```python
# Verify network metrics
import networkx as nx

# Betweenness centrality
betweenness = nx.betweenness_centrality(G)

# Clustering coefficient
clustering = nx.clustering(G)

# Compare with dataset values
print(nodes[['id', 'betweenness', 'clustering']].head())
```

## Citation

If you use this dataset or EDA, please cite:

```
Burt, Ronald S. 2004. "Structural Holes and Good Ideas." 
American Journal of Sociology 110(2):349-399.
```

And acknowledge this synthetic companion dataset:

```
Synthetic companion dataset based on Burt (2004), generated for 
research and teaching purposes. SMM638 Network Analysis Course.
```

## License

This is a synthetic educational dataset created for teaching purposes. The original research is published in the American Journal of Sociology.

## Contact

For questions or issues:

- Review the `DATASET_OVERVIEW.md` for detailed documentation
- Check the EDA script comments for implementation details
- Consult the original Burt (2004) paper for theoretical background
