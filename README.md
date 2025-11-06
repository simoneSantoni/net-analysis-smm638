# Network Analytics (SMM638)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Quarto](https://img.shields.io/badge/Quarto-1.4-blue)](https://quarto.org)
[![R](https://img.shields.io/badge/R-4.3+-blue.svg)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)

This is the official repository for **SMM638 - Network Analytics**, an MSc module at City, University of London. The course teaches network analysis theory and practice using R and Python, with a focus on business and organizational applications.

**🌐 Course Website**: [https://simonesantoni.github.io/net-analysis-smm638](https://simonesantoni.github.io/net-analysis-smm638)

---

## 📚 About This Course

Networks are ubiquitous in modern life:
- Job opportunities reach us through interpersonal connections
- Social media content is shaped by our digital relationships
- Market valuations emerge from social influence spreading across networks
- Innovation diffuses through organizational and professional networks

This module provides students with **cutting-edge network theories** and **practical analytical tools** to understand the organization and functioning of diverse networks. The goal is to develop a distinctive perspective on how networks create value for individuals, organizations, and communities.

---

## 🎯 Learning Objectives

By the end of this module, students will be able to:

1. **Understand Network Properties**
   - Analyze structural characteristics of networks (density, centralization, clustering)
   - Identify network substructures (dyads, triads, motifs)
   - Evaluate reciprocity and transitivity patterns

2. **Analyze Communities**
   - Detect community structures using multiple algorithms
   - Evaluate community quality and overlap
   - Understand modularity and community evolution

3. **Assess Individual Positions**
   - Calculate node centrality measures (degree, betweenness, closeness, eigenvector)
   - Identify influential nodes and structural holes
   - Analyze brokerage positions

4. **Visualize Networks**
   - Create effective network visualizations
   - Choose appropriate layouts for different network types
   - Communicate network insights visually

5. **Apply Technical Skills**
   - Use R packages: `igraph`, `tidygraph`, `ggraph`, `network`, `sna`
   - Use Python libraries: `networkx`, `graph-tool`, `plotly`, `pyvis`
   - Implement statistical tests for network properties

6. **Solve Real-World Problems**
   - Apply network analytics to business challenges
   - Design recommendation systems
   - Analyze organizational structures
   - Study information diffusion

---

## 📁 Repository Structure

```
net-analysis-smm638/
├── website/                    # Quarto website source (PRIMARY)
│   ├── weeks/                 # Weekly course materials
│   │   ├── week-1/           # Introduction to networks
│   │   ├── week-2/           # Network visualization
│   │   ├── week-3/           # Node centrality
│   │   ├── week-4/           # Dyads and triads
│   │   ├── week-5/           # Network dynamics & case study
│   │   ├── week-6/           # Community detection
│   │   └── week-7-10/        # Advanced topics
│   ├── course/               # Course information
│   │   ├── syllabus.qmd      # Course syllabus
│   │   ├── schedule.qmd      # Weekly schedule
│   │   ├── support.qmd       # Office hours & help
│   │   └── team.qmd          # Teaching team
│   ├── project/              # Course projects
│   │   ├── midTermProject/   # Mid-term project specs
│   │   └── finalCourseProject/ # Final project specs
│   ├── _quarto.yml           # Website configuration
│   ├── theme.scss            # Light theme
│   ├── theme-dark.scss       # Dark theme
│   └── _site/                # Generated website (auto-built)
│
├── data/                      # Network datasets
│   ├── soundcloud/           # SoundCloud case study data
│   ├── deezer/               # Music streaming network
│   ├── twitch/               # Gaming platform network
│   └── xoxoday/              # Employee network
│
├── tutorials/                 # Python tutorials
├── finalCoursework/          # Final coursework materials
├── CLAUDE.md                 # Repository guide for AI assistants
└── README.md                 # This file
```

---

## 🆕 Recent Updates

### Week 5 (Latest)
- **📊 SoundCloud Case Study**: Platform ecosystem analysis with network dynamics
- **📈 Network Properties Analysis**: Comprehensive reciprocity and transitivity testing
  - Implemented Conditional Uniform Graph (CUG) tests
  - Statistical comparison with Erdős-Rényi random graphs
  - Fixed package conflicts between `sna` and `igraph`
- **🔧 Technical Improvements**:
  - Added `freeze: auto` for reproducible builds
  - Resolved GitHub Actions deployment issues
  - Enhanced data visualization with course branding

### Week 4
- **Dyads and Triads**: Comprehensive analysis of network substructures
- **Structural Balance**: Theory and practice of signed networks
- **Practical Exercises**: Hands-on dyad census and triad census calculations

### Week 3
- **Node Centrality**: In-depth coverage of centrality measures
- **Interactive Visualizations**: Custom network plots with `ggraph`
- **Practice Exercises**: Centrality calculations on real networks

### Week 1-2
- **Network Terminology Glossary**: Interactive visualizations covering:
  - One-mode and two-mode networks
  - Directed vs undirected networks
  - Signed and weighted networks
- **Enhanced Materials**: Updated with visual examples and case studies

---

## 🚀 Getting Started

### Prerequisites

#### For R Users
```r
# Install required R packages
install.packages(c(
  "tidyverse",      # Data manipulation and visualization
  "igraph",         # Network analysis
  "tidygraph",      # Tidy network manipulation
  "ggraph",         # Network visualization
  "network",        # Network objects
  "sna",            # Social network analysis
  "ergm",           # Exponential random graph models
  "intergraph"      # Convert between network formats
))
```

#### For Python Users
```bash
# Create conda environment
conda env create -f smm638.yaml
conda activate smm638

# Or install with pip
pip install numpy scipy matplotlib pandas networkx plotly pyvis
```

### Building the Website Locally

```bash
# Clone the repository
git clone https://github.com/simonesantoni/net-analysis-smm638.git
cd net-analysis-smm638

# Navigate to website directory
cd website

# Render the entire website
quarto render

# Or preview with live reload
quarto preview
```

---

## 📖 Course Content

### Weekly Structure

Each week follows a consistent **5P framework**:

1. **📚 Prepare**: Pre-class readings and materials
2. **👥 Participate**: Interactive lectures and discussions
3. **💻 Practice**: Hands-on coding exercises
4. **📝 Perform**: Assessed assignments
5. **🤔 Ponder**: Reflection questions and further reading

### Core Topics

| Week | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Introduction to Networks | Network terminology, data structures, basic visualization |
| 2 | Network Visualization | Layout algorithms, aesthetic principles, interactive plots |
| 3 | Node Centrality | Degree, betweenness, closeness, eigenvector centrality |
| 4 | Dyads & Triads | Subgraph analysis, structural balance, transitivity |
| 5 | Network Dynamics | Reciprocity, platform ecosystems, case study |
| 6 | Community Detection | Modularity, Louvain, Label Propagation algorithms |
| 7 | Two-Mode Networks | Bipartite graphs, affiliation networks, projections |
| 8 | Exponential Random Graph Models | Statistical modeling of networks, ERGM estimation |
| 9-10 | Advanced Topics | Temporal networks, diffusion, link prediction |

---

## 🔬 Featured Analyses

### SoundCloud Network Analysis (Week 5)

Comprehensive analysis of a music streaming platform with:
- 8,000 users, 1.2M tracks, 100K+ social connections
- **Exploratory Data Analysis**: User behavior, content patterns, engagement metrics
- **Network Properties Testing**: Statistical tests for reciprocity and transitivity
- **Visualization**: Interactive network plots and statistical distributions

**Technologies**: R, `igraph`, `tidyverse`, `sna`, CUG tests

### Key Features
- **Rigorous Statistical Testing**: Both Erdős-Rényi and Conditional Uniform Graph (CUG) tests
- **Reproducible Research**: Frozen computational outputs for CI/CD compatibility
- **Professional Visualizations**: Course-branded plots with consistent styling

---

## 🛠️ Technical Stack

### Website Infrastructure
- **Framework**: [Quarto](https://quarto.org) - Scientific and technical publishing system
- **Languages**: R (primary), Python (supplemental)
- **Deployment**: GitHub Pages via GitHub Actions
- **Theme**: Custom dual-mode (light/dark) with Atkinson Hyperlegible font

### R Packages
```r
# Core network analysis
igraph, tidygraph, ggraph, network, sna

# Statistical modeling
ergm, btergm, statnet

# Visualization
networkD3, visNetwork, ggplot2, gridExtra

# Data manipulation
tidyverse (dplyr, tidyr, purrr, readr)
```

### Python Libraries
```python
# Core network analysis
networkx, graph-tool

# Visualization
plotly, bokeh, pyvis, matplotlib, seaborn

# Data manipulation
numpy, scipy, pandas
```

---

## 📊 Datasets

The repository includes several curated network datasets:

| Dataset | Nodes | Edges | Type | Description |
|---------|-------|-------|------|-------------|
| SoundCloud | 8,000 | 100K+ | Directed | Music platform with users, tracks, follows |
| Deezer | 50K | 200K+ | Undirected | Music streaming social network |
| Twitch | 10K | 30K+ | Directed | Gaming platform follower network |
| Xoxoday | 500 | 1.5K | Undirected | Employee collaboration network |

**Data Location**: `data/` directory (some files are `.gitignore`d due to size)

---

## 🎓 Assessments

### Mid-Term Project (30%)
- Network analysis of real-world dataset
- Individual work
- Due: Week 6

### Final Project (70%)
- Comprehensive network analytics project
- Group work (2-3 students)
- Includes presentation and written report
- Due: End of term

---

## 🤝 Contributing

This is an active teaching repository. Contributions are welcome:

1. **Report Issues**: Use GitHub Issues for bugs or suggestions
2. **Submit Pull Requests**: For typos, clarifications, or enhancements
3. **Share Feedback**: Contact the teaching team

---

## 👥 Teaching Team

- **Module Leader**: Dr. Simone Santoni
- **Teaching Assistants**: See [course website](https://simonesantoni.github.io/net-analysis-smm638/course/team.html)

**Office Hours**: Check the [support page](https://simonesantoni.github.io/net-analysis-smm638/course/support.html)

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

Educational materials are provided for academic use. Please cite appropriately when using course materials in your work.

---

## 🔗 Links

- **Course Website**: https://simonesantoni.github.io/net-analysis-smm638
- **City, University of London**: https://www.city.ac.uk
- **Bayes Business School**: https://www.bayes.city.ac.uk

---

## 📧 Contact

For course-related queries:
- Email: simone.santoni.1@city.ac.uk
- Moodle: SMM638 course forum
- Office Hours: See support page

---

## ⭐ Acknowledgments

- Built with [Quarto](https://quarto.org)
- Network analysis powered by [`igraph`](https://igraph.org) and [`NetworkX`](https://networkx.org)
- Visualization using [`ggraph`](https://ggraph.data-imaginist.com) and [`Plotly`](https://plotly.com)
- Hosted on [GitHub Pages](https://pages.github.com)

---

**Last Updated**: November 2025
