# How to Use the Dropbox App

**Article ID:** 360050665413
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360050665413-How-to-Use-the-Dropbox-App
**Last Updated:** 2026-10-16T16:32:20+00:00
---

With the Dropbox app, it's possible to play the images and videos in a Dropbox folder on your screens. The app turns the folder into a playlist and keeps it in sync, so when you add, change or remove a file in Dropbox, your screens update too. Your team can update what's on screen without ever signing in to OptiSigns.

Let's get started.

---

## What You'll Need

* An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
* A Dropbox account with access to the folder you want to show
* An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
* A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))

---

## Creating a Dropbox App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

Search for **Dropbox** and select the **Dropbox** app.

Click **Sign in with Dropbox**.

Sign in to Dropbox and allow OptiSigns to access your Dropbox.

Choose the folder you want to show on your screens:

The Dropbox app settings will open.

Fill them in:

* **Name** - The name of your Dropbox asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
* **Folder** - The Dropbox folder you chose.
* **Transition Effects** - The effect between each image and video. Choose from **None**, **Fade**, **Slide from Right**, **Slide from Left**, **Rotate In**, **Flip** or **Gallery**.
* **Transition Speed** - How fast the transition plays. Choose **Slow**, **Medium** or **Fast**, or **Custom** to set your own speed.
* **Duration for Image** - How long each image shows, in seconds. The default is **10**.
* **Max Video Duration** - The longest each video plays, in seconds. The default is **0**, which plays every video to the end. For example, at **60**, a 90-second video is cut off after 60 seconds, while a 45-second video plays in full.

### Advanced

Click **Advanced** for more options:

* **Force Sync Interval** - How often, in hours, OptiSigns runs a full sync of your folder. Changes are normally picked up automatically, and this scheduled sync catches anything that was missed. The default is **12**, and you can set any value from **1** to **24**.

Now hit **Save**. You'll have created a Dropbox app, and it will appear in your **Files/Assets**. Depending on how many files are in your folder, the first sync may take a moment, as every file is copied to OptiSigns.

|  |
| --- |
| **TIP** |
| Files play in order by name. To control the order, rename your files in Dropbox, for example by starting each name with **1**, **2**, **3**. |

### Checking and Refreshing a Sync

When files are added, changed or removed in your Dropbox folder, OptiSigns syncs the changes automatically. To see when the last change was synced and which file was synced last, open the app again from **Files/Assets**. To sync right away, click **Refresh Data**.

---

## Deploying a Dropbox App

To push your Dropbox app to a screen, go to the **Screens** tab, then click **Edit** next to the screen you want to display it on.

The **Edit Screen** pop-up will appear. Select **Asset** under **Content Type**, then hit **Change** next to **Selected Asset**.

The **Select Asset** window will open. Search for your Dropbox app, click it, then hit **Select**.

Back in **Edit Screen**, hit **Save**. Your Dropbox files will now play on your screen.

Your Dropbox app can also be displayed in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

## Supported File Types

The Dropbox app syncs these file types from your folder:

* **Images** - **JPG**, **PNG**, **BMP** and **GIF**
* **Videos** - **MP4**. For the best compatibility, we recommend MP4 videos encoded in **H.264**. If a video won't play, see [How to re-encode video files](https://support.optisigns.com/hc/en-us/articles/360042143753).

Any other files in the folder, such as documents or spreadsheets, are skipped. For the full list of file types OptiSigns supports on its own, see [What types of files are supported?](https://support.optisigns.com/hc/en-us/articles/360016342373)

---

## Limitations

* Only the file types listed under **Supported File Types** are synced. Any other files in the folder are ignored.
* Sub-folders aren't supported. Only files directly inside the folder you choose are synced.
* To keep the app running smoothly, keep each file to 100 MB or less, and keep up to 200 files per folder. For large videos, we recommend uploading them directly to OptiSigns. For more than 200 files, split them across several folders.
* Dropbox Teams folders use a different API from personal accounts. As a workaround, create a folder in your personal Dropbox space, upload your content there, and choose that folder in OptiSigns.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).