# Swap test
The swap test can tell us if two registers are in the same state without measuring them, making it a pretty useful tool in bigger quantum algorithms or even by its own. However, it cannot tell us what state they are in, but it will tell us how similar two qubits (or registers) are.  

## Description
Let's say that we have two states, |q<sub>1</sub>> and |q<sub>2</sub>>, along with one ancillary qubit, |a<sub>0</sub>>. We will not focus on the exact state the first two qubits are in, but on the state of the ancillary qubit (which will eventually give us the output we are looking for). 

First, |a<sub>0</sub>> goes through a Hadamard gate, leaving it in a state of equal superposition. So, the state of our entire circuit at this point is:

<img src="https://user-images.githubusercontent.com/63567458/104123647-bbe68a00-534c-11eb-901b-993b52f2db25.png" height="70px">

Then, we apply the CSWAP gate with |a<sub>0</sub>> as the control qubit. This changes the state of the circuit to:

<img src="https://user-images.githubusercontent.com/63567458/104123622-9194cc80-534c-11eb-80e6-15b1280eac78.png" height="70px">

Then, we apply the next Hadamard gate to |a<sub>0</sub>>, giving us:

<img src="https://user-images.githubusercontent.com/63567458/104123631-9eb1bb80-534c-11eb-9c2f-2fa8f99fa717.png" height="70px">

Finally, we apply a Pauli-X gate to |a<sub>0</sub>>, giving us:

<img src="https://user-images.githubusercontent.com/63567458/104123642-ac674100-534c-11eb-99ec-cdec198cd72d.png" height="70px">

It may be hard to notice at first, but there is something very interesting about this final state we got to. Let's imagine for a second that |q<sub>1</sub>> = |q<sub>2</sub>>, and we wil denote this common state as |q>. With this in mind, the circuit of our state will simplify to:

<img src="https://user-images.githubusercontent.com/63567458/104123699-049e4300-534d-11eb-8a2c-9f7f2b13713a.png" height="70px">

This shows that whenever |q<sub>1</sub>> = |q<sub>2</sub>>, we will get |1> as an output of the ancillary qubit. Now, what happens when our states differ? Let's look at the simple example where |q<sub>1</sub>> = |0> and |q<sub>2</sub>> = |1>. In this case our final state will turn into:

<img src="https://user-images.githubusercontent.com/63567458/104123752-416a3a00-534d-11eb-984e-dad3105356c2.png" height="70px">

Thus, in the case that |q<sub>1</sub>> =/= |q<sub>2</sub>>, the ancillary qubit will have an equal chance of measuring |0> or |1>. This results can be extended to registers of qubits |q<sub>1</sub>> and |q<sub>2</sub>> rather than the single qubits we used to work through this example. 

## Implementation and results
In the implementation of the swap test presented here, |q<sub>1</sub>> and |q<sub>2</sub>> are quantum registers of two qubits each. The circuit presented below first prepares the registers into their initial states (which we chose to be equal so |a<sub>0</sub>> outputs |1>) and then applies the same procedure described above, with the only difference that the CSWAP gate is applied for each qubit and its pair in the other register. The circuit looks as follows: 

![circuit](https://user-images.githubusercontent.com/63567458/102344325-0538f900-3f9c-11eb-87aa-dcfb800d299a.jpg)

The more times we observe |1> as the output, the more certain we can be that the two registers are in the same state. The moment we get the state |0> as an output, we can be certain that the registers are **not** in an identical state.<sup>[1](#footnote_1)</sup>

Another way to look at the output of the swap test is a measure of how identical the two states you are comparing are. Getting a 50-50 distribution of states |0> and |1> tell us that the states are completely different, while measuring |1> all of the times tells us that the states are completely identical. Anything in between can be interpreted as the states being somewhat similar, where a distribution closer to 50-50 indicates less similarity and a distribution closer to 0-100 indicates more similarity. 

The histogram for this implementation of the swap test looks like this (we get the state |1> 100% of the time since the two registers are set to the same state and there is no noise from an actual quantum computer):

![histogram](https://user-images.githubusercontent.com/63567458/102344351-0ec26100-3f9c-11eb-87b2-347cc3f75a13.jpg)

<a name="footnote_1">1</a>: Note that to account for errors in the quantum computer itself we can allow some occurences of the state |0> and still be certain that the two registers are in the same state.

## Running on hardware
Running this circuit on hardware is possible, but it increases the amount of error drastically. This happens because CSWAP gates are not available in IBM's computers, so they have to be constructed from several other gates, therefore increasing the circuit's depth which increases the error rate. The circuit goes from containing 5 gates (we don't count the gates we use to prepare |q<sub>1</sub>> and |q<sub>2</sub>> because they are not part of the swap test itself) to containing 50+ gates. The following photo is what the circuit looks like when ran in IBM's Q16 Melbourne machine.

![circuit-kjtzmqvm](https://user-images.githubusercontent.com/63567458/104316268-840e4c80-54dc-11eb-8e75-b0859f5bead3.png)

For alternatives to the canonical swap test (the one implemented here) that reduce circuit depth and therefore increase reliability when running on hardware, read [this](https://bsiegelwax.medium.com/the-simplest-way-to-compare-single-qubit-quantum-states-8ddbefa5a93e) and [this](https://arxiv.org/pdf/1803.04114.pdf).
