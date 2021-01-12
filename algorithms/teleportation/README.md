# Teleportation Protocol
The quantum teleportation protocol is a fundamental part of many quantum algorithms. It enables you to transfer the state of one qubit to another qubit instantly. An important distinction to make is that teleportation in this context refers to the transfer of information rather than matter, since the qubits stay in the same place, but the state is transferred.

This protocol is useful to overcome the difficulties imposed by the [no-cloning theorem](https://en.wikipedia.org/wiki/No-cloning_theorem), which tells us that it is not possible to create an exact copy of a quantum state. Which means we cannot copy the state of one qubit into another, but we can teleport it. In fact, most uses of the teleportation protocol are to transfer the state of a qubit into another within a single QPU rather than across large distances like most sci-fi movies portray it. 

The circuit is composed the following way:
![circuit](https://user-images.githubusercontent.com/63567458/102338421-1e3dac00-3f94-11eb-8673-1086ce5c8ab2.jpg)

The gates before the first barrier entangle two qubits, one that the sender will use and one that the receiver will use. The qubit that the receiver will use will eventually be in the state that the sender sends him.

The gates between the first barrier and the second one only act on the first qubit, which is the one the sender will prepare to the state she wants to send to the receiver. This gates prepare the desired state to send, so they can be anything the sender wants them to be.

**TODO: explain third and fourth sections of the circuit.**

Thanks to the last part of the circuit, where the receiver applys the same gates the sender prepared her qubit with in the first place but inversely, we should get the state |0> all of the time. This is because the "detangler" at the end reverts the qubit to its state at the very beggining of the circuit, which is always |0>. This can be confirmed with the histogram of the circuit, where the leftmost bit corresponds to the receiving qubit and we see we measure it to be in state |0> everytime.
![histogram](https://user-images.githubusercontent.com/63567458/102122809-5505ac00-3e46-11eb-8f72-93bf4098fc83.jpg)

## Running on hardware
Running this circuit on hardware requires some modifications. First, let's see how the circuit looks like after the modifications and then we can explain them. 

![circuit](https://user-images.githubusercontent.com/63567458/104216688-ad769c00-543a-11eb-9be0-252abab79fe7.jpg)

As you can see, the gates that changed are the ones that were conditioned in a classical bit. This types of gates are not available currently in IBM's computers, so we need to change them in order to run the circuit on them. It's quite easy to overcome this difficulty, since we can condition the gates with the corresponding qubits (this time without measuring) and we will get the same result. However, we lose the advantage that we haved where the only connection between the sender and the receiver was at the beggining to split the entangled qubits and afterwards through classical channels. Now, the whole quantum circuit has to be connected. Read more about this [here](https://qiskit.org/textbook/ch-algorithms/teleportation.html#5.-Teleportation-on-a-Real-Quantum-Computer-).
