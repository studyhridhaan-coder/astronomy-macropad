import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digitalio import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        'A', 'B', 'C',
        'D', 'E', 'F'
    ]
]

if __name__ == '__main__':
    keyboard.go()
