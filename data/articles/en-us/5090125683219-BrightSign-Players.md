# BrightSign Players

**Article ID:** 5090125683219
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/5090125683219-BrightSign-Players
**Last Updated:** 2026-10-29T17:44:28+00:00
---

BrightSign makes commercial-grade digital signage players known for their reliability. OptiSigns runs on BrightSign players, and we recommend the HD, XD and XT product lines for the best performance.

You can set up OptiSigns on a BrightSign player in two ways:

* **With BSN.Cloud:** create a setup file in BrightAuthor:connected that installs OptiSigns as a partner application.
* **Standalone:** copy the OptiSigns autorun file to an SD card.

Either way, the player downloads your content to its own storage, so it keeps playing if the internet drops for a while.

---

## Set Up with BSN.Cloud

Download and install [BrightAuthor:connected](https://www.brightsign.biz/resources/software-downloads/) from BrightSign.

Open BrightAuthor:connected and sign in to your BSN.Cloud account.

Go to **Admin** > **Device Setup**.

Enter a **Package Name** and a **Device Name**.

Under **Device Type**, select **Partner Application**, then select **Select a Partner Application** and choose **OptiSigns**.

Select **Save Setup Files** to save the setup files.

Copy the setup files to the root folder of your SD card.

Make sure the BrightSign player is connected to the internet, then insert the SD card and power it on.

The player reads the setup files and installs OptiSigns. This takes a few minutes, and the player may restart a few times. When it's done, OptiSigns opens and shows a pairing code. Then pair the player with your account, as shown below.

---

## Set Up in Standalone Mode

[Download the OptiSigns autorun file](https://links.optisigns.com/brightsign) (**autorun.zip**).

Copy **autorun.zip** to the root folder of your SD card. Don't unzip it.

|  |
| --- |
| **IMPORTANT** |
| The SD card must be formatted as FAT32. NTFS doesn't work for this setup. |

Make sure the BrightSign player is connected to the internet, then insert the SD card and power it on.

The player unpacks the file, installs OptiSigns and restarts. This takes a few minutes, and the player may restart more than once. When it's done, OptiSigns opens and shows a pairing code.

---

## Pair the Player with Your Account

Go to [app.optisigns.com](https://app.optisigns.com/) and log in. If you don't have an account yet, select **Create Account**. You can also log in with Google, Microsoft or Facebook.

On the **Screens** page, select **Add Screen**.

Enter the pairing code shown on the player in **Pair code**, then select **Pair**.

**Note:** Codes are case-sensitive, and the portal enters them in capitals. If the code on your player has lowercase letters, select **Use lowercase pairing code** and type it exactly as shown. If pairing fails with a case error, the portal switches this on for you, so check the code and select **Pair** again.

---

## Keep the Player Up to Date

OptiSigns starts by itself every time the BrightSign player powers on, so you don't need to open it after a restart.

With **Auto Update** on, the player downloads new OptiSigns versions by itself and restarts to install them. You'll find **Auto Update** in the player's side menu under **Advanced Options**.

If you still have trouble running OptiSigns, your BrightSign software may be out of date. Download the latest version from [BrightSign software downloads](https://www.brightsign.biz/resources/software-downloads/) and update the player.

---

## Update the BrightSign Registry to Use a Newer Chromium

Some content, especially Power BI, needs a newer version of Chromium than the BrightSign player uses by default. You can switch it with a registry command.

Open BrightAuthor:connected and select **Admin**.

Find your BrightSign player's IP address.

On a computer on the same network as the player, enter the IP address in your browser. The player's settings page opens.

Then, select the **Registry** tab.

5. In **Command**, enter `registry write html widget_type chromium110`.

Select **Submit**. The result shows `widget_type = 'chromium110'`.

Restart the player. It doesn't restart by itself after a registry change, so restart it manually or select **Reboot Player** on the **Control** tab.

---

## Next Steps

Your player is ready to show content. To get started:

* [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
* [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
* [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)
* [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)

If you have questions or feedback, contact our support team at support@optisigns.com.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).