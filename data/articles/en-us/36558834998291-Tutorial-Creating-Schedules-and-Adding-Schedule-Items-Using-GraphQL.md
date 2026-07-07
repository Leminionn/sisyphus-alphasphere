# Tutorial: Creating Schedules and Adding Schedule Items Using GraphQL

**Article ID:** 36558834998291
**Locale:** en-us
**Article URL:** https://support.optisigns.com/hc/en-us/articles/36558834998291-Tutorial-Creating-Schedules-and-Adding-Schedule-Items-Using-GraphQL
**Last Updated:** 2025-09-04T14:03:45+00:00
---

Using GraphQL, it’s possible to create a schedule on OptiSigns, then add items to it and assign values to them. We’ll cover each of these steps in turn.

**1. Creating a New Schedule**

To create a new schedule, we’ll need a specific Mutation:

```
mutation CreateSchedule($payload: ScheduleInput!, $teamId: String)  
  
{saveSchedule (payload:$payload,teamId:$teamId){  
   _id,  
   accountId,  
   createdAt,  
   createdBy,  
   groupId,  
   lastTeamId,  
   lastUpdatedBy,  
   lastUpdatedDate,  
   name,  
   path,  
   tags,  
   teamId  
   }  
}
```

**Variables:**

```
{“payload”: {  
   “groupId”:  
   “Name”:  
   “Path”:  
   “Tags”:  
   “teamId”:  
   }  
}
```

This Mutation creates a brand new schedule, as you can see from the data to the right:

**2. Updating Schedules**

This same Mutation can be used to update the schedule itself. In order to update the schedule, you’ll need to input the “\_id” value in the payload:

Doing this will update the existing schedule.

**3. Adding Assets or Playlists to the Schedule**

Now, we’ll want to add an item to the schedule. For that, we’ll need another Mutation:

```
mutation addScheduleItem($force:Boolean,$payload: AddScheduleItemInput!, $teamId: String!){  
  
  addScheduleItem(force:$force,payload:$payload,teamId:$teamId){  
  
         _id,  
  
       name,  
  
       assetId,        
  
       teamId,  
  
       playlistId,  
  
       repeatObject{  
  
         id,  
  
         repeat,  
  
         text,  
  
         type,  
  
         rrule  
  
       },  
  
       range{startDate,endDate},  
  
       documentDuration  
  
  }  
  
}
```

**Variables:**

```
{"force": false,  
 "payload": {"scheduleId": "",  
            "assetId": "",  
            "playlistId":"",  
            "type": "",  
            "repeatObject": {  
              "rrule": ""  
            },  
             "range": {  
               "startDate": "",  
               "endDate": ""  
            }  
     },  
 "teamId": ""  
}
```

When the values are set up correctly, your data should display like this:

**4. Editing Schedule Items**

Once you’ve created a schedule and set an item on it, it’s possible to edit those items. This requires yet another Mutation:

```
mutation updateScheduleItem($force:Boolean,$payload: UpdateScheduleItemInput!, $scope: APPLY_SCHEDULE_ITEM_SCOPES!){  
  
  updateScheduleItem(force:$force,payload:$payload,scope:$scope){  
       _id,  
       name,  
       assetId,        
       teamId,  
       playlistId,  
       repeatObject{  
         id,  
         repeat,  
         text,  
         type,  
         rrule  
       },  
       range{startDate,endDate},  
       documentDuration  
  }  
}
```

With this mutation, we’ll input these variables:

```
{"force": false,  
 "payload": {"_id": "",  
            "assetId": "",  
            "playlistId":"",  
            "repeatObject": {  
              "rrule": ""  
             },  
            "range": {  
              "startDate": "",  
              "endDate": ""  
            }  
 },  
 "scope": ""  
}
```

Here, we’ve changed the repeat frequency from daily to weekly, and the start date from December 18, 2024 to December 20, 2024. This is reflected in the data retrieved:

**Previous Article - [Tutorial: Creating or Updating Website Assets Using GraphQL](https://support.optisigns.com/hc/en-us/articles/36562094987795-Tutorial-Creating-or-Updating-Website-Assets-Using-GraphQL)**

**Next Article - [Pagination](https://support.optisigns.com/hc/en-us/articles/4414558369811-Pagination)**