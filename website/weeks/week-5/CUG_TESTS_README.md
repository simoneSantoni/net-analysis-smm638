# CUG Tests Added to Network Properties Analysis

## Summary of Enhancements

The `network_properties.qmd` notebook has been expanded with **Conditional Uniform Graph (CUG) tests** for reciprocity and transitivity. This provides a more rigorous statistical assessment than simple Erdős-Rényi random graph comparisons.

## What Was Added

### 1. Additional R Packages (Setup)
- `sna` - For CUG test functions
- `network` - Required for sna (network objects)
- `intergraph` - For converting between igraph and network objects

### 2. New Section: "Conditional Uniform Graph (CUG) Tests"

This comprehensive section includes:

#### a) Understanding CUG Conditioning
- Explanation of different conditioning strategies (size, edges, dyad census)
- Why "edges" conditioning is used (preserves density)

#### b) Network Conversion
- Converts igraph object to network object for sna compatibility
- Verifies node and edge counts

#### c) CUG Test for Reciprocity
- Runs 1000 simulations with edge count conditioning
- Uses `grecip()` function to calculate reciprocity
- Computes observed value, expected value, SD, z-score, and p-value
- Provides automatic interpretation

#### d) CUG Test for Transitivity
- Custom transitivity function compatible with sna
- Runs 1000 simulations with edge count conditioning
- Computes statistics and p-values
- Provides automatic interpretation

#### e) Visualizations
- Side-by-side histograms of null distributions
- Observed values marked with vertical lines
- P-values annotated on plots
- Uses course color scheme (magenta #c41c85 and emerald #50C878)

#### f) Summary Tables
- CUG test results table (observed, expected, SD, z-score, p-value, significance)
- Comparison table: Erdős-Rényi vs CUG tests
- Highlights differences between the two approaches

#### g) Interpretation Guide
- Explains why CUG is more conservative than Erdős-Rényi
- Key differences between the two testing approaches
- What it means if results differ between tests

### 3. Updated "Key Findings" Section

Enhanced to include:
- Both Erdős-Rényi and CUG test results
- P-values and significance indicators
- Dynamic interpretation based on both tests
- Comprehensive statistical evidence summary

## Key Concepts Explained

### Erdős-Rényi Random Graphs
- **Null hypothesis**: Network is random with uniform connection probability
- **Tests**: "Is this different from complete randomness?"
- **Pros**: Simple baseline
- **Cons**: Doesn't preserve degree distribution

### CUG Tests
- **Null hypothesis**: Network properties are random *given* structural constraints (e.g., edge count)
- **Tests**: "Is this different from random, controlling for density?"
- **Pros**: More realistic null model, controls for network density
- **Cons**: More computationally intensive

### Why Both Tests Matter

Using both approaches provides complementary insights:

1. If **significant in both**: Strong evidence of non-random structure
2. If **significant only in Erdős-Rényi**: Pattern may be explained by density alone
3. If **significant only in CUG**: Pattern exists beyond what density predicts
4. If **not significant in either**: No evidence of non-random patterns

## How to Run

### Install Required Packages (if needed)
```r
install.packages(c("sna", "network", "intergraph"))
```

### Render the Notebook
```bash
cd website
quarto render weeks/week-5/network_properties.qmd
```

### Preview Live
```bash
cd website
quarto preview weeks/week-5/network_properties.qmd
```

## Computation Time

- **CUG tests run 1000 simulations each** (2000 total)
- Expected runtime: 2-5 minutes depending on network size
- For faster testing during development, reduce `reps` parameter (e.g., 100 instead of 1000)

## Expected Output

The notebook will produce:

1. **Numerical results**: Reciprocity and transitivity values with p-values
2. **Visualizations**:
   - Distribution histograms with observed values
   - Comparison plots (Erdős-Rényi vs CUG)
3. **Tables**:
   - CUG test summary
   - Comparison of both testing approaches
4. **Interpretation**: Automated, context-aware findings based on results

## Educational Value

This notebook demonstrates:
- How to conduct rigorous hypothesis testing in network analysis
- The importance of appropriate null models
- Converting between network object formats in R
- Visualizing statistical test results
- Interpreting p-values and z-scores in network context
- Comparing multiple testing approaches

## References

- Butts, C.T. (2008). "Social network analysis with sna". *Journal of Statistical Software*, 24(6).
- Anderson, B.S., Butts, C., & Carley, K. (1999). "The interaction of size and density with graph-level indices". *Social Networks*, 21(3), 239-267.
