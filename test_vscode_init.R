# Test VSCode R extension initialization
cat("Testing VSCode R initialization...\n")
cat("Interactive session:", interactive(), "\n")
cat("TERM_PROGRAM:", Sys.getenv("TERM_PROGRAM"), "\n")
cat("RSTUDIO:", Sys.getenv("RSTUDIO"), "\n")

# Try to manually source the VSCode initialization
if (interactive() && Sys.getenv("TERM_PROGRAM") == "vscode") {
    init_file <- file.path(
        path.expand("~"), 
        ".vscode-server/extensions/reditorsupport.r-2.8.6/R/session/init.R"
    )
    if (file.exists(init_file)) {
        cat("Sourcing VSCode init file...\n")
        source(init_file)
        cat("VSCode functions available:\n")
        print(ls(pattern = "vsc"))
    } else {
        cat("Init file not found at:", init_file, "\n")
    }
}