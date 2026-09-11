# Clean install OptiSigns on Raspberry Pi/Linux

**Article ID:** 4411956075027
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/4411956075027-Clean-install-OptiSigns-on-Raspberry-Pi-Linux
**Last Updated:** 2026-09-10T09:47:36+00:00
---

To completely clean out old installation of OptiSigns on Linux or Raspberry Pi

Please run:

```
rm -rf ~/.config/OptiSigns  
rm ~/.config/autostart/'OptiSigns Digital Signage.desktop'
```

Also delete the long string text on this ~/.config folder

Then install the new AppImage download from <https://www.optisigns.com/download>