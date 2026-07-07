# How to use Remote Command Execution - Windows/Linux

**Article ID:** 4408658251027
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4408658251027-How-to-use-Remote-Command-Execution-Windows-Linux
**Last Updated:** 2025-09-05T14:59:20+00:00
---

|  |
| --- |
| **NOTE** |
| In order to use this feature, you will need a **Pro Plus** **or above plan**. |

The Execute Remote Commands feature allows you to remotely manage screens running on Windows/Linux/Raspberry Pi. It allows command to be pushed remotely to individual devices or groups of devices simultaneously.

---

## Enable Remote Command Feature on Account

Remote Command Execution is disabled by default. To use it, it will need to be turned on. To do this, navigated to [the Preferences section](https://app.optisigns.com/app/s/preference-settings) in the OptiSigns portal.

|  |
| --- |
| For security reasons, **only the account owner** can enable or disable Remote Command Execution. |

---

## How to Execute Remote Commands

To submit the command to manage the devices remotely, you will need to go to the remote command execution console. Click **Screens**, then the **More Options (Three Dots)**

Screens -> More Options Icon -> Execute Remote Commands

The Execute Remote Commands console can be broken down into three sections:

* **Section 1** - Where you specify the target of the commands.
* **Section 2** - The command you want to execute.
* **Section 3** - The execution result and history.

For section 1, there are 2 types of targets you can choose from:

* **Screens** - You can select the screen name here, it can be one screen or multiple screens.
* **Tags** - Utilizing tags, you can execute the command on a group of devices. In the below example, the command will be submitted to all devices tagged as Windows or Raspberry Pi.

For section 2, you can enter the command you want to execute in the text box. The command needs to be OS-specific, depending on the OS your device is running on, you will need to build the scripts accordingly. Once you have your commands ready, just click the submit button. The command will be pushed to the devices for execution.

Other than the free-form scripts, there are some common commands built into the platform, to achieve these functions, you will just need to select it from the drop-down menu. Depending on the type of device OS, the command will be submitted accordingly.

After a command is executed, it will appear in section 3: the command history.

|  |
| --- |
| **NOTE** |
| The **Refresh & Relaunch** command can be used on any device. The **Reboot Device** command cannot be used on certain Android devices. |

---

## Controlling Remote Commands Received by the Device

In some cases, you may not want some of your devices to be controlled remotely for any reason. The ability to receive remote commands can be toggled on the device.

Go to the side menu on the OptiSigns player, click **Advanced Options**, and you'll find the toggle for **Execute Remote Commands**. Toggling this off will cause the device to reject remote commands.

### That's all!

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)