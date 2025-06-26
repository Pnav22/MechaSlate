import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

keyboard.col_pins = (
    board.D2, board.D3, board.D4, board.D5, board.D6,
    board.D7, board.D8, board.D9, board.D10, board.D11,
    board.D12, board.D13, board.D14, board.D15, board.D16,
)

keyboard.row_pins = (
    board.D20, board.D19, board.D18,
    board.D17, board.D22, board.D21,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [  
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NO, KC.DEL,
        KC.GRV, KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7, KC._8, KC._9, KC._0, KC.MINS, KC.EQL, KC.BSPC, KC.INS,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.HOME,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO, KC.PGUP,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.PGDN, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.RALT, KC.RGUI, KC.MENU, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.NO, KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
