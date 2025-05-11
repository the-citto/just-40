
import gc
import machine
import neopixel
import time


ALPHA_KEYS = (
    ("ESC",     "Q",        "W",        "E",        "R",    "T",        "Y",    "U",    "I",    "O",    "P",    "BACKSPACE"),
    ("TAB",     "A",        "S",        "D",        "F",    "G",        "H",    "J",    "K",    "L",    None,   "ENTER"),
    ("L_SHIFT", "Z",        "X",        "C",        "V",    "B",        "N",    "M",    "FN3",  None,   None,   "R_SHIFT"),
    ("L_CTRL",  "L_SUP",    "L_ALT",    None,       None,   "SPACE",    None,   None,   "FN1",  "FN2",  None,   "R_CTRL"),
)
NAV_KEYS = (
    ("ESC",     "PRINT",    "UP",       "PGUP",     "HOME", "INS",      "F9",   "F10",  "F11",  "F12",  "MENU", "DEL"),
    ("TAB",     "LEFT",     "DOWN",     "RIGHT",    "PGDN", "END",      "F5",   "F6",   "F7",   "F8",   None,   "ENTER"),
    ("L_SHIFT", "CAPS",     "NUM",      None,       "F1",   "F2",       "F3",   "F4",   "FN3",  None,   None,   "R_SHIFT"),
    ("L_CTRL",  "R_SUP",    "R_ALT",    None,       None,   "SPACE",    None,   None,   "FN1",  "FN2",  None,   "R_CTRL"),
)



np = neopixel.NeoPixel(machine.Pin(4), 3)

np[0] = (0, 255, 0)
np[1] = (0, 0, 255)
np[0] = (0, 0, 0)
np.write()

np.fill((0, 0, 255))
np.write()

np.fill((0, 0, 0))
np.write()

np.write()



np = neopixel.NeoPixel(machine.Pin(4), 5)


np[0] = (255, 0, 0) # set to red, full brightness
np[1] = (0, 128, 0) # set to green, half brightness
np[2] = (0, 0, 64)  # set to blue, quarter brightness

np.fill((255, 0, 0))
np.write()

# sda = machine.Pin(4)
# scl = machine.Pin(5)
# i2c = I2C(0, sda=sda, scl=scl, freq=100000)
#
#
# i2c_devs = i2c.scan()
#
# for i2c_dev in i2c_devs:
#     print(i2c_dev, hex(i2c_dev))


class Matrix:

    r_gpios = (0, 1, 2, 3)
    c_gpios = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

    def __init__(self) -> None:
        self._set_pins()

    def _set_pins(self) -> None:
        self.r_pins = [machine.Pin(r_gpio, machine.Pin.OUT) for r_gpio in self.r_gpios]
        self.c_pins = [machine.Pin(c_gpio, machine.Pin.IN, machine.Pin.PULL_DOWN) for c_gpio in self.c_gpios]

    def read(self) -> None:
        for r_id, r_pin in enumerate(self.r_pins):
            # print()
            r_pin.on()
            # print("row", r_id, "\t")
            for c_id, c_pin in enumerate(self.c_pins):
                # print("col", c_id, "\t", c_pin.value())
                if c_pin.value():
                    print("\t\t", ALPHA_KEYS[r_id][c_id])
            r_pin.off()



matrix = Matrix()
matrix.read()



gpio_04 = machine.Pin(4, machine.Pin.OUT)
gpio_04.toggle()


gpio_00 = machine.Pin(0, machine.Pin.OUT)

gpio_10 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
gpio_12 = machine.Pin(12, machine.Pin.IN)

gpio_00.on()
gpio_00.off()

gpio_00.toggle()
gpio_12.value()

# gpio_10.toggle()
gpio_10.value()

# gpio_10.init(pull=machine.Pin.PULL_DOWN)
gpio_10.value()
gpio_10.value(0)
gpio_10.value()



#     def matrix_read(self):
#         total_sum = 0
#         for switch in self.rows:
#             
#             switch.value(0)
#             time.sleep(0.01)
#             self.result=[self.cols[0].value(),self.cols[1].value(),self.cols[2].value(),self.cols[3].value(),self.cols[4].value(),self.cols[5].value()]
#             total_sum += sum(self.result)
#             
#             if min(self.result)==0:
#                 if self.cur_mod == "SUPER1" or self.cur_mod == "SUPER2":
#                     self.key_map = key_map1
#                 else:
#                     self.key_map = key_map0
#                     
#                 self.key_name = self.key_map[int(self.rows.index(switch))][int(self.result.index(0))]
#                 if self.key_name in self.mod_keys:
#                     self.cur_mod = self.key_name
#                 else:
#                     self.cur_key = self.key_name
#                 switch.value(1)
#             switch.value(1)
#         if self.cur_mod != "NONE" and self.cur_key != "NONE" and self.key_pressed == False:
#             self.key_pressed = True
#             if self.cur_mod == "SUPER2":
#                 k.press(KEY_CODES["RIGHTSHIFT"][0], KEY_CODES[self.cur_mod][0], KEY_CODES[self.cur_key][0])
#                 k.release(KEY_CODES[self.cur_key][0])
#                 print(KEY_CODES[self.cur_key][2])
#                 self.cur_key = "NONE"
#             else:
#                 k.press(KEY_CODES[self.cur_mod][0], KEY_CODES[self.cur_key][0])
#                 k.release(KEY_CODES[self.cur_key][0])
#                 if self.cur_mod == "RIGHTSHIFT":
#                     print(KEY_CODES[self.cur_key][2])
#                 else:
#                     print(KEY_CODES[self.cur_key][1])
#                 self.cur_key = "NONE"
#         else:
#             if self.cur_key != "NONE" and self.key_pressed == False:
#                 self.key_pressed = True
#                 k.press(KEY_CODES[self.cur_key][0])
#                 k.release(KEY_CODES[self.cur_key][0])
#                 print(KEY_CODES[self.cur_key][1])
#                 self.cur_key = "NONE"
#                 self.key_name = "NONE"
#         if total_sum == 42:
#             self.key_pressed = False
#             self.cur_mod = "NONE"
#             self.cur_key = "NONE"
#             self.key_name = "NONE"
#             k.release_all()
#         else:
#             if total_sum == 41 and self.cur_mod != "NONE":
#                 self.key_pressed = False
#                 self.cur_key = "NONE"
#                 self.key_name = "NONE"
#






# led = machine.Pin("LED", machine.Pin.OUT)
#
# led_value = True
#
# while True:
#     led.value(led_value)
#     led_value = not led_value
#     time.sleep(1)




# row_0 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
# row_1 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
# row_2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
#
# col_0 = machine.Pin(10, machine.Pin.OUT)
# col_1 = machine.Pin(11, machine.Pin.OUT)
# col_2 = machine.Pin(12, machine.Pin.OUT)
#
# # print(ROW_0.value())
# # print(COL_0.value())
#
# def show():
#     r_0_v = row_0.value()
#     r_1_v = row_1.value()
#     r_2_v = row_2.value()
#     c_0_v = col_0.value()
#     c_1_v = col_1.value()
#     c_2_v = col_2.value()
#     print(" ",      " ",    c_0_v,              c_1_v,              c_2_v)
#     print()
#     print(r_0_v,    " ",    r_0_v and c_0_v,    r_0_v and c_1_v,    r_0_v and c_2_v)
#     print(r_1_v,    " ",    r_1_v and c_0_v,    r_1_v and c_1_v,    r_1_v and c_2_v)
#     print(r_2_v,    " ",    r_2_v and c_0_v,    r_2_v and c_1_v,    r_2_v and c_2_v)
#
#
# show()


# led = machine.Pin("LED", machine.Pin.OUT)

# led_value = True

# while True:
#     led.value(led_value)
#     led_value = not led_value
#     time.sleep(1)

# u = machine.USBDevice()




# from machine import Pin
# import keyboard
# import time
# import gc
#
# k = keyboard.Keyboard()
# print(gc.mem_free())
#
# KEY_CODES = {
#     "NONE":[0x00,"NONE","NONE"],
#     "ERR_OVF":0x01, 
#     "A":[0x04,"a","A"],
#     "B":[0x05,"b","B"], 
#     "C":[0x06,"c","C"],
#     "D":[0x07,"d","D"], 
#     "E":[0x08,"e","E"], 
#     "F":[0x09,"f","F"],
#     "G":[0x0a,"g","G"],
#     "H":[0x0b,"h","H"],
#     "I":[0x0c,"i","I"],
#     "J":[0x0d,"j","J"],
#     "K":[0x0e,"k","K"],
#     "L":[0x0f,"l","L"],
#     "M":[0x10,"m","M"],
#     "N":[0x11,"n","N"],
#     "O":[0x12,"o","O"],
#     "P":[0x13,"p","P"],
#     "Q":[0x14,"q","Q"],
#     "R":[0x15,"r","R"],
#     "S":[0x16,"s","S"],
#     "T":[0x17,"t","T"],
#     "U":[0x18,"u","U"],
#     "V":[0x19,"v","V"],
#     "W":[0x1a,"w","W"],
#     "X":[0x1b,"x","X"],
#     "Y":[0x1c,"y","Y"],
#     "Z":[0x1d,"z","Z"],
#     "1":[0x1e,"1","!"],
#     "2":[0x1f,"2","@"],
#     "3":[0x20,"3","#"],
#     "4":[0x21,"4","$"],
#     "5":[0x22,"5","%"],
#     "6":[0x23,"6","^"],
#     "7":[0x24,"7","&"],
#     "8":[0x25,"8","*"],
#     "9":[0x26,"9","("],
#     "0":[0x27,"0",")"],
#     "ENTER":[0x28,"\n","\n"], 
#     "ESC":[0x29,"ESC","ESC"],
#     "BACKSPACE":[0x2a,"BACKSPACE","BACKSPACE"], 
#     "TAB":[0x2b,"    ","    "],
#     "SPACE":[0x2c," "," "], 
#     "MINUS":[0x2d,"-","_"],
#     "EQUAL":[0x2e,"=","+"],
#     "LEFTBRACE":[0x2f,"[","{"], 
#     "RIGHTBRACE":[0x30,"]","}"],
#     "BACKSLASH":[0x31,"\\","|"],
#     "HASHTILDE":[0x32,"~","`"],
#     "SEMICOLON":[0x33,";",":"],
#     "APOSTROPHE":[0x34,"'","\""],
#     "GRAVE":[0x35,"`","~"],
#     "COMMA":[0x36,",","<"],
#     "DOT":[0x37,".",">"],
#     "SLASH":[0x38,"/","?"], 
#     "CAPSLOCK":[0x39,"CAPSLOCK","CAPSLOCK"],
#     "F1":[0x3a,"F1","F1"],
#     "F2":[0x3b,"F2","F2"],
#     "F3":[0x3c,"F3","F3"],
#     "F4":[0x3d,"F4","F4"],
#     "F5":[0x3e,"F5","F5"],
#     "F6":[0x3f,"F6","F6"],
#     "F7":[0x40,"F7","F7"],
#     "F8":[0x41,"F8","F8"],
#     "F9":[0x42,"F9","F9"],
#     "F10":[0x43,"F10","F10"],
#     "F11":[0x44,"F11","F11"],
#     "F12":[0x45,"F12","F12"],
#     "HOME":[0x4a,"HOME","HOME"],
#     "PAGEUP":[0x4b,"PAGEUP","PAGEUP"], 
#     "DELETE":[0x4c,"DELETE","DELETE"],
#     "END":[0x4d,"END","END"],
#     "PAGEDOWN":[0x4e,"PAGEDOWN","PAGEDOWN"],
#     "RIGHT":[0x4f,"RIGHT","RIGHT"],
#     "LEFT":[0x50,"LEFT","LEFT"],
#     "DOWN":[0x51,"DOWN","DOWN"],
#     "UP":[0x52,"UP","UP"],
#     "LEFTCTRL":[0xe0,"LEFTCTRL","LEFTCTRL"], 
#     "LEFTSHIFT":[0xe1,"LEFTSHIFT","LEFTSHIFT"],
#     "LEFTALT":[0xe2,"LEFTALT","LEFTALT"],
#     "LEFTMETA":[0xe3,"LEFTMETA","LEFTMETA"],
#     "RIGHTCTRL":[0xe4,"RIGHTCTRL","RIGHTCTRL"],
#     "RIGHTSHIFT":[0xe5,"RIGHTSHIFT","RIGHTSHIFT"],
#     "RIGHTALT":[0xe6,"RIGHTALT","RIGHTALT"],
#     "RIGHTMETA":[0xe7,"RIGHTMETA","RIGHTMETA"],
#     "SUPER1":[0x00,"SUPER1","SUPER1"],
#     "SUPER2":[0x00,"SUPER2","SUPER2"]
# }
#
# key_map0=(("ESC","TAB","CAPSLOCK","ENTER","DELETE","BACKSPACE"),\
#          ("A","B","C","D","E","RIGHTALT"),\
#          ("F","G","H","I","J","RIGHTCTRL"),\
#          ("K","L","M","N","O","SUPER1"),\
#          ("P","Q","R","S","T","SUPER2"),\
#          ("U","V","W","X","UP","RIGHTSHIFT"),\
#          ("Y","Z","SPACE","LEFT","DOWN","RIGHT"))
#
# key_map1=(("ESC","TAB","CAPSLOCK","ENTER","DELETE","BACKSPACE"),\
#          ("1","2","3","4","5","RIGHTALT"),\
#          ("6","7","8","9","0","RIGHTCTRL"),\
#          ("GRAVE","LEFTBRACE","RIGHTBRACE","BACKSLASH","SEMICOLON","SUPER1"),\
#          ("APOSTROPHE","COMMA","DOT","SLASH","MINUS","SUPER2"),\
#          ("EQUAL","NONE","NONE","NONE","UP","RIGHTSHIFT"),\
#          ("NONE","NONE","SPACE","LEFT","DOWN","RIGHT"))
#
# class Keypad:
#     def __init__(self):
#         self.cols=[1,2,3,4,5,6]
#         self.rows=[7,8,9,10,11,12,13]
#         self.key_map = key_map0
#         self.mod_keys = ("RIGHTCTRL","RIGHTALT","RIGHTSHIFT","SUPER1","SUPER2")
#         self.cur_mod = "NONE"
#         self.key_name = "NONE"
#         self.cur_key = "NONE"
#         self.key_pressed = False
#     
#     def matrix_init(self):
#         for x in range(0,7):
#             self.rows[x]=Pin(self.rows[x], Pin.OUT)
#             self.rows[x].value(1)
#
#         for x in range(0,6):
#             self.cols[x] = Pin(self.cols[x], Pin.IN, Pin.PULL_UP)
#
#     def matrix_read(self):
#         total_sum = 0
#         for switch in self.rows:
#             
#             switch.value(0)
#             time.sleep(0.01)
#             self.result=[self.cols[0].value(),self.cols[1].value(),self.cols[2].value(),self.cols[3].value(),self.cols[4].value(),self.cols[5].value()]
#             total_sum += sum(self.result)
#             
#             if min(self.result)==0:
#                 if self.cur_mod == "SUPER1" or self.cur_mod == "SUPER2":
#                     self.key_map = key_map1
#                 else:
#                     self.key_map = key_map0
#                     
#                 self.key_name = self.key_map[int(self.rows.index(switch))][int(self.result.index(0))]
#                 if self.key_name in self.mod_keys:
#                     self.cur_mod = self.key_name
#                 else:
#                     self.cur_key = self.key_name
#                 switch.value(1)
#             switch.value(1)
#         if self.cur_mod != "NONE" and self.cur_key != "NONE" and self.key_pressed == False:
#             self.key_pressed = True
#             if self.cur_mod == "SUPER2":
#                 k.press(KEY_CODES["RIGHTSHIFT"][0], KEY_CODES[self.cur_mod][0], KEY_CODES[self.cur_key][0])
#                 k.release(KEY_CODES[self.cur_key][0])
#                 print(KEY_CODES[self.cur_key][2])
#                 self.cur_key = "NONE"
#             else:
#                 k.press(KEY_CODES[self.cur_mod][0], KEY_CODES[self.cur_key][0])
#                 k.release(KEY_CODES[self.cur_key][0])
#                 if self.cur_mod == "RIGHTSHIFT":
#                     print(KEY_CODES[self.cur_key][2])
#                 else:
#                     print(KEY_CODES[self.cur_key][1])
#                 self.cur_key = "NONE"
#         else:
#             if self.cur_key != "NONE" and self.key_pressed == False:
#                 self.key_pressed = True
#                 k.press(KEY_CODES[self.cur_key][0])
#                 k.release(KEY_CODES[self.cur_key][0])
#                 print(KEY_CODES[self.cur_key][1])
#                 self.cur_key = "NONE"
#                 self.key_name = "NONE"
#         if total_sum == 42:
#             self.key_pressed = False
#             self.cur_mod = "NONE"
#             self.cur_key = "NONE"
#             self.key_name = "NONE"
#             k.release_all()
#         else:
#             if total_sum == 41 and self.cur_mod != "NONE":
#                 self.key_pressed = False
#                 self.cur_key = "NONE"
#                 self.key_name = "NONE"
#                 
#
# kp = Keypad()
# kp.matrix_init()
#
# while True:
#     gc.collect()
#     kp.matrix_read()
#     time.sleep(0.02)
