# How to Use the Dropbox App

**Article ID:** 360050665413
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360050665413-How-to-Use-the-Dropbox-App
**Last Updated:** 2026-10-01T21:20:35+00:00
---

With OptiSigns, you can quickly put images, videos from your Dropbox on your digital signage screens by using the Dropbox app. The app will create a playlist for files in your Dropbox, any changes, additions or removals will sync automatically. This allows you to quickly update, share contents within your team without needing to login to OptiSigns portal.

With the OptiSigns Dropbox app you can:

* Connect to Dropbox and choose a folder with images and videos
* Choose the timing, duration of your images/videos
* Choose transition effect between your files

## **Let's jump in and get started:**

First, you will need to have your screens set up and paired. For more information on how to do that, click [here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv).

Then log on to our portal: <https://app.optisigns.com/>

Within the OptiSigns portal, go to **Files/Assets > Apps**, then find the Dropbox app.

Click Dropbox app:

Click "Sign in with Dropbox".

Sign in and allow OptiSigns to access your Dropbox.

Select the folder you want to use:

 Enter information for your Dropbox app

* Name: Name of your Dropbox App, this is the name of the wall in your asset list. It will **not** be displayed on your screens.
* Transition Effects: Transition effect between your images, videos in the folder.
* Transition Speed: How fast you want your transitions to animate.
* Duration for Image: How long each image should show on your screen. The default is 10 seconds.
* Max Video Duration: Default is 0, which means the app will play each video till the end. You can set it to some other values to cut off long videos. For example, if you set this value to 60 seconds and a video is longer than 60s, it will get cut off at 60s to play next item. If a video is shorter than 60s, it will play the duration of the video.

Click **Advanced** to see more settings:

* Force Sync Interval: How often, in hours, OptiSigns runs a full sync of your Dropbox folder. Changes in your folder are normally picked up automatically; the forced sync is a scheduled refresh that catches anything that was missed. The default is 12 hours, and you can set any value from 1 to 24. Use a lower value if changes need to reach your screens sooner.

Click **Save**.  
Depending on how many files you have in the folder, **it may take a moment** to sync to OptiSigns, as all the files will be synced and copied to our servers.

Files will be sorted and played by name. You can control the order of playback by changing the name of the files in your Dropbox.

---

## **That's all! Congratulations!**

You have created your Dropbox app.  
You can change the wall any time by clicking on it in the Files/Assets tab.

You can assign the newly created app to your screen by going to Screens, click Edit screens and assign the wall to screens that you want.

You can put the created Dropbox app in a Playlist or Schedule too.

**Notes:**

When files are changed, added or removed in your Dropbox folder, OptiSigns will automatically sync the changes. You can check when the last change was synced and which file was synced last by opening the app modal again.

You can also force a refresh and sync by clicking the Refresh Data button.

**Limitations:**

* Only image and video files are supported. If there are other files in the folder, they will be ignored.
* To ensure good performance of the app, the maximum size is 100MB per file, and the maximum number of files supported in a folder is 200. If you have big video files, it's better to upload directly to OptiSigns; and if you have more than 200 files, you can split them up in multiple Dropbox folders.
* The Dropbox app with Teams features requires a workaround to use properly, as it uses a different API from personal accounts. To get around this limitation:
  + **Create a personal folder** within your Dropbox account and upload your content there. You should then be able to create and access it within the **OptiSigns portal**.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)