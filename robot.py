import wpilib

from utils.signalLogging import SignalWrangler
from wrapperedSparkMax import WrapperedSparkMax 
from wrapperedKraken import WrapperedKraken

class MyRobot(wpilib.TimedRobot):
    def __init__(self):
        wpilib._wpilib.TimedRobot.__init__(self)
        self.testKraken = WrapperedKraken(3, "testKraken")
        self.testSparkMax = WrapperedSparkMax(10, "testSparkMax")
        self.testKraken.setPID(0.3,0.0,0.0)
        self.testSparkMax.setPID(0.05,0.0,0.0)

        self.tmpCmd = 200.0
        self.lastTime = wpilib.Timer.getFPGATimestamp()


    def teleopPeriodic(self):

        if(wpilib.Timer.getFPGATimestamp() - self.lastTime > 1.0):
            self.tmpCmd *= -1.0
            self.lastTime = wpilib.Timer.getFPGATimestamp()

        self.testKraken.setVelCmd(self.tmpCmd/10.0)
        self.testSparkMax.setPosCmd(self.tmpCmd)
        
        wpilib.SmartDashboard.putNumber("Test Kraken Position", self.testKraken.getMotorPositionRad())
        wpilib.SmartDashboard.putNumber("Test SparkMax Position", self.testSparkMax.getMotorPositionRad())

        SignalWrangler().update()
