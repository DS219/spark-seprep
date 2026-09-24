# Eamon Woodruff
I'm Eamon and my favorite programming language is Python because it's intuitive to learn and works well with solidifying statistics and linear algebra concepts I've learned in other classes. 

## Example Code

```
def one_sample_mean(table, label, sample_size):
    new_sample = table.sample(sample_size, with_replacement=True)
    new_sample_mean = np.mean(new_sample.column(label))
    return new_sample_mean

def simulate_sample_mean(table, label, sample_size, repetitions):
    
    means = make_array()

    for i in np.arange(repetitions):
        new_sample_mean = one_sample_mean(table,label,sample_size)
        means = np.append(means, new_sample_mean)

    sample_means = Table().with_column('Sample Means', means)
    
    # Display empirical histogram and print all relevant quantities
    sample_means.hist(bins=20)
    plots.xlabel('Sample Means')
    plots.title('Sample Size {sample_size}; {repetitions} Resamples'.format(sample_size=sample_size, repetitions=repetitions))
    print("Sample size: ", sample_size)
    print("Population mean:", np.mean(table.column(label)).round(2))
    print("Average of sample means: ", np.mean(means).round(2))
    print("Population SD:", np.std(table.column(label)).round(2))
    print("SD of sample means:", np.std(means).round(2))
    return np.std(means)
```

### Code Explanation
The code above generates the empirical distribution of random sample means. It samples (with replacement) from a dataset in a table and generates a distribution by calculating the mean of each generated sample and adding it to an array. 