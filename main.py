from qiskit import IBMQ
from algorithms import *
import config

def main():
    """
    Main function.
    """
    loadIBM()
    teleportation(hardware=True)

def loadIBM():
    """
    Loads IBM account to access real hardware to run circuits on.
    """
    try:
        IBMQ.load_account()
    except Exception:
        try:
            IBMQ.save_account(f"{config.IBM_KEY}", overwrite = True)
        except NameError:
            raise Exception("You have not set up your config file correctly.")

if __name__ == "__main__":
    main()
