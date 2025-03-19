import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Set random seed for reproducibility
np.random.seed(42)

def generate_distributions(n_samples=1000):
    """Generate random samples from different distributions."""
    # Normal (Gaussian) distribution
    normal = np.random.normal(loc=0, scale=1, size=n_samples)
    
    # Uniform distribution
    uniform = np.random.uniform(low=-3, high=3, size=n_samples)
    
    # Exponential distribution
    exponential = np.random.exponential(scale=1, size=n_samples)
    
    # Log-normal distribution
    lognormal = np.random.lognormal(mean=0, sigma=0.5, size=n_samples)
    
    # Binomial distribution
    binomial = np.random.binomial(n=20, p=0.3, size=n_samples)
    
    return {
        "Normal": normal,
        "Uniform": uniform,
        "Exponential": exponential,
        "Log-normal": lognormal,
        "Binomial": binomial
    }

def visualize_distributions(distributions):
    """Create histograms for each distribution."""
    n_dists = len(distributions)
    fig, axes = plt.subplots(n_dists, 1, figsize=(10, 3*n_dists))
    
    for i, (name, data) in enumerate(distributions.items()):
        ax = axes[i]
        ax.hist(data, bins=30, alpha=0.7, density=True)
        ax.set_title(f"{name} Distribution")
        ax.set_ylabel("Density")
        
        # Add descriptive statistics
        mean = np.mean(data)
        median = np.median(data)
        std = np.std(data)
        ax.text(0.7, 0.7, f"Mean: {mean:.2f}\nMedian: {median:.2f}\nStd Dev: {std:.2f}", 
                transform=ax.transAxes, 
                bbox=dict(boxstyle="round", fc="white", alpha=0.7))
    
    plt.tight_layout()
    return fig

def main():
    print("🧪 Generating Data Distribution Examples 📊")
    print("="*50)
    
    # Generate distributions
    distributions = generate_distributions()
    
    # Display basic statistics for each distribution
    for name, data in distributions.items():
        print(f"\n{name} Distribution:")
        print(f"  - Mean: {np.mean(data):.4f}")
        print(f"  - Median: {np.median(data):.4f}")
        print(f"  - Std Dev: {np.std(data):.4f}")
        print(f"  - Min: {np.min(data):.4f}")
        print(f"  - Max: {np.max(data):.4f}")
    
    # Create visualization
    fig = visualize_distributions(distributions)
    
    # Save the figure to an image file
    print("\n📊 Saving distribution histogram to 'distributions.png'...")
    canvas = FigureCanvas(fig)
    fig.savefig("distributions.png")
    
    print("\n✨ Done! You can now examine the distributions.png file")
    print("This image shows histograms of different probability distributions")
    print("commonly used in data science and statistics.")

if __name__ == "__main__":
    main()
