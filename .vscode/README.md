# VSCode R Configuration

This directory contains VSCode workspace settings for R development.

## Setup Requirements

### 1. Required R Packages

The following R packages must be installed for full VSCode R integration:

```r
install.packages(c("languageserver", "jsonlite"))
```

For plot viewing, install `httpgd` via conda:

```bash
conda activate smm638  # or smm635
conda install -c conda-forge r-httpgd
```

### 2. VSCode Extensions

Install the R extension for Visual Studio Code:
- **Extension ID**: `REditorSupport.r`
- Install via: Extensions → Search for "R"

### 3. User .Rprofile Configuration

The `.Rprofile` file in your home directory (`~/.Rprofile`) has been configured with:

- VSCode-specific options for plot viewing, browser, and viewer integration
- httpgd graphics device for interactive plot display
- Variable viewer enablement

## Features Enabled

### Plot Viewing
- **httpgd**: Modern graphics device that displays plots in VSCode's Plot pane
- Plots appear automatically when created
- Interactive navigation through plot history

### Variable Viewer
- Global environment variables appear in the "Variables" pane
- Shows object sizes and types
- Click variables to view details

### Code Intelligence
- **Language Server Protocol (LSP)**: Code completion, diagnostics, and hover information
- Real-time syntax checking
- Function signatures and documentation on hover

### Interactive Terminal
- R terminal with bracketed paste support
- Session watching for automatic variable updates
- Always uses the active terminal for consistency

## Troubleshooting

### Plots not displaying
1. Verify httpgd is installed: `library(httpgd)` in R
2. Check VSCode settings: `r.plot.useHttpgd` should be `true`
3. Restart R session: `Ctrl+Shift+F5` or restart terminal

### Variables not showing
1. Ensure you're using an interactive R session
2. Check `r.sessionWatcher` is enabled in settings
3. Try manually refreshing: Click the refresh icon in Variables pane

### Language server not working
1. Verify languageserver package is installed
2. Check `r.lsp.enabled` is `true`
3. Restart VSCode: `Ctrl+Shift+P` → "Developer: Reload Window"

## Conda Environment Integration

This project uses conda environments:
- **smm638**: Main environment for this course
- **smm635**: Alternative environment (if applicable)

Activate before starting R:
```bash
conda activate smm638
```

## Additional Resources

- [VSCode R Extension Documentation](https://github.com/REditorSupport/vscode-R)
- [httpgd Package](https://github.com/nx10/httpgd)
- [languageserver Package](https://github.com/REditorSupport/languageserver)