# Generate & Manage an OptiSigns API Key

**Article ID:** 4414563797139
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4414563797139-Generate-Manage-an-OptiSigns-API-Key
**Last Updated:** 2026-09-09T21:49:12+00:00
---

In order to use the API, you will need first get an API key. To get an API key, you can either use the link below, or click the **API Keys** button in the side menu of account management on the OptiSigns portal.

|  |
| --- |
| **NOTE** |
| In order to generate an API Key, you must:   * Be on the OptiSigns [**Pro Plus plan or above**](https://www.optisigns.com/pricing) * Be the **Account Owner** or **Super Admin** * Not be using a white-labeled portal |

To get an Within OptiSigns, click the profile menu on the top right, go to **More**, then **API Keys**.

Or, click this link: <https://app.optisigns.com/app/s/apikeys>

### 

### Create API Key

1. Click the **New API Key** button

2. Enter the API Key name, and select the scopes and permissions for the API key.

3. Save the API key safely, the key will be used to access your account via API. It can be re-displayed at any time from the row's three-dot menu and selecting Reveal.

Click **Copy** to quickly get the key and Paste it where it needs to go.

### Use API Key

To use the API key, put it in the HTTP request header following this format.

Authorization: Bearer YOUR\_KEY\_HERE

In the OptiSigns GraphQL playground, you will be able to query your data if the API key is successfully added.

**Previous Article -** [**Introduction**](https://support.optisigns.com/hc/en-us/articles/4414552808467-Introduction)

**Next Article -** [**Get Started**](https://support.optisigns.com/hc/en-us/articles/4414563863827-Get-Started)