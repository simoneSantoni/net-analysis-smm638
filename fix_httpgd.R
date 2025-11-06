# Script to fix httpgd issues in VSCode R extension
# Run this script if you're still getting httpgd errors

# Disable httpgd options
options(
  vsc.use_httpgd = FALSE,
  vsc.plot = FALSE,
  httpgd.token = FALSE,
  device = "png"
)

# Unload httpgd if it's loaded
if ("httpgd" %in% loadedNamespaces()) {
  cat("Unloading httpgd package...\n")
  try(unloadNamespace("httpgd"), silent = TRUE)
}

# Define a dummy .vsc.browser function to prevent errors
.vsc.browser <- function(...) {
  cat("VSCode browser function called - ignoring to prevent httpgd errors\n")
  invisible(NULL)
}

# Set up alternative plotting function
plot_to_file <- function(plot_expr, filename = "plot.png", width = 800, height = 600) {
  png(filename, width = width, height = height)
  eval(plot_expr)
  dev.off()
  cat("Plot saved to:", filename, "\n")
}

cat("httpgd workaround applied successfully!\n")
cat("Use plot_to_file() function for plots if needed.\n")
cat("Example: plot_to_file(plot(1:10), 'myplot.png')\n")