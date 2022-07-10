function servo_select (ang: number, mp: number) {
    if (mp == 1) {
        kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo1, ang)
    } else if (mp == 2) {
        kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo2, ang)
    } else if (mp == 3) {
        kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo3, ang)
    } else if (mp == 4) {
        kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo4, ang)
    }
}
input.onButtonPressed(Button.A, function () {
    angle[mp] = angle[mp] + 1
    servo_select(angle[mp], mp)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("=" + convertToText(angle[mp]))
    if (mp <= 3) {
        mp += 1
    } else {
        mp = 1
    }
    basic.showNumber(mp)
})
input.onButtonPressed(Button.B, function () {
    angle[mp] = angle[mp] - 1
    servo_select(angle[mp], mp)
})
let mp = 0
let angle: number[] = []
basic.showIcon(IconNames.Heart)
angle = [
0,
90,
90,
90,
90
]
kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo1, angle[1])
kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo2, angle[2])
kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo3, angle[3])
kitronik_i2c_16_servo.servoWrite(kitronik_i2c_16_servo.Servos.Servo4, angle[4])
mp = 1
basic.showString("" + convertToText(mp) + "=" + convertToText(angle[mp]))
basic.showNumber(mp)
