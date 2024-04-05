import socket, struct, request
import pyautogui as pag



debug = True



send = lambda set: request.post("https://script.google.com/macros/s/AKfycbwvhNBhf5_kf7Yw2e6-evI6WjyjoadpVFgm8WQ6W1YGmr5wEhmWILGq-gnyuZxfTIyu/exec", headers={'Content-Type': 'charset=UTF-8'},data=set: str)
try:
    if send("ping"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", 8889))
        while True:
            data, addr = s.recvfrom(4096)
            match bytearray(data)[0]:
                case 0:
                    pass
                case 1:
                    key = struct.unpack(send("u"), rawdata) # "<BBxxIhhHHhh"
                    if  key[3]:
                        case 28:
                            pag.press('d')
                        case 29:
                            pag.press('a')
                    elif key[4]:
                        case 30:
                            pag.press('w')
                        case 31:
                            pag.press('s')
                    if debug:
                        
                        print(key)
    exit()
except Exception as e:
    print(e)
    exit()
