from .. import *

def phase_kickback(img_path = IMG_PATH):
    """
    Phase kickback.
    """
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    qc   = QuantumCircuit(qreg, creg)

    # Prepare initial state
    qc.x(qreg[1])

    qc.barrier()

    # Put first qubit into superposition
    qc.h(qreg[0])
    qc.h(qreg[1])

    # Apply CNOT gate
    qc.cx(qreg[0], qreg[1])

    # Apply Hadamard gate to both qubits
    qc.h(qreg[0])
    qc.h(qreg[1])

    qc.barrier()

    # Measure
    qc.measure(qreg, creg)

    # Output
    backend = BasicAer.get_backend('qasm_simulator')
    result  = execute(qc, backend, shots = 1000).result()
    counts  = result.get_counts(qc)
    print(counts)

    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))
    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))
