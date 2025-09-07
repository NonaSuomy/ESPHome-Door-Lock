# ESPHome-PoE-TOTP-Door-Lock
Standalone PoE Door Lock for ESPHome / HA

Generate your ToTP code: https://nonasuomy.github.io/ESPHome-Door-Lock/

You only need the "Base32 Encoded Key" to add to your secret file in esphome. Then scan the QR code into your Google Authenticator or other app like Yubico Authenticator.

![image](https://github.com/user-attachments/assets/1ce40b82-e158-4852-8764-35c7b0fdb3b9)

**Features**

- [TOTP](https://github.com/NonaSuomy/esphome/tree/totp/esphome/components/totp) Pin Codes
- Auto-Lock via UDP to [Sensor Panel](https://github.com/NonaSuomy/ESPHome-Standalone-Rack-Mount-Alarm-Panel)
- Delay knob macro for auto-lock
- Face Recognition - [Frigate](https://github.com/blakeblackshear/frigate) / [Compreface](https://github.com/exadel-inc/CompreFace) / [DoubleTake](https://github.com/skrashevich/double-take)
- RFID [PN523](https://esphome.io/components/binary_sensor/pn532.html) - Yubikey TOTP NFC / Homekit Homekey
- [LED Controls](https://esphome.io/components/output/ledc.html)
- [Piezo Speaker](https://esphome.io/components/rtttl.html)
- [Limit Switches](https://esphome.io/components/switch/)
- [Motor Control](https://esphome.io/components/output/ledc.html)
- [Car Door Lock Monitor](https://github.com/NonaSuomy/ESPHome-Door-Lock/blob/main/homeassistant_generic_car_remote_bridge.py)
- Static 4 to 8 digit codes set via HA service
Developer Tools -> Actions -> ezhacklock_update_user_codes -> codes_list: 12345678,7654321 -> Perform action

**Maybe Features**

Palm Vein Scanner

Finger Print Scanner


Videos

https://github.com/user-attachments/assets/9385ae38-2424-474d-9252-5e10f75ed9bb

https://github.com/user-attachments/assets/8c5ce937-d575-4ba7-a67f-deb81a605d14

![IMG_4823](https://github.com/user-attachments/assets/9a781541-7756-4bc7-a405-9dbed2648b56)
![IMG_4820](https://github.com/user-attachments/assets/6bd1ac63-4605-421f-be82-58db4b258806)
![IMG_4814](https://github.com/user-attachments/assets/24dd9078-e968-4c4d-85bc-d2eb15fbce83)
![IMG_4811](https://github.com/user-attachments/assets/f4c2172f-d9bb-432c-b15d-057c316f9fa6)
![IMG_4810](https://github.com/user-attachments/assets/150ee124-b38c-4d57-ad51-f7c8ba9aeb02)

![IMG_4808](https://github.com/user-attachments/assets/dffecc4f-ddcd-46fd-b395-2961e8ddc743)
![IMG_4807](https://github.com/user-attachments/assets/d9a0b240-5298-43ff-9a54-defecba8813a)

Special thanks to the esphome crew in discord: ssieb, jesserockz, pzich
