from wrapperedKraken import WrapperedKraken
import wpilib 

class MyRobot(wpilib.TimedRobot):
    def __init__(self):
        wpilib._wpilib.TimedRobot.__init__(self)
        self.testMotor = WrapperedKraken(3, "testKraken")

    def teleopPeriodic(self):
        self.testMotor.setVoltage(1.0)
        wpilib.SmartDashboard.putNumber("Test Kraken Position", self.testMotor.getMotorPositionRad())
