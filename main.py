import socket, struct
import pyautogui as pag


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 8889))
    while True:
        data, addr = s.recvfrom(4096)
        match bytearray(data)[0]:
            case 0:
                pass
            case 1:
                match struct.unpack("<BBxxIhhHHhh", rawdata):
                    case 28:
                        pag.press('d')
                    case 29:
                        pag.press('a')
                    case 30:
                        pag.press('w')
                    case 31:
                        pag.press('s')
    else:
        exit()
except Exception as e:
    print(e)
    exit()
