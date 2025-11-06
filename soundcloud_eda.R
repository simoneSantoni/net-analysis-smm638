library(tidyverse)
library(gridExtra)

# Configure graphics device
if (interactive()) {
  # Use default graphics device instead of httpgd
  options(device = "RStudioGD")
  if (!capabilities("RStudioGD")) {
    options(device = "X11")
  }
}

# Set theme for plots
theme_set(theme_minimal())

# 1. Load all CSV files
users <- read_csv("data/soundcloud/output/users.csv")
tracks <- read_csv("data/soundcloud/output/tracks.csv")
follows <- read_csv("data/soundcloud/output/follows.csv")
engagements <- read_csv("data/soundcloud/output/engagements.csv")
streaming_events <- read_csv("data/soundcloud/output/streaming_events.csv")
playlists <- read_csv("data/soundcloud/output/playlists.csv")

# Print separator function
print_section <- function(title) {
  cat("\n", paste(rep("=", 80), collapse=""), "\n")
  cat(title, "\n")
  cat(paste(rep("=", 80), collapse=""), "\n\n")
}

# ===== USERS DATA =====
print_section("USERS DATA EXPLORATION")

# Basic info
cat("Dimensions:", dim(users), "\n")
cat("Column names:", paste(names(users), collapse=", "), "\n\n")

# Data summary
cat("Summary statistics:\n")
print(summary(users))

# Missing values
cat("\nMissing values:\n")
users %>% 
  summarise_all(~sum(is.na(.))) %>% 
  pivot_longer(everything(), names_to = "column", values_to = "missing") %>% 
  filter(missing > 0) %>% 
  print()

# User statistics
cat("\nUser Statistics:\n")
users %>% 
  summarise(
    total_users = n(),
    avg_follower_count = mean(follower_count, na.rm = TRUE),
    median_follower_count = median(follower_count, na.rm = TRUE),
    avg_following_count = mean(following_count, na.rm = TRUE),
    median_following_count = median(following_count, na.rm = TRUE),
    avg_track_count = mean(track_count, na.rm = TRUE),
    median_track_count = median(track_count, na.rm = TRUE)
  ) %>% 
  print()

# User type distribution
cat("\nUser Type Distribution:\n")
users %>% 
  count(user_type, sort = TRUE) %>% 
  print()

# ===== TRACKS DATA =====
print_section("TRACKS DATA EXPLORATION")

# Basic info
cat("Dimensions:", dim(tracks), "\n")
cat("Column names:", paste(names(tracks), collapse=", "), "\n\n")

# Data summary
cat("Summary statistics:\n")
print(summary(tracks))

# Track statistics
cat("\nTrack Statistics:\n")
tracks %>% 
  summarise(
    total_tracks = n(),
    avg_duration = mean(duration_sec, na.rm = TRUE),
    median_duration = median(duration_sec, na.rm = TRUE),
    avg_play_count = mean(play_count, na.rm = TRUE),
    median_play_count = median(play_count, na.rm = TRUE),
    avg_like_count = mean(like_count, na.rm = TRUE),
    median_like_count = median(like_count, na.rm = TRUE)
  ) %>% 
  print()

# Genre distribution
cat("\nTop 10 Primary Genres:\n")
tracks %>% 
  count(genre_primary, sort = TRUE) %>% 
  head(10) %>% 
  print()

# ===== FOLLOWS DATA =====
print_section("FOLLOWS DATA EXPLORATION")

# Basic info
cat("Dimensions:", dim(follows), "\n")
cat("Column names:", paste(names(follows), collapse=", "), "\n\n")

# Follow network statistics
cat("\nFollow Network Statistics:\n")
follows %>% 
  summarise(
    total_follows = n(),
    unique_followers = n_distinct(follower_id),
    unique_followed = n_distinct(followee_id)
  ) %>% 
  print()

# Top followed users
cat("\nTop 10 Most Followed Users:\n")
follows %>% 
  count(followee_id, sort = TRUE) %>% 
  head(10) %>% 
  left_join(users, by = c("followee_id" = "user_id")) %>% 
  select(followee_id, username, n) %>% 
  print()

# ===== ENGAGEMENTS DATA =====
print_section("ENGAGEMENTS DATA EXPLORATION")

# Basic info
cat("Dimensions:", dim(engagements), "\n")
cat("Column names:", paste(names(engagements), collapse=", "), "\n\n")

# Engagement type distribution
cat("\nEngagement Type Distribution:\n")
engagements %>% 
  count(engagement_type, sort = TRUE) %>% 
  print()

# Engagement statistics
cat("\nEngagement Statistics:\n")
engagements %>% 
  summarise(
    total_engagements = n(),
    unique_users = n_distinct(user_id),
    unique_tracks = n_distinct(track_id),
    avg_engagements_per_user = n() / n_distinct(user_id)
  ) %>% 
  print()

# ===== STREAMING EVENTS DATA =====
print_section("STREAMING EVENTS DATA EXPLORATION")

# Basic info
cat("Dimensions:", dim(streaming_events), "\n")
cat("Column names:", paste(names(streaming_events), collapse=", "), "\n\n")

# Streaming statistics
cat("\nStreaming Statistics:\n")
streaming_events %>% 
  summarise(
    total_events = n(),
    unique_users = n_distinct(user_id),
    unique_tracks = n_distinct(track_id),
    avg_duration = mean(duration_played_sec, na.rm = TRUE),
    median_duration = median(duration_played_sec, na.rm = TRUE),
    avg_completion_rate = mean(completion_rate, na.rm = TRUE)
  ) %>% 
  print()

# Source distribution
cat("\nStreaming Source Distribution:\n")
streaming_events %>% 
  count(source, sort = TRUE) %>% 
  print()

# ===== PLAYLISTS DATA =====
print_section("PLAYLISTS DATA EXPLORATION")

# Basic info
cat("Dimensions:", dim(playlists), "\n")
cat("Column names:", paste(names(playlists), collapse=", "), "\n\n")

# Playlist statistics
cat("\nPlaylist Statistics:\n")
playlists %>% 
  mutate(track_count = str_count(track_ids, ",") + 1) %>%
  summarise(
    total_playlists = n(),
    unique_creators = n_distinct(creator_id),
    avg_track_count = mean(track_count, na.rm = TRUE),
    median_track_count = median(track_count, na.rm = TRUE),
    avg_follower_count = mean(follower_count, na.rm = TRUE),
    median_follower_count = median(follower_count, na.rm = TRUE)
  ) %>% 
  print()

# ===== VISUALIZATIONS =====
print_section("CREATING VISUALIZATIONS")

# Create output directory for plots
dir.create("soundcloud_eda_plots", showWarnings = FALSE)

# 1. User follower distribution
p1 <- users %>% 
  filter(follower_count < quantile(follower_count, 0.99, na.rm = TRUE)) %>% 
  ggplot(aes(x = follower_count)) +
  geom_histogram(fill = "steelblue", bins = 50) +
  scale_x_log10() +
  labs(title = "Distribution of Follower Counts (log scale)",
       x = "Follower Count (log10)", y = "Number of Users")

ggsave("soundcloud_eda_plots/follower_distribution.png", p1, width = 10, height = 6)

# 2. Track playback distribution
p2 <- tracks %>% 
  filter(play_count > 0) %>% 
  ggplot(aes(x = play_count)) +
  geom_histogram(fill = "coral", bins = 50) +
  scale_x_log10() +
  labs(title = "Distribution of Track Play Counts (log scale)",
       x = "Play Count (log10)", y = "Number of Tracks")

ggsave("soundcloud_eda_plots/playback_distribution.png", p2, width = 10, height = 6)

# 3. Engagement types
p3 <- engagements %>% 
  count(engagement_type) %>% 
  ggplot(aes(x = reorder(engagement_type, n), y = n)) +
  geom_col(fill = "darkgreen") +
  coord_flip() +
  labs(title = "Distribution of Engagement Types",
       x = "Engagement Type", y = "Count") +
  scale_y_continuous(labels = scales::comma)

ggsave("soundcloud_eda_plots/engagement_types.png", p3, width = 10, height = 6)

# 4. User type distribution
p4 <- users %>% 
  count(user_type, sort = TRUE) %>% 
  ggplot(aes(x = reorder(user_type, n), y = n)) +
  geom_col(fill = "purple") +
  coord_flip() +
  labs(title = "User Type Distribution",
       x = "User Type", y = "Number of Users")

ggsave("soundcloud_eda_plots/user_types.png", p4, width = 10, height = 6)

# 5. Genre distribution
p5 <- tracks %>% 
  filter(!is.na(genre_primary), genre_primary != "") %>% 
  count(genre_primary, sort = TRUE) %>% 
  head(20) %>% 
  ggplot(aes(x = reorder(genre_primary, n), y = n)) +
  geom_col(fill = "orange") +
  coord_flip() +
  labs(title = "Top 20 Primary Music Genres",
       x = "Genre", y = "Number of Tracks")

ggsave("soundcloud_eda_plots/top_genres.png", p5, width = 10, height = 8)

# 6. Streaming source distribution
p6 <- streaming_events %>% 
  count(source) %>% 
  ggplot(aes(x = reorder(source, n), y = n)) +
  geom_col(fill = "navy") +
  coord_flip() +
  labs(title = "Streaming Source Distribution",
       x = "Source Type", y = "Number of Streams") +
  scale_y_continuous(labels = scales::comma)

ggsave("soundcloud_eda_plots/streaming_sources.png", p6, width = 10, height = 6)

# Combined overview plot
combined <- grid.arrange(p1, p2, p3, p6, nrow = 2, ncol = 2)
ggsave("soundcloud_eda_plots/combined_overview.png", combined, width = 16, height = 12)

cat("\nAll plots saved to 'soundcloud_eda_plots/' directory\n")

# ===== NETWORK ANALYSIS PREVIEW =====
print_section("NETWORK ANALYSIS PREVIEW")

# Degree distribution in follow network
degree_dist <- follows %>% 
  count(follower_id, name = "out_degree") %>% 
  full_join(
    follows %>% count(followee_id, name = "in_degree"),
    by = c("follower_id" = "followee_id")
  ) %>% 
  replace_na(list(out_degree = 0, in_degree = 0))

cat("\nDegree Distribution Summary:\n")
degree_dist %>% 
  summarise(
    avg_out_degree = mean(out_degree),
    median_out_degree = median(out_degree),
    max_out_degree = max(out_degree),
    avg_in_degree = mean(in_degree, na.rm = TRUE),
    median_in_degree = median(in_degree, na.rm = TRUE),
    max_in_degree = max(in_degree, na.rm = TRUE)
  ) %>% 
  print()

# User-track bipartite network preview
cat("\nUser-Track Interaction Summary:\n")
user_track_interactions <- bind_rows(
  engagements %>% select(user_id, track_id) %>% mutate(type = "engagement"),
  streaming_events %>% select(user_id, track_id) %>% mutate(type = "stream")
)

user_track_interactions %>% 
  group_by(type) %>% 
  summarise(
    total_interactions = n(),
    unique_users = n_distinct(user_id),
    unique_tracks = n_distinct(track_id),
    avg_tracks_per_user = n_distinct(track_id) / n_distinct(user_id)
  ) %>% 
  print()

cat("\nEDA Complete! Check 'soundcloud_eda_plots/' directory for visualizations.\n")