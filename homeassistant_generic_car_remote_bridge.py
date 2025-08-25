#!/usr/bin/env python3
"""
Home Assistant Generic Car Remote Bridge
Usage: rtl_433 -f 433.922M -R 282 -F json | python3 homeassistant_generic_car_remote_bridge.py
"""

import json
import sys
import paho.mqtt.client as mqtt

# MQTT Configuration
MQTT_HOST = "10.13.37.42"
MQTT_PORT = 1883
MQTT_TOPIC = "rtl_433/generic_car_remote/events"
MQTT_USERNAME = "username"
MQTT_PASSWORD = "password"

# Device mappings
DEVICES = {
    "00001a23bc4d": {
        "model": "Manufacture-CarRemoteA",
        "commands": {0x604: "LOCK", 0x610: "UNLOCK", 0x602: "PANIC"}
    },
    "000012a3456b": {
        "model": "Manufacture-CarRemoteB", 
        "commands": {0x604: "LOCK", 0x610: "UNLOCK", 0x602: "PANIC"}
    }
}
    
# Track last rolling code to filter duplicates
last_rolling_code = None

# MQTT client setup
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()  # Start background loop to maintain connection

def process_message(line):
    try:
        data = json.loads(line)
        if data.get("model") != "Generic-CarRemote":
            return
        
        device_id = data.get("id")
        command = data.get("command")
        
        if device_id in DEVICES:
            device = DEVICES[device_id]
            command_3digit = command >> 4
            
            # Filter duplicates
            global last_rolling_code
            rolling_code = data.get("rolling_code")
            if rolling_code == last_rolling_code:
                return
            last_rolling_code = rolling_code
            
            # Prepare Home Assistant message
            ha_data = {
                "model": device["model"],
                "id": device_id,
                "command_name": device["commands"].get(command_3digit, "UNKNOWN"),
                "remote_id": command & 0xF,
                "rolling_code": rolling_code,
                "timestamp": data.get("time")
            }
            
            # Publish to MQTT
            result = client.publish(MQTT_TOPIC, json.dumps(ha_data))
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Published: {ha_data['command_name']} from Generic Car Remote {ha_data['model']}")
            else:
                print(f"Failed to publish: {result.rc}")
        
    except (json.JSONDecodeError, KeyError):
        pass

if __name__ == "__main__":
    for line in sys.stdin:
        process_message(line.strip())
