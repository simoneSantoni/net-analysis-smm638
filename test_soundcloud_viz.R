# Test script to verify SoundCloud data loading and visualization
# Run this from the repository root

# Load required libraries
library(tidyverse)

# Set data path (from repository root)
data_path <- "data/soundcloud/output/"

# Load data
cat("Loading data...\n")
users <- read_csv(paste0(data_path, "users.csv"), show_col_types = FALSE)
tracks <- read_csv(paste0(data_path, "tracks.csv"), show_col_types = FALSE)

# Verify columns exist
cat("\nUsers columns:\n")
print(colnames(users))

cat("\nTracks columns:\n")
print(colnames(tracks))

# Test the visualizations that were failing

# 1. Test follower_count visualization
cat("\n--- Testing follower count visualization ---\n")
if ("follower_count" %in% colnames(users)) {
  cat("✓ follower_count column found\n")

  users %>%
    filter(follower_count < quantile(follower_count, 0.99)) %>%
    ggplot(aes(x = follower_count + 1)) +
    geom_histogram(fill = "steelblue", bins = 50, alpha = 0.8) +
    scale_x_log10() +
    labs(
      title = "Distribution of Follower Counts",
      x = "Follower Count + 1 (log10 scale)",
      y = "Number of Users"
    )

  cat("✓ Follower count plot created successfully\n")
} else {
  cat("✗ follower_count column NOT found\n")
}

# 2. Test play_count visualization
cat("\n--- Testing play count visualization ---\n")
if ("play_count" %in% colnames(tracks)) {
  cat("✓ play_count column found\n")

  tracks %>%
    filter(play_count > 0) %>%
    ggplot(aes(x = play_count)) +
    geom_histogram(fill = "coral", bins = 50, alpha = 0.8) +
    scale_x_log10() +
    labs(
      title = "Distribution of Track Play Counts",
      x = "Play Count (log10 scale)",
      y = "Number of Tracks"
    )

  cat("✓ Play count plot created successfully\n")
} else {
  cat("✗ play_count column NOT found\n")
}

cat("\n--- All tests completed ---\n")