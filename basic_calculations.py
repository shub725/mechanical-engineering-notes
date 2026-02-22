# Mechanical Engineering Basic Calculations

# Torque Calculation
def calculate_torque(force, radius):
    return force * radius

# Stress Calculation
def calculate_stress(force, area):
    return force / area

# Example usage
force = 100  # Newton
radius = 0.5  # Meter
area = 0.02  # m^2

print("Torque:", calculate_torque(force, radius), "Nm")
print("Stress:", calculate_stress(force, area), "Pa")
