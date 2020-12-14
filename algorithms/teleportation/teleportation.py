from .. import *

def teleportation(img_path = 'output_images'):
    """
    Teleports the precise state of one qubit into another. 
    """
    qreg_sender   = QuantumRegister(1, name='q_sender')
    qreg_ep       = QuantumRegister(1, name='q_entangled')
    qreg_receiver = QuantumRegister(1, name='q_receiver')
    creg_sender   = ClassicalRegister(1, name='c_sender')
    creg_ep       = ClassicalRegister(1, name='c_entangled')
    creg_receiver = ClassicalRegister(1, name='c_receiver')
    qc = QuantumCircuit(qreg_sender, qreg_ep, qreg_receiver, creg_sender, creg_ep, creg_receiver)

    # Entangle ep register with receiver register
    qc.h(qreg_ep)
    qc.cx(qreg_ep, qreg_receiver)

    qc.barrier()

    # Prepare qubit to be sent with specific state
    qc.reset(qreg_sender)
    qc.h(qreg_sender)
    qc.rz(math.radians(45), qreg_sender)
    qc.h(qreg_sender)

    qc.barrier()

    # Send qubit
    qc.cx(qreg_sender, qreg_ep)
    qc.h(qreg_sender)
    qc.measure(qreg_sender, creg_sender)
    qc.measure(qreg_ep, creg_ep)

    qc.barrier()

    # Receive qubit and apply gates depending on measures of sender's and entangled's qubits
    qc.x(qreg_receiver).c_if(creg_ep, 1)
    qc.z(qreg_receiver).c_if(creg_sender, 1)

    qc.barrier()

    # Measure
    qc.h(qreg_receiver)
    qc.rz(math.radians(-45), qreg_receiver)
    qc.h(qreg_receiver)
    qc.measure(qreg_receiver, creg_receiver)

    # Get results, draw charts and figures
    backend = Aer.get_backend('qasm_simulator')
    result  = execute(qc, backend, shots = 1024).result()
    
    counts  = result.get_counts(qc)
    print(counts)

    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))

    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))
    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))