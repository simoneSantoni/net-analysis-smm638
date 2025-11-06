library(tidyverse)

# Load users data
users <- read_csv("data/soundcloud/output/users.csv", show_col_types = FALSE)

# Test 1: Basic summary
cat("Test 1: Basic summary\n")
print(summary(users))

# Test 2: Missing values check
cat("\nTest 2: Missing values check\n")
missing_check <- users %>% 
  summarise_all(~sum(is.na(.)))
print(missing_check)

# Test 3: Convert to long format
cat("\nTest 3: Convert to long format\n")
missing_long <- missing_check %>% 
  pivot_longer(everything(), names_to = "column", values_to = "missing")
print(missing_long)

# Test 4: Check data types
cat("\nTest 4: Data types of missing values\n")
print(str(missing_long))

# Test 5: Filter attempt
cat("\nTest 5: Filter numeric values\n")
tryCatch({
  filtered <- missing_long %>% 
    filter(missing > 0)
  print(filtered)
}, error = function(e) {
  cat("Error in filter:", e$message, "\n")
  cat("Class of 'missing' column:", class(missing_long$missing), "\n")
})

# Test 6: User statistics
cat("\nTest 6: User statistics\n")
user_stats <- users %>% 
  summarise(
    total_users = n(),
    avg_follower_count = mean(follower_count, na.rm = TRUE),
    median_follower_count = median(follower_count, na.rm = TRUE),
    avg_following_count = mean(following_count, na.rm = TRUE),
    median_following_count = median(following_count, na.rm = TRUE),
    avg_track_count = mean(track_count, na.rm = TRUE),
    median_track_count = median(track_count, na.rm = TRUE)
  )
print(user_stats)