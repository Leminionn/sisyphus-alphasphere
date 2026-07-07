# How to get the MAC Address on your media player

**Article ID:** 8099928867475
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/8099928867475-How-to-get-the-MAC-Address-on-your-media-player
**Last Updated:** 2025-08-29T20:29:34+00:00
---

If your IT team is looking for the MAC address on your media player, you can follow this article to get the MAC Address on your devices.

* OptiSigns Android Stick
* Fire Stick
* Raspberry Pi
* Windows

### 1) How to get the MAC Address on the OptiSigns Android Stick

1. Go to the Android Home Page > Settings

2. Click "Network & Internet"

3. Select "your wifi SSID name"

4. You will see your device's MAC Address.

### 2) How to get the MAC Address on the Fire Stick

1. Go to the Fire Stick Home Page > Settings > My Fire TV

2. Click "About"

3. Then go to "Network", you will see the MAC Address

### 3) How to get the MAC Address on the Raspberry Pi

1. Open the "**terminal**"

2. Type the

```
ifconfig
```

3. The result will be like this, check section eth0 if you are using wired connection. Check section wlan0 if you are using WiFi connection.

The MAC address is visible after the **“ether”** keyword.

### 4) How to get the MAC Address on the Windows

1. Enter **cmd**in the search box at the bottom left-hand corner of your screen. You will see the "Command Prompt" and click it

It will show like this.

2. Type the

```
ipconfig /all
```

3. Navigate to the section “Wireless LAN adapter Wi-Fi” or "Ethernet adapter Ethernet" depending on whether you connect through wireless or wire network. The MAC Address will be shown next to “Physical Address”.

## That's all!

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)