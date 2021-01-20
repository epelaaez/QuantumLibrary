from .. import *

def swap_test(img_path = IMG_PATH, hardware = False):
    qreg_1  = QuantumRegister(2, 'q1')
    qreg_2  = QuantumRegister(2, 'q2')
    ancilla = QuantumRegister(1, 'a')
    acreg   = ClassicalRegister(1, 'c')
    qc      = QuantumCircuit(qreg_1, qreg_2, ancilla, acreg)

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
    qc.measure(ancilla, acreg)

    # Run circuit and output
    if hardware:
        provider = IBMQ.get_provider(hub='ibm-q')
        backend  = least_busy(provider.backends())
    else:
        backend = BasicAer.get_backend('qasm_simulator')

    result  = execute(qc, backend, shots = 1024).result()
    counts  = result.get_counts(qc)
    print(counts)

    qc.draw(output = "mpl", filename = join(img_path, 'circuit.jpg'))
    plot_histogram(counts).savefig(join(img_path, 'histogram.jpg'))