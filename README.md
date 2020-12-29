# Quantum Circuits
This repository contains implementations of important quantum circuits used in quantum computing using Qiskit; along with a brief description and explanation for each one of them. I will be adding circuits while I learn them, so the implementations or descriptions may not be completely correct at all times. But I will make sure to correct anything as soon as I notice it. 

The main goal of this project is to build a large collection of quantum circuits, from the simplest ones to more complicated ones. To achieve this, contributions are very welcome and encouraged, see more in [Contributing](#contributing)

The images contained in [output](/output) are examples of the images generated with [Qiskit](https://qiskit.org). The examples contained there are from the [teleportation](/algorithms/teleportation/teleportation.py) circuit.

## Set up
If you want to have access to all the algorithms implemented, clone the repository into your local machine and treat the `algorithms` module like any other one. Since the algorithms implemented in this module are mostly to experiment rather than practical uses, it may be best to just use the `main.py` file contained within the repository to call the different circuits (functions).

Once you clone the repository, you will need to create a new file called `config.py`, this is where you will store your IBM Quantum Experience API token. If you don't have an account yet, go to [IBM Quantum Experience](https://quantum-computing.ibm.com) to create one. Inside this file, just paste the following code replacing `YOUR_KEY` with your actual key.
```python
IBM_KEY = "YOUR_KEY"
```

You will also need to setup the path in which you want the output images to be stored. To do this, go into the `__init__.py` file inside the `algorithms` module (folder) and change the `IMG_PATH` variable to your desired path. Here is the default value. 
```python
IMG_PATH = 'output_images'
```

If you want to run a certain circuit without downloading the whole `algorithms` module, make sure to include these imports at the top of your file instead of the single import given.
```python
from os.path import join
from qiskit import *
from qiskit.visualization import plot_histogram, circuit_drawer, plot_bloch_multivector
```
Imports from `qiskit.visualization` may vary depending on the circuit, so be sure to import only the neccesary ones.

## Contributing
Anyone is welcome and encouraged to contribute to this project, whether you are an expert in the field or just getting started on it. To contribute, you can clone the repository in your local machine, make the changes you want to contribute in a separate branch, and then open a pull request describing the changes you made. The pull request will then be reviewed and discussed prior to merging. 
