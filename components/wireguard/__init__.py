# Copyright (C) 2022 Tomoyuki Sakurai <y@trombik.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.components import sensor
from esphome.const import CONF_ID, ICON_WIFI

AUTO_LOAD = ["text_sensor"]
DEPENDENCIES = ["network"]

MULTI_CONF = True

wg_namespace = cg.esphome_ns.namespace("wireguard")
WireGuardSensor = wg_namespace.class_("WireGuard", cg.Component)
CONF_PEER_IP_ADDRESS = "peer_ip_address"
CONF_PEER_PORT = "peer_port"
CONF_PEER_PUBLIC_KEY = "peer_public_key"
CONF_ALLOWED_IP_ADDRESS = "allowed_ip_address"
CONF_ALLOWED_IP_MASK = "allowed_ip_mask"
CONF_LOCAL_PORT = "local_port"
CONF_SENSOR_PEER_IP_ADDRESS = "sensor_peer_ip_address"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(WireGuardSensor),
            cv.Required(CONF_PEER_IP_ADDRESS): cv.string,
            cv.Optional(CONF_PEER_PORT, 12912): cv.port,
            cv.Required(CONF_PEER_PUBLIC_KEY): cv.string,
            cv.Required(CONF_ALLOWED_IP_ADDRESS): cv.string,
            cv.Required(CONF_ALLOWED_IP_MASK): cv.string,
            cv.Optional(CONF_LOCAL_PORT, 11010): cv.port,
            cv.Optional(CONF_SENSOR_PEER_IP_ADDRESS): text_sensor.text_sensor_schema(
                icon = ICON_WIFI)
        }
    )
).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_peer_ip_address(config[CONF_PEER_IP_ADDRESS]))
    cg.add(var.set_peer_public_key(config[CONF_PEER_PUBLIC_KEY]))
    cg.add(var.set_allowed_ip_address(config[CONF_ALLOWED_IP_ADDRESS]))
    cg.add(var.set_allowed_ip_mask(config[CONF_ALLOWED_IP_MASK]))

    if CONF_PEER_PORT in config:
        cg.add(var.set_peer_port(config[CONF_PEER_PORT]))
    if CONF_LOCAL_PORT in config:
        cg.add(var.set_local_port(config[CONF_LOCAL_PORT]))

    yield cg.register_component(var, config)
