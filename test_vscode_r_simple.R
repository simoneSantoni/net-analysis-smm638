# Simple test to verify VSCode R integration works
print("Testing VSCode R integration")

# Test basic operations
x <- 1:5
print(x)

# Test data frame creation
df <- data.frame(a = 1:3, b = letters[1:3])
print(df)

# Test simple plot
plot(1:10, (1:10)^2, main = "Simple Test Plot")