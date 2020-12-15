# Quantum Circuits
This repository contains implementations of important quantum circuits used in quantum computing using Qiskit; along with a brief description and explanation for each one of them. I will be adding circuits while I learn them, so the implementations or descriptions may not be completely correct at all times. But I will make sure to correct anything as soon as I notice it. 

The images contained in [output](/output) are examples of the images generated with [Qiskit](https://qiskit.org). The examples contained there are from the [teleportation](/algorithms/teleportation/teleportation.py) circuit.

## Set up
If you want to have access to all the algorithms implemented, clone the repository into your local machine and treat the `algorithms` module like any other one. Since the algorithms implemented in this module are mostly to experiment rather than practical uses, it may be best to just use the `main.py` file contained within the repository to call the different circuits (functions).

Once you clone the repository, you will need to create a new file called `config.py`, this is where you will store your IBM Quantum Experience API token. If you don't have an account yet, go to [IBM Quantum Experience](https://quantum-computing.ibm.com) to create one. Inside this file, just paste the following code replacing `YOUR_KEY` with your actual key.
```python
ibm_key = "YOUR_KEY"
```

If you want to run a certain circuit without downloading the whole `algorithms` module, make sure to include these imports at the top of your file instead of the single import given.
```python
from os.path import join
from qiskit import *
from qiskit.visualization import plot_histogram, circuit_drawer, plot_bloch_multivector
```
