import enum

class URL(enum.Enum):
	QC_GREY_ORANGE_URL = 'radio://0/80/2M/E7E7E7E7E8'
	QC_GREY_BROWN_URL = 'radio://0/120/2M/E7E7E7E7EF'
	QC_BLUE_BLUE_URL = 'radio://0/80/2M/E7E7E7E7E9'
	QC_ITRI_URL = 'radio://0/80/2M/E7E7E7E7E7'
	QC_SCISR1_URL = 'radio://0/100/2M/E7E7E7E7E7'
	QC_SCISR2_URL = 'radio://0/100/2M/E7E7E7E7E8'
	QC_SCISR3_URL = 'radio://0/100/2M/E7E7E7E7E9'
	QC_SCISR4_URL = 'radio://0/80/2M/E7E7E7E7EA'
class CONTROLLER_TYPE(enum.Enum):
	CONTROLLER_TYPE_SINGLEPPID = 5
	CONTROLLER_TYPE_GIMBAL2D = 7
 
class REF_TYPE(enum.Enum):
	REF_TYPE_STEP = 1
	REF_TYPE_RAMP = 2
	REF_TYPE_THRUST = 3
	REF_TYPE_PWM = 10
 
class LOG_TYPE(enum.Enum):
    LOG_TYPE_ANGPOS_TRQ = 1
    LOG_TYPE_PWM_CMD = 2
    
class SUB_GIMBAL2D_TYPE(enum.Enum):
	SUB_GIMBAL2D_TYPE_PID = 0
	SUB_GIMBAL2D_TYPE_PID_JALPHA = 1
	SUB_GIMBAL2D_TYPE_OFL = 2
	SUB_GIMBAL2D_TYPE_NSF = 3
	SUB_GIMBAL2D_TYPE_PWMTEST = 10
	SUB_GIMBAL2D_TYPE_THRUST = 11

class MOTOR_TYPE(enum.Enum):
	MOTOR_NORMAL = 0
	MOTOR_UPGRADE = 1