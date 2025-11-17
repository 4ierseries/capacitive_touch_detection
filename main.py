def on_button_pressed_a():
    global time
    basic.show_leds("""
        # # . . .
        # . . . .
        # # # . .
        . . # . .
        # # # . .
        """)
    time = -1
    music.ring_tone(392)
input.on_button_pressed(Button.A, on_button_pressed_a)

time = 0
basic.show_leds("""
    # # # . .
    # . . . .
    # # # . .
    . . # . .
    # # # . .
    """)
pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
time = -1
music.ring_tone(262)

def on_forever():
    global time
    while input.pin_is_pressed(TouchPin.P1):
        if time < 0:
            time = control.millis()
        basic.show_leds("""
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            """)
        if control.millis() - time >= 8000:
            music.stop_all_sounds()
            basic.clear_screen()
            break
basic.forever(on_forever)
