import can as can_library
import os


# RasberryPi
# os.system("sudo ip link set can0 type can bitrate 500000")
# os.system("sudo ip link set can0 up")


class CANCommunicatie:
    def __init__(self) -> None:
        # RaspberryPi
        self.canbus = can_library.Bus(interface='socketcan', channel='can0', bitrate=500000)
        
        # PC
        # self.canbus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=500000)

    def send_msg(self, id, data):
        can_msg = can_library.Message(arbitration_id=id, is_extended_id=False, data=data)

        try:
            self.canbus.send(can_msg)
            print(f"Message sent on {self.canbus.channel_info}")
        except can.CanError:
            print("Message NOT sent")


if __name__ == "__main__":
    can_comm = CANCommunicatie()
    can_comm.send_msg(0x122, [0, 0, 1, 0, 0, 7, 0, 0])

    print('Script succesvol doorgelopen')