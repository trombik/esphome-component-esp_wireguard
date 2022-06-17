#include "wireguard.h"
#include "esphome/core/log.h"
#include "esp_err.h"
#include <cstdio>
#include "esp_wireguard.h"

namespace esphome {
namespace wireguard {

static const char *const TAG = "wireguard";

void WireGuard::setup() {
  esp_err_t err = ESP_FAIL;
  ESP_LOGI(TAG, "init_esp_wireguard()");

  wireguard_config_t wg_config = ESP_WIREGUARD_CONFIG_DEFAULT();

  wg_config.private_key = const_cast<char*>(this->peer_public_key.c_str());
  wg_config.listen_port = local_port;
  wg_config.public_key = const_cast<char*>(peer_public_key.c_str());
  wg_config.allowed_ip = const_cast<char*>(allowed_ip_address.c_str());
  wg_config.allowed_ip_mask = const_cast<char*>(allowed_ip_mask.c_str());
  wg_config.endpoint = const_cast<char*>(peer_ip_address.c_str());
  wg_config.port = peer_port;

  wireguard_ctx_t ctx = {0};
  err = esp_wireguard_init(&wg_config, &ctx);
}

void WireGuard::loop() {
}

void WireGuard::on_safe_shutdown() {
}

void WireGuard::dump_config() {
  ESP_LOGI(TAG, "empty");
}

}
}
