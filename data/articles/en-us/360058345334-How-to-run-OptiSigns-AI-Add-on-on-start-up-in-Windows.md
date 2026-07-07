# How to run OptiSigns AI Add-on on start up in Windows

**Article ID:** 360058345334
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360058345334-How-to-run-OptiSigns-AI-Add-on-on-start-up-in-Windows
**Last Updated:** 2025-08-29T19:07:49+00:00
---

In Windows, you can use Windows' Task Scheduler to set up OptiSigns AI Add-on to run on start up.

It only take a few simple steps

Click **Start** -> Type "**Task Scheduler**" and open it

Then click **Create Basic task**

Give it a name (e.g. OptiSigns AI Add-on Autostart)

Then click **Next**

Next in Trigger section select "**When I Log on**"  
Please do not select other event like When computer start, it may not work.

Next in Action section select "**Start a program**"

Click Browse and browse to optisigns-ai-detection.exe that you've downloaded.

Then click **Finish**

That's all!

Next time your PC start up, it will start OptiSigns AI Detection app, doing it this way will also ensure that it will get started before the OptiSigns Digital Signage Player app start.