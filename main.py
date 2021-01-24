from qiskit import IBMQ
from algorithms import *
import config

def main():
    loadIBM()
    promptCircuits()

def promptCircuits():
    circuits = {
        'Bell state': bell_state,
        'Basic phase kickback': basic_phase_kickback,
        'Swap test': swap_test,
        'Teleportation protocol': teleportation,
    }
    
    print('Select the circuit you want to run:', end='')
    
    circuitKeys = list(circuits.keys())

    for n, circuit in enumerate(circuitKeys):
        print(f'\n \t {n}: {circuit}', end='')
    
    print()

    selection = None
    while type(selection) != int:
        selection = input('Your selection: ')
        try:
            selection = int(selection)
        except ValueError:
            pass
        if selection < 0 or selection >= len(circuits):
            selection = None
    
    print(f'Running {circuitKeys[selection]}')
    circuits[circuitKeys[selection]]()


def loadIBM():
    """
    Loads IBM account to access real hardware to run circuits on. You need to call this function to run your circuit in hardware; if you only want to simulate the circuit in your local machine, there is no need to call it.
    """
    load = input('Load IBM account? (Y/N): ')
    if load.upper().strip() == 'Y':
        try:
            IBMQ.load_account()
            print('Successfully loaded IBM account.')
        except Exception:
            try:
                IBMQ.save_account(f"{config.IBM_KEY}", overwrite = True)
            except NameError:
                raise Exception("You have not set up your config file correctly.")

if __name__ == "__main__":
    main()
