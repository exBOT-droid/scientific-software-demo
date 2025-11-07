# simulation.py
def simulate_growth(population, growth_rate, years):
    for year in range(years):
        population += population * growth_rate
        print(f"Year {year + 1}: Population = {population:.2f}")

# Test the function with a population of 1000, growth rate of 5%, over 10 years
simulate_growth(1000, 0.05, 10)