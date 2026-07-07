# Video codec or video playback issues

**Article ID:** 360038992973
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/360038992973-Video-codec-or-video-playback-issues
**Last Updated:** 2025-08-29T20:15:48+00:00
---

There are different codecs that used by videos, such as H264, HEVC, VP9, Mpeg-4, AV1. The support of the codec are dependent on the hardware, when the codec is not supported by the device used for video playback, you may see this error screen like below on OptiSigns. Or it could be simply that the video playback is slow and dropping frames, because it is use software decoding instead of hardware decoding. Similarly, when the video resolution or bit rate is too high for the hardware to handle, you may experience the same issue.

Here are some options you can try to resolve the issue:

* Try a different video player
* Re-encode the video

### **Try a different video player**

To improve the supportability of different codecs, we provided users options to use different video players on different devices.

For example, with OptiSigns Pro player, you can choose to use HTML5 video player or MPV player for video playback on the OptiSigns portal under Edit Screen. Or if you are using RPi with OptiSigns pre-built image, you can choose between HTML5 Video Player, OMX player or MPV player.

If you are using Android devices, you can open the side menu of the player and go to Video Player Settings. This will allow you to change between Texture View and Surface View. Changing from the default Texture View to Surface View may provide better performance on certain hardware if the hardware is optimized only for Surface View.

### **Re-encode the video**

H264 is the most widely supported codec, VP9 and HEVC(H265) are well supported by a lot of the hardware as well. However, there could be times when codec is not recognized or support by your devices. For example, here's a link to Amazon's [supported codec](https://developer.amazon.com/docs/fire-tv/device-specifications.html).

To solve the problem you will need to convert/re-encode your video into something that Amazon or your Android device support.

There's a [Handbreak is a free](https://handbrake.fr/) and very popular software to do that. It runs on Windows, Mac and Linux.

To re-encode your video.

Download, Run Handbreak.

Drag your video in there.

Select the output format you desired.

Amazon, Android or General would work. Pick appropriate video resolution you want too.

Select a location you want the new video file to be output to.

Click Start.

Depend on video length and quality, and how fast your computer is. It could take some time.

When it's done, you can upload the file back to OptiSigns and assign to your playlists, screens.

If you have further questions, issues, please feel free to contact us at [support@optisigns.com](mailto:support@optisigns.com)