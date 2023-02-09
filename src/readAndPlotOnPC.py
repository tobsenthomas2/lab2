
# #for the controler we need to change a file and the send datat like this
#code classnotebook: https://cpslo-my.sharepoint.com/personal/crefvem_calpoly_edu/_layouts/15/Doc.aspx?sourcedoc={94383b5e-1602-443c-822b-e03c434c9049}&action=view&wd=target%28_Lecture%20Notes%2FSection%2001.one%7C55db1e55-014b-4a31-8024-ff1c5151a70a%2FCharacter%20I%5C%2FO%20Using%20pyb.USB_VCP%20%7Cc5a1326e-ba0c-42c2-ad94-b665f1864fb7%2F%29&wdorigin=NavigationUrl

import sys
sys.path.append('c:/users/admin/anaconda3/lib/site-packages')
#issue: serial module not found --> pip show pyserial and add the path
import serial
import time
from matplotlib import pyplot

#cant start program from "usaual" python terminal --> use thonny python and use the following command
#& 'C:\Program Files (x86)\Thonny\python.exe' .\readAndPlotOnPC.py
"""!
The plot function takes in a data list that is 2 items wide (one for t, one for x). These are then stored line by line into two seperate lists, t and x, and each value is converted into a float.
The pyplot function is then used to plot the two lists against each other.
"""
def plot_data(input):
    t = []
    x = []
    for line in input:
        data=line
        try:
            t_val = float(data[0])
            x_val = float(data[1])
            t.append(t_val)
            x.append(x_val)
        except ValueError:
            # ignore row if data is not a float
            pass
    pyplot.plot(t, x)
    pyplot.title("best guess - Kp good")
    pyplot.xlabel("time")
    pyplot.ylabel("value")
    print("MAX Value: "+ str(max(x)))
    pyplot.show()

with (serial.Serial("COM5",115200) as ser):
    #ser.flush() #clear Input buffer
    #ser.in_waiting()#NUM of CHArs in Buffer

    #ser.read(n)
    #ser.readlines()#read until \n or \r
    #ser.readlines()
    

    """!
    first while loop is set up for doing multiple plots in a row. Since that is not needed for this project it wont be used, but the structure is here for future applications.
    The second while loop is true so long as the data is being sent in. Once the end of data flag has been sent, we exit the second while loop. Before entering this loop, we initialize the data list, and clear out the data stream.
    Inside the second while loop, we take the next line from the stream of data, seperate it at the comma and store it in the next row of a list called data.
    After the loop is exited, we input the data list into our plot function (shown above).
    """
    morePlots=True
    while morePlots:
        ser.flushInput()
        ser.flushOutput()
        data=[]
        dataStream=1
        while dataStream:
            buf=ser.readline ().split (b',')
            data.append(buf)
            if buf==[b'99999', b'99999\r\n']:
                dataStream=False
                print("end works!")
                data.pop()
                if(ser.readline()==(b'99999,99999\r\n')):
                    print("last plot. you can stop now")
                    morePlots=False
        plot_data(data)
        
    time.sleep(5)
    print("last dataset was sent! will stop listening now")
    


