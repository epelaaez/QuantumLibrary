# Quantum Library

<sub>By Emilio Peláez</sub>

This repository contains work I have done in quantum computing using the Qiskit library in Python. Most of it consists of notebooks going through an specific algorithm or protocol in quantum computation while trying to give the best description possible and linking to useful resources to get a more in-depth view of the topic discussed. I am relatively new to the field of quantum information and quantum computation (I started in summer of 2020), so the topics covered in this repo may not be very advanced as they mostly reflect my learning process and progress.

The main goal of this repo is to have a reliable library which I or anyone can access to learn or verify something about the topics covered. Therefore, anyone is welcomed to contribute to the project if they find a mistake, would like to add to an explanation, or simply thinks that something should be different.  

Some instructions to run this project locally and collaborate to it are included in the rest of this document in case someone wants to do so. 

## Set up
Once you clone the repository, you will need to create a new file called `config.py` (or change the name of the provided [`config_ex.py`](/config_ex.py) file) inside the `algorithms` folder, this is where you will store your IBM Quantum Experience API token. If you don't have an account yet, go to [IBM Quantum Experience](https://quantum-computing.ibm.com) to create one. Inside this file, just replace the following code `YOUR_KEY` with your actual key.
```python
IBM_KEY = "YOUR_KEY"
```

## Run on hardware
To run the circuits on real hardware, you will need to set up your IBM account as specified above. To run the circuit you desire in a real quantum computer, just uncomment the few lines of code that are above the code that runs the simulator. You will also need to load your IBM account, which relies on your `config.py` file being correctly written, to gain access to the hardware.

Note that not all circuits may be run in real hardware and some require modifications to run correctly. Those that require modifications to run correctly will make the necessary modifications when the function that builds the circuit gets the argument `hardware=True`, so you don't have to worry about modifying anything. However, I encourage you to check the code and the description of the circuit to understand the modifications made, why they are needed and how they work. The circuits that can't run in real hardware  or don't need any changes won't accept the optional argument `hardware`. 

**Note**: running a circuit on hardware can take time depending on the computers available and their queue. The `least_busy()` function is used to choose the least busy machine, but this doesn't guarantee that it will run immediately.

## Contributing
Anyone is welcome and encouraged to contribute to this project, whether you are an expert in the field or just getting started on it. To contribute, you can clone the repository in your local machine, make the changes you want to contribute in a separate branch, and then open a pull request describing the changes you made. The pull request will then be reviewed and discussed prior to merging. 
