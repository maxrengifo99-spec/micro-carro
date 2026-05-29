def on_button_pressed_a():
    mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 126)
    if mbit_Robot.Avoid_Sensor(mbit_Robot.enAvoidState.OBSTACLE):
        mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 255)
    else:
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_BACK)
        basic.pause(2000)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_STOP)
        basic.pause(5000)
        mbit_Robot.car_ctrl(mbit_Robot.CarState.CAR_RUN)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_SPINRIGHT, 255)
    basic.pause(2000)
    mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 255)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . # . # .
        . # # # .
        . . # . .
        . . . . .
        """)
basic.forever(on_forever)
