import pyb
import time
import utime
"""!Supply as an input the setpoint, the desired location of the motor.

Subtract the measured location of the motor from the setpoint; the difference is the error signal, a signed number indicating which way the motor is off and how far.

Multiply the error signal by a control gain called KP to produce a result called the actuation signal. The larger the error, the larger the actuation, so the harder the controller will push. The formula is
\mathrm{PWM} = K_p * (\theta_{setpoint} - \theta_{actual})

Send the actuation signal to the motor driver which you have already written to control the magnitude and direction of motor torque."""
#import matplotlib as 

class PWM_Calc:
    
    def __init__(self):
        self.KP_set = 0
        self.Theta_Set = 0
        self.time = []
        self.position = []
        self.error = []
        self.timeinit = utime.ticks_ms()
    def set_KP(self, KP):
        
        self.KP_set = KP
        
    def set_setpoint(self, ThetaSet):
        
        self.Theta_Set = ThetaSet
    def Run(self, Theta_Act):
        
        PWM = (self.Theta_Set - Theta_Act)*self.KP_set
        error = self.Theta_Set - Theta_Act
        
        self.time.append(utime.ticks_ms()-self.timeinit)
        self.position.append(Theta_Act)
        self.error.append(error)
        
        return PWM
    
    def Print_Data(self):
        print(self.time)
        print(self.position)
         
        
        
        
        
        
        #user supplies thetaset, takes thetaact from encoder
        #subtracts and multiplies by KP that we define and outputs the PWM magnitude for MotorDriver()
        
        
    