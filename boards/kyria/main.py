from kyria_v1_rp2040 import KMKKeyboard

from kmk.extensions.international import International
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.oled import Oled, OledData
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.holdtap import ModTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

keyboard.modules = [Layers(), HoldTap(), TapDance()]
keyboard.extensions = [MediaKeys(), International()]

split = Split(split_type=SplitType.UART, use_pio=True)
keyboard.modules.append(split)

rgb_ext = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=10,
    val_limit=200,
    val_default=20,
    animation_mode=AnimationModes.BREATHING_RAINBOW,
)
keyboard.extensions.append(rgb_ext)

oled_ext = Oled(
    OledData(
        entries=[
            OledData.oled_text_entry(text='Kyria v1.4\nKB2040', line_spacing=0.75, inverted=True, x=0, y=0),
            OledData.oled_text_entry(text='americ', x=128, y=0, x_anchor=1.0),
            OledData.oled_text_entry(text='anfootball', x=128, y=10, x_anchor=1.0),
            OledData.oled_text_entry(text='Layer: ', x=0, y=32, y_anchor=1.0),
            OledData.oled_text_entry(text='BASE', x=40, y=32, y_anchor=1.0, layer=0),
            OledData.oled_text_entry(text='LOWER', x=40, y=32, y_anchor=1.0, layer=3),
            OledData.oled_text_entry(text='RAISE', x=40, y=32, y_anchor=1.0, layer=4),
            OledData.oled_text_entry(text='ADJUST', x=40, y=32, y_anchor=1.0, layer=6),
        ]
    ),
    height=64,
    flip=True,
)

keyboard.extensions.append(oled_ext)

# Edit your layout below
# Currently, that's a default QMK Kyria Layout - https://config.qmk.fm/#/splitkb/kyria/rev1/LAYOUT

ESC_LCTL = KC.HT(KC.ESC, KC.LCTL)
QUOTE_RCTL = KC.HT(KC.QUOTE, KC.RCTL)
ENT_LALT = KC.HT(KC.ENT, KC.LALT)
MINUS_RCTL = KC.HT(KC.MINUS, KC.RCTL)

keyboard.keymap = [
    [
        KC.TAB,        KC.Q,          KC.W,          KC.E,          KC.R,          KC.T,                                                                      KC.Y,          KC.U,          KC.I,          KC.O,          KC.P,          KC.BSPC,
        ESC_LCTL,      KC.A,          KC.S,          KC.D,          KC.F,          KC.G,                                                                      KC.H,          KC.J,          KC.K,          KC.L,          KC.SCLN,       QUOTE_RCTL,
        KC.LSFT,       KC.Z,          KC.X,          KC.C,          KC.V,          KC.B,          KC.LBRC,       KC.CAPS,       KC.MO(5),      KC.RBRC,       KC.N,          KC.M,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.RSFT,
                                                     KC.MO(6),      KC.LGUI,       ENT_LALT,      KC.SPC,        KC.MO(3),      KC.MO(4),      KC.SPC,        KC.RALT,       KC.RGUI,       KC.APP,
    ],
    [
        KC.TAB,        KC.QUOT,       KC.COMM,       KC.DOT,        KC.P,          KC.Y,                                                                      KC.F,          KC.G,          KC.C,          KC.R,          KC.L,          KC.BSPC,
        ESC_LCTL,      KC.A,          KC.O,          KC.E,          KC.U,          KC.I,                                                                      KC.D,          KC.H,          KC.T,          KC.N,          KC.S,          MINUS_RCTL,
        KC.LSFT,       KC.SCLN,       KC.Q,          KC.J,          KC.K,          KC.X,          KC.LBRC,       KC.CAPS,       KC.MO(5),      KC.RBRC,       KC.B,          KC.M,          KC.W,          KC.V,          KC.Z,          KC.RSFT,
                                                     KC.MO(6),      KC.LGUI,       ENT_LALT,      KC.SPC,        KC.MO(3),      KC.MO(4),      KC.SPC,        KC.RALT,       KC.RGUI,       KC.APP,
    ],
    [
        KC.TAB,        KC.Q,          KC.W,          KC.F,          KC.P,          KC.B,                                                                      KC.J,          KC.L,          KC.U,          KC.Y,          KC.SCLN,       KC.BSPC,
        ESC_LCTL,      KC.A,          KC.R,          KC.S,          KC.T,          KC.G,                                                                      KC.M,          KC.N,          KC.E,          KC.I,          KC.O,          QUOTE_RCTL,
        KC.LSFT,       KC.Z,          KC.X,          KC.C,          KC.D,          KC.V,          KC.LBRC,       KC.CAPS,       KC.MO(5),      KC.RBRC,       KC.K,          KC.H,          KC.COMM,       KC.DOT,        KC.SLSH,       KC.RSFT,
                                                     KC.MO(6),      KC.LGUI,       ENT_LALT,      KC.SPC,        KC.MO(3),      KC.MO(4),      KC.SPC,        KC.RALT,       KC.RGUI,       KC.APP,
    ],
    [
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,                                                    KC.PGUP,    KC.HOME,    KC.UP,      KC.END,     KC.VOLU,    KC.DEL,
        KC.TRNS,    KC.LGUI,    KC.LALT,    KC.LCTL,    KC.LSFT,    KC.TRNS,                                                    KC.PGDN,    KC.LEFT,    KC.DOWN,    KC.RGHT,    KC.VOLD,    KC.INS,
        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.SLCK,    KC.TRNS,    KC.TRNS,    KC.PAUS,    KC.MPRV,    KC.MPLY,    KC.MNXT,    KC.MUTE,    KC.PSCR,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                                                      KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.EQL,
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,                                                    KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.PLUS,
        KC.PIPE,    KC.BSLS,    KC.COLN,    KC.SCLN,    KC.MINS,    KC.LBRC,    KC.LCBR,    KC.TRNS,    KC.TRNS,    KC.RCBR,    KC.RBRC,    KC.UNDS,    KC.COMM,    KC.DOT,     KC.SLSH,    KC.QUES,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.TRNS,    KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.TRNS,                                                    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
        KC.TRNS,    KC.F5,      KC.F6,      KC.F7,      KC.F8,      KC.TRNS,                                                    KC.TRNS,    KC.RSFT,    KC.RCTL,    KC.LALT,    KC.RGUI,    KC.TRNS,
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.DF(0),      KC.TRNS,       KC.TRNS,                                                                   KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,
        KC.TRNS,       KC.OLED_BRI,   KC.TRNS,       KC.DF(1),      KC.TRNS,       KC.TRNS,                                                                   KC.RGB_TOG,    KC.RGB_SAI,    KC.RGB_HUI,    KC.RGB_VAI,    KC.RGB_M_P,    KC.TRNS,
        KC.TRNS,       KC.OLED_BRD,   KC.TRNS,       KC.DF(2),      KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.RGB_SAD,    KC.RGB_HUD,    KC.RGB_VAD,    KC.RGB_M_P,    KC.TRNS,
                                                     KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,       KC.TRNS,
    ],
]
# fmt: on

# Edit your encoder layout below
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
    ((KC.VOLD, KC.VOLU),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
    ((KC.MPRV, KC.MNXT),),
)

keyboard.extensions.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
