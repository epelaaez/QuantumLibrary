# Quantum Library
This repository contains work I have done in quantum computing using the Qiskit library in Python. Most of it consists of notebooks going through an specific algorithm or protocol in quantum computation while trying to give the best description possible and linking to useful resources to get a more in-depth view of the topic discussed. I am relatively new to the field of quantum information and quantum computation (I started in summer of 2020), so the topics covered in this repo may not be very advanced as they mostly reflect my learning process and progress.

The main goal of this repo is to have a reliable library which I or anyone can access to learn or verify something about the topics covered. Therefore, anyone is welcomed to contribute to the project if they find a mistake, would like to add to an explanation, or simply thinks that something should be different.  

Some instructions to run this project locally and collaborate to it are included in the rest of this document in case someone wants to do so. 

## Set up
Once you clone the repository, you will need to create a new file called `config.py` (or change the name of the provided [`config_ex.py`](/config_ex.py) file) inside the `algorithms` folder, this is where you will store your IBM Quantum Experience API token. If you don't have an account yet, go to [IBM Quantum Experience](https://quantum-computing.ibm.com) to create one. Inside this file, just replace the following code `YOUR_KEY` with your actual key.
```python
IBM_KEY = "YOUR_KEY"
```

If you want to run a certain circuit without cloning the repository, copy the function that builds your desired circuit and make sure to include these imports at the top of your file instead of the single import given (since this import imports all libraries and functions from `_Functions.ipynb`).
```python
from qiskit import *
from qiskit.visualization import plot_histogram, circuit_drawer, plot_bloch_multivector
```
Imports from `qiskit.visualization` may vary depending on the circuit, so be sure to import only the neccesary ones. You may also need to change the code a little bit since I frequently use imported functions from `_Functions.ipynb`. However, these are not too complicated and I only use them to not write the same thing over and over. 

## Run on hardware
To run the circuits on real hardware, you will need to set up your IBM account as specified above. To run the circuit you desire in a real quantum computer, just call the function as you normally would but set the optional argument `hardware` to `True`.
```python
run(circ, hardware=True)
```

You will also need to call the function `loadIBM()`, which relies on the your `config.py` file, beforehand to set up your IBM account correctly and gain access to the hardware. It is not necessary to call this function if you're not going to be using IBM's hardware to run the circuits, so you may remove it to increase the speed of the program. It is recommended to run this function on `_Functions.ipynb` before opening the other notebooks, this way the information gets imported.

Note that not all circuits may be run in real hardware and some require modifications to run correctly. Those that require modifications to run correctly will make the necessary modifications when the function that builds the circuit gets the argument `hardware=True`, so you don't have to worry about modifying anything. However, I encourage you to check the code and the description of the circuit to understand the modifications made, why they are needed and how they work. The circuits that can't run in real hardware  or don't need any changes won't accept the optional argument `hardware` (you need to pass it to `run()`, though). 

**Note**: running a circuit on hardware can take time depending on the computers available and their queue. The `run()` function is programmed to choose the least busy machine, but this doesn't guarantee that it will run immediately.

## Contributing
Anyone is welcome and encouraged to contribute to this project, whether you are an expert in the field or just getting started on it. To contribute, you can clone the repository in your local machine, make the changes you want to contribute in a separate branch, and then open a pull request describing the changes you made. The pull request will then be reviewed and discussed prior to merging. 

There is a previous version of this project, which has some unfinished circuits and descriptions, therefore I don't recommend it. However, you can find it [here](https://github.com/epelaaez/QuantumLibrary/tree/master/_old).
