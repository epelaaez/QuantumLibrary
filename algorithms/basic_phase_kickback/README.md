# Basic phase kickback
Phase kickback is a fundamental building block of larger quantum circuit. As you may imagine, this circuit by itself may not have a lot of practical uses, but when incorporated into a larger algorithm, it turns out to be very useful. If you want to get a deeper explanation, I recommend looking at this [answer in Quora](https://qr.ae/pNZ46i) by Pranav Gokhale. 

First, let's take a look at how the circuit we implemented looks like:

![circuit](https://user-images.githubusercontent.com/63567458/104107811-b7c05b00-52bf-11eb-8ce6-b49ed6de9258.jpg)

As you can see, the circuit implemented in this example is very **basic**, but it works as an introduction to the very important concept of phase kickback.

First, our top qubit goes through a Hadamard gate and the bottom qubit goes to a Pauli-X gate, giving us the following state:

<img src="https://user-images.githubusercontent.com/63567458/104455460-9903e200-55a7-11eb-89d5-cfee698d04df.png" height="70px">

Then, the qubits go through a controlled phase gate, with the control qubit being the top one and the target qubit the bottom one. The names **control** and **target** are misleading in this case, since the qubit that ends up changing is the **control** qubit. Remember that a controlled gate acts only when the control qubit is in state |1>, so the phase rotation is only applied in this case. When passing through this gate, the resulting state is the following:

<img src="https://user-images.githubusercontent.com/63567458/104456456-f8aebd00-55a8-11eb-8072-6ff4381a2df4.png" height="70px">

As you can see, the states are not entangled since we can write them as a tensor product of the two qubits and a relative phase was added to the **control** qubit instead of the **target** qubit. We can see this effect with the statevector simulation that Qiskit gives us, notice that the **control** qubit (qubit 0) has a phase rotation, while the **target** qubit is right in the |1> state without any rotation. 

![vector](https://user-images.githubusercontent.com/63567458/104107710-b04c8200-52be-11eb-9efa-97816d6c7121.jpg)

## Running on hardware
In this circuit, an option to run the circuit on hardware is not included. This is due to the fact that we use Qiskit's statevector simulation, which allows us see the quantum states (including its phases) without actually measuring the qubits. This is not possible using hardware, because we need to measure the qubit to get information about its state, but measuring will make the qubit go to one of the basis states. 
