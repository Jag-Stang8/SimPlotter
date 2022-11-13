#!python3

import irsdk
import time

class State:
    ir_connected = False
    last_car_setup_tick = -1

def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        
        state.last_car_setup_tick = -1
        
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')

# main loop
def loop():
    ir.freeze_var_buffer_latest()

    

    

if __name__ == '__main__':
    # initializing ir and state
    ir = irsdk.IRSDK()
    state = State()

    try:
        while True:
            check_iracing()
            if state.ir_connected:
                loop()

            time.sleep(1)
    except KeyboardInterrupt:
        pass
