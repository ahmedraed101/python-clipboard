import win32clipboard as wincb
from time import sleep

def read_clipboard():
    wincb.OpenClipboard()
    data = wincb.GetClipboardData()
    wincb.CloseClipboard()
    return data

def manage_clipboard():
    old = ""
    while True:
        data = read_clipboard()
        
        if data != old:
            with open("history-clipboards.txt", "a") as f:
                f.write(data + "\n")
            old = data
        sleep(0.5)

def main():
    while True:
        command = input("enter (S) to stop: ")
        if command.lower() == "s":
            break

if __name__ == "__main__":
    import threading
    t1 = threading.Thread(target=manage_clipboard, daemon=True)
    t3 = threading.Thread(target=main)
    
    t1.start()
    t3.start()
