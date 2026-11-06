# Remotely Control and Command OptiSigns Devices

**Article ID:** 360055486554
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360055486554-Remotely-Control-and-Command-OptiSigns-Devices
**Last Updated:** 2026-11-05T22:33:29+00:00
---

Reboot a screen, take a screenshot of what it's showing, change its Wi-Fi or time zone, or see it live, all from the OptiSigns portal. You can also send the same command to many screens at once.

These remote management tools come preinstalled on OptiSigns players such as the [OptiSigns Android Stick](https://shop.optisigns.com/products/optisigns-android-stick-player-2), Pro and [ProMax](https://shop.optisigns.com/products/optisigns-promax-signage-player), and are available on many other devices too.

---

## What You'll Need

* An OptiSigns [Pro Plus](https://www.optisigns.com/pricing) plan or higher
* A screen that is paired and online - commands can't reach a screen that is offline or powered off
* To send commands to many screens at once: the account owner must turn on **Enable Remote Command**, and the devices must run a supported player version (see [Send Commands to Many Screens at Once](#SendCommandsToManyScreensAtOnce))

---

## Control a Single Screen

### Open the Remote Commands for a Screen

Go to **Screens**.

Find the screen you want to manage and click **Edit**.

In the **Edit Screen** dialog, click **Advanced**.

At the bottom of the **Advanced** section is a row of green command buttons.

|  |
| --- |
| **NOTE** |
| The buttons you see depend on the device, your plan and the device's current state, so a device may show fewer buttons than in these pictures. If the screen is offline, no buttons appear at all. |

### Reboot the Device

Click **Reboot**.

Click **Reboot** again to confirm. The device restarts and is unavailable for a short while.

### Take a Screenshot

Click the camera button.

Click **Take screenshot** to confirm.

The screenshot appears in a gallery below the buttons, stamped with the date and time. The gallery keeps several screenshots: use the arrows or the thumbnails to move between them, and click one to enlarge it.

### Add or Remove Wi-Fi

Click the Wi-Fi button.

The **Wi-Fi access points** dialog lists the networks saved on the device. Click the trash icon next to a network to remove it.

To add a network, fill in **Wi-Fi SSID**, **Wi-Fi Security Type** and **Wi-Fi Password** below the list, turn on **Hidden** if the network doesn't broadcast its name, and click **Add**.

### Set the Time Zone

Click the globe button.

In **Set Timezone**, choose the time zone and click **Apply**.

### View Device Info

Click the **i** button to see the device's hardware and network details.

**Device Info** shows the Wi-Fi network and MAC address, display resolution and refresh rate, memory and storage use, temperature, uptime and time zone. The MAC address is handy when you need to find the device in a network monitoring tool.

### See the Remote Command History

Click the history button.

**Remote Commands History** lists the commands sent to this screen, with their **Status**, **Result** and **Date**.

### Use More Commands

Click the arrow at the end of the button row to see more commands.

Which commands appear depends on the device:

* **Refresh & Relaunch** - Restart the OptiSigns app without rebooting the device. Useful when the screen is frozen or misbehaving.
* **Send HDMI CEC** - Turn the TV on or off with HDMI CEC commands. HDMI CEC must be turned on in the TV's settings.
* **Send RS232** - Turn the TV on or off with RS232 commands.
* **Storage Details** - Show how much of the device's storage is used and free.
* **Install OptiSigns Versions** - Install a different version of the OptiSigns app. If you install an older version, disable auto update first, or the device updates itself back to the latest version.
* **Disable Auto Update** or **Enable Auto Update** - Stop or restart automatic updates of the OptiSigns app.
* **Install APK** - Install an Android app from a direct link to its APK file.
* **OTA Update** - Update the device's software over the air.

### Remotely View and Control the Screen

Remote Control lets you see what's actually playing on the device and use its menus with your mouse. This is different from **Preview**, which only shows an approximation of how an asset or Playlist will look.

In the **Advanced** section of **Edit Screen**, click **More**.

Next to **Remote Control**, click **Activate**.

Click **Activate** to confirm.

Activating Remote Control for the first time can take several seconds. A **Remote** button then appears at the start of the button row. Click it to open the remote view of the device.

### Use the Mobile Admin App

The OptiSigns [Mobile Admin App](https://www.optisigns.com/mobile-app) lets you control your devices in the same way from your phone. See [How to Use the OptiSigns Mobile Admin App](https://support.optisigns.com/hc/en-us/articles/30003143806099) for details.

---

## Send Commands to Many Screens at Once

**Execute Remote Commands** sends a command or script to one screen, several screens, or every screen with a tag, all at once. Use it for mass provisioning, updates and troubleshooting.

It works on Windows, Linux, Raspberry Pi and macOS players, and on Android devices such as the OptiSigns Android Stick. The devices must run a recent player. The dialog lists the versions it needs: "Applicable to Win, Linux, Raspberry Pi version 4.3.1, OptiSigns Player 5.17.3 or newer".

### Turn On Remote Commands for Your Account

Remote command execution is off by default. For security reasons, only the account owner can turn it on or off.

Go to [Preferences](https://app.optisigns.com/app/s/preference-settings) and check **Enable Remote Command**.

### Execute Remote Commands

Go to **Screens**, click the **More Options** (three dots) button and click **Execute Remote Commands**.

|  |
| --- |
| **NOTE** |
| **Execute Remote Commands** only appears in this menu once **Enable Remote Command** is on, and only for account owners and admins. |

The **Execute Remote Commands** dialog has three parts:

1. **Target** - Which devices get the command.
2. **Command** - The command to run.
3. **History / Execution status** - The commands you sent and their results.

For **Target**, choose one of these:

* **Screens** - Pick one or more screens by name.
* **Tags** - Send the command to every device with the tags you choose, for example all screens tagged "Windows" or "Raspberry Pi".

In **Command**, type the command and click **Submit**. Write it for the operating system the devices run: for example a Linux shell command for OptiSigns Pro and ProMax players, a Windows command for Windows players, or an Android command for the OptiSigns Android Stick.

You can also pick a built-in command from the dropdown next to the command box. These work whatever the device's operating system is:

* **Refresh & Relaunch** - Works on any device.
* **Reboot Device** - Works on most devices, but not on some Android devices.

Each command you send appears under **History / Execution status** with its status and result.

### Stop a Device From Accepting Remote Commands

You can stop a single device from accepting remote commands. On the device, open the OptiSigns side menu, click **Advanced Options** and turn off **Execute Remote Commands**. The device then rejects any remote command.

---

## Troubleshooting

Here are a few common issues our customers can encounter, and their solutions.

#### The Command Buttons Don't Appear in Edit Screen

Check that the screen is online. An offline screen shows no command buttons. If it is online, check that your account is on Pro Plus or higher.

#### Execute Remote Commands Is Missing From the Screens Menu

The account owner needs to check **Enable Remote Command** in [Preferences](https://app.optisigns.com/app/s/preference-settings). The menu item is also only shown to account owners and admins.

#### "Execute Remote Command Is Disabled"

The device has remote commands turned off. On the device, open **Advanced Options** in the side menu and turn on **Execute Remote Commands**.

#### "Command Rate Limit Exceeded"

You sent too many commands in a short time. Wait a moment, then submit the command again.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).