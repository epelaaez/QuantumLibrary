from algorithms import *

def swap_test(img_path = 'output_images/circuit.jpg'):
    """
    The swap test circuit can tell us if two registers are in the same state without measuring them. However, it cannot tell us what state they are in. 
    """
    qreg_1  = QuantumRegister(2, 'q1')
    qreg_2  = QuantumRegister(2, 'q2')
    ancilla = QuantumRegister(1, 'a')
    creg    = ClassicalRegister(1, 'c')
    qc      = QuantumCircuit(qreg_1, qreg_2, ancilla, creg)

    # Initialize first two quantum registers to desired state
    qc.h(qreg_1[0])
    qc.x(qreg_1[1])
    qc.h(qreg_2[0])
    qc.x(qreg_2[1])

    # Swap test 
    qc.h(ancilla[0])
    for i in range(len(qreg_1)):
        qc.cswap(ancilla[0], qreg_1[i], qreg_2[i])
    qc.h(ancilla[0])
    qc.x(ancilla[0])

    # Measure ancilla qubit
    qc.measure(ancilla[0], creg[0])

    backend = BasicAer.get_backend('qasm_simulator')
    result  = execute(qc, backend, shots = 1000).result()
    counts  = result.get_counts(qc)
    print(counts)

    qc.draw(output = "mpl", filename = img_path)
    plot_histogram(counts).savefig(img_path)