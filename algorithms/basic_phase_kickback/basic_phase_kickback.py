from .. import *

def basic_phase_kickback(img_path = IMG_PATH):
    """
    Phase kickback.
    """
    qreg = QuantumRegister(2, 'q')
    qc   = QuantumCircuit(qreg)

    qc.x(qreg[1])
    qc.h(qreg[0])
    qc.cp(math.pi/4, 0, 1) # Controlled T gate with control qubit |0> and target qubit |1>

    # Output
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc, backend).result()
    statevector = result.get_statevector(qc)
    
    plot_bloch_multivector(statevector).savefig(join(img_path, 'vector.jpg'))
    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))