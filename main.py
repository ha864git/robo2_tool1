def servo_select(ang: number, mp: number):
    if mp == 1:
        kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO1, ang)
    elif mp == 2:
        kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO2, ang)
    elif mp == 3:
        kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO3, ang)
    elif mp == 4:
        kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO4, ang)

def on_button_pressed_a():
    angle[mp2] = angle[mp2] + 1
    servo_select(angle[mp2], mp2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global mp2
    basic.show_string("=" + convert_to_text(angle[mp2]))
    if mp2 <= 3:
        mp2 += 1
    else:
        mp2 = 1
    basic.show_number(mp2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    angle[mp2] = angle[mp2] - 1
    servo_select(angle[mp2], mp2)
input.on_button_pressed(Button.B, on_button_pressed_b)

mp2 = 0
angle: List[number] = []
basic.show_icon(IconNames.HEART)
angle = [0, 90, 90, 90, 90]
kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO1, angle[1])
kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO2, angle[2])
kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO3, angle[3])
kitronik_i2c_16_servo.servo_write(kitronik_i2c_16_servo.Servos.SERVO4, angle[4])
mp2 = 1
basic.show_string("" + convert_to_text(mp2) + "=" + convert_to_text(angle[mp2]))
basic.show_number(mp2)