# Karabiner
App to rebind Keyboard Buttons
[Download](https://karabiner-elements.pqrs.org)

Die gezeigten drei Anderungen unter "Simple Modifications" bei "Kinesis Adv360" eintragen
![[KarabinerRemapSettings.png]]
## Config File
``` JSON karabiner.json
{
    "profiles": [
        {
            "devices": [
                {
                    "identifiers": {
                        "is_keyboard": true,
                        "product_id": 864,
                        "vendor_id": 10730
                    },
                    "simple_modifications": [
                        {
                            "from": { "key_code": "caps_lock" },
                            "to": [{ "apple_vendor_top_case_key_code": "keyboard_fn" }]
                        },
                        {
                            "from": { "key_code": "right_command" },
                            "to": [{ "key_code": "left_option" }]
                        },
                        {
                            "from": { "key_code": "left_option" },
                            "to": [{ "key_code": "left_command" }]
                        }
                    ]
                }
            ],
            "name": "Default profile",
            "selected": true,
            "virtual_hid_keyboard": { "keyboard_type_v2": "ansi" }
        }
    ]
}
```



# Multiport

- 3x USB-B 2.0
- 2x USB-B 3.0
- 2x USB-C
- SD-Card
- MicroSD-Card
- HDMI

[Amazon](https://www.amazon.de/-/en/MacBook-Adapter-Multiport-microSD-Surface/dp/B0F4KMJ3G4/ref=sr_1_7?crid=2HB8UK3IMDRZY&dib=eyJ2IjoiMSJ9.G5qlgU2GFnNDLUx6j07Bm9uc7184awppOsTbHrL74kK6ok-9walfFiMwFGPeuyyjW3sz-1Eb59EpzKIM8KFSmBu_X0BxAVlaSAjbVak-yGLAbejlfX1FaJQGRW4RhwMlUJKFOLO8MEybSQTttiYPnNSM7cZGP_gIqqqZWJzttR92A315qcGKN_oDPk6KFE_uDfIqDIICqOYZaUeIyZtmINIRDefwftxWPSTS0sbj4ubXqBVq7swAO5_pNWM-jFW5CesFh9ILgOkGC9tFYNXEpnsSvGcGfSMrewmw-FHJw-8.QUq5UgjErE_LeHnFiuqeV0klrL_HJO6wCQmzZvj2YW4&dib_tag=se&keywords=multiport+dongle&qid=1760952258&s=computers&sprefix=multiport+dongle%2Ccomputers%2C87&sr=1-7)
