import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv

from homeassistant.components.light import (ATTR_BRIGHTNESS, PLATFORM_SCHEMA, LightEntity)
from homeassistant.const import CONF_NAME, CONF_MAC, CONF_DEVICE_ID

from .controller import Device

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Optional(CONF_MAC): cv.string,
        vol.Required(CONF_DEVICE_ID): cv.byte
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([BleLight(config[CONF_NAME], config[CONF_MAC], config[CONF_DEVICE_ID])])

class BleLight(LightEntity):
    def __init__(self, name, mac, mesh_id):
        self._name = name
        self._mac = mac
        self._mesh_id = mesh_id
        self._state = False
        self._dev = Device(self._name, self._mac, self._mesh_id)

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._dev.turn_on()
        self._state = True

    def turn_off(self, **kwargs):
        self._dev.turn_off()
        self._state = False

    def update(self):
        logging.info("Update device info")