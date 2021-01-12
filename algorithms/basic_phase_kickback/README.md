# Basic phase kickback
Phase kickback is a fundamental building block of larger quantum circuit. As you may imagine, this circuit by itself may not have a lot of practical uses, but when incorporated into a larger algorithm, it turns out to be very useful. If you want to get a deeper explanation, I recommend looking at this [answer in Quora](https://qr.ae/pNZ46i) by Pranav Gokhale. 

First, let's take a look at how the circuit we implemented looks like:

![circuit](https://user-images.githubusercontent.com/63567458/104107811-b7c05b00-52bf-11eb-8ce6-b49ed6de9258.jpg)


As you can see, the circuit implemented in this example is very **basic**, but it works as an introduction to the very important concept of phase kickback.

**TODO: explain circuit**

Our resulting statevector is the following:
![vector](https://user-images.githubusercontent.com/63567458/104107710-b04c8200-52be-11eb-9efa-97816d6c7121.jpg)

## Running on hardware
In this circuit, an option to run the circuit on hardware is not included. This is due to the fact that we use Qiskit's statevector simulation, which allows us see the quantum states (including its phases) without actually measuring the qubits. This is not possible using hardware, because we need to measure the qubit to get information about its state, but measuring will make the qubit go to one of the basis states. 
