from . import *

def phase_kickback(img_path = 'output_images'):
    """
    Phase kickback
    """
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    qc   = QuantumCircuit(qreg, creg)

    # Put both qubits into superposition
    qc.h(qreg[0])
    qc.h(qreg[1])

    # Apply CNOT gate
    qc.cx(qreg[0], qreg[1])

    # Apply Hadamard gate to both qubits
    qc.h(qreg[0])
    qc.h(qreg[1])

    # Measure both qubits
    qc.measure(qreg[0], creg[0])
    qc.measure(qreg[1], creg[1])

    backend = BasicAer.get_backend('qasm_simulator')
    result  = execute(qc, backend, shots = 1000).result()
    counts  = result.get_counts(qc)
    print(counts)

    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))
    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))