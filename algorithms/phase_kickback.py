from . import *

def phase_kickback(img_path = 'output_images'):
    """
    Phase kickback
    """
    qreg = QuantumRegister(2, 'q')
    qc   = QuantumCircuit(qreg)
    
    # Put both qubits into superposition
    qc.h(qreg[0])
    qc.h(qreg[1])

    # Apply CNOT gate
    qc.cx(qreg[0], qreg[1])

    # Apply Hadamard gate to both qubits
    qc.h(qreg[0])
    qc.h(qreg[1])

    state_vector_backend = Aer.get_backend('statevector_simulator')
    final_state_vector   = execute(qc, state_vector_backend).result().get_statevector()

    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))
    plot_bloch_multivector(final_state_vector).savefig(join(img_path, 'vector.jpg'))
