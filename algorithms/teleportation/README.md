# Teleportation Protocol
The quantum teleportation protocol is a fundamental part of many quantum algorithms. It enables you to transfer the state of one qubit to another qubit instantly. An important distinction to make is that teleportation in this context refers to the transfer of information rather than matter, since the qubits stay in the same place, but the state is transferred.

This protocol is useful to overcome the difficulties imposed by the [no-cloning theorem](https://en.wikipedia.org/wiki/No-cloning_theorem), which tells us that it is not possible to create an exact copy of a quantum state. Which means we cannot copy the state of one qubit into another, but we can teleport it. In fact, most uses of the teleportation protocol are to transfer the state of a qubit into another within a single QPU rather than across large distances like most sci-fi movies portray it. 

The circuit is composed the following way:
![circuit](https://user-images.githubusercontent.com/63567458/104822897-3f6d1300-5846-11eb-9d13-93d744c37ded.jpg)

We define three states |ψ>, |φ>, and |ω>. |ψ> will be the state we want to send, |φ> will be an ancillary qubit,
and |ω> will be the qubit to which we want to send the state originally in |ψ>. 

<img src="https://user-images.githubusercontent.com/63567458/104965200-7a09b380-59de-11eb-80a6-12b424e1bace.png">

The gates before the first barrier entangle the last two qubits, leaving the whole system in the following state:

<img src="https://user-images.githubusercontent.com/63567458/104965310-c3f29980-59de-11eb-913e-0c3b4fa86eb7.png" height="70px">

Here we are using the tensor product just to indicate that the three qubits are part of the same system. It's also important to keep in mind that the order in which we will write them is |ψφω>, so |010> would mean that the sender qubit is in state |0>, the ancillary qubit in state |1>, and the receiver qubit in state |0>. 

The gates between the first barrier and the second one only act on the first qubit: the sender qubit. This gates prepare the desired state to send, so they can be anything the sender wants them to be. In this example we are applying a Hadamard gate, followed by a phase rotation of π/4 radians, and another Hadamard gate at the end. The following equations show how the state is modified:

<img src="https://user-images.githubusercontent.com/63567458/104965711-99eda700-59df-11eb-828f-5fbf2fcc3eae.png" height="210px">

If you don't understand the part where we go from an exponential function to trigonometric functions, I'll advise looking into [Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula). I just applied this identity to the exponential functions, allowing me to simplify the state into an easier one we can work with. 

Before looking at the next gates, let's see the state of our three qubits together. To do this, we can use the state of |ψ> we prepared in the above equation and plug it in the first equation. The following equation shows us this state:

<img src="https://user-images.githubusercontent.com/63567458/104965995-2d26dc80-59e0-11eb-9dc2-a19555e85a96.png">

Now, the following part of the circuit is going to entangle our sender and ancillary qubits with a CNOT gate and then we are going to apply a Hadamard gate to the sender qubit only. To get a better idea of what is happening, we are going to apply this operators to our whole state, so we can see the relations between the three qubits. |ψφω> in the following equation is just a short way of reffering to the state described in the above equation. The following equation shows us what happens to our state:

<img src="https://user-images.githubusercontent.com/63567458/104966256-b76f4080-59e0-11eb-9c5e-e926e27e964e.png">
 
Here it gets a little bit tricky, since we are going to measure |ψ> and |φ>. As you may know, there are 4 possible states we might end up with, these are |00>, |01>, |10> and |11>. And for each of this four states, you can have either |0> or |1> for our last qubit: |ω>. To help illustrate the different possibilites, let's look at what state |ω> will be depending on the state we measure in |ψφ>.

<img src="https://user-images.githubusercontent.com/63567458/104966447-306e9800-59e1-11eb-8040-3829e2fd8dff.png" height="280">

You can make sure that this relation is true by checking it with the previous equation. The first two qubits will determine the third one and you can disregard the states where the first two qubits don't correspond to the measured ones. This shows us that there is a relation between the three qubits (thanks to entanglement!).

And this relation between the three qubits is what we are going to exploit next. The sender will inform the receiver of his measurements and the receiver will apply some gates to |ω> depending on them. This information is transferred via classical channels. A Pauli-X gate is applied if |φ> = |1> and a Pauli-Z gate is applied if |ψ> = |1>, if both states are |1> the two gates are applied in that order. Let's have a look case by case. 

First, the case in which |ψφ> = |00>. No further gates are applied, so we already have the following state:

<img src="https://user-images.githubusercontent.com/63567458/104966841-344eea00-59e2-11eb-903b-5df7d7fb0ec3.png" height="70px">

In the case that |ψφ> = |01>, we only apply a Pauli-X gate:

<img src="https://user-images.githubusercontent.com/63567458/104966937-65c7b580-59e2-11eb-8ddb-6be3fd191d72.png" height="70px">

The next case is that |ψφ> = |10>, in this case we only apply a Pauli-Z gate:

<img src="https://user-images.githubusercontent.com/63567458/104967013-9f002580-59e2-11eb-9258-5762a5234125.png" height="70px">

Finally, the case in which |ψφ> = |11>, here we apply a Pauli-X gate folowed by a Pauli-Z gate:

<img src="https://user-images.githubusercontent.com/63567458/104967073-c7881f80-59e2-11eb-85c3-c0c23af03512.png" height="145px">

At this point, the quantum telepertation protocol is over, the state |ω> is in the state we intended to teleport from |ψ> in each of the four possible cases. To achieve this, we needed to send two bits of information through classical channels. It is common to think that this use of classical channels throws away the whole purpose of teleporting a quantum state, but it really doesn’t. This classical communication is really the only way of ensuring that we teleport the state successfully; if we didn’t apply this step, we would be stuck with one of the four possibilities shown above without the person that has |ωi having a clue about what |ψφ> is, therefore this person would only have the intended state 1/4 of the time.

In this example, we have three more gates in our circuit. This gates are not really part of the protocol, but they help us ensure the teleportation protocol was successful. Thanks to this last part, where the receiver applies the same gates the sender prepared her qubit with in the first place but inversely, we should get the state |0> all of the time. This is because the "resetter" at the end reverts the qubit to its state at the very beggining of the circuit, which is |0>. This part is not included in practical applications of the teleportation protocol, since the qubit is often used to perform other operations, but we do it in this case to ensure that we teleported our qubit correctly. This can be confirmed with the histogram of the circuit, where the leftmost bit corresponds to the receiving qubit and we see we measure it to be in state |0> everytime.
![histogram](https://user-images.githubusercontent.com/63567458/102122809-5505ac00-3e46-11eb-8f72-93bf4098fc83.jpg)

## Running on hardware
Running this circuit on hardware requires some modifications. First, let's see how the circuit looks like after the modifications and then we can explain them. 

![circuit](https://user-images.githubusercontent.com/63567458/104822939-9377f780-5846-11eb-9be3-9aef149656c5.jpg)

As you can see, the gates that changed are the ones that were conditioned in a classical bit. This types of gates are not available currently in IBM's computers, so we need to change them in order to run the circuit on them. It's quite easy to overcome this difficulty, since we can condition the gates with the corresponding qubits (this time without measuring) and we will get the same result. However, we lose the advantage that we haved where the only connection between the sender and the receiver was at the beggining to split the entangled qubits and afterwards through classical channels. Now, the whole quantum circuit has to be connected. Read more about this [here](https://qiskit.org/textbook/ch-algorithms/teleportation.html#5.-Teleportation-on-a-Real-Quantum-Computer-).
