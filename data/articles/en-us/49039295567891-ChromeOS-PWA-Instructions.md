# ChromeOS PWA Instructions

**Article ID:** 49039295567891
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/49039295567891-ChromeOS-PWA-Instructions
**Last Updated:** 2026-10-14T19:21:13+00:00
---

Chrome boxes are common for large-scale digital signage deployment as there are industrial-grade chrome boxes such as [AOpen Chromebox Commercial 3](https://www.aopen.com/us_en/products_info/Chromebox_Commercial_3/).

Chrome devices are very stable, and provide excellent performance, they can also be managed by Google Chrome Device Management which will simplify your large-scale deployment, ensure enterprise security, and reduce device management overhead. You can learn more about Google's ChromeOS device management [here](https://support.google.com/chrome/a/answer/1289314?hl=en#:~:text=Enforce%20policies%20and%20manage%20apps&text=You%20can%20make%20Wi%2DFi,Manage%20policies%20for%20Chrome%20devices.).

Displaying OptiSigns on a ChromeOS device consists of these broad steps:

1. Adding OptiSigns Player to your Google Admin account
2. Adding the OptiSigns Player app as an extension
3. Mass Provisioning devices (optional)
4. Pushing Content to Your ChromeOS Device

---

## What You'll Need

* An OptiSigns [**Standard plan or higher**](https://www.optisigns.com/pricing) - touch screens require the **Engage** plan or higher.
* [ChromeOS Enterprise Single App](https://chromeos.google/products/device-management/) licenses per device
* An administrator account for the Google Admin console
* ChromeOS devices, [**enrolled in Google Admin Console and organizational unit**](https://support.google.com/chrome/a/answer/1360534?hl=en)

---

## Adding OptiSigns Player to a Google Admin Account

To begin, go to [**Google Admin console**](https://admin.google.com).

Now go to **Menu** → **Devices** → **Chrome** → **Apps & extensions** → **Kiosks**. Select the organizational unit for your signage devices on the left before adding the app.

On the bottom left, click the **+ symbol (Add button)**. Then, choose **Add by URL**.

Now copy and paste our OptiSigns PWA URL ([webapp.optisigns.com](https://webapp.optisigns.com)) into the open window. Click **Save**.

The OptiSigns app will appear as a kiosk app:

---

## Adding the OptiSigns Player App as an Extension

Now that OptiSigns is registered, we need to add it as an extension. Click on the **OptiSigns row**, then in the side panel go to the **Extensions** section and click **Add Extension**.

Click this button and choose **Add from Chrome Web Store:**

Now, find the **OptiSigns Digital Signage** app in the Chrome Web Store. Input **foendllmjcjfmcpfkkeinenelpnoinoc** in the **"Search by ID"** field. Then hit **Select.**

Now, you should see that the OptiSigns Digital Signage app has been added to your extensions

Technically, your ChromeOS devices are now configured, and can be treated like any other screen in OptiSigns.

If mass-provisioning, keep reading. If not, you can follow our [**Getting Started**](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)guide to pair the device in OptiSigns, upload content, then get your displays working!

---

## Mass Provisioning on ChromeOS Devices (optional)

Mass provisioning requires two steps:

1. Creating a mass provisioning template on the OptiSigns Portal
2. Adding the JSON of that template into your Policy for Extensions area in Google Admin

### Creating a Mass Provisioning Template on OptiSigns

To create a provisioning template, go to the OptiSigns portal and go to the account menu at the top right of the portal: **Username** → **More** → **Provisioning Templates**.

Hit **Create New Provisioning Template:**

You'll be asked to set up the template.

* **Template Name**: Name of your template, this is for you to distinguish it when you have multiple provisioning templates.
* **Device Name Prefix**: This is used to generate the device name during provisioning.
* **Device Name Suffix**: This is used to generate the device name during provisioning, the default setting will add timestamps as a suffix.
* **Folder**: The folder that provisioned devices are added to.
* **Wi-Fi**: Select from the stored Wi-Fi, need to be created first. Only required if you want to setup WIFI during provisioning. Wi-Fi setup is normally not needed for ChromeOS deployment, since the deployment will be managed in the Google Admin console.
* **Time Zone**: Specify the time zone of the device.
* **Tags**: Specify the tags you want to associate to the devices.
* **Initial Default Content Type**: Used to set the initial content on the device after provisioning.
* **Orientation**: Set the orientation, landscape is the default.
* **Sync Play**: Turns Sync Play on or off. See [Synchronized playback (Sync Play)](https://support.optisigns.com/hc/en-us/articles/4412065189267-Synchronized-playback-Sync-Play-feature) for more information.
* **Location**: Set the location of the device.

#### Advanced

* **If device already paired**: Provides options for devices which have already been paired in OptiSigns and how to handle that:
  + **Add Wifi only**: Adds the additional Wi-Fi as an option and leaves other configurations alone.
  + **Replace Wifi only:** Replaces the Wi-Fi configuration and leaves other configurations alone.
  + **Replace all configuration:** Replaces all configurations on the device.
  + **Do nothing:** Does not overwrite or change any existing configurations on the device.

Once the template is created, it will be available under the list of provisioning templates. You can download the config file and it will be available for deployment. Click **Download**, then **ChromeOS**.

Your configuration file will be "provisionting-template-<Your Template Name>.txt".

This file contains a JSON object. This is what you will need to set up auto-provisioning in the next step.

---

### Adding to Extension Policy and Applying to OptiSigns Player

Now, go back to [**Google Admin**](http://admin.google.com) and navigate back to the **Apps & Extensions** menu.

Click the **OptiSigns extension**. Under Policy for extensions, paste the JSON from the provisioning-template.txt file you downloaded.

Your JSON value will now appear in the field:

Then click **Save**.

Now your ChromeOS devices are provisioned. Your devices will pick up the policy at the next sync or restart. Follow our [**Getting Started**](https://support.optisigns.com/hc/en-us/articles/18823504383891-OptiSigns-Getting-Started-Guide)guide to pair the device in OptiSigns, upload content, then get your displays working!

---

## Adding OptiSigns Player to a Private Account

If you don't have a Google Admin account, you can still get the OptiSigns PWA to work on ChromeOS devices. Just follow these steps.

First, go to the Chrome Web Store and **Search extensions and themes:**

Search **OptiSigns Digital Signage** and select it.

Click **Add to Chrome** and wait for it to install.

You can go to **Chrome menu (More)** → **Extensions** → **Manage Extensions** → **My Extensions** to see if it successfully downloaded:

Now you can launch OptiSigns from the ChromeOS Launcher on any ChromeOS device (TV, etc.):

### That's all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).