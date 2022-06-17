#pragma once

#include "esphome/core/component.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/core/helpers.h"

#include "esp_err.h"
#include "esp_log.h"
#include "esp_wireguard.h"

namespace esphome {
namespace wireguard {
class WireGuard : public Component {
 public:
  void on_safe_shutdown() override;
  void setup() override;
  void loop() override;
  void dump_config() override;
  void set_peer_ip_address(const std::string address) { peer_ip_address = address; }
  void set_peer_port(const uint32_t port) { peer_port = port; }
  void set_peer_public_key(const std::string public_key) { peer_public_key = public_key; }
  void set_allowed_ip_address(const std::string address) { allowed_ip_address = address; }
  void set_allowed_ip_mask(const std::string mask) { allowed_ip_mask = mask; }
  void set_local_port(const uint32_t port) { local_port = port; }
  // void on_safe_shutdown() override {}

 protected:
  uint32_t peer_port = 12912;
  uint32_t local_port = 11010;
  std::string peer_ip_address = "";
  std::string peer_public_key = "";
  std::string allowed_ip_address = "";
  std::string allowed_ip_mask = "";
};
}  // namespace wireguard
}  // namespace esphome
