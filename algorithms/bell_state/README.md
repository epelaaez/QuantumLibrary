# Bell State
Bell states are quantum states of two qubits that represent the maximally entangled states possible. The four Bell states form what is called the [Bell basis](https://en.wikipedia.org/wiki/Bell_state#Bell_basis), which form the maximally entangled basis for two qubits. In this circuit, the first Bell state is prepared, which is the simplest and easiest one to prepare.

This circuit creates the bell state (|00> and |11>)/sqrt(2), using the following gates: 

![circuit](https://user-images.githubusercontent.com/63567458/101940817-5dac7700-3be7-11eb-8994-e2e36b2e0457.jpg)

And here is an histogram obtained from measuring the two qubits into classical bits. We can see that there was a 50-50 chance of getting either |00> or |11> (without considering noise from the quantum computer).

![histogram](https://user-images.githubusercontent.com/63567458/101940920-8b91bb80-3be7-11eb-8e74-628c142b8edb.jpg)
