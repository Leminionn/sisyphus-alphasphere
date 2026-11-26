# Displaying SharePoint Sites on OptiSigns

**Article ID:** 4414539282067
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4414539282067-Displaying-SharePoint-Sites-on-OptiSigns
**Last Updated:** 2026-11-25T18:05:11+00:00
---

|  |
| --- |
| **NOTE** |
| The SharePoint app is available to customers with a Standard plan or above. |

With OptiSigns, it's possible to showcase your SharePoint site on any of your screens. Even sites that require a login can be shown, including accounts that use two-step verification. All you'll need is a URL to your SharePoint site and a valid Microsoft account.

If you want to display SharePoint News, check out our article on [Connecting SharePoint News to OptiSigns](https://support.optisigns.com/hc/en-us/articles/55450681344915).

Let's get started.

---

## What You Need

* An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
* A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))
* A valid Microsoft username and password with access to the SharePoint page
* A SharePoint URL
* If the Microsoft account uses two-step verification, the secret key from its authenticator app setup

---

## Setting Up the SharePoint App

First, head to the SharePoint page you'd like to display on your screens.

Next, hit **Share**. Click **Copy link to page**.

The below screen should appear. Hit **Copy**.

This is the URL you will use to set up a SharePoint app in OptiSigns.

Next, log in to the [OptiSigns portal](https://app.optisigns.com/). Go to **Files/Assets** and select **Apps**.

Search for **SharePoint** and select the **SharePoint** app.

The SharePoint app settings will open. Fill in the following:

* **Name** - The name of your SharePoint asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
* **URL** - The address of your SharePoint page. This is the URL you copied earlier.
* **Sign in with Credential** - Turn this on so OptiSigns can sign in to SharePoint for you. Most SharePoint sites require a sign-in.

Turning on **Sign in with Credential** opens the **Sign In** section:

* **Master Password** - Optional. When checked, you'll set a Master Password for extra encryption. Your password is already encrypted with OptiSigns; this adds another layer, so that even OptiSigns cannot decrypt it. See the FAQ below for more detail.
* **Username/Email** - Your Microsoft account username.
* **Password** - Your Microsoft account password.
* **Secret 2FA** - Only for accounts with two-step verification. See **Signing In With Two-Step Verification** below. Leave it empty if the account doesn't use it.
* **Recorded 2FA Code** - A placeholder for the code step. Leave it as **123456**; the screen replaces it with the live code each time it signs in.
* **Delay Execute 2FA JavaScript** - How many seconds the screen waits before entering the code. The default is 5.
* **Delay Execute JavaScript** - How many seconds the screen waits before it starts the sign-in steps. The default is 5.

Please note that the username and password you enter need access to the SharePoint page URL.

Finally, click **Save**.

You've successfully created a SharePoint asset! You can use it on your screens just like a regular web page: on its own, in a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843), a Schedule, or a zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

## Signing In With Two-Step Verification

Many Microsoft accounts ask for a code from an authenticator app when they sign in. The screen can now enter that code by itself, so no one has to type a code at the screen.

To set it up, you'll need the account's authenticator **secret key**. In the Microsoft account's **Security info** page, add an **Authenticator app** sign-in method and choose to use a different authenticator app. When the QR code appears, click **Can't scan image?** to show the **Secret key**. Copy that key and paste it into **Secret 2FA**. You can add the same key to your own authenticator app to finish the setup with Microsoft.

The key is stored encrypted. Leave **Recorded 2FA Code** as **123456**.

If the screen gets stuck on the code step, raise **Delay Execute 2FA JavaScript** so the code page has more time to load before the screen types into it. If it gets stuck before that, on the username or password step, raise **Delay Execute JavaScript**.

|  |
| --- |
| **NOTE** |
| Accounts without two-step verification keep working exactly as before. Leave **Secret 2FA** empty, and nothing changes for your existing SharePoint apps. |

---

## Frequently Asked Questions

Here we'll tackle the most common issues and questions we get about displaying SharePoint on OptiSigns.

#### I tried to get SharePoint on my screen, but it's prompting me to sign in! What's going on?

The first time OptiSigns connects to SharePoint, it uses a Web Scripting feature to sign you in automatically with the username and password you entered in the app. You'll know it's working when your username fills in the proper field by itself after a few seconds.

This takes about a minute the first time the asset signs in. After that, it should remember your login.

If the account uses two-step verification and the screen stops at the code prompt, check that **Secret 2FA** holds the account's secret key, and that **Recorded 2FA Code** is still **123456**.

#### I want to display multiple SharePoint pages. How can I do that?

The easiest way to display several SharePoint pages is to create several SharePoint assets, then use them [in a Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843).

#### I'd like to display only SharePoint News, and have it automatically update. Can I do that?

Yes! Please see our complete article on [Creating Custom News Feeds with SharePoint](https://support.optisigns.com/hc/en-us/articles/35337746613139) for more information.

#### I'm trying to display SharePoint on my Samsung SSSP or LG webOS TVs and all I'm seeing is a blank screen. Why won't it work?

Microsoft requires a minimum Chromium version of 95 for their apps to display. These TVs typically don't update very often. This is a Microsoft requirement, and there is little we can do on our end.

If you have one of these TVs and wish to display SharePoint, we recommend our [Pro Player](https://shop.optisigns.com/products/optisigns-digital-signage-player).

#### How does the encryption of my password work at OptiSigns? If I input it, will I be at risk?

Here's how the encryption flow works:

When you enter your username, password and 2FA secret key into the OptiSigns SharePoint app, they are used as a [Web Script](https://support.optisigns.com/hc/en-us/articles/1500012522362). This script is encrypted in your browser, transferred securely using HTTPS/SSL and stored on our servers.

It is then sent the same way to your devices, and decrypted on the device before it runs on the target website. In this case, that's SharePoint.

If you want to add security by using a Master Password and our Zero Knowledge Encryption framework, you will have to enter your Master Password when:

* Creating or editing assets
* One time on each device, so it knows how to decrypt

The Master Password can be entered on each device under the **Advanced Options** menu, under **Master Password**.

Then enter the Master Password. It needs to match the Master Password entered on your assets.

This ensures no one, not even OptiSigns, can decrypt your password under any circumstance.

---

## Related Articles

* [Connect SharePoint News to OptiSigns Digital Signage](https://support.optisigns.com/hc/en-us/articles/55450681344915?ref=related)
* [How to Use Microsoft PowerPoint with OptiSigns](https://support.optisigns.com/hc/en-us/articles/4414355658899?ref=related)
* [How to Use Microsoft Excel Online with OptiSigns](https://support.optisigns.com/hc/en-us/articles/4529298306963?ref=related)
* [How to Display Microsoft Power BI Dashboards & Reports with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360024859713?ref=related)
* [How to Create Custom News Feeds with OptiSync](https://support.optisigns.com/hc/en-us/articles/35337746613139?ref=related)

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).