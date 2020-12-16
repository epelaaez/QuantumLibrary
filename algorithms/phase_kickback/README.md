# Phase kickback
Phase kickback is a fundamental building block of larger quantum circuit. As you may imagine, this circuit by itself may not have a lot of practical uses, but when incorporated into a larger algorithm, it turns out to be very useful. The circuit implemented is just an example between two qubits, which makes it easier to understand and simplify, but there is a way to extend phase kickback into many more qubits. However, this explanation will only focus on the circuit implemented here. If you want to get a deeper explanation, I recommend looking at this [explanation](https://qr.ae/pNZ46i) by Pranav Gokhale. 

With this explained, we can look into the circuit implemented here. It looks like this:
![circuit](https://user-images.githubusercontent.com/63567458/102343375-c0609280-3f9a-11eb-92ed-0825d0efec6c.jpg)

As usual, both qubits are initialized to the state |0>.

**TODO: explain circuit**

The histogram when measuring the qubits in the (|0>, |1>) basis looks like this:
![histogram](https://user-images.githubusercontent.com/63567458/102343943-7af09500-3f9b-11eb-8793-8e5e7dc502be.jpg)
