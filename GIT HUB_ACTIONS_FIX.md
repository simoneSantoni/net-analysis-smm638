# GitHub Actions Build Fix

## Problem

GitHub Actions was failing with error:
```
'../../../data/soundcloud/output/users.csv' does not exist
```

The data files in `data/soundcloud/output/` are ignored by Git (`.gitignore`) and not available during CI builds.

## Solution Implemented

Added `execute: freeze: auto` to both Quarto notebooks to cache computational results:

### Files Updated

1. **website/weeks/week-5/soundcloud_eda.qmd**
2. **website/weeks/week-5/network_properties.qmd**
3. **website/weeks/week-5/main.qmd** - Added link to network_properties notebook

## How It Works

- `freeze: auto` tells Quarto to cache computational results in `_freeze/` directory
- When rendering locally, Quarto executes code and saves results
- When rendering on GitHub Actions, Quarto uses cached results instead of re-running code
- The `_freeze/` directory MUST be committed to Git

## Next Steps

### 1. Render Locally (Already Done)

```bash
cd website
quarto render weeks/week-5/soundcloud_eda.qmd
quarto render weeks/week-5/network_properties.qmd
```

### 2. Commit the Frozen Output

```bash
git add website/_freeze/weeks/week-5/
git add website/weeks/week-5/soundcloud_eda.qmd
git add website/weeks/week-5/network_properties.qmd
git add website/weeks/week-5/main.qmd
git commit -m "Add Week 5 network properties analysis with frozen output

- Add comprehensive network properties analysis (reciprocity & transitivity)
- Implement CUG tests for rigorous statistical testing
- Fix package conflicts between sna and igraph
- Add freeze:auto to prevent CI build errors
- Update week-5 main.qmd with new notebook link"
git push
```

### 3. Verify GitHub Actions

After pushing, GitHub Actions will:
1. Use the frozen output from `_freeze/` directory
2. Skip code execution (since freeze exists and is up-to-date)
3. Successfully build the site without needing data files

## Important Notes

### When to Re-render

You need to re-render locally and commit new frozen output when:
- You modify the `.qmd` code
- You want to update the analysis with new data
- The Quarto version changes significantly

### Checking Freeze Status

```bash
# Check if freeze directories exist
ls -la website/_freeze/weeks/week-5/

# Should show:
# - soundcloud_eda/
# - network_properties/
```

### If Freeze Doesn't Work

If GitHub Actions still fails:
1. Delete `_freeze/` directory
2. Re-render locally: `quarto render website/`
3. Commit the entire `_freeze/` directory
4. Push again

## Technical Details

### Package Dependencies

The network_properties notebook requires:
- `sna` - For CUG tests
- `network` - For network objects
- `intergraph` - For format conversion
- Standard packages: `igraph`, `tidyverse`, `gridExtra`

### Function Conflicts

- `sna` and `igraph` have overlapping function names
- Use `igraph::function()` prefix when needed (e.g., `igraph::degree()`, `igraph::transitivity()`)
- The notebook includes comments explaining these conflicts

### CUG Test Performance

- Each CUG test runs 1000 simulations
- Total render time: ~5-10 minutes
- This is why freezing is essential for CI/CD

## Files Modified

| File | Change |
|------|--------|
| `website/weeks/week-5/soundcloud_eda.qmd` | Added `execute: freeze: auto` |
| `website/weeks/week-5/network_properties.qmd` | Created new notebook with CUG tests, added `freeze: auto` |
| `website/weeks/week-5/main.qmd` | Added link to network_properties |
| `website/weeks/week-5/network_properties.qmd` | Fixed degree() conflict, fixed transitivity CUG function |

## Expected Outcome

✅ Local rendering works (uses data files)
✅ GitHub Actions works (uses frozen output)
✅ Website shows both notebooks with full analysis
✅ No need to commit 185MB of data files to Git
