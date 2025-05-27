import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

# Load the data
file_path = "star_data.csv"
data = pd.read_csv(file_path)

x = data['x'].values
y = data['y'].values
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

polar_data = pd.DataFrame({'theta': theta, 'r': r, 'x': x, 'y': y})
polar_data.sort_values('theta', inplace=True)

n_segments = 5
segment_bounds = np.linspace(-np.pi, np.pi, n_segments + 1)

functions = []
for i in range(n_segments):
    lower = segment_bounds[i]
    upper = segment_bounds[i + 1]
    
    segment = polar_data[(polar_data['theta'] >= lower) & (polar_data['theta'] < upper)]
    if len(segment) < 5:
        continue
    
    # Fit a 4th-degree polynomial: r = f(theta)
    p = Polynomial.fit(segment['theta'], segment['r'], deg=4)
    coeffs = p.convert().coef  # convert to standard basis
    
    functions.append({
        'bounds': (lower, upper),
        'coefficients': coeffs.tolist()
    })

for i, f in enumerate(functions):
    lower, upper = f['bounds']
    coeffs = f['coefficients']
    print(f"Function {i+1} (for θ in [{lower:.3f}, {upper:.3f}]):")
    terms = [f"{c:.2f}θ^{i}" if i > 0 else f"{c:.2f}" for i, c in enumerate(coeffs)]
    print("r =", " + ".join(terms))
    print()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, polar=True)
ax.scatter(theta, r, s=10, label='Original Data', alpha=0.5)

theta_fit = np.linspace(-np.pi, np.pi, 1000)

for f in functions:
    lower, upper = f['bounds']
    coeffs = f['coefficients']
    
    segment_theta = theta_fit[(theta_fit >= lower) & (theta_fit < upper)]
    
    segment_r = sum(c * segment_theta**i for i, c in enumerate(coeffs))
    
    ax.plot(segment_theta, segment_r, linewidth=2)

ax.set_title("Star Shape with Piecewise Polar Polynomial Fits", fontsize=14)
ax.legend()
plt.show()
