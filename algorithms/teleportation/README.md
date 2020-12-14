# Teleportation Protocol
The quantum teleportation protocol is a fundamental part of many quantum algorithms. It enables you to transfer the state of one qubit to another qubit instantly. An important distinction to make is that teleportation in this context refers to the transfer of information rather than matter, since the qubits stay in the same place, but the state is transferred.

This protocol is useful to overcome the difficulties imposed by the [no-cloning theorem](https://en.wikipedia.org/wiki/No-cloning_theorem), which tells us that it is not possible to create an exact copy of a quantum state. Which means we cannot copy the state of one qubit into another, but we can teleport it. In fact, most uses of the teleportation protocol are to transfer the state of a qubit into another within a single QPU rather than across large distances like most sci-fi movies portray it. 

** TODO: explain how the circuit works **

Thanks to the last part of the circuit, where we apply the same gates we prepared our qubit with in the first place but inversely, we should get the state |0> all of the time. This is because the "detangler" at the end reverts the qubit to its state at the very beggining of the circuit, which is always |0>. This can be confirmed with the histogram of the circuit, where the leftmost bit corresponds to the receiving qubit and we see we measure it to be in state |0> everytime.

![histogram](https://user-images.githubusercontent.com/63567458/102122809-5505ac00-3e46-11eb-8f72-93bf4098fc83.jpg)
