# Quantum Library
This project aims to be a quantum library containing various circuits and algorithms commonly used in quantum computing. These will be implemented using Qiskit, one of many tools out there to write quantum algorithms but, in my opinion, the easier one to understand. Each circuit will be accompanied with a brief description of it including how it works and how it is used in larger-scale circuits or algorithms. 

The main goal of this project is to build a large collection of quantum circuits, from the simplest ones to more complicated ones. To achieve this, contributions are very welcome and encouraged, see more in [Contributing](#contributing)

The images contained in [output](/output) are examples of the images generated with [Qiskit](https://qiskit.org). The examples contained there are from the [teleportation](/algorithms/teleportation/teleportation.py) circuit.

## Set up
If you want to have access to all the algorithms implemented, clone the repository into your local machine and treat the `algorithms` module like any other one. Since the algorithms implemented in this module are mostly to experiment rather than practical uses, it may be best to just use the `main.py` file contained within the repository to call the different circuits (functions).

Once you clone the repository, you will need to create a new file called `config.py` (or change the name of the provided [`config_ex.py`](/config_ex.py) file), this is where you will store your IBM Quantum Experience API token. If you don't have an account yet, go to [IBM Quantum Experience](https://quantum-computing.ibm.com) to create one. Inside this file, just replace the following code `YOUR_KEY` with your actual key.
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

## Run on hardware
To run the circuits on real hardware, you will need to set up your IBM account as specified above. To run the circuit you desire in a real quantum computer, just call the function as you normally would but set the optional argument `hardware` to `True`. For example, to run the bell state circuit in real hardware, use the following code:
```python
create_bell_state(hardware=True)
```

You will also need to call the function `loadIBM()`, which relies on the your `config.py` file, beforehand to set up your IBM account correctly and gain access to the hardware. It is not necessary to call this function if you're not going to be using IBM's hardware to run the circuits, so you may remove it to increase the speed of the program. 

Note that not all circuits may be run in real hardware and some require modifications to run correctly. Those that require modifications to run correctly will make the necessary modifications when `hardware=True`, so you don't have to worry about modifying anything. However, I encourage you to check the code and the description of the circuit to understand the modifications made, why they are needed and how they work. The circuits that can't run in real hardware won't accept the optional argument `hardware`. Again, I encourage you to check the circuit's description to understand why they can't run in real hardware. 

**Note**: running a circuit on hardware can take time depending on the computers available and their queue. The circuits are programmed to choose the least busy machine, but this doesn't guarantee that it will run immediately.

## Contributing
Anyone is welcome and encouraged to contribute to this project, whether you are an expert in the field or just getting started on it. To contribute, you can clone the repository in your local machine, make the changes you want to contribute in a separate branch, and then open a pull request describing the changes you made. The pull request will then be reviewed and discussed prior to merging. 
