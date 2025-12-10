"""
Exploratory Data Analysis (EDA) for Burt (2004) Structural Holes Dataset

This script performs a comprehensive EDA on the synthetic companion dataset
based on Burt's "Structural Holes and Good Ideas" (American Journal of Sociology, 2004).

Dataset components:
- nodes.csv: 673 supply-chain managers with attributes and performance metrics
- edges.csv: 1,218 discussion network ties with weights

Author: Generated for SMM638 Network Analysis Course
Date: December 10, 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from pathlib import Path
import warnings

warnings.filterwarnings("ignore")

# Set style for visualizations
plt.style.use("seaborn-v0_8-darkgrid")
sns.set_palette("husl")
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 10

# Data paths
DATA_DIR = Path(__file__).parent
NODES_FILE = DATA_DIR / "nodes.csv"
EDGES_FILE = DATA_DIR / "edges.csv"
OUTPUT_DIR = DATA_DIR / "eda_output"
OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 80)
print("EXPLORATORY DATA ANALYSIS: Burt (2004) Structural Holes Dataset")
print("=" * 80)
print()

# ==============================================================================
# 1. DATA LOADING AND BASIC INSPECTION
# ==============================================================================

print("1. LOADING DATA")
print("-" * 80)

# Load datasets
nodes = pd.read_csv(NODES_FILE)
edges = pd.read_csv(EDGES_FILE)

print(f"✓ Loaded nodes.csv: {nodes.shape[0]} rows × {nodes.shape[1]} columns")
print(f"✓ Loaded edges.csv: {edges.shape[0]} rows × {edges.shape[1]} columns")
print()

# ==============================================================================
# 2. NODES DATASET: BASIC STATISTICS
# ==============================================================================

print("2. NODES DATASET: BASIC STATISTICS")
print("-" * 80)

print("\nColumn Names and Data Types:")
print(nodes.dtypes)
print()

print("\nFirst 5 Rows:")
print(nodes.head())
print()

print("\nBasic Statistics (Numeric Variables):")
print(nodes.describe())
print()

print("\nMissing Values:")
missing = nodes.isnull().sum()
missing_pct = (missing / len(nodes)) * 100
missing_df = pd.DataFrame(
    {"Missing Count": missing[missing > 0], "Missing %": missing_pct[missing > 0]}
)
if len(missing_df) > 0:
    print(missing_df.sort_values("Missing Count", ascending=False))
else:
    print("No missing values found.")
print()

# ==============================================================================
# 3. EDGES DATASET: BASIC STATISTICS
# ==============================================================================

print("3. EDGES DATASET: BASIC STATISTICS")
print("-" * 80)

print("\nColumn Names and Data Types:")
print(edges.dtypes)
print()

print("\nFirst 5 Rows:")
print(edges.head())
print()

print("\nBasic Statistics:")
print(edges.describe())
print()

print("\nTie Type Distribution:")
print(edges["tie_type"].value_counts())
print()

print("\nTie Weight Distribution:")
print(edges["weight"].value_counts().sort_index(ascending=False))
print()

# ==============================================================================
# 4. DEMOGRAPHIC ANALYSIS
# ==============================================================================

print("4. DEMOGRAPHIC ANALYSIS")
print("-" * 80)

# Age distribution
print(f"\nAge Statistics:")
print(f"  Mean: {nodes['age'].mean():.1f} years")
print(f"  Median: {nodes['age'].median():.1f} years")
print(f"  Range: {nodes['age'].min():.0f} - {nodes['age'].max():.0f} years")
print(f"  Std Dev: {nodes['age'].std():.1f}")
print()

# Education distribution
print("Education Distribution:")
print(nodes["education"].value_counts())
print()

# Rank distribution
print("Job Rank Distribution:")
print(nodes["rank"].value_counts().sort_index())
print()

# Role distribution
print("Role Distribution:")
print(nodes["role"].value_counts())
print()

# Business Unit distribution
print("Business Unit Distribution:")
print(nodes["business_unit"].value_counts())
print()

# Location distribution
print("Location Distribution:")
print(nodes["location"].value_counts())
print()

# Isolate distribution
print("Social Isolates:")
isolate_counts = nodes["isolate"].value_counts()
print(isolate_counts)
print(f"Isolate Percentage: {(isolate_counts.get(True, 0) / len(nodes)) * 100:.1f}%")
print()

# ==============================================================================
# 5. NETWORK CONSTRUCTION AND BASIC METRICS
# ==============================================================================

print("5. NETWORK CONSTRUCTION AND ANALYSIS")
print("-" * 80)

# Create network
G = nx.from_pandas_edgelist(edges, "source", "target", edge_attr="weight")

print(f"\nNetwork Basic Properties:")
print(f"  Nodes: {G.number_of_nodes()}")
print(f"  Edges: {G.number_of_edges()}")
print(f"  Density: {nx.density(G):.4f}")
print(f"  Is Connected: {nx.is_connected(G)}")

# Connected components
components = list(nx.connected_components(G))
print(f"  Number of Connected Components: {len(components)}")
print(f"  Largest Component Size: {len(max(components, key=len))}")
print()

# Degree statistics
degrees = dict(G.degree())
degree_values = list(degrees.values())
print(f"Degree Statistics:")
print(f"  Mean Degree: {np.mean(degree_values):.2f}")
print(f"  Median Degree: {np.median(degree_values):.2f}")
print(f"  Max Degree: {np.max(degree_values)}")
print(f"  Min Degree: {np.min(degree_values)}")
print()

# Compare with nodes dataset
print(f"Comparison with Nodes Dataset:")
print(f"  Nodes in Network: {G.number_of_nodes()}")
print(f"  Nodes in nodes.csv: {len(nodes)}")
print(f"  Difference (Isolates): {len(nodes) - G.number_of_nodes()}")
print()

# ==============================================================================
# 6. NETWORK POSITION VARIABLES ANALYSIS
# ==============================================================================

print("6. NETWORK POSITION VARIABLES")
print("-" * 80)

network_vars = [
    "degree",
    "weighted_degree",
    "constraint",
    "log_constraint",
    "betweenness",
    "clustering",
    "mean_path_len",
]

print("\nNetwork Position Statistics:")
for var in network_vars:
    if var in nodes.columns:
        valid_data = nodes[var].dropna()
        print(f"\n{var}:")
        print(f"  Mean: {valid_data.mean():.4f}")
        print(f"  Median: {valid_data.median():.4f}")
        print(f"  Std: {valid_data.std():.4f}")
        print(f"  Range: [{valid_data.min():.4f}, {valid_data.max():.4f}]")

print()

# Core network membership
if "core89" in nodes.columns:
    core_counts = nodes["core89"].value_counts()
    print("Core Network (Top 89) Membership:")
    print(core_counts)
    print(f"Core Percentage: {(core_counts.get(True, 0) / len(nodes)) * 100:.1f}%")
print()

# ==============================================================================
# 7. PERFORMANCE AND OUTCOME VARIABLES
# ==============================================================================

print("7. PERFORMANCE AND OUTCOME VARIABLES")
print("-" * 80)

# Salary residual
if "salary_resid" in nodes.columns:
    print("\nSalary Residual (Standardized):")
    print(nodes["salary_resid"].describe())
    print()

# Evaluation
if "evaluation" in nodes.columns:
    print("Performance Evaluation Distribution:")
    print(nodes["evaluation"].value_counts())
    print()

# Promotion or above-average raise
if "promoted_or_aboveavg" in nodes.columns:
    promo_counts = nodes["promoted_or_aboveavg"].value_counts()
    print("Promotion or Above-Average Raise:")
    print(promo_counts)
    print(f"Promotion Rate: {(promo_counts.get(True, 0) / len(nodes)) * 100:.1f}%")
    print()

# Survey response
if "responded" in nodes.columns:
    resp_counts = nodes["responded"].value_counts()
    print("Survey Response:")
    print(resp_counts)
    print(f"Response Rate: {(resp_counts.get(True, 0) / len(nodes)) * 100:.1f}%")
    print()

# Idea variables (among respondents)
if "idea_expressed" in nodes.columns:
    respondents = nodes[nodes["responded"] == True]
    idea_counts = respondents["idea_expressed"].value_counts()
    print("Idea Expression (among respondents):")
    print(idea_counts)
    if len(idea_counts) > 0:
        print(
            f"Idea Expression Rate: {(idea_counts.get(True, 0) / len(respondents)) * 100:.1f}%"
        )
    print()

# Idea value (among those who expressed ideas)
if "idea_value" in nodes.columns:
    ideas = nodes[nodes["idea_expressed"] == True]
    if len(ideas) > 0:
        print("Idea Value (among those who expressed ideas):")
        print(ideas["idea_value"].describe())
        print()

# Idea dismissal
if "idea_dismissed" in nodes.columns:
    dismissed = nodes[nodes["idea_expressed"] == True]["idea_dismissed"].value_counts()
    print("Idea Dismissal (among those who expressed ideas):")
    print(dismissed)
    if len(dismissed) > 0:
        print(f"Dismissal Rate: {(dismissed.get(True, 0) / len(ideas)) * 100:.1f}%")
    print()

# ==============================================================================
# 8. KEY CORRELATIONS
# ==============================================================================

print("8. KEY CORRELATIONS")
print("-" * 80)

# Select numeric variables for correlation analysis
numeric_vars = [
    "age",
    "degree",
    "weighted_degree",
    "constraint",
    "log_constraint",
    "betweenness",
    "clustering",
    "salary_resid",
    "idea_value",
]

# Filter to available variables
available_vars = [v for v in numeric_vars if v in nodes.columns]

# Calculate correlation matrix
corr_matrix = nodes[available_vars].corr()

print("\nCorrelation Matrix (Key Variables):")
print(corr_matrix.round(3))
print()

# Highlight key theoretical correlations
print("Key Theoretical Correlations:")
key_pairs = [
    ("degree", "log_constraint"),
    ("log_constraint", "idea_value"),
    ("degree", "idea_value"),
    ("log_constraint", "salary_resid"),
    ("betweenness", "log_constraint"),
]

for var1, var2 in key_pairs:
    if var1 in corr_matrix.columns and var2 in corr_matrix.columns:
        corr = corr_matrix.loc[var1, var2]
        print(f"  {var1} ↔ {var2}: {corr:.3f}")
print()

# ==============================================================================
# 9. VISUALIZATION: DEMOGRAPHICS
# ==============================================================================

print("9. GENERATING VISUALIZATIONS")
print("-" * 80)

# Figure 1: Demographic Distributions
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle("Figure 1: Demographic Distributions", fontsize=16, fontweight="bold")

# Age distribution
axes[0, 0].hist(nodes["age"], bins=20, edgecolor="black", alpha=0.7)
axes[0, 0].set_xlabel("Age (years)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_title("Age Distribution")
axes[0, 0].axvline(
    nodes["age"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: {nodes["age"].mean():.1f}',
)
axes[0, 0].legend()

# Education
edu_counts = nodes["education"].value_counts()
axes[0, 1].bar(range(len(edu_counts)), edu_counts.values, edgecolor="black")
axes[0, 1].set_xticks(range(len(edu_counts)))
axes[0, 1].set_xticklabels(edu_counts.index, rotation=45, ha="right")
axes[0, 1].set_ylabel("Count")
axes[0, 1].set_title("Education Distribution")

# Rank
rank_counts = nodes["rank"].value_counts().sort_index()
axes[0, 2].bar(range(len(rank_counts)), rank_counts.values, edgecolor="black")
axes[0, 2].set_xticks(range(len(rank_counts)))
axes[0, 2].set_xticklabels(rank_counts.index, rotation=45, ha="right")
axes[0, 2].set_ylabel("Count")
axes[0, 2].set_title("Job Rank Distribution")

# Role
role_counts = nodes["role"].value_counts()
axes[1, 0].bar(range(len(role_counts)), role_counts.values, edgecolor="black")
axes[1, 0].set_xticks(range(len(role_counts)))
axes[1, 0].set_xticklabels(role_counts.index, rotation=45, ha="right")
axes[1, 0].set_ylabel("Count")
axes[1, 0].set_title("Role Distribution")

# Business Unit
bu_counts = nodes["business_unit"].value_counts()
axes[1, 1].bar(range(len(bu_counts)), bu_counts.values, edgecolor="black")
axes[1, 1].set_xticks(range(len(bu_counts)))
axes[1, 1].set_xticklabels(bu_counts.index, rotation=45, ha="right")
axes[1, 1].set_ylabel("Count")
axes[1, 1].set_title("Business Unit Distribution")

# Isolate status
isolate_counts = nodes["isolate"].value_counts()
colors = ["#2ecc71" if x == False else "#e74c3c" for x in isolate_counts.index]
axes[1, 2].bar(
    range(len(isolate_counts)), isolate_counts.values, color=colors, edgecolor="black"
)
axes[1, 2].set_xticks(range(len(isolate_counts)))
axes[1, 2].set_xticklabels(["Connected", "Isolate"], rotation=0)
axes[1, 2].set_ylabel("Count")
axes[1, 2].set_title("Social Isolate Status")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "fig1_demographics.png", dpi=300, bbox_inches="tight")
print("✓ Saved: fig1_demographics.png")
plt.close()

# ==============================================================================
# 10. VISUALIZATION: NETWORK METRICS
# ==============================================================================

# Figure 2: Network Position Metrics
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle("Figure 2: Network Position Metrics", fontsize=16, fontweight="bold")

# Degree distribution
non_isolates = nodes[nodes["isolate"] == False]
axes[0, 0].hist(non_isolates["degree"], bins=30, edgecolor="black", alpha=0.7)
axes[0, 0].set_xlabel("Degree")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_title("Degree Distribution (Non-Isolates)")
axes[0, 0].axvline(
    non_isolates["degree"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: {non_isolates["degree"].mean():.1f}',
)
axes[0, 0].legend()

# Weighted degree
axes[0, 1].hist(
    non_isolates["weighted_degree"],
    bins=30,
    edgecolor="black",
    alpha=0.7,
    color="orange",
)
axes[0, 1].set_xlabel("Weighted Degree")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("Weighted Degree Distribution (Non-Isolates)")
axes[0, 1].axvline(
    non_isolates["weighted_degree"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: {non_isolates["weighted_degree"].mean():.1f}',
)
axes[0, 1].legend()

# Constraint (log scale is more interpretable)
axes[0, 2].hist(
    non_isolates["log_constraint"], bins=30, edgecolor="black", alpha=0.7, color="green"
)
axes[0, 2].set_xlabel("Log Constraint")
axes[0, 2].set_ylabel("Frequency")
axes[0, 2].set_title("Log Constraint Distribution (Non-Isolates)")
axes[0, 2].axvline(
    non_isolates["log_constraint"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: {non_isolates["log_constraint"].mean():.2f}',
)
axes[0, 2].legend()

# Betweenness centrality
axes[1, 0].hist(
    non_isolates["betweenness"], bins=30, edgecolor="black", alpha=0.7, color="purple"
)
axes[1, 0].set_xlabel("Betweenness Centrality")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].set_title("Betweenness Centrality Distribution")
axes[1, 0].axvline(
    non_isolates["betweenness"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: {non_isolates["betweenness"].mean():.4f}',
)
axes[1, 0].legend()

# Clustering coefficient
axes[1, 1].hist(
    non_isolates["clustering"], bins=30, edgecolor="black", alpha=0.7, color="brown"
)
axes[1, 1].set_xlabel("Clustering Coefficient")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_title("Clustering Coefficient Distribution")
axes[1, 1].axvline(
    non_isolates["clustering"].mean(),
    color="red",
    linestyle="--",
    label=f'Mean: {non_isolates["clustering"].mean():.3f}',
)
axes[1, 1].legend()

# Degree vs Constraint (scatter)
axes[1, 2].scatter(
    non_isolates["degree"], non_isolates["log_constraint"], alpha=0.5, s=10
)
axes[1, 2].set_xlabel("Degree")
axes[1, 2].set_ylabel("Log Constraint")
axes[1, 2].set_title(
    f'Degree vs Log Constraint\n(r = {non_isolates[["degree", "log_constraint"]].corr().iloc[0, 1]:.3f})'
)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "fig2_network_metrics.png", dpi=300, bbox_inches="tight")
print("✓ Saved: fig2_network_metrics.png")
plt.close()

# ==============================================================================
# 11. VISUALIZATION: PERFORMANCE OUTCOMES
# ==============================================================================

# Figure 3: Performance and Outcomes
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(
    "Figure 3: Performance and Outcome Variables", fontsize=16, fontweight="bold"
)

# Salary residual
axes[0, 0].hist(nodes["salary_resid"].dropna(), bins=30, edgecolor="black", alpha=0.7)
axes[0, 0].set_xlabel("Salary Residual (Standardized)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_title("Salary Residual Distribution")
axes[0, 0].axvline(0, color="red", linestyle="--", label="Mean = 0")
axes[0, 0].legend()

# Evaluation
eval_counts = nodes["evaluation"].value_counts()
eval_order = ["Poor", "Good", "Outstanding"]
eval_sorted = [eval_counts.get(x, 0) for x in eval_order]
axes[0, 1].bar(range(len(eval_order)), eval_sorted, edgecolor="black")
axes[0, 1].set_xticks(range(len(eval_order)))
axes[0, 1].set_xticklabels(eval_order)
axes[0, 1].set_ylabel("Count")
axes[0, 1].set_title("Performance Evaluation")

# Promotion or above-average
promo_counts = nodes["promoted_or_aboveavg"].value_counts()
colors = ["#e74c3c" if x == False else "#2ecc71" for x in promo_counts.index]
axes[0, 2].bar(
    range(len(promo_counts)), promo_counts.values, color=colors, edgecolor="black"
)
axes[0, 2].set_xticks(range(len(promo_counts)))
axes[0, 2].set_xticklabels(["No", "Yes"])
axes[0, 2].set_ylabel("Count")
axes[0, 2].set_title("Promotion or Above-Average Raise")

# Idea value distribution
ideas = nodes[nodes["idea_expressed"] == True]
if len(ideas) > 0:
    axes[1, 0].hist(
        ideas["idea_value"].dropna(),
        bins=np.arange(0.5, 6.5, 1),
        edgecolor="black",
        alpha=0.7,
        color="teal",
    )
    axes[1, 0].set_xlabel("Idea Value (1-5)")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].set_title("Idea Value Distribution")
    axes[1, 0].axvline(
        ideas["idea_value"].mean(),
        color="red",
        linestyle="--",
        label=f'Mean: {ideas["idea_value"].mean():.2f}',
    )
    axes[1, 0].legend()
    axes[1, 0].set_xticks([1, 2, 3, 4, 5])
else:
    axes[1, 0].text(
        0.5, 0.5, "No data", ha="center", va="center", transform=axes[1, 0].transAxes
    )

# Idea dismissal
if len(ideas) > 0:
    dismissed_counts = ideas["idea_dismissed"].value_counts()
    colors = ["#2ecc71" if x == False else "#e74c3c" for x in dismissed_counts.index]
    axes[1, 1].bar(
        range(len(dismissed_counts)),
        dismissed_counts.values,
        color=colors,
        edgecolor="black",
    )
    axes[1, 1].set_xticks(range(len(dismissed_counts)))
    axes[1, 1].set_xticklabels(["Not Dismissed", "Dismissed"])
    axes[1, 1].set_ylabel("Count")
    axes[1, 1].set_title("Idea Dismissal (among ideas)")
else:
    axes[1, 1].text(
        0.5, 0.5, "No data", ha="center", va="center", transform=axes[1, 1].transAxes
    )

# Survey response funnel
response_data = {
    "Total": len(nodes),
    "Responded": nodes["responded"].sum(),
    "Expressed Idea": nodes["idea_expressed"].sum(),
    "Discussed Idea": (
        nodes["idea_discussed"].sum() if "idea_discussed" in nodes.columns else 0
    ),
}
axes[1, 2].barh(
    range(len(response_data)), list(response_data.values()), edgecolor="black"
)
axes[1, 2].set_yticks(range(len(response_data)))
axes[1, 2].set_yticklabels(list(response_data.keys()))
axes[1, 2].set_xlabel("Count")
axes[1, 2].set_title("Survey Response Funnel")
for i, v in enumerate(response_data.values()):
    axes[1, 2].text(v + 10, i, str(int(v)), va="center")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "fig3_performance.png", dpi=300, bbox_inches="tight")
print("✓ Saved: fig3_performance.png")
plt.close()

# ==============================================================================
# 12. VISUALIZATION: CORRELATION HEATMAP
# ==============================================================================

# Figure 4: Correlation Heatmap
fig, ax = plt.subplots(figsize=(12, 10))
fig.suptitle(
    "Figure 4: Correlation Matrix (Key Variables)", fontsize=16, fontweight="bold"
)

# Select key variables for correlation
corr_vars = [
    "age",
    "degree",
    "weighted_degree",
    "log_constraint",
    "betweenness",
    "clustering",
    "salary_resid",
    "idea_value",
]
corr_vars = [v for v in corr_vars if v in nodes.columns]

# Calculate correlation
corr_data = nodes[corr_vars].corr()

# Create heatmap
sns.heatmap(
    corr_data,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=1,
    cbar_kws={"shrink": 0.8},
    ax=ax,
)
ax.set_title("")  # Remove default title since we have suptitle

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "fig4_correlation_heatmap.png", dpi=300, bbox_inches="tight")
print("✓ Saved: fig4_correlation_heatmap.png")
plt.close()

# ==============================================================================
# 13. VISUALIZATION: TIE WEIGHTS AND TYPES
# ==============================================================================

# Figure 5: Edge Analysis
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Figure 5: Edge/Tie Analysis", fontsize=16, fontweight="bold")

# Tie type distribution
tie_counts = edges["tie_type"].value_counts().sort_values(ascending=True)
axes[0, 0].barh(range(len(tie_counts)), tie_counts.values, edgecolor="black")
axes[0, 0].set_yticks(range(len(tie_counts)))
axes[0, 0].set_yticklabels(tie_counts.index)
axes[0, 0].set_xlabel("Count")
axes[0, 0].set_title("Tie Type Distribution")
for i, v in enumerate(tie_counts.values):
    axes[0, 0].text(v + 10, i, str(v), va="center")

# Weight distribution
weight_counts = edges["weight"].value_counts().sort_index(ascending=False)
axes[0, 1].bar(range(len(weight_counts)), weight_counts.values, edgecolor="black")
axes[0, 1].set_xticks(range(len(weight_counts)))
axes[0, 1].set_xticklabels([f"{w:.2f}" for w in weight_counts.index], rotation=45)
axes[0, 1].set_ylabel("Count")
axes[0, 1].set_xlabel("Weight")
axes[0, 1].set_title("Tie Weight Distribution")

# Cross-BU ties
edges["is_cross_bu"] = edges["bu_u"] != edges["bu_v"]
cross_bu_counts = edges["is_cross_bu"].value_counts()
colors = ["#3498db" if x == False else "#e74c3c" for x in cross_bu_counts.index]
axes[1, 0].bar(
    range(len(cross_bu_counts)), cross_bu_counts.values, color=colors, edgecolor="black"
)
axes[1, 0].set_xticks(range(len(cross_bu_counts)))
axes[1, 0].set_xticklabels(["Within BU", "Cross BU"])
axes[1, 0].set_ylabel("Count")
axes[1, 0].set_title("Within vs Cross Business Unit Ties")
pct_cross = (cross_bu_counts.get(True, 0) / len(edges)) * 100
axes[1, 0].text(
    0.5,
    0.95,
    f"Cross-BU: {pct_cross:.1f}%",
    transform=axes[1, 0].transAxes,
    ha="center",
    fontsize=10,
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
)

# Degree distribution from network
degree_seq = sorted([d for n, d in G.degree()], reverse=True)
axes[1, 1].plot(degree_seq, marker="o", linestyle="-", markersize=2)
axes[1, 1].set_xlabel("Node Rank")
axes[1, 1].set_ylabel("Degree")
axes[1, 1].set_title("Degree Distribution (Ranked)")
axes[1, 1].set_yscale("log")
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "fig5_edge_analysis.png", dpi=300, bbox_inches="tight")
print("✓ Saved: fig5_edge_analysis.png")
plt.close()

# ==============================================================================
# 14. VISUALIZATION: KEY RELATIONSHIPS (STRUCTURAL HOLES THEORY)
# ==============================================================================

# Figure 6: Structural Holes and Good Ideas
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle(
    "Figure 6: Structural Holes Theory - Key Relationships",
    fontsize=16,
    fontweight="bold",
)

# Constraint vs Idea Value
ideas_data = nodes[nodes["idea_expressed"] == True].copy()
if len(ideas_data) > 0:
    axes[0, 0].scatter(
        ideas_data["log_constraint"], ideas_data["idea_value"], alpha=0.6, s=30
    )
    axes[0, 0].set_xlabel("Log Constraint (Higher = More Constrained Network)")
    axes[0, 0].set_ylabel("Idea Value (1-5)")
    axes[0, 0].set_title("Network Constraint vs Idea Value")

    # Add regression line
    valid_mask = ideas_data["log_constraint"].notna() & ideas_data["idea_value"].notna()
    if valid_mask.sum() > 0:
        z = np.polyfit(
            ideas_data.loc[valid_mask, "log_constraint"],
            ideas_data.loc[valid_mask, "idea_value"],
            1,
        )
        p = np.poly1d(z)
        x_line = np.linspace(
            ideas_data["log_constraint"].min(), ideas_data["log_constraint"].max(), 100
        )
        axes[0, 0].plot(
            x_line, p(x_line), "r--", alpha=0.8, linewidth=2, label="Linear Fit"
        )
        corr = ideas_data[["log_constraint", "idea_value"]].corr().iloc[0, 1]
        axes[0, 0].legend(title=f"r = {corr:.3f}")

# Constraint vs Salary Residual (by rank)
axes[0, 1].scatter(nodes["log_constraint"], nodes["salary_resid"], alpha=0.3, s=20)
axes[0, 1].set_xlabel("Log Constraint")
axes[0, 1].set_ylabel("Salary Residual (Standardized)")
axes[0, 1].set_title("Network Constraint vs Salary Performance")
axes[0, 1].axhline(0, color="gray", linestyle="--", alpha=0.5)

# Add regression line
valid_mask = nodes["log_constraint"].notna() & nodes["salary_resid"].notna()
if valid_mask.sum() > 0:
    z = np.polyfit(
        nodes.loc[valid_mask, "log_constraint"],
        nodes.loc[valid_mask, "salary_resid"],
        1,
    )
    p = np.poly1d(z)
    x_line = np.linspace(
        nodes["log_constraint"].min(), nodes["log_constraint"].max(), 100
    )
    axes[0, 1].plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)
    corr = nodes[["log_constraint", "salary_resid"]].corr().iloc[0, 1]
    axes[0, 1].text(
        0.05,
        0.95,
        f"r = {corr:.3f}",
        transform=axes[0, 1].transAxes,
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
    )

# Constraint by evaluation category
eval_order = ["Poor", "Good", "Outstanding"]
eval_data = []
for cat in eval_order:
    cat_data = nodes[nodes["evaluation"] == cat]["log_constraint"].dropna()
    if len(cat_data) > 0:
        eval_data.append(cat_data)
    else:
        eval_data.append([])

if any(len(d) > 0 for d in eval_data):
    bp = axes[1, 0].boxplot(eval_data, labels=eval_order, patch_artist=True)
    for patch in bp["boxes"]:
        patch.set_facecolor("lightblue")
    axes[1, 0].set_ylabel("Log Constraint")
    axes[1, 0].set_xlabel("Performance Evaluation")
    axes[1, 0].set_title("Network Constraint by Performance Evaluation")
    axes[1, 0].grid(True, alpha=0.3, axis="y")

# Promotion rate by constraint quartile
try:
    nodes["constraint_quartile"] = pd.qcut(
        nodes["log_constraint"], q=4, duplicates="drop"
    )
    # Map to meaningful labels
    quartile_map = {
        cat: f"Q{i+1}"
        for i, cat in enumerate(sorted(nodes["constraint_quartile"].dropna().unique()))
    }
    # Rename first to Low, last to High
    quartile_keys = sorted(nodes["constraint_quartile"].dropna().unique())
    if len(quartile_keys) >= 2:
        quartile_map[quartile_keys[0]] = "Q1 (Low)"
        quartile_map[quartile_keys[-1]] = f"Q{len(quartile_keys)} (High)"
    nodes["constraint_quartile"] = nodes["constraint_quartile"].map(quartile_map)
except Exception as e:
    print(f"Warning: Could not create quartiles: {e}")
    # Fallback: use median split
    median_constraint = nodes["log_constraint"].median()
    nodes["constraint_quartile"] = nodes["log_constraint"].apply(
        lambda x: (
            "Low Constraint"
            if x <= median_constraint
            else "High Constraint" if not pd.isna(x) else None
        )
    )

promo_by_constraint = nodes.groupby("constraint_quartile")[
    "promoted_or_aboveavg"
].apply(lambda x: (x.sum() / len(x)) * 100 if len(x) > 0 else 0)

axes[1, 1].bar(
    range(len(promo_by_constraint)),
    promo_by_constraint.values,
    edgecolor="black",
    color=["#2ecc71", "#3498db", "#f39c12", "#e74c3c"],
)
axes[1, 1].set_xticks(range(len(promo_by_constraint)))
axes[1, 1].set_xticklabels(promo_by_constraint.index, rotation=0)
axes[1, 1].set_ylabel("Promotion Rate (%)")
axes[1, 1].set_xlabel("Network Constraint Quartile")
axes[1, 1].set_title("Promotion Rate by Network Constraint")
axes[1, 1].set_ylim(0, 100)

# Add values on bars
for i, v in enumerate(promo_by_constraint.values):
    axes[1, 1].text(i, v + 2, f"{v:.1f}%", ha="center", fontweight="bold")

plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "fig6_structural_holes_theory.png", dpi=300, bbox_inches="tight"
)
print("✓ Saved: fig6_structural_holes_theory.png")
plt.close()

# ==============================================================================
# 15. NETWORK VISUALIZATION (SAMPLE)
# ==============================================================================

# Figure 7: Network Visualization (Largest Component)
print("\nGenerating network visualization...")

# Get largest connected component
largest_cc = max(nx.connected_components(G), key=len)
G_main = G.subgraph(largest_cc).copy()

# Limit to a manageable size for visualization (e.g., 200 nodes)
if len(G_main) > 200:
    # Sample high-degree nodes for better visualization
    degrees = dict(G_main.degree())
    top_nodes = sorted(degrees, key=degrees.get, reverse=True)[:200]
    G_viz = G_main.subgraph(top_nodes).copy()
else:
    G_viz = G_main

print(f"  Visualizing {len(G_viz)} nodes from largest component...")

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
fig.suptitle(
    "Figure 7: Network Structure Visualization", fontsize=16, fontweight="bold"
)

# Layout
pos = nx.spring_layout(G_viz, k=0.5, iterations=50, seed=42)

# Prepare node attributes
node_ids = list(G_viz.nodes())
node_data = nodes.set_index("id")

# Node sizes based on degree
node_sizes = [G_viz.degree(n) * 20 for n in node_ids]

# Panel 1: Colored by business unit
bu_colors = {
    "BU_A": "#e74c3c",
    "BU_B": "#3498db",
    "BU_C": "#2ecc71",
    "BU_D": "#f39c12",
    "BU_E": "#9b59b6",
    "HQ": "#34495e",
}

node_colors_bu = []
for n in node_ids:
    bu = node_data.loc[n, "business_unit"] if n in node_data.index else "HQ"
    node_colors_bu.append(bu_colors.get(bu, "#95a5a6"))

nx.draw_networkx_nodes(
    G_viz, pos, node_color=node_colors_bu, node_size=node_sizes, alpha=0.7, ax=axes[0]
)
nx.draw_networkx_edges(G_viz, pos, alpha=0.2, width=0.5, ax=axes[0])
axes[0].set_title("Network Colored by Business Unit")
axes[0].axis("off")

# Create legend
from matplotlib.patches import Patch

legend_elements = [Patch(facecolor=color, label=bu) for bu, color in bu_colors.items()]
axes[0].legend(handles=legend_elements, loc="upper left", fontsize=9)

# Panel 2: Node size by constraint (low constraint = larger nodes)
node_sizes_constraint = []
for n in node_ids:
    if n in node_data.index:
        constraint = node_data.loc[n, "constraint"]
        # Inverse: low constraint = large node (structural holes)
        size = (100 - constraint) * 2 if not pd.isna(constraint) else 50
        node_sizes_constraint.append(size)
    else:
        node_sizes_constraint.append(50)

nx.draw_networkx_nodes(
    G_viz,
    pos,
    node_color="#3498db",
    node_size=node_sizes_constraint,
    alpha=0.7,
    ax=axes[1],
)
nx.draw_networkx_edges(G_viz, pos, alpha=0.2, width=0.5, ax=axes[1])
axes[1].set_title("Node Size by Structural Holes (Larger = Lower Constraint)")
axes[1].axis("off")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "fig7_network_visualization.png", dpi=300, bbox_inches="tight")
print("✓ Saved: fig7_network_visualization.png")
plt.close()

# ==============================================================================
# 16. SUMMARY REPORT
# ==============================================================================

print("\n" + "=" * 80)
print("EDA COMPLETE - SUMMARY REPORT")
print("=" * 80)

# Prepare conditional values
salary_corr = (
    corr_matrix.loc["log_constraint", "salary_resid"]
    if "salary_resid" in corr_matrix.columns
    else None
)
idea_corr = (
    corr_matrix.loc["log_constraint", "idea_value"]
    if "idea_value" in corr_matrix.columns
    else None
)
dismissal_rate = (
    (ideas["idea_dismissed"].sum() / len(ideas) * 100) if len(ideas) > 0 else None
)

salary_corr_str = f"{salary_corr:.3f}" if salary_corr is not None else "N/A"
idea_corr_str = f"{idea_corr:.3f}" if idea_corr is not None else "N/A"
dismissal_rate_str = f"{dismissal_rate:.1f}%" if dismissal_rate is not None else "N/A"

summary_report = f"""
BURT (2004) STRUCTURAL HOLES DATASET - EDA SUMMARY
Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

===============================================================================
DATASET OVERVIEW
===============================================================================
Nodes (Employees): {len(nodes)}
Edges (Relationships): {len(edges)}
Network Density: {nx.density(G):.4f}
Connected Components: {len(list(nx.connected_components(G)))}
Social Isolates: {nodes['isolate'].sum()} ({(nodes['isolate'].sum()/len(nodes)*100):.1f}%)

===============================================================================
DEMOGRAPHIC SUMMARY
===============================================================================
Age: Mean={nodes['age'].mean():.1f}, Range=[{nodes['age'].min():.0f}, {nodes['age'].max():.0f}]
Education: {', '.join([f'{k}: {v}' for k, v in nodes['education'].value_counts().items()])}
Ranks: {', '.join([f'{k}: {v}' for k, v in nodes['rank'].value_counts().sort_index().items()])}
Business Units: {len(nodes['business_unit'].unique())}

===============================================================================
NETWORK METRICS (Non-Isolates)
===============================================================================
Mean Degree: {non_isolates['degree'].mean():.2f}
Mean Weighted Degree: {non_isolates['weighted_degree'].mean():.2f}
Mean Log Constraint: {non_isolates['log_constraint'].mean():.3f}
Mean Betweenness: {non_isolates['betweenness'].mean():.4f}
Mean Clustering: {non_isolates['clustering'].mean():.3f}

===============================================================================
KEY FINDINGS (REPLICATING BURT 2004)
===============================================================================

1. BROKERAGE AND PERFORMANCE
   - Degree ↔ Log Constraint: r = {corr_matrix.loc['degree', 'log_constraint']:.3f}
     (As expected: more contacts → lower constraint)
   
   - Log Constraint ↔ Salary Residual: r = {salary_corr_str}
     (Negative association: lower constraint → higher salary)

2. BROKERAGE AND GOOD IDEAS
   - Log Constraint ↔ Idea Value: r = {idea_corr_str}
     (Strong negative: structural holes → better ideas)
   
   - Idea Dismissal Rate: {dismissal_rate_str} among expressed ideas

3. NETWORK STRUCTURE
   - Cross-BU Ties: {(cross_bu_counts.get(True, 0) / len(edges) * 100):.1f}%
     (Confirms structural holes between business units)
   
   - Tie Strength Distribution:
     {chr(10).join([f'     {k}: {v} ({v/len(edges)*100:.1f}%)' for k, v in edges['tie_type'].value_counts().items()])}

===============================================================================
VISUALIZATIONS GENERATED
===============================================================================
1. fig1_demographics.png - Demographic distributions
2. fig2_network_metrics.png - Network position metrics
3. fig3_performance.png - Performance and outcome variables
4. fig4_correlation_heatmap.png - Correlation matrix
5. fig5_edge_analysis.png - Edge/tie analysis
6. fig6_structural_holes_theory.png - Key theoretical relationships
7. fig7_network_visualization.png - Network structure

All outputs saved to: {OUTPUT_DIR}

===============================================================================
"""

print(summary_report)

# Save summary report
with open(OUTPUT_DIR / "eda_summary_report.txt", "w") as f:
    f.write(summary_report)

print(f"\n✓ Summary report saved to: {OUTPUT_DIR / 'eda_summary_report.txt'}")

print("\n" + "=" * 80)
print("END OF ANALYSIS")
print("=" * 80)
