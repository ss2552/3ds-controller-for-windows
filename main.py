import socket, struct, request
import pyautogui as pag

debug = True
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 8889))
    while True:
        data, addr = s.recvfrom(4096)
        match bytearray(data)[0]:
            case 0:
                pass
            case 1:
                key = struct.unpack("<BBxxIhhHHhh", rawdata)
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
                    request.post("", )
                print(key)
    else:
        exit()
except Exception as e:
    print(e)
    exit()
