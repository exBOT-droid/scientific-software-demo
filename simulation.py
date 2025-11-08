# Enhanced simulation.py
def simulate_growth():
    population = float(input("Enter initial population: "))
    growth_rate = float(input("Enter growth rate (as a decimal): "))
    years = int(input("Enter number of years: "))
    
    for year in range(years):
        population += population * growth_rate
        print(f"Year {year + 1}: Population = {population:.2f}")

# Run the simulation
simulate_growth()