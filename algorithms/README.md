# Algorithms

In this directory you can find implementations and explanations of various quantum algorithms and protocols. These are presented both with Qiskit code and written text that go over the mathematics and intuition of what is being done. Right now, the algorithms available are:

- [Bell state](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/Bell%20States.ipynb): the most common bell state (|00⟩+|11⟩, normalized) is prepared.
- [Deutsch-Jozsa](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/Deutsch–Jozsa.ipynb): the Deutsch-Jozsa algorithm is implemented, first with 2 qubits and then generalized to *n* qubits. 
- [Phase kickback](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/Phase%20Kickback.ipynb): the phase kickback "trick" is implemented and a small example with 2 qubits is given.
- [Prime factorization](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/Prime%20Factorization.ipynb): Shor's algorithm is used to get the prime factorization of a number; some familiarity with quantum phase estimation is assumed.
- [Swap test](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/Swap%20Test.ipynb): the swap test is implemented for 2 qubit registers and the transpiled circuit is shown to state how expensive it is to run on hardware.
- [Teleportation](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/Teleportation.ipynb): the quantum teleportation protocol is motivated briefly and then implemented on simulator and hardware.
- [VQE](https://github.com/epelaaez/QuantumLibrary/blob/master/algorithms/VQE.ipynb): the mathematical background for the simulation and optimization tasks are introduced, then VQE is implemented using Qiskit's built in functions.
