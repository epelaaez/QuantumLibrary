from .. import *

def deutsch_jozsa(img_path = IMG_PATH, hardware = False, n = 3):
    qreg  = QuantumRegister(n, 'qreg')
    aqreg = QuantumRegister(1, 'ancillary')
    creg  = ClassicalRegister(n, 'creg')
    qc    = QuantumCircuit(qreg, aqreg, creg)

    # Prepare initial states
    qc.x(aqreg)
    qc.h(aqreg)
    qc.h(qreg)

    qc.barrier()

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