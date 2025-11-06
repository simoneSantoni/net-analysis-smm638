# Test R integration in VSCode
# This will test if the R extension is properly configured

# Test basic R functionality
print("R is working in VSCode!")

# Test plot functionality
x <- 1:10
y <- x^2
plot(x, y, main = "Test Plot", xlab = "X", ylab = "Y")

# Test data frame display
df <- data.frame(
  x = 1:5,
  y = letters[1:5],
  z = rnorm(5)
)
print(df)

# The VSCode R extension should now work properly
# You can:
# 1. Run code with Ctrl+Enter (line) or Ctrl+Shift+Enter (selection)
# 2. View plots in the plot viewer
# 3. View variables in the workspace viewer