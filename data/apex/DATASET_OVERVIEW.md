# Burt (2004) "Structural Holes and Good Ideas" - Companion Synthetic Dataset

## Overview

This is a fully-fledged companion dataset created based on the correlation matrix and empirical findings reported in:

**Burt, Ronald S. 2004. "Structural Holes and Good Ideas." _American Journal of Sociology_ 110(2):349-399.**

The dataset was synthetically generated to replicate the key structural and statistical properties reported in the paper while maintaining confidentiality of the original proprietary data.

---

## Dataset Components

### 1. **Relational Dataset** (`edges.csv`)
Network data representing discussion relationships among supply-chain managers.

**Structure:**
- **N edges:** 1,218 undirected ties
- **Format:** Edge list with source-target pairs
- **Tie weights:** Based on tie strength categories from the paper:
  - `often` (1.00): Both cited each other + frequent discussion
  - `frequent` (0.86): One cited the other for frequent discussion  
  - `sometimes` (0.65): Colleagues reported sometimes discussing
  - `idea_only` (0.50): One cited the other only for idea discussion

**Columns:**
- `source`: Employee ID of first person in relationship
- `target`: Employee ID of second person in relationship
- `weight`: Numerical tie strength (0.50-1.00)
- `tie_type`: Categorical label for tie strength
- `bu_u`, `bu_v`: Business units of source and target

**Network Structure:**
- Dense within business units (5 BUs + HQ)
- Sparse cross-BU ties (only 3% of ties bridge BUs directly)
- Hierarchical structure with HQ acting as hub
- 193 social isolates (29% of population)

---

### 2. **Attributive Dataset** (`nodes.csv`)
Employee characteristics and performance outcomes for N=673 supply-chain managers.

#### Employee Characteristics

**Demographic Variables:**
- `id`: Unique employee identifier (E0001-E0673)
- `age`: Employee age (24-68 years, mean=50)
- `education`: Educational level (Less/Bachelor/Graduate)
- `rank`: Job rank (Mgr1/Mgr2/Mgr3/SrMgr/Exec)
- `role`: Job role (Purchasing/Internal)
- `business_unit`: Organizational unit (BU_A/BU_B/BU_C/BU_D/BU_E/HQ)
- `location`: Geographic location (Urban1/Urban2/Other)
- `isolate`: Social isolate indicator (TRUE/FALSE)

**Job Rank Distribution:**
- Exec (Directors/VPs): 25 managers
- SrMgr (Senior Managers): 161 managers  
- Mgr3: 169 managers
- Mgr2: 191 managers
- Mgr1: 127 managers

#### Network Position Variables

Computed from the relational network using standard network analysis algorithms:

- `degree`: Number of discussion partners
- `weighted_degree`: Sum of tie weights
- `constraint`: Burt's network constraint index (0-100)
  - **High constraint (→100)**: Dense, closed network with redundant contacts
  - **Low constraint (→0)**: Sparse network spanning structural holes
- `log_constraint`: Natural log of constraint (used in regression models)
- `betweenness`: Betweenness centrality (normalized, 0-1)
- `clustering`: Local clustering coefficient (0-1)
- `mean_path_len`: Average path distance to other managers
- `core89`: Member of top 89 core network (TRUE/FALSE)

#### Performance & Outcome Variables

**Compensation & Evaluation:**
- `salary_resid`: Salary residual relative to peers (standardized)
  - Adjusted for rank, role, age, education, business unit, location
  - **Key finding:** Negatively associated with network constraint at senior ranks
- `evaluation`: Performance evaluation (Poor/Good/Outstanding)
  - Based on consistent ratings across two review cycles
  - **Key finding:** Better evaluations for those with low constraint
- `promoted_or_aboveavg`: Promotion or above-average raise (TRUE/FALSE)
  - **Key finding:** 68% probability at low constraint vs. 28% at high constraint

**Idea Generation & Value:**
- `responded`: Completed survey (TRUE/FALSE, 68% response rate)
- `idea_expressed`: Proposed an idea (TRUE/FALSE among respondents)
  - **Key finding:** Much less likely with high network constraint
- `idea_discussed`: Discussed idea with colleague (TRUE/FALSE)
  - **Key finding:** Associated with low constraint + longer explanations
- `idea_value`: Rated value of idea (1-5 scale)
  - Evaluated by two senior managers
  - **Key finding:** Mean 3.2 at low constraint, 1.5 at high constraint
- `idea_dismissed`: Idea dismissed by both judges (TRUE/FALSE)
  - **Key finding:** 14% dismissal at low constraint, 43% at high constraint
- `idea_length`: Length of idea explanation in characters
- `seq_order`: Sequential order in which idea was evaluated (1-n)

---

## Key Empirical Patterns

The dataset replicates the following core findings from Burt (2004):

### 1. **Brokerage and Performance**
Managers with networks spanning structural holes (low constraint):
- Receive **higher salaries** relative to peers (especially at senior ranks)
- Get **better performance evaluations**
- Have **higher promotion rates** (42% base rate → 68% at low constraint)

### 2. **Brokerage and Good Ideas**
The hypothesized "vision advantage" of brokerage:
- **More likely to express ideas** (model escapes organizational silence)
- **More likely to discuss ideas** with colleagues
- **Less likely to have ideas dismissed** by senior management  
- **Ideas rated as more valuable** by expert judges

### 3. **Network Structure**
- Organization riddled with **structural holes**:
  - Between supply chain and other functions
  - Between business units
  - Between individual managers (81% avg network density)
- **Opportunities for brokerage** are abundant but underutilized
- **Short path lengths** (mean=4.2 steps) despite fragmentation
- Integration depends heavily on **formal hierarchy** (HQ connections)

### 4. **Structural Reproduction**
Two feedback cycles maintain fragmentation:
- **Negative cycle:** High-constraint managers get ideas dismissed → withdraw → remain isolated
- **Positive cycle:** Low-constraint managers get ideas valued → continue proposing → discuss with local contacts (not bridging further)

---

## Variable Correlations

Key correlations from `observed_correlations.csv`:

| Variable Pair | Correlation | Interpretation |
|--------------|-------------|----------------|
| degree ↔ log_constraint | -0.97 | More contacts = lower constraint |
| log_constraint ↔ idea_value | -0.47 | **Brokerage → better ideas** |
| degree ↔ idea_value | +0.48 | More diverse contacts → better ideas |
| log_constraint ↔ salary_resid | -0.03 | Weak overall (stronger at senior ranks) |
| betweenness ↔ log_constraint | -0.28 | Brokers have high betweenness |

---

## Data Generation Method

### Synthetic Data Approach
To maintain confidentiality while enabling research and teaching:

1. **Population structure** matches reported N, job ranks, isolate counts
2. **Network generation**:
   - Erdős-Rényi-style random graph with tuned probabilities
   - Dense within-BU ties (p=0.065)
   - Sparse between-BU ties (p=0.003)  
   - HQ hub connections (p=0.02)
   - Tie weights assigned from categorical distribution
3. **Network metrics** computed using standard algorithms:
   - Constraint: Burt's formula Σ(p_ij + Σp_iq×p_qj)²
   - Other metrics: NetworkX implementations
4. **Outcomes modeled** using regression equations calibrated to match:
   - Sign and magnitude of reported effects
   - Nonlinear associations (logistic/log transformations)
   - Approximate distributions (e.g., 32% idea dismissal rate)

### Data Quality
- **Correlation matrix** closely matches patterns described in paper
- **Effect sizes** are directionally consistent (not exact replicas)
- **Distributions** approximate reported summary statistics
- **Missing data patterns** match survey response and idea expression

---

## Usage Examples

### Network Analysis
```python
import pandas as pd
import networkx as nx

# Load data
nodes = pd.read_csv('nodes.csv')
edges = pd.read_csv('edges.csv')

# Create network
G = nx.from_pandas_edgelist(edges, 'source', 'target', 
                             edge_attr='weight')

# Verify constraint calculation
from your_module import compute_constraint
calc_constraint = compute_constraint(G)
```

### Regression Analysis
```python
import statsmodels.formula.api as smf

# Replicate Table 1, Model 1 (Salary)
model = smf.ols('''salary_resid ~ log_constraint + log_constraint:C(rank) + 
                   age + C(education) + C(business_unit) + C(location)''', 
                data=nodes).fit()
print(model.summary())
```

### Idea Value Analysis  
```python
# Replicate Table 4, Model 5 (Idea Value)
ideas = nodes[nodes['idea_expressed'] == True].copy()

model = smf.ols('''idea_value ~ log_constraint + C(rank) + age + 
                   C(education) + C(role) + idea_length + seq_order''',
                data=ideas).fit()
print(model.summary())
```

---

## Teaching Applications

This dataset is ideal for teaching:

1. **Social Network Analysis**
   - Network metrics (degree, constraint, betweenness, clustering)
   - Structural holes theory
   - Brokerage vs. closure strategies

2. **Organizational Behavior**
   - Social capital and performance
   - Innovation and creativity
   - Informal organizations

3. **Regression Analysis**
   - Control variables and confounding
   - Interaction effects (rank × network structure)
   - Nonlinear associations (logarithmic transformations)
   - Missing data patterns (survey response, idea expression)

4. **Research Design**
   - Cross-sectional observational studies
   - Measurement of latent constructs (network position, idea value)
   - Causal inference limitations

---

## Files Summary

| File | Rows | Description |
|------|------|-------------|
| `nodes.csv` | 673 | Employee attributes, network metrics, performance outcomes |
| `edges.csv` | 1,218 | Discussion network ties with weights |
| `observed_correlations.csv` | 10×10 | Correlation matrix for numeric variables |
| `summary.json` | - | Dataset summary statistics |
| `README.md` | - | Brief dataset description |
| `DATASET_OVERVIEW.md` | - | This comprehensive guide |
| `generate_burt_companion.py` | - | Python script to regenerate data |

---

## Citation

If you use this dataset, please cite the original paper:

```
Burt, Ronald S. 2004. "Structural Holes and Good Ideas." 
American Journal of Sociology 110(2):349-399.
```

And acknowledge this synthetic companion dataset:
```
Synthetic companion dataset based on Burt (2004), generated for 
research and teaching purposes. Available at: 
https://github.com/[your-repo]/networks-and-performance
```

---

## Limitations

**This is synthetic data:**
- Values are **illustrative**, not the original confidential data
- Effect sizes are **calibrated** to match reported patterns, not exact
- Network structure is **simulated** to reflect described properties
- Use for **teaching and methods development**, not substantive research claims

**For substantive research:** Consult the original published paper and conduct new empirical studies.

---

## Contact & Contributions

For questions, suggestions, or contributions:
- Open an issue on GitHub
- Submit a pull request with improvements
- Contact: [your contact information]

---

**Generated:** November 30, 2024  
**Version:** 1.0  
**Random Seed:** 42 (reproducible)
