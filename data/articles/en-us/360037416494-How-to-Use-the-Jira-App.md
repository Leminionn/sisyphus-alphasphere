# How to Use the Jira App

**Article ID:** 360037416494
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360037416494-How-to-Use-the-Jira-App
**Last Updated:** 2026-10-13T21:50:54+00:00
---

Jira is Atlassian's project management tool for planning and tracking work. With the Jira app, it's possible to display your Jira boards and dashboards on your digital signs, so your team can see what's in progress without opening a laptop.

Let's get started.

---

## What You'll Need

* An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
* A Jira account, with access to the project board or dashboard you want to display
* An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
* A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))
* A keyboard and mouse you can connect to the device, for the first sign-in

---

## Creating a Jira App

First, open the Jira project board or dashboard you want to display. Copy its address from your browser's address bar.

|  |
| --- |
| **NOTE** |
| The URL must be a Jira Cloud link, such as https://yourcompany.atlassian.net/jira/…. Any other address shows **Please enter a valid Atlassian JIRA URL** and you won't be able to save. |

Next, go to the OptiSigns portal. Go to **Files/Assets** and select **Apps**.

Search for **Jira** and select the **Jira** app.

The Jira app settings will open. Fill in the following:

* **Name** - The name of your Jira asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
* **Type** - **URL** to show a board or dashboard from its link, or **Embed** to paste an embed code. You can't change this after saving.
* **URL** - The Jira address you copied. (With **Embed**, paste your embed code into **Embed Code** instead.)
* **Update Interval** - How often the app checks Jira for updates, measured in seconds. The default is 600 (every 10 minutes). Set it to 0 to check only when the app first loads.
* **Sign in with Credential** - Turn this on so OptiSigns can sign in to Jira for you. See [**Signing In to Jira**](#SigningInToJira) below.

Now hit **Save**. You'll have created a Jira app, and it will appear in your **Files/Assets**.

---

## Signing In to Jira

Most Jira boards and dashboards are private, so OptiSigns needs to sign in to show them. Turn on **Sign in with Credential** and fill in the **Sign In** section:

* **Username/Email** - The Jira login the screen should use.
* **Password** - The password for that login.
* **Master Password** - Optional. Check **Use master password** to add an extra layer of encryption to the saved login. If you use it, you'll need to enter the master password once in the OptiSigns app on each device.

The first time the app plays on a device, Jira may email a verification code to that account. Connect a keyboard and mouse to the device to enter it. After that, Jira remembers the device.

|  |
| --- |
| **NOTE** |
| If a dashboard displays empty, check its sharing settings in Jira. A dashboard shared publicly can skip the sign-in step and come up blank. Making it private lets OptiSigns sign in and load it.  **TIP:** Sign-in isn't available with the **Embed** type. Use **URL** for anything that needs a login. |

---

## Deploying a Jira App

To push your Jira app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

The **Select Asset** window will open. Search for your Jira app, click it, then hit **Select**.

Back in **Edit Screen**, hit **Save**. Your Jira board will now display on your screen.

Your Jira app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).