# SMM638 Network Analysis - Final Project

## Community Detection for Customer Segmentation in Music Streaming

### Project Overview

This final project challenges you to apply network analysis and community detection methods to solve a real-world business problem: customer segmentation for a music streaming platform. You will work with actual data from Deezer to help Chief Data Scientist Elena Martinez decide whether to adopt a network-based approach to customer segmentation.

### Background

Traditional demographic segmentation (age, location, subscription tier) has proven inadequate for music streaming platforms. Music preferences transcend demographic boundaries—a 45-year-old executive might share the same taste in electronic music as a 22-year-old student. The platform needs a better way to segment 6 million active listeners based on their genre preferences and social connections.

### The Business Challenge

Elena Martinez's team at a major European music streaming platform faces a critical decision: should they move from demographic segmentation to a genre-based, network-driven approach? If so, how should they implement it?

The fundamental insight is that **genres cluster naturally based on audience similarity**—genres that share overlapping listener bases tend to form communities. But there's also a social dimension: users connect with friends on the platform, and these social ties might influence genre preferences.

### Your Task

You will analyze Deezer platform data to develop and evaluate a network-based customer segmentation strategy. Specifically, you must:

1. **Conduct exploratory network analysis** of genre preferences and social connections
2. **Implement community detection methods** to identify genre clusters
3. **Compare different approaches** to community detection (preference-only vs. network-enhanced)
4. **Develop actionable recommendations** for the business

### Data

You have been provided with real data from 54,573 Deezer users in Croatia:

- **Genre preferences** (`HR_genres.json`): User listening habits across 84 music genres
- **Social network** (`HR_edges.csv`): 498,202 friendship connections between users

**Data Location:**
- Genre preferences: `https://github.com/simoneSantoni/net-analysis-smm638/blob/master/data/deezer/HR_genres.json`
- Social edges: `https://github.com/simoneSantoni/net-analysis-smm638/blob/master/data/deezer/HR_edges.csv`

### Required Analysis Components

Your project must address the following:

#### 1. Network Construction and Exploration
- Build a **two-mode network** (users-genres affiliation network)
- Build a **one-mode social network** (user-user friendship network)
- Calculate basic network statistics (density, degree distributions, clustering coefficients)
- Visualize the network structures

#### 2. Genre Similarity Analysis
Develop at least one method to measure genre similarity:
- **Audience similarity**: Calculate overlap in listener bases between genres (e.g., Jaccard coefficient)
- **Social proximity**: Measure how genres are bridged by social connections
- Create a genre similarity network based on your chosen metric(s)

#### 3. Community Detection
Apply community detection algorithms to identify genre clusters:
- Implement at least one community detection method (e.g., Louvain, Label Propagation, Girvan-Newman)
- Evaluate community quality using appropriate metrics (e.g., modularity, conductance)
- Interpret the discovered communities in business terms

#### 4. Comparative Analysis
Compare different segmentation approaches:
- Traditional demographic approach (baseline)
- Preference-only clustering (genre co-occurrence)
- Network-enhanced clustering (incorporating social ties)
- Dual clustering (combining both approaches)

Which approach provides the most meaningful customer segments?

#### 5. Business Recommendations
Translate your technical findings into actionable business insights:
- What are the key genre communities?
- How should these communities inform marketing strategy?
- What are the practical advantages over demographic segmentation?
- How could the platform validate whether these communities improve business outcomes?

### Deliverables

Your final submission must include:

#### 1. Technical Report (PDF)
A 10-12 page report (excluding appendices) containing:
- Executive summary
- Network construction methodology
- Community detection approach and results
- Comparative analysis of segmentation strategies
- Business recommendations
- Technical appendix with algorithms and code snippets

#### 2. Jupyter Notebook or R Markdown
Complete, well-documented code that:
- Loads and preprocesses the data
- Constructs networks
- Implements community detection
- Generates visualizations
- Produces all analysis results
- Is fully reproducible

#### 3. Presentation Slides (PDF)
A 10-minute presentation (approximately 10-12 slides) suitable for presenting to Elena Martinez and the advisory board, covering:
- The business problem
- Your analytical approach
- Key findings (with visualizations)
- Strategic recommendations
- Implementation considerations

#### 4. Network Visualizations
High-quality visualizations including:
- Genre similarity network with communities highlighted
- Social network structure (sample or aggregated)
- Community comparison charts
- At least one interactive visualization (optional but encouraged)

### Evaluation Criteria

Your project will be evaluated based on:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Technical Rigor** | 30% | Correct implementation of network analysis and community detection methods; appropriate use of algorithms and metrics |
| **Analytical Depth** | 25% | Quality of insights; comparison of multiple approaches; understanding of trade-offs |
| **Business Relevance** | 20% | Translation of technical results into actionable business recommendations; understanding of practical constraints |
| **Communication** | 15% | Clarity of writing; quality of visualizations; logical flow of argument |
| **Code Quality** | 10% | Well-documented, reproducible, efficient code; proper use of libraries and best practices |

### Key Questions to Address

Your analysis should answer:

1. **How would you analyze this data to persuade the advisory board to fund the innovative, network-based approach to customer segmentation?**
   - What evidence demonstrates the limitations of demographic segmentation?
   - What insights does network analysis provide that traditional methods miss?

2. **What are the expected advantages of genre-based segmentation over demographic segmentation?**
   - How does it improve recommendation accuracy?
   - How does it enable better targeting for marketing campaigns?
   - What operational efficiencies might it create?

3. **How might the identified communities change if we include social network data?**
   - Do social connections reveal different genre communities than preference overlap alone?
   - Which approach (preference-only, network-enhanced, or dual) is most valuable?

4. **How could the platform validate whether these communities lead to better business outcomes?**
   - What metrics would you track (engagement, retention, revenue)?
   - What A/B test would you design?
   - What are the risks and limitations?

### Technical Guidance

#### Suggested Python Libraries
- `pandas`, `numpy`: Data manipulation
- `networkx`: Network construction and analysis
- `python-louvain` or `leidenalg`: Community detection
- `matplotlib`, `seaborn`, `plotly`: Visualization
- `scipy`: Statistical analysis
- `scikit-learn`: Clustering validation

#### Suggested R Packages
- `igraph`: Network analysis and community detection
- `tidyverse`: Data manipulation
- `ggraph`: Network visualization
- `ggplot2`: General visualization
- `Matrix`: Sparse matrix operations

#### Recommended Workflow
1. Start with exploratory data analysis of the raw data
2. Clean and preprocess (remove inactive users, rare genres)
3. Build networks incrementally (start simple, add complexity)
4. Implement one community detection method thoroughly before comparing multiple
5. Validate your results using multiple quality metrics
6. Create visualizations iteratively as you develop insights
7. Draft business recommendations based on concrete findings

### Resources

- **Course materials**: Lectures on two-mode networks, community detection, and network metrics
- **NetworkX documentation**: https://networkx.org/documentation/stable/
- **igraph documentation**: https://igraph.org/r/doc/
- **Academic reference**: Xu, J. et al. (2025). "The dual clustering of tastes and ties." *Poetics*.
- **Teaching case**: Case NA-2024-CD-012 (provided separately)

### Submission Details

- **Due date**: [To be specified by instructor]
- **Format**: Submit all deliverables as a single ZIP file
- **Filename**: `SMM638_FinalProject_[YourName].zip`
- **Contents**: 
  - `report.pdf`
  - `analysis.ipynb` or `analysis.Rmd` (and HTML output)
  - `presentation.pdf`
  - `data/` folder (if you generated intermediate datasets)
  - `README.md` with instructions to run your code

### Academic Integrity

- This is an **individual project**
- You may discuss high-level approaches with classmates, but all analysis and code must be your own
- Properly cite any external resources, libraries, or references you use
- Use of large language models (e.g., ChatGPT, GitHub Copilot) for code assistance is allowed but must be disclosed

### Tips for Success

1. **Start early**: Network analysis can be computationally intensive
2. **Version control**: Use git to track your progress
3. **Document as you go**: Don't leave documentation until the end
4. **Focus on interpretation**: Technical correctness is necessary but not sufficient—explain what your results mean
5. **Think like a data scientist**: Balance technical sophistication with practical business value
6. **Visualize effectively**: A good network visualization is worth a thousand words
7. **Validate your assumptions**: Check that your data processing steps make sense
8. **Test your code**: Make sure everything runs from start to finish

### Optional Extensions (Bonus Credit)

For students seeking additional challenge:

- **Statistical significance testing**: Use randomization tests to validate that discovered communities are not random
- **Temporal analysis**: If you can infer user join dates, analyze how communities evolve over time
- **Multiplex networks**: Model both preference and social layers simultaneously
- **Recommendation system prototype**: Build a simple genre recommendation engine based on your communities
- **Cross-validation**: Compare your communities against external genre taxonomies (e.g., AllMusic, Spotify)

---

**Questions?** Contact the instructor or post in the course discussion forum.

**Good luck!** This project is your opportunity to demonstrate mastery of network analysis methods while solving a realistic business problem.
