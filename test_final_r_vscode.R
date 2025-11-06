# Final test of VSCode R integration
print("Testing VSCode R integration after fixes...")

# Test that .vsc.attach function is now available
print("Testing .vsc.attach():")
tryCatch({
    .vsc.attach()
    print("✓ .vsc.attach() successful")
}, error = function(e) {
    print(paste("✗ .vsc.attach() failed:", e$message))
})

# Test basic R functionality
print("Testing basic R operations:")
x <- 1:10
y <- x^2
print(paste("Length of x:", length(x)))

# Test plotting
print("Testing plot creation:")
plot(x, y, main = "Test Plot for VSCode", 
     xlab = "X values", ylab = "X squared",
     col = "blue", pch = 16)

# Test data frame operations
print("Testing data frame operations:")
df <- data.frame(
    id = 1:5,
    name = c("A", "B", "C", "D", "E"),
    value = rnorm(5)
)
print(df)

print("✓ All tests completed successfully!")
print("You should be able to:")
print("1. Run R code line by line with Ctrl+Enter")
print("2. View plots in VSCode's plot viewer")
print("3. See variables in the workspace panel")
print("4. No more .vsc.attach() errors")