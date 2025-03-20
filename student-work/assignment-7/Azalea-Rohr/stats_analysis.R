library(ggplot2)
set.seed(42)

data <- rnorm(100, mean = 50, sd = 10)
summary_stats <- summary(data)

cat("Summary Statistics:\n")
print(summary_stats)
t_test_result <- t.test(data, mu = 50)

cat("\nT-test Results:\n")
print(t_test_result)

# Create and save a histogram
histogram_plot <- ggplot(data.frame(data), aes(x = data)) +
  geom_histogram(binwidth = 5, color = "black", fill = "blue", alpha = 0.7) +
  labs(title = "Histogram of Generated Data", x = "Values", y = "Frequency") +
  theme_minimal()

# Save the plot
ggsave("histogram.png", plot = histogram_plot)

cat("\nHistogram saved as 'histogram.png'.\n")

