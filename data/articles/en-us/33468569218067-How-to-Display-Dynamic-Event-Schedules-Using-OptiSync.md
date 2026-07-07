# How to Display Dynamic Event Schedules Using OptiSync

**Article ID:** 33468569218067
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/33468569218067-How-to-Display-Dynamic-Event-Schedules-Using-OptiSync
**Last Updated:** 2025-09-04T14:59:16+00:00
---

### With OptiSync, you can dynamically map data from sources such as Google Sheets, Microsoft Excel, APIs, and more to display updating event schedules on your screens. In this article, we will walk you through the steps.

* [Examples of Some Event Schedules OptiSync Can Make](#Examples)
* [Setting up a Daily Event Schedule with OptiSync](https://support.optisigns.com/hc/en-us/articles/undefined#Daily)
  + [Option 1: Via Google Sheet/Excel](#Google)
    - [How to Set Up a Daily Event Schedule that Updates with the Passage of Time](#Time)
  + [Option 2: Via API](#API)
* [Setting up a Weekly Event Schedule with OptiSync](#Weekly)
* [Setting up a Monthly Event Calendar with OptiSync](#Monthly)

Automatically updating your screens with event information is useful in many situations, including providing real-time updates across a wide area.

Providing updated daily, weekly, or monthly event schedules for conventions, trade shows, schools, local governments, public places, nonprofits, company internal events, and far more is OptiSync’s specialty.

In this guide, we’ll give very high level instructions on how to make several types of event schedules: daily, weekly, and monthly. This will not be an exhaustive guide on every possible way to format your spreadsheets for uploading into OptiSigns, or how to provide data for your API for uploading into OptiSigns. If you’d like a more comprehensive guide on how to input data into OptiSigns, see our [Dynamic Data mapping guide](https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync).

|  |
| --- |
| **NOTE:** OptiSync and dynamic data mapping are exclusive to **Pro Plus** plans and above. |

---

## Examples of Some Event Schedules Made with OptiSync

#### **Daily:**

#### **Weekly:**

#### **Monthly:**

#### **Split Screen:**

---

## Setting up a Daily Event Schedule with OptiSync

Daily event schedules are common for all kinds of businesses, which we won’t exhaustively list here.

### Option 1: Via Google Sheet/Excel

The simplest way to create a daily schedule is by organizing your event data similarly to the screenshot below:

The **data is mapped from Row 2 onwards**, and is **grouped by Row.** This means when the DataSource is added to OptiSigns, it will be clustered like this:

Since this is a daily schedule, we’re only worried about the time of the event, and we’ve also included a description. However, you can include all kinds of information should you feel it necessary.

Now, you’ll need to add your DataSource to OptiSigns.

**Please follow these guides to upload different kinds of DataSources:**

* [How to add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211)
* [How to add a Microsoft 365 Excel Spreadsheet as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29863080711059)

Now that your DataSource is added, we can get started in Designer.

Daily events are best mapped as a **Repeater**. These allow you to set up a single design and have all your data appear within it

To set up a repeater, drag your first **Row** onto your design. You’ll receive the below prompt. Select **Use in a Repeater**.

You’ll be able to format your data however you wish.

#### How to Set Up a Daily Event Schedule that Updates with the Passage of Time

With a Daily Event schedule, once an event happens, there’s no need to keep displaying the event. With OptiSync, you can configure your DataSource to ignore events which are now in the past.

To do this, we’ll need to set up an additional column in our spreadsheet. We’ll call it the **Event Over?** column.

In the “Event Over?” column, put this formula:

```
=IF(B2<=NOW(),"Yes","No")
```

|  |
| --- |
| **NOTE:** This formula will only work if both the Date and Time are present in the Event Time cell. The “B2” part should match the actual event time, i.e. B3 for Zumba in the Example. |

B2 is your reference value, which maps up with the event time. This formula will work regardless of whether or not the current date is referenced in the “Event Time” column.

Within the settings of your Google Sheet, please ensure Recalculation is on (e.g., On change and every hour/minute), otherwise the formula won't recalculate.

You can access this in your Google Sheet by selecting **File** **→** **Settings** **→** **Calculation.**

All the “Event Over?” column does is check whether or not the event time has passed with a simple yes or no. When this screenshot was taken, it was between 1:00 and 3:30, so the first event to be shown should be “Rowing,” followed by “Surrender Yoga.”

To do this, we’ll make use of the **DataSource** **Filter**.

To get started, highlight the data you want to filter, then hit **Settings.** Then, hit the **Filter** option under your DataSource.

This screen will appear:

What follows is, essentially, an [AND statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) or an [OR statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) you might use in Excel or Google Sheets. The easiest way to understand the Filter option is as an Excel or Google Sheet formula you input within OptiSigns.

You can add **Rules** or **RuleSets** to your filter to create as much complexity as you need:

In order to set up a Rule, you’ll need to configure three values.

Selecting the first box gives you these options:

By default, these options equate to the **headers of your columns in the spreadsheet you have mapped.** This list will vary in length depending on how many headers you have. You can also input any value you wish by typing it in the box.

The second box is your **Variable.** OptiSigns provides these options:

The final option provides the following default values:

By default, these map to a screen or other device, allowing your filter to target only certain screens.

However, this value **can be changed to anything you want.** Simply type any value you wish.

For our purposes, we want to check to see if the “Event Over?” is equal to No:

That removes every row where the “Event Over?” value is Yes. Now, your Event Schedule will display this:

There are dozens of possibilities using the OptiSync filter to show even more precise automated data on your screens.

---

### Option 2: Via API

In order to pull event data from an API, follow our guide on [integrating API and publishing API data.](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync)

Data can be set up in Designer in the same manner as if you were using a spreadsheet.

---

## Setting up a Weekly Event Schedule with OptiSync

Setting up a weekly event schedule is much the same as a daily schedule. There are numerous ways you can format your spreadsheet, but one of the easiest is like this:

Here, we’ve grouped all our events together with their location, date, and time. Depending on your needs, these may need to be input as individual rows, or individual pieces rather than as Repeaters.

Complex weekly schedules like the one above will be easiest to input individually. Selecting the **Row** and dragging it onto your Design will open the following prompt. Hit **Use on its own**.

Organizing your data this way will allow precise placement. We recommend this option when data can’t be easily repeated, as in this example where there are different numbers of events on different days.

Your spreadsheet can be updated every week, and a simple refresh will update the design on OptiSigns.

---

## Setting up a Monthly Event Schedule with OptiSync

Monthly event calendars let you alert your customers or organization of upcoming events well in advance. Using Google Sheets as an example, the data can be organized in much the same way we did our weekly events. Simply add as many columns as you might want to place on your design. Remember, not every piece of data needs to be added to your final design, so you’re free to pick and choose as needed.

Importing this example data to OptiSigns will provide us with these clusters:

---

### Creating a Calendar-Style Monthly Event Schedule

Calendar-style monthly event schedules, as the name suggests, present your event data in a calendar format. This is the best option if you want to see a great many events at a glance.

Should you choose the calendar-style format, space is a primary concern. You’ll have to pick and choose which pieces of data you want to display - long descriptions of an event, for example, would not be able to fit on a normal sized calendar. Fortunately, you do not have to discard any of your data, nor edit your spreadsheet. All you have to do is choose what individual pieces of data you want to place on your calendar.

For this example, we’ll only use the name of the Lunch and the Day of the Month on the menu. You could easily add a time repeater, as well.

Your data can be placed on a calendar design anywhere you like. Below, we’ve set up the entire calendar as a repeater and added the days of the week above.

---

## Setting Up a Split Screen Event Schedule

Creating a split-screen for your event schedule is a fantastic way to maximize your screens, allowing both pertinent information and promotional material to be disseminated simultaneously. A split screen event schedule can make use of either Landscape or Portrait formatted designs of any type. You can use any of the above types of event schedules in a split screen.

For this example, we’re going to put together a number of techniques we’ve learned above, using this data example:

For this event schedule, we want to make use of all our data. So, we’ll need a repeater which shows the Event Name, Event Time, End Time (or Duration), Event Location, and Event Description, as well as organizing them by day of the week.

There are a few ways to do this. You can simply attach the Day of the Week to each Repeater value, giving us something like this:

Or, you can create individual repeaters for each day of the week, allowing them to cycle.

Then, when you’re ready, you can attach it to your split screen app, creating a beautiful event schedule without getting in the way of anything else you'd like to display.

For a step-by-step walkthrough on putting together a split screen, see our guide on [how to create and use the Split Screen app](https://support.optisigns.com/hc/en-us/articles/360026559573-How-to-Create-and-Use-the-Split-Screen-App).

### That’s all!

If you have any questions or issues that need support, please feel free to reach out to us at [support@optisigns.com](mailto:support@optisigns.com).