import time
from bluepy import btle
from bluepy.btle import BTLEDisconnectError
from .const import CMD_FUNCTION, CMD_ON, CMD_OFF, CMD_GPIO_CONTROL, CMD_OUT_1, HANDLE_ID


class Device:
    def __init__(self, name, mac, mesh_id):
        self._name = name
        self._mac = mac
        self._mesh_id = mesh_id

    def turn_on(self):
        self.__execute(CMD_ON)

    def turn_off(self):
        self.__execute(CMD_OFF)

    def __execute(self, cmd):
        frame = bytearray()
        frame.append(CMD_FUNCTION)
        frame.append(self._mesh_id)
        frame.append(CMD_GPIO_CONTROL)
        frame.append(CMD_OUT_1)
        frame.append(cmd)

        successful = False
        while successful is False:
            try:
                peripheral = btle.Peripheral(self._mac, btle.ADDR_TYPE_PUBLIC)
                peripheral.writeCharacteristic(HANDLE_ID, frame, True)
                peripheral.waitForNotifications(1.0)
                successful = True
            except BTLEDisconnectError as e:
                time.sleep(0.5)
        