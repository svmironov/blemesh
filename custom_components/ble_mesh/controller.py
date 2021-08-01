import logging
from bluepy import btle
from .const import CMD_FUNCTION, CMD_ON, CMD_OFF, CMD_GPIO_CONTROL, CMD_OUT_1, HANDLE_ID

_LOGGER = logging.getLogger(__name__)

class Device:
    def __init__(self, name, mac, mesh_id):
        self._name = name
        self._mac = mac
        self._mesh_id = mesh_id

    def turn_on(self):
        self.sendCmd(CMD_ON)

    def turn_off(self):
        self.sendCmd(CMD_OFF)

    def sendCmd(self, cmd):
        frame = bytearray()
        frame.append(CMD_FUNCTION)
        frame.append(self._mesh_id)
        frame.append(CMD_GPIO_CONTROL)
        frame.append(CMD_OUT_1)
        frame.append(cmd)

        peripheral = btle.Peripheral(self._mac, btle.ADDR_TYPE_PUBLIC);
        peripheral.writeCharacteristic(HANDLE_ID, frame, False)