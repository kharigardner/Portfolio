# this is a cli wrapper for the qrcode module

if __name__ == "__main__":
    import sys
    import qrcode
    import time
    import os
    # defining the data
    data = sys.argv[1]
    # defining the filename
    filename = sys.argv[2]
    # generating the qr code
    qrcode.generate_qr(data, filename)
    # waiting for 5 seconds
    time.sleep(5)
    # exiting the program
    sys.exit()