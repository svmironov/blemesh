import pygatt
from .const import CMD_FUNCTION, CMD_ON, CMD_OFF, CMD_GPIO_CONTROL, CMD_OUT_1, SERVICE_UUID


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

        adapter = pygatt.backends.GATTToolBackend()

        adapter.start(reset_on_start=False)
        device = adapter.connect(self._mac, address_type=pygatt.BLEAddressType.public)
        characteristic = SERVICE_UUID
        device.char_write(characteristic, frame, False)
        adapter.stop()