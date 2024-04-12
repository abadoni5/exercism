"""
Approach:
- The problem involves optimizing the total cost of purchasing books in bundles, considering different bundle sizes and discounts.
- The code implements a solution using a greedy approach, initially aiming to create bundles with the maximum size possible.
- However, there's a special case where having two bundles of four books is cheaper than bundles of three and five, making the greedy solution less effective.
- To address this, after applying the greedy solution, the code adjusts any (5, 3) bundle pairs to (4, 4) bundles to optimize the cost.
- Here's how the algorithm works:
    1. Count the number of each book title in the basket using Counter.
    2. Initialize a defaultdict to track the number of bundles by size.
    3. While there are still books in the basket:
        - Determine the size of the current bundle (number of distinct titles).
        - Update the bundle count for the current size.
        - Remove the titles of the current bundle from the basket.
    4. Identify the number of fixes needed to adjust (5, 3) bundle pairs to (4, 4) bundles.
    5. Adjust the bundle counts accordingly: decrease counts for 5-bundles and 3-bundles and increase counts for 4-bundles.
    6. Calculate the total cost by summing the cost of each bundle size multiplied by the number of bundles and the book price, considering discounted rates for each bundle size.
"""
from collections import Counter, defaultdict

BUNDLE_RATES = [1.0, 1.0, 0.95, 0.90, 0.80, 0.75]

def total(basket):
    num_bundles_by_size = defaultdict(int)
    title_counts = Counter(basket)
    while title_counts:
        titles = title_counts.keys()
        num_bundles_by_size[len(titles)] += 1
        title_counts.subtract(titles)
        title_counts += Counter()
    
    fixes = min(num_bundles_by_size[5], num_bundles_by_size[3])
    num_bundles_by_size[5] -= fixes
    num_bundles_by_size[3] -= fixes
    num_bundles_by_size[4] += 2 * fixes
    
    return sum(
        num_bundles * bundle_size * 800 * BUNDLE_RATES[bundle_size]
        for (bundle_size, num_bundles) in num_bundles_by_size.items()
    )