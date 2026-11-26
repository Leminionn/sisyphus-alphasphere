# How to Use Google Sheets with OptiSigns

**Article ID:** 360056977214
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360056977214-How-to-Use-Google-Sheets-with-OptiSigns
**Last Updated:** 2026-11-25T18:06:56+00:00
---

Google Sheets is one of the most popular spreadsheet tools online. With the OptiSigns Google Sheets app, you can show a sheet on your screens and have it update on its own whenever the sheet changes.

Let's get started.

---

## What You'll Need

* An OptiSigns account - [**Standard Plan** or higher](https://www.optisigns.com/pricing)
* An [OptiSigns-enabled device](https://support.optisigns.com/hc/en-us/articles/360021855653)
* A screen, set up and paired with OptiSigns ([see our Getting Started guide](https://support.optisigns.com/hc/en-us/articles/18823504383891))
* A Google Sheet, and for a private sheet, a Google account that can open it

---

## How It Works

The Google Sheets app works with two kinds of links:

* **Public links** - A sheet published with **Publish to web**, or shared with **Anyone with the link**. No Google account is needed. Your screens show the live sheet, cells only, fitted to the screen, and reload it on a timer you set.
* **Private links** - Any other sheet. You sign in with a Google account that can open it. OptiSigns turns the sheet into pages that fit your screen and updates them when Google tells us the sheet has changed.

Pick public if the sheet holds nothing sensitive and you want the quickest setup. Pick private if the sheet must stay private.

---

## Creating a Google Sheets App

From the OptiSigns portal, go to **Files/Assets** and select **Apps**.

Search for **Google Sheets** and select the **Google Sheets** app.

The Google Sheets app settings will open. Everything you need to start is on one screen:

* **Name** - The name of your Google Sheets asset. This is for organizational purposes within OptiSigns only and will not display on your screens.
* **URL** - The link to your sheet. Paste the sheet's Share link or its Publish to web link. If you've signed in with Google, you can click **Browse** instead to pick the sheet from your Google Drive. Browse fills in the URL and the tab for you, and the Name too if it's empty.
* **Google account** - The Google account that can open the sheet. Only private links need one.

As you paste a link, OptiSigns checks it. If the sheet can be opened, its name appears under the URL. If not, a short message tells you why.

To copy your sheet's link, open the sheet in Google Sheets and copy the address from your browser's address bar.

Next, follow the section for the kind of link you have.

---

## Using a Public Sheet

A public link needs no Google account. There are two ways to make one in Google Sheets:

* **Publish to web** - Go to **File** > **Share** > **Publish to web**. Click **Publish**, then **OK**.
* **Anyone with the link** - Click **Share**, and under **General access** choose **Anyone with the link**.

If you published the sheet, copy the link Google shows. If you shared it, copy the sheet's link instead.

Back in OptiSigns, enter a **Name** and paste the link into **URL**. You'll see **No account needed for this link** under **Google account**.

Pick the tab to show from **Select Sheet**. If you've added a tab in Google Sheets since, click **Reload Sheets** to refresh the list.

Set any **Display** and **Advanced** options you want (see **Display and Advanced Settings** below), then hit **Save**.

|  |
| --- |
| **NOTE** |
| A published sheet updates on Google's schedule, which is roughly every 5 minutes after a change. Your screens then pick up the change at their next reload, set by **Update Interval**. |

---

## Using a Private Sheet

Enter a **Name** and paste your sheet's link into **URL**. OptiSigns will tell you the sheet is private and ask for the Google account it is shared with.

Under **Google account**, click **Sign in with Google**. A Google window will open. Choose your account and click **Continue**.

Right after you sign in, choose who can use this Google account:

* **Only me** - Only you can use the account in your assets. This is the default.
* **Share with team** - Your teammates can use the account in their own assets. They just paste a sheet link and save.

OptiSigns remembers the account, so next time you can pick it from **Google account** without signing in again. To use a different account, pick another saved account or click **Add another Google account**.

Pick the tab to show from **Select Sheet**, set any **Display** and **Advanced** options, then hit **Save**.

|  |
| --- |
| **IMPORTANT** |
| The Google account must be able to open the sheet. If it can't, you'll see **The account you chose has no access to this sheet.** Share the sheet with that account in Google Sheets, or choose another account. |

---

## Display and Advanced Settings

Click **Display** to choose how your sheet looks on screen.

* **Customize Display Region** - Turn this on to show only part of the sheet. Click **Select Display Region**, then drag over the cells you want, or type a **Start cell** and **End cell**. Click **Select** to save it. You can change the region at any time.
* **Scale** - How the sheet fits the screen: **Fit to page**, **Fit to width** or **Fit to height**. Private sheets also offer **Normal (100%)** and **Custom (%)**.
* **Orientation** - Private sheets only. Choose **Portrait** for screens mounted vertically.
* **Speed** - How long each page stays on the screen when the sheet is too long to fit on one.

Click **Advanced** to choose how often your sheet updates.

* **Update Interval** - Public links only. How often your screens reload the sheet, in seconds. The default and the minimum is 600 (every 10 minutes). Set it to 0 to load the sheet only once.
* **Force Sync Interval** - Private links only. OptiSigns refreshes your sheet at least this often, in hours, even if Google sends no change notice. Choose from 1 to 24. The default is 12.

---

## How Your Sheet Updates

**Public links** show the live sheet. Your screens reload it every **Update Interval**. A published sheet can also lag by Google's own republishing delay, roughly 5 minutes.

**Private links** update in three ways:

* When you edit the sheet, Google tells OptiSigns, and your screens get the new version about 5 minutes after your last edit.
* At the **Force Sync Interval**, whether or not Google sent a notice.
* Right away when you open the asset in OptiSigns and hit **Save**.

|  |
| --- |
| **NOTE** |
| If a private sheet is edited nonstop, for example by a script or a form that writes to it every minute, each edit restarts the 5-minute wait. The sheet then updates when the edits pause, or at the next **Force Sync Interval**. |

---

## Managing Your Google Accounts

Team admins can see and manage every saved Google account in one place. Go to **Integrations** under your main menu and click the **Google Sheets** tab.

From **Google Sheets Accounts**, admins can:

* Add an account with **Add Connection**.
* Turn sharing with the team on or off with the **Shared** switch. Assets that already use an account keep updating when you stop sharing it.
* Reauthorize an account that stopped working.
* Revoke an account. Assets that use it keep showing their last pages but stop updating.

---

## Deploying a Google Sheets App

To show your sheet on a screen, go to the **Screens** tab and click **Edit** next to the screen. Select **Asset** under **Content Type**, click **Change** next to **Selected Asset**, pick your Google Sheets asset, and click **Select**. Then hit **Save**.

Your Google Sheets app can also play in a Playlist or Schedule, or as one zone of a [Split Screen](https://support.optisigns.com/hc/en-us/articles/360026559573).

---

## Troubleshooting

Here are a few of the more common issues our customers may face when using Google Sheets, and how to solve them.

#### My Sheet Stopped Updating, and the Asset Says "Connection Stopped Working"

The Google account behind the asset can no longer connect. This happens when someone changes the account's password, removes OptiSigns from the account's Google settings, or a Google Workspace admin blocks access. Your screens keep showing the last version of the sheet in the meantime.

Open the asset. The message under **Google account** tells you what happened:

* **This Google account was signed out** or **needs to sign in again** - Choose another account, or have the account owner sign in with Google again. Signing back in updates the sheet right away.
* **A team admin turned off this Google account** - Choose another account, or ask a team admin to turn it back on from **Integrations** > **Google Sheets**.
* **This Google account was removed** - Choose another account and save.

#### My Sheet Stopped Updating, and the Asset Says "No File Access"

The Google account can no longer open this sheet. The sheet may have been unshared from that account, moved or deleted. In Google Sheets, share the sheet with the account again. Or open the asset, choose another account that has access, and hit **Save**.

#### My Public Sheet Shows an Error on Screen

The link stopped working. Open the asset in OptiSigns to see why:

* **This sheet is no longer published** - Publish it again in Google Sheets with **File** > **Share** > **Publish to web**.
* **This sheet is no longer shared with Anyone with the link** - Share it with **Anyone with the link** again.
* **This sheet can't be found** - The sheet may have been deleted. Paste the link of a sheet that exists.
* **This tab was deleted from the sheet** - Choose another tab in **Select Sheet** and save the asset.

#### My Public Sheet Never Updates

Check **Update Interval** under **Advanced**. If it's 0, your screens load the sheet only once. Set it to 600 or more. For a published sheet, also check that **Automatically republish when changes are made** is on under **Published content & settings** in Google's **Publish to web** window.

#### My Private Sheet Updates Late

Updates arrive about 5 minutes after your last edit. A sheet that keeps changing pushes that back until the edits pause. To get the latest version now, open the asset and hit **Save**. To catch up more often, set a lower **Force Sync Interval**.

#### Formulas Like NOW() or GOOGLEFINANCE() Don't Refresh on My Private Sheet

Formulas that recalculate on their own, like NOW() or GOOGLEFINANCE(), normally update on your screens without any extra steps. If one seems stuck, open the asset and hit **Save** to update the sheet right away. To have OptiSigns check more often, set a lower **Force Sync Interval**. If you need these values to stay current at all times, use a public link instead.

#### My Screen Shows Old Data While It's Offline

If a screen loses its internet connection, it keeps showing the last version of the sheet. It catches up once it's back online.

---

## Related Articles

* [How to add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211?ref=related)
* [How to Display Birthday Lists with OptiSync Data Mapping and Google Sheets](https://support.optisigns.com/hc/en-us/articles/29979283289235?ref=related)
* [How to Use Google Slides with OptiSigns](https://support.optisigns.com/hc/en-us/articles/360050642833?ref=related)
* [How to Use the Google Drive App](https://support.optisigns.com/hc/en-us/articles/360049518313?ref=related)
* [How to Use Microsoft Excel Online with OptiSigns](https://support.optisigns.com/hc/en-us/articles/4529298306963?ref=related)

### That’s all!

OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).