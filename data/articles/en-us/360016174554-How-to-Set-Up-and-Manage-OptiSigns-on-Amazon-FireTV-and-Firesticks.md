# How to Set Up and Manage OptiSigns on Amazon FireTV and Firesticks

**Article ID:** 360016174554
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360016174554-How-to-Set-Up-and-Manage-OptiSigns-on-Amazon-FireTV-and-Firesticks
**Last Updated:** 2026-11-04T17:44:59+00:00
---

Turn a TV with an Amazon Fire TV Stick into a digital sign. Install the OptiSigns app from the Amazon Appstore, pair it with your account, and manage what it shows from the OptiSigns portal.

This article also covers the Fire TV settings that keep OptiSigns running smoothly, from clearing the app's cache to a full factory reset.

|  |
| --- |
| **IMPORTANT** |
| Amazon is removing digital signage support from Fire TV devices, and OptiSigns will end support for Fire TV Sticks in the near future. For a new screen, we recommend the [OptiSigns Android Stick Player](https://links.optisigns.com/szzk) or the [Amazon Signage Stick](https://support.optisigns.com/hc/en-us/articles/34087061669523). |

---

## Which Fire TV Devices Work with OptiSigns?

Whether a Fire TV can run OptiSigns unattended depends on its operating system:

* **Fire OS 7** - Works, including starting OptiSigns automatically when the device powers on. This covers the Fire TV Stick 4K (Gen 1), older Fire TV Sticks and the [Fire TV Stick Lite](https://www.amazon.com/fire-tv-stick-lite-latest-alexa-voice-remote-lite/dp/B091G4YP57/). The Lite is slow, so we don't recommend it even though it works. Amazon may update these devices to a newer OS in the future.
* **Fire OS 8** - Not supported. Since October 2024, [Amazon no longer lets apps start automatically](https://www.aftvnews.com/amazon-blocks-long-running-fire-tv-capability-breaking-popular-apps-with-no-warning-and-giving-developers-the-runaround/) on Fire OS 8. This covers the current [Fire TV Stick 4K](https://www.amazon.com/all-new-amazon-fire-tv-stick-4k/dp/B0BP9MDCQZ/), the [Fire TV Stick 4K Max](https://www.amazon.com/all-new-amazon-fire-tv-stick-4k-max/dp/B0BP9SNVH9/) and TVs with Fire TV built in. If you are comfortable with ADB commands, see [How to Enable Auto-Start on Fire OS 8 Devices](https://support.optisigns.com/hc/en-us/articles/23274673797139).
* **Vega OS** - Works with limits. This covers the [Fire TV Stick 4K Select](https://amzn.to/3PaJaRD) and the [Fire TV Stick HD](https://amzn.to/4efNBop). OptiSigns must be opened by hand each time the device starts, and the app goes to sleep unless a video plays every few minutes, so it can't show images on their own. Add at least one video to your Playlist, between your images.

If you already have a Fire OS 7 device, read on to set it up.

---

## What You'll Need

* An OptiSigns account - any plan
* An Amazon Fire TV Stick or Fire TV running Fire OS 7 or Vega OS
* The power adapter and cable that came with your Fire TV
* A Wi-Fi connection and an Amazon account
* A TV with a free HDMI port

---

## Setting Up Your Fire TV

Plug the Fire TV Stick into your TV's HDMI port and connect it to power.

|  |
| --- |
| **NOTE** |
| Use the power adapter and cable that came with the Fire TV. It's tempting to power it from the TV's USB port, but a TV's USB port can't supply enough power to keep a Fire TV running reliably. |

Turn on the Fire TV and follow the on-screen instructions to connect to Wi-Fi and sign in with your Amazon account. The Fire TV needs an internet connection to work.

---

## Installing the OptiSigns App

On the Fire TV home screen, go to **Find** and select **Search**.

Type **OptiSigns**. Fire TV search can be fiddly while you type, so once you've entered the name, press down on the remote until **Optisigns** is highlighted, then select it.

Select **Download** on the OptiSigns Digital Signage app.

Once the app is installed, open it. It asks whether to start automatically when the device starts up. Select **Yes**, unless you want to open the app by hand every time.

---

## Pairing Your Fire TV with OptiSigns

When the app opens, it shows a pairing code:

On your computer, go to [app.optisigns.com](https://app.optisigns.com/app/screenManagement) and sign in. If you don't have an account yet, you can create one, or sign in with Google, Facebook or Microsoft.

On the **Screens** page, click **Add Screen**.

Type the pair code shown on your TV, then click **Pair**.

The TV now shows **Paired**, and you're ready to assign content.

To get content onto your new screen, see:

* [Set Up & Add a Screen](https://support.optisigns.com/hc/en-us/articles/360016374813)
* [How to Upload & Manage Your Files/Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
* [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
* [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)

---

## Managing Your Fire TV

Everything in this section starts from the Fire TV's **Settings**. Press **Home** on the remote, then select the gear icon at the right of the menu bar.

### Keep OptiSigns Running

A Fire TV can pause OptiSigns after 4 hours without a button press and ask "Are you still watching?". To stop it, turn off **Still Watching**.

In **Settings**, select **Preferences**.

Select **Data Usage Monitoring**.

Select **Still Watching** to turn it **OFF**.

Open OptiSigns again. It won't be interrupted by the prompt anymore.

### Allow OptiSigns to Use Storage

OptiSigns downloads your images and videos to the device before playing them. If it isn't allowed to use the Fire TV's storage, your screen can stay black.

In **Settings**, select **Applications**.

Select **Manage Installed Applications**.

Select **OptiSigns**.

Select **Permissions**.

**Storage** is set to **DENY**. Select it to change it to **ALLOW**.

Open OptiSigns again, and your content will start playing.

### Clear the OptiSigns App's Cache or Data

If OptiSigns is slow or not working correctly, its cached data may be corrupted or too large. Clearing the cache usually fixes it.

In **Settings**, go to **Applications** > **Manage Installed Applications** > **OptiSigns**, as in the steps above. Select **Clear cache**.

If the app still doesn't work correctly, come back to the same menu and select **Clear data**. This removes the app's downloaded content too, so it downloads everything again.

|  |
| --- |
| **NOTE** |
| If OptiSigns still doesn't work after clearing its data, [Reinstall the OptiSigns App](#ReinstallTheOptiSignsApp). As a last resort, [Factory Reset Your Fire TV](#FactoryResetYourFireTV). |

### Turn On Automatic App Updates

The Fire TV keeps OptiSigns up to date by itself, as long as automatic updates are on. They are on by default.

To check, go to **Settings** > **Applications** and select **Appstore**.

Make sure **Automatic Updates** is **ON**. If it isn't, select it to turn it on.

### Update Fire OS

If apps such as weather or social media don't display correctly, the Fire TV's own software may be out of date.

In **Settings**, select **My Fire TV**.

Select **About**.

Select **Install Update**. If there's no update waiting, this option reads **Check for Updates** instead.

The update downloads and installs, then the Fire TV restarts by itself. If it doesn't restart, press and hold **Select** and **Play/Pause** on the remote together for 5 seconds.

### Change the Time Zone

If your Schedules start or end at the wrong time, check the Fire TV's time zone.

In **Settings**, select **Preferences**, then **Time Zone**.

Select **Time Zone** again.

Select your region, then your time zone. The Fire TV sets its clock from your choice.

### Reinstall the OptiSigns App

Reinstalling OptiSigns is a common fix when the app keeps misbehaving.

In **Settings**, go to **Applications** > **Manage Installed Applications** > **OptiSigns**, as in the steps above. Select **Uninstall**.

Select **Uninstall** again to confirm.

Then install the app again from the Appstore, as in [Installing the OptiSigns App](#InstallingTheOptiSignsApp) above. The Fire TV keeps its pairing, so you don't need to pair it again.

### Install the OptiSigns App from an APK File

We strongly recommend installing OptiSigns from the Amazon Appstore, so Amazon keeps it up to date for you. If you can't use the Appstore, you can install the app file (APK) directly.

In **Settings**, select **My Fire TV**, then **Developer options**.

Select **Apps from Unknown Sources**.

Select **Turn On** to accept the warning.

From the Appstore, install the free **Downloader** app.

Open Downloader and enter `https://links.optisigns.com/fireos`. When the file has downloaded, select **Install**. OptiSigns then appears with your other apps on the Fire TV home screen.

### Factory Reset Your Fire TV

If nothing else has worked, a factory reset returns the Fire TV to the state it left the factory in.

|  |
| --- |
| **IMPORTANT** |
| A factory reset deletes all of your apps, data and settings, including your Amazon sign-in. You'll need to set up the Fire TV, install OptiSigns and pair it again. |

In **Settings**, select **My Fire TV**, then **Reset to Factory Defaults**.

Select **Reset**. The reset takes a few minutes.

---

## Connecting a Keyboard and Mouse

To sign in to content behind a login, such as a Jira board or a Power BI or Tableau dashboard, you need to type on the Fire TV. Pair a [Bluetooth keyboard](https://www.amazon.com/Logitech-Illuminated-Living-Room-Keyboard-Touchpad/dp/B00ZOPVSKW/), or use a [USB hub adapter](https://www.amazon.com/gp/product/B00LTHBCNM/) to connect a wired or wireless USB keyboard and mouse.

|  |
| --- |
| **NOTE** |
| Set the switch on the USB hub adapter to **OTG**. |

---

## Restarting OptiSigns Remotely

If you're not on site, you can check whether a Fire TV is on and restart OptiSigns from your phone with the Amazon Fire TV app, available for iPhone and Android.

Set this up while you're on site:

* The Fire TV must be signed in to your Amazon account.
* Sign in to the Fire TV app on your phone with the same Amazon account.
* Write down each device's name, so you know which is which.

The app lists the Fire TVs it can reach. If a device isn't listed, it's powered off or has lost its Wi-Fi connection.

To restart OptiSigns, select the Fire TV in the list. Press **Back** to close OptiSigns, then open your apps list.

Select OptiSigns to open it again.

---

## Troubleshooting

For black screens, network problems and power issues, start with the [Amazon TV / FireStick Troubleshooting Guide](https://support.optisigns.com/hc/en-us/articles/27463953562899). These are the fixes covered in this article:

#### "Are you still watching?" appears, or OptiSigns stops after 4 hours

Turn off Still Watching. See [Keep OptiSigns Running](#KeepOptiSignsRunning).

#### The screen stays black

Allow OptiSigns to use the Fire TV's storage. See [Allow OptiSigns to Use Storage](#AllowOptiSignsToUseStorage).

#### Weather or social media apps don't display correctly

Update the Fire TV's software. See [Update Fire OS](#UpdateFireOS).

#### Schedules start or end at the wrong time

Check the Fire TV's time zone. See [Change the Time Zone](#ChangeTheTimeZone).

#### OptiSigns is slow or stops working

Work through these in order, checking after each one: [Clear the OptiSigns App's Cache or Data](#ClearTheOptiSignsAppsCacheOrData), then [Reinstall the OptiSigns App](#ReinstallTheOptiSignsApp), and finally [Factory Reset Your Fire TV](#FactoryResetYourFireTV).

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).