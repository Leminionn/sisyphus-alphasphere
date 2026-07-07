# Advanced: How to assign security for users to only edit certain zones of the screens

**Article ID:** 1500002047642
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/1500002047642-Advanced-How-to-assign-security-for-users-to-only-edit-certain-zones-of-the-screens
**Last Updated:** 2025-09-02T19:14:05+00:00
---

This article will guide you through how to assign security for users to only edit certain zones of the screens.  
Use Case: a Company with 2 departments, Department A and Department B, each will have a section/zone of the screen that they can update freely, but they cannot change the zone belong to other departments. Administrators can edit modify the whole screen.

To do this we will need to:

1) You need to add the users to the Account Member. Please set them as a User. Here is a related [article](https://support.optisigns.com/hc/en-us/articles/360016990233-Multi-users-Invite-your-team-members-to-your-account).

2) Create Files/Assets folders for Department A & Department B

3) Create 2 playlists: Department A & Department B

4) Create a SplitScreen & Assign playlist

5) Set up security for Screens, Files/Assets, Playlist folders

For the screen: You can edit the "Change Permission" in the folder. You can set **Admin Only**.

Put your screens in this folder so only Admins can edit & change assignment for the screens.

For the Department A folder in Files/Assets: You can edit the "Change Permission" in the folder. You can set it to **DepartmentA User**.

For the Department B folder in Files/Assets: You can edit the "Change Permission" in the folder. You can set it to **DepartmentB User**.

For the Department A Playlist folder in Playlist: You can edit the "Change Permission" in the folder. You can set it to **DepartmentA User**.

For the Department B Playlist folder in Playlist: You can edit the "Change Permission" in the folder. You can set it to **DepartmentB User**.

Now we have:   
Admin can see:

* Administration folder in the Screen.
* Department A and Department B folder in the Files/Assets
* Department A and Department B folder in the Playlist

DepartmentA User can see the

* Department A folder in the Files/Assets
* Department A Playlist Folder in the Playlist

DepartmentB User can see the

* Department B folder in the Files/Assets
* Department B Playlist Folder in the Playlist

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)