"""!Supply as an input the setpoint, the desired location of the motor.

Subtract the measured location of the motor from the setpoint; the difference is the error signal, a signed number indicating which way the motor is off and how far.

Multiply the error signal by a control gain called KP to produce a result called the actuation signal. The larger the error, the larger the actuation, so the harder the controller will push. The formula is
\mathrm{PWM} = K_p * (\theta_{setpoint} - \theta_{actual})

Send the actuation signal to the motor driver which you have already written to control the magnitude and direction of motor torque."""


def PWM_Calc(Theta_Set, Theta_Act, KP):
        
    PWM = (Theta_Set - Theta_Act)*KP
    
    return PWM
        
        
        
        
        
        #user supplies thetaset, takes thetaact from encoder
        #subtracts and multiplies by KP that we define and outputs the PWM magnitude for MotorDriver()
        
        
    