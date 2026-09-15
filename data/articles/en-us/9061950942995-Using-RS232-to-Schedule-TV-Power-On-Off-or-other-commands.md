# Using RS232 to Schedule TV Power On/Off or other commands

**Article ID:** 9061950942995
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/9061950942995-Using-RS232-to-Schedule-TV-Power-On-Off-or-other-commands
**Last Updated:** 2026-09-14T20:13:11+00:00
---

With OptiSigns, you can schedule TV Power On/Off using the advanced schedule feature. There are 2 ways you can do it with OptiSigns depending on what devices you are using.

* If you are using a consumer-grade TV and an OptiStick, the TV Power On/Off is achieved through HDMI-CEC. See our [**Operational Schedule**](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232)article for more information.
* If you are using a commercial-grade display, RS232 will be the option for you.

1. Set up RS232 connection for serial communication.
2. Configure the RS232 command for your display and set up the template
3. Create the Power On/Off Schedule

The same procedures can be used to send other RS232 compliant commands as well.

Supported devices/platforms: Windows, Linux, Raspberry Pi, OptiStick, and OptiSigns Pro/ProMax players.

RS232 controls do exist on certain built-in TVs (usually commercial grade) as well. You'll need to check your TV for it.

**1. Create RS-232 connection**

Go to the admin console and expand Advanced, click on the link for external communication. You can also use the link below.

<https://app.optisigns.com/app/s/external-coms>

Click **Connections**, then hit the "Add New" button to create a new RS232 connection.

In the **Add Connection** window, you can give a name to the connection and define the serial port to use, Baud Rate, Data bits, Stop bits, and Parity. This info is determined by the commercial display used. You should be able to get it from your TV user manual.  Flow control is normally not needed in this case, you can just leave it blank.

Click **Save** once the configuration is complete.

To know which serial port is used, you will need to check it on your device. Using Windows as an example, you can find it in the device manager, it will list out the COM port available. On Linux/Raspberry Pi, the serial port is normally "/dev/ttyS0" or "/dev/ttyUSB0" if a USB serial adapter is used. On OptiSigns pre-configured Android Stick, you can use "USB0" as the serial port.

**2. Configure RS232 command and set up the template**

Go to the "Commands" tab, and click the "Add New" button.

Set the RS232 command of your commercial display in the pop-up window. You can choose "asc ii" or "hex" encoding depending on your TV, and the end of line value can be set here accordingly as well. By default, it is set to "CR+LF".

You will need to create a command for Power On, and a command for Power Off.

Once commands are created, go to the "Templates" tab. This is where you map the commands to the Power On/Off action. You only need to create a template if the commands are different. For example, if you are only using Samsung commercial TVs, which all have the same commands for power on/off, then you only need to create one template for it, it can be used on all the Samsung TVs you have deployed.

Map the command to the actions. The actions will be used in the advanced schedule. Save it after the mapping is complete, then the template is ready for use.

**3. Set up Power On/Off schedule**

Once the RS-232 configuration is complete, you will need to set up an Operational Schedule.

Go to the Edit Screens, then go to the **Operational Schedule**section. Hit **New**.

You'll see the Operational Schedule screen. Here, click anywhere you'd like to schedule a Power On/Off.

Once you've done this, you'll see this menu:

Here, the relevant piece is **Power State**. Clicking this will show a drop-down:

To power your screen on or off using RS-232, there are two relevant options:

* **To Power Screen ON -** Choose **On**. You can also specify **RS232** in the Control Method menu. The first option will make use of RS-232 first, then HDMI-CEC as a fallback. The second will only utilize RS-232.
* **To Power Screen OFF -**Choose **Off**. You can also specify **RS232** in the Control Method menu. The first option will make use of RS-232 first, then HDMI-CEC as a fallback. The second will only utilize RS-232.

That's all! Now you have learned how to schedule TV power on/off using RS232.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)