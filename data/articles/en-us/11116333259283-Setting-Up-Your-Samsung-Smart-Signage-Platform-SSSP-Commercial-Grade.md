# Setting Up Your Samsung Smart Signage Platform (SSSP - Commercial Grade)

**Article ID:** 11116333259283
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/11116333259283-Setting-Up-Your-Samsung-Smart-Signage-Platform-SSSP-Commercial-Grade
**Last Updated:** 2026-10-29T20:48:30+00:00
---

Samsung Smart Signage Platform (SSSP) displays are some of the most popular commercial-grade screens. OptiSigns runs natively on them: the app saves your content on the display so it keeps playing offline, and it updates itself when a new version is released.

This article is for Samsung SSSP displays only. Your display should be marked as "SSSP" or "Samsung Smart Signage Platform". Samsung also sells consumer Smart TVs that run Tizen OS but aren't SSSP displays. To check your model, see the [Samsung Smart Signage Platform (SSSP) Supported Model List](https://support.optisigns.com/hc/en-us/articles/17882306279315).

**Note:** If you have a consumer Samsung Smart TV running Tizen OS, follow [How to Install OptiSigns on Samsung Tizen Smart TVs](https://support.optisigns.com/hc/en-us/articles/14726570281875) instead.

---

## Choose Your Installation Option

You install OptiSigns through the display's **URL Launcher**, using the app address **https://t.optisigns.com**. There are two ways to get there:

* **Option 1: Install on an SSSP display that's already in use.** Use this if your display is already set up.
* **Option 2: Install on a brand new SSSP display.** Use this if your display is new or was just factory reset. You set up OptiSigns during Samsung's first-time setup.

For a visual walkthrough of both options, watch our [SSSP installation video](https://www.youtube.com/watch?v=uraaVW53dAQ).

The menus look different on current and older SSSP models. Each option below shows both.

---

## Option 1: Install on an SSSP Display That's Already in Use

Make sure the display is connected to the internet before you start.

### Current and New Models

Press the **Home** button on the remote.

Select **App Management**.

If an app is already installed, select **Uninstall** first. Continue once no app is installed.

Select **Install Custom App**.

Enter **https://t.optisigns.com**, then select **Go**.

### Older Models

Press the **Home** button on the remote.

Select **URL Launcher Settings**.

If an app is already installed, select **Uninstall** first. Continue once no app is installed.

Select **Install Web App**.

Enter **https://t.optisigns.com**, then select **Done**.

### Open OptiSigns

The OptiSigns app downloads automatically. When it's installed, it opens and shows a pairing code. Keep it on screen; you'll need it to pair.

Next, follow the steps in **Pair the Display with Your Account** below.

---

## Option 2: Install on a Brand New SSSP Display

Use this option if your display is new or was just factory reset. Samsung's first-time setup walks you through each screen.

**Note:** If a screen doesn't move on by itself, press the right arrow on the remote and select **Next** at the top right of the screen.

|  |
| --- |
| **IMPORTANT** |
| Set the **Display Orientation** correctly during setup and ***don't skip it***. You can't change it remotely from OptiSigns, only on-site with the remote.  Set the correct date and time during setup and ***don't skip it***. If the date or time is wrong, the display can't connect to OptiSigns. |

### Current and New Models

Select your language.

Connect to your network.

On **Smart Signage Privacy Notice**, select **OK**.

On **Installation Type**, select **Basic Setup**.

On **Display Orientation**, select the orientation the display is mounted in.

On **Player Selection**, select **Custom App**.

Enter **https://t.optisigns.com**, then select **Go**.

On **Connect to RM Server**, select **Skip**.

On **Set Current Time**, enter the correct date and time, then select **Next**.

On **Set PIN**, enter a new PIN or leave it blank, then select **Next**. A PIN is optional.

Setup is complete.

A menu appears at the bottom of the screen. If it doesn't, press **Home** on the remote. Select **Custom App** to open OptiSigns.

### Older Models

Older models go through the same steps in a different order.

Select your language.

On **Installation Type**, select **Basic Setup**.

On **Display Orientation**, select the orientation the display is mounted in.

Connect to your network.

On **Smart Signage Privacy Notice**, select **Agree**.

On **Play via**, select **URL Launcher**.

Enter **https://t.optisigns.com**, then select **Done**.

On **Connect to RM Server**, select **Skip**.

On **Clock Set**, enter the correct date and time. This is critical, as OptiSigns will set to your timezone, and relies on this information for scheduling.

Depending on the software version, you may be asked to set a PIN. Create one or skip that step.

On **Complete**, select **Done**.

A menu appears at the bottom of the screen. If it doesn't, press **Home** on the remote. Select **URL Launcher** to open OptiSigns.

### Open OptiSigns

OptiSigns opens and shows a pairing code. Keep it on screen; you'll need it to pair.

---

## Pair the Display with Your Account

1. Go to [app.optisigns.com](https://app.optisigns.com/) and log in. If you don't have an account yet, select **Create Account**. You can also log in with Google, Microsoft or Facebook.

2. On the **Screens** page, select **Add Screen**.

3. Enter the pairing code shown on the display in **Pair code**, then select **Pair**.

**Note:** Codes are case-sensitive, and the portal enters them in capitals. If the code on your display has lowercase letters, select **Use lowercase pairing code** and type it exactly as shown. If pairing fails with a case error, the portal switches this on for you, so check the code and select **Pair** again.

Once the display is paired, URL Launcher opens OptiSigns each time the display turns on.

---

## Limitations

* Samsung SSSP displays output graphics at 1080p only. Take care when you use 4K videos.
* SSSP displays can process only one video at a time, so the next video can't be preloaded. Video-to-video transitions aren't as smooth as on players that preload videos.

---

## SSSP 10 (Tizen 6.5)

On SSSP 10 models, Samsung's **Seamless Video Playback** feature can cause screen glitches. Seamless playback is meant to play videos back to back without the screen going black in between.

Known workarounds:

* Keep all videos encoded in H.264, but use the same resolution for all of them. Don't mix HD (1920x1080) and 4K (3840x2160) videos.
* Re-encode all videos to H.265, for example with [HandBrake](https://handbrake.fr/). This lets your videos keep their own resolutions.

---

## Next Steps

Your display is ready to show content. To get started:

* [How to Upload & Manage Your Files/ Assets](https://support.optisigns.com/hc/en-us/articles/360016247974)
* [How to Create & Use Playlists](https://support.optisigns.com/hc/en-us/articles/28295104605843)
* [Creating and Using Schedules with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360016981853)
* [Set up & add a screen](https://support.optisigns.com/hc/en-us/articles/360016374813)

If you have questions or feedback, contact our support team at support@optisigns.com.

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).