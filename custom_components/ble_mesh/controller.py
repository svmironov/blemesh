import logging
from bluepy import btle
from bluepy.btle import BTLEDisconnectError
from .const import CMD_FUNCTION, CMD_ON, CMD_OFF, CMD_GPIO_CONTROL, CMD_OUT_1, HANDLE_ID

_LOGGER = logging.getLogger(__name__)


class Device:
    def __init__(self, name, mac, mesh_id):
        self._name = name
        self._mac = mac
        self._mesh_id = mesh_id

    def turn_on(self):
        self.execute(CMD_ON)

    def turn_off(self):
        self.execute(CMD_OFF)

    def execute(self, cmd):
        attempts = 5
        for i in range(attempts):
            try:
                self.send_сmd(cmd)
            except BTLEDisconnectError as e:
                if i < attempts - 1:
                    continue
                else:
                    raise
            break

    def send_сmd(self, cmd):
        frame = bytearray()
        frame.append(CMD_FUNCTION)
        frame.append(self._mesh_id)
        frame.append(CMD_GPIO_CONTROL)
        frame.append(CMD_OUT_1)
        frame.append(cmd)

        peripheral = btle.Peripheral(self._mac, btle.ADDR_TYPE_PUBLIC)
        peripheral.writeCharacteristic(HANDLE_ID, frame, False)
        