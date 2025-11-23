# Karabiner
App to rebind Keyboard Buttons
[Download](https://karabiner-elements.pqrs.org)

Die gezeigten drei Anderungen unter "Simple Modifications" bei "Kinesis Adv360" eintragen
![[KarabinerRemapSettings.png]]

> [!Warning] Nebenwirkung
> Karabiner überschreibt eine Umbelegung in den MacOS Tastatureinstellungen. Um auf der integrierten Tastatur  `CAPS` mit `ESC` zu belegen muss das ebenfalls in Karabiner geändert werden.


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



# Hidden Files
Hotkey um versteckte Dateien anzuzeigen
`Command + Shift + '.'`

Oder folgender Command
```Terminal
defaults write com.apple.finder AppleShowAllFiles -boolean true; killall Finder
```

