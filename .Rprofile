# VSCode R Extension Configuration
# This file configures R to work properly with VSCode

# Set CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))

# Disable httpgd completely
options(
  vsc.use_httpgd = FALSE,
  vsc.plot = FALSE,
  httpgd.token = FALSE
)

# Configure graphics device for VSCode
if (interactive() && Sys.getenv("TERM_PROGRAM") == "vscode") {
  # Disable httpgd package if loaded
  if ("httpgd" %in% loadedNamespaces()) {
    try(unloadNamespace("httpgd"), silent = TRUE)
  }
  
  # Use standard R graphics device instead of httpgd
  options(device = function(...) {
    # Try to use the default device
    if (.Platform$OS.type == "windows") {
      windows(...)
    } else if (.Platform$OS.type == "unix") {
      if (capabilities("X11")) {
        X11(...)
      } else if (capabilities("aqua")) {
        quartz(...)
      } else {
        # Fallback to PNG for headless systems
        png("Rplot%03d.png", width = 800, height = 600)
      }
    }
  })
  
  # Override .vsc.browser function to prevent errors
  .vsc.browser <- function(...) {
    # Do nothing - just prevent the error
    invisible(NULL)
  }
  
  # Set plot dimensions
  options(
    width = 80,
    scipen = 999,
    digits = 4
  )
}

# Load commonly used packages silently
suppressPackageStartupMessages({
  if (require("tidyverse", quietly = TRUE)) {
    # Tidyverse loaded successfully
  }
})

# Custom prompt
options(prompt = "R> ", continue = "+  ")

# Enable command history
if (interactive()) {
  try(utils::loadhistory(".Rhistory"), silent = TRUE)
  .Last <- function() try(utils::savehistory(".Rhistory"), silent = TRUE)
}

# R attach
if (interactive() && Sys.getenv("RSTUDIO") == "") {
  source(file.path(Sys.getenv(if (.Platform$OS.type == "windows") "USERPROFILE" else "HOME"), ".vscode-R", "init.R"))
}
