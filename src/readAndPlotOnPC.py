
# #for the controler we need to change a file and the send datat like this
#code classnotebook: https://cpslo-my.sharepoint.com/personal/crefvem_calpoly_edu/_layouts/15/Doc.aspx?sourcedoc={94383b5e-1602-443c-822b-e03c434c9049}&action=view&wd=target%28_Lecture%20Notes%2FSection%2001.one%7C55db1e55-014b-4a31-8024-ff1c5151a70a%2FCharacter%20I%5C%2FO%20Using%20pyb.USB_VCP%20%7Cc5a1326e-ba0c-42c2-ad94-b665f1864fb7%2F%29&wdorigin=NavigationUrl

#code instruction
# u2 = pyb.UART(2, baudrate=115200)      # Set up the second USB-serial port

# for number in range(10):               # Just some example output
#     u2.write(f"Count: {number}\r\n")   # The "\r\n" is end-of-line stuff
#     number += 1


# import serial
#    ...
#    with serial.Serial ('COMx', 115200) as s_port:
#        ...
#        s_port.write (b'something')       # Write bytes, not a string
#        ...


#reading:
#print (s_port.readline ().split (b','))


import pyserial

with (serial.serial("COM11",115200) as ser):
    ser.flush() #clear Input buffer
    ser.in_waiting()#NUM of CHArs in Buffer

    ser.read(n)
    ser.readlines()#read until \n or \r
    ser.readlines()