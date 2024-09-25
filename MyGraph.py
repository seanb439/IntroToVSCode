import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

print("Hello there!")

print("Hi again!")

#To install virtual environment in terminal:
# Create Virtual Environment
# py -3 -m venv myvenv (or whatever you want to call it)

# Activate Virtual Environment
# \myvenv\Scripts\activate (tab to autocomplete)

#Install the third party libraries
# Pip3 install matplotlib 