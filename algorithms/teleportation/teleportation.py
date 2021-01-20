from .. import *

def teleportation(img_path = IMG_PATH, hardware = False):
    qreg_sender   = QuantumRegister(1, name='qsender')
    qreg_ep       = QuantumRegister(1, name='qancillary')
    qreg_receiver = QuantumRegister(1, name='qreceiver')
    creg_receiver = ClassicalRegister(1, name='receiver')
    if not hardware:
        creg_ep       = ClassicalRegister(1, name='cancillary')
        creg_sender   = ClassicalRegister(1, name='csender')
        qc            = QuantumCircuit(qreg_sender, qreg_ep, qreg_receiver, creg_sender, creg_ep, creg_receiver)
    else:
        qc = QuantumCircuit(qreg_sender, qreg_ep, qreg_receiver, creg_receiver)

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

    if not hardware:
        qc.measure(qreg_sender, creg_sender)
        qc.measure(qreg_ep, creg_ep)

        qc.barrier()

        # Receive qubit and apply gates depending on measures of sender's and entangled's qubits
        qc.x(qreg_receiver).c_if(creg_ep, 1)
        qc.z(qreg_receiver).c_if(creg_sender, 1)

        qc.barrier()
    else:
        qc.barrier()

        # Use conditional quantum gates instead of classical controlled gates
        qc.cx(qreg_ep, qreg_receiver)
        qc.cz(qreg_sender, qreg_receiver)

        qc.barrier()

    # Measure
    qc.h(qreg_receiver)
    qc.rz(math.radians(-45), qreg_receiver)
    qc.h(qreg_receiver)
    qc.measure(qreg_receiver, creg_receiver)

    # Run circuit and output
    if hardware:
        provider = IBMQ.get_provider(hub='ibm-q')
        backend  = least_busy(provider.backends())
    else:
        backend = BasicAer.get_backend('qasm_simulator')

    result  = execute(qc, backend, shots = 1024).result()
    counts  = result.get_counts(qc)
    print(counts)

    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))

    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))
    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))