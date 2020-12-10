from qiskit import *
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib
import config

def main():
    """
    Main program driver.
    """
    try:
        qiskit.IBMQ.save_account(config.ibm_key, overwrite = True)
    except NameError:
        raise Exception("You have not set up your config file correctly.")

    create_bell_state()

def create_bell_state():
    """
    Creates bell state with equal probability of getting state |00> and |11>.
    """
    qreg = QuantumRegister(2, 'q')
    creg = ClassicalRegister(2, 'c')
    qc   = QuantumCircuit(qreg, creg)

    qc.h(qreg[0])
    qc.cx(qreg[0], qreg[1])
    qc.measure(qreg[0], creg[0])
    qc.measure(qreg[1], creg[1])

    backend = BasicAer.get_backend('qasm_simulator')
    result  = execute(qc, backend, shots = 1000).result()
    counts  = result.get_counts(qc)
    print(counts)

    qc.draw(output = "mpl", filename = "output_images/circuit.jpg")
    plot_histogram(counts).savefig("output_images/histogram.png")


if __name__ == "__main__":
    main()
