
### Environment Interaction 1
----------------------------------------------------------------------------
```python
print('=== ACTIVE TASK ==='); print(apis.supervisor.show_active_task())
print('=== ACCOUNT PASSWORDS (use these, never guess) ==='); print(apis.supervisor.show_account_passwords())
print('=== YOUR (SUPERVISOR) PROFILE ==='); print(apis.supervisor.show_profile())
print('=== AVAILABLE APPS ==='); print(apis.api_docs.show_app_descriptions())
```

```
=== ACTIVE TASK ===
{
 "instruction": "We are planning a get-together with our friends next week. Buy stuff according to the checklist my husband sent me over email.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": ")Lun@YH"
 },
 {
  "account_name": "file_system",
  "password": "{R0sv}t"
 },
 {
  "account_name": "gmail",
  "password": "}v0#GvJ"
 },
 {
  "account_name": "phone",
  "password": "Xm4bukk"
 },
 {
  "account_name": "simple_note",
  "password": "F%rYCAJ"
 },
 {
  "account_name": "splitwise",
  "password": "Z}TYe(T"
 },
 {
  "account_name": "spotify",
  "password": "t#CZstC"
 },
 {
  "account_name": "todoist",
  "password": "!PT38{C"
 },
 {
  "account_name": "venmo",
  "password": "F[QML{n"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Patricia",
 "last_name": "Ritter",
 "email": "pa_ritter@gmail.com",
 "phone_number": "2444880289",
 "birthday": "1960-09-12",
 "sex": "female"
}
=== AVAILABLE APPS ===
[
 {
  "name": "api_docs",
  "description": "An app to search and explore API documentation."
 },
 {
  "name": "supervisor",
  "description": "An app to access supervisor's personal information, account credentials, addresses, payment cards, and manage the assigned task."
 },
 {
  "name": "amazon",
  "description": "An online shopping app to buy products and manage orders, returns, etc."
 },
 {
  "name": "phone",
  "description": "An app to find and manage contact information for friends, family members, etc., send and receive messages, and manage alarms."
 },
 {
  "name": "file_system",
  "description": "A file system app to create and manage files and folders."
 },
 {
  "name": "spotify",
  "description": "A music streaming app to stream songs and manage song, album and playlist libraries."
 },
 {
  "name": "venmo",
  "description": "A social payment app to send, receive and request money to and from others."
 },
 {
  "name": "gmail",
  "description": "An email app to draft, send, receive, and manage emails."
 },
 {
  "name": "splitwise",
  "description": "A bill splitting app to track and split expenses with people."
 },
 {
  "name": "simple_note",
  "description": "A note-taking app to create and manage notes"
 },
 {
  "name": "todoist",
  "description": "A task management app to manage todo lists and collaborate on them with others."
 }
]
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='login'))
gmail_access_token = apis.gmail.login(email='pa_ritter@gmail.com', password='}v0#GvJ')
print(gmail_access_token)
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    gmail_access_token = apis.gmail.login(email='pa_ritter@gmail.com', password='}v0#GvJ')
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Validation error. Reason: \nusername: field required"}
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='login'))
```

```
{
 "app_name": "gmail",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
gmail_access_token = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')
print(gmail_access_token)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtwYV9yaXR0ZXJAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDk4fQ.5JelcCEQI_OEjeauhpcKxH0GjgsMtDqeBHcHJzIFV3w",
 "token_type": "Bearer"
}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='search_emails'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='gmail', api_name='search_emails'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name search_emails found for the gmail app. Check the api and app name again."}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "search_users",
  "description": "Search Gmail users by name or email address."
 },
 {
  "name": "show_inbox_threads",
  "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_outbox_threads",
  "description": "Show or search email threads you have sent. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_archived_threads",
  "description": "Show or search email threads you have archived. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_spam_threads",
  "description": "Show or search email threads that have been marked as spam. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_category_sizes",
  "description": "Show the number of email threads in each category of inbox, outbox, archived, spam, and the number of unscheduled and scheduled email drafts."
 },
 {
  "name": "show_thread",
  "description": "Show detailed information about a given email thread, including emails and drafts within it."
 },
 {
  "name": "delete_thread",
  "description": "Delete an email thread."
 },
 {
  "name": "show_email",
  "description": "Show detailed information about a given email."
 },
 {
  "name": "label_thread",
  "description": "Label an email thread."
 },
 {
  "name": "unlabel_thread",
  "description": "Remove label from an email thread."
 },
 {
  "name": "mark_thread_read",
  "description": "Mark an email thread as read."
 },
 {
  "name": "mark_thread_unread",
  "description": "Mark an email thread as unread."
 },
 {
  "name": "mark_thread_archived",
  "description": "Mark an email thread as archived."
 },
 {
  "name": "mark_thread_unarchived",
  "description": "Mark an email thread as unarchived."
 },
 {
  "name": "mark_thread_spam",
  "description": "Mark an email thread as spam."
 },
 {
  "name": "mark_thread_not_spam",
  "description": "Mark an email thread as not spam."
 },
 {
  "name": "mark_thread_starred",
  "description": "Mark an email thread as starred."
 },
 {
  "name": "mark_thread_unstarred",
  "description": "Mark an email thread as unstarred."
 },
 {
  "name": "delete_email_in_thread",
  "description": "Delete an email in a thread."
 },
 {
  "name": "send_email",
  "description": "Send a new email to one or more recipients."
 },
 {
  "name": "reply_to_email",
  "description": "Reply to an existing email in a thread."
 },
 {
  "name": "forward_email_from_thread",
  "description": "Forward an email from an email thread to one or more recipients."
 },
 {
  "name": "forward_email_thread",
  "description": "Forward entire email thread to one or more recipients."
 },
 {
  "name": "show_drafts",
  "description": "Show a list of user drafts."
 },
 {
  "name": "create_draft",
  "description": "Create a new draft."
 },
 {
  "name": "show_draft",
  "description": "Show detailed draft information."
 },
 {
  "name": "delete_draft",
  "description": "Delete draft information."
 },
 {
  "name": "update_draft",
  "description": "Update draft information."
 },
 {
  "name": "send_email_from_draft",
  "description": "Send a new email from a draft right away."
 },
 {
  "name": "download_attachment",
  "description": "Download a file attachment."
 },
 {
  "name": "upload_attachments_to_draft",
  "description": "Upload attachments to a draft."
 },
 {
  "name": "remove_attachment_from_draft",
  "description": "Delete an attachment from a draft."
 }
]
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_inbox_threads'))
```

```
{
 "app_name": "gmail",
 "api_name": "show_inbox_threads",
 "path": "/email_threads/category/inbox",
 "method": "GET",
 "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from gmail app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "label",
   "type": "string",
   "required": false,
   "description": "The label to filter the emails by.",
   "default": null,
   "constraints": []
  },
  {
   "name": "starred",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by starred status.",
   "default": null,
   "constraints": []
  },
  {
   "name": "archived",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by archived status.",
   "default": false,
   "constraints": []
  },
  {
   "name": "spam",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by spam status.",
   "default": false,
   "constraints": []
  },
  {
   "name": "read",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by read status.",
   "default": null,
   "constraints": []
  },
  {
   "name": "attachment",
   "type": "boolean",
   "required": false,
   "description": "Filter emails by whether they have an attachment or not.",
   "default": null,
   "constraints": []
  },
  {
   "name": "from_email",
   "type": "string",
   "required": false,
   "description": "Filter emails by sender email address.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "to_email",
   "type": "string",
   "required": false,
   "description": "Filter emails by recipient email address.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "min_created_at",
   "type": "string",
   "required": false,
   "description": "Filter emails by minimum created_at date in YYYY-MM-DD format.",
   "default": "1500-01-01",
   "constraints": []
  },
  {
   "name": "max_created_at",
   "type": "string",
   "required": false,
   "description": "Filter emails by maximum created_at date in YYYY-MM-DD format.",
   "default": "3000-01-01",
   "constraints": []
  },
  {
   "name": "page_index",
   "type": "integer",
   "required": false,
   "description": "The index of the page to return.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "page_limit",
   "type": "integer",
   "required": false,
   "description": "The maximum number of results to return per page.",
   "default": 5,
   "constraints": [
    "value >= 1.0, <= 20.0"
   ]
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the email threads by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and updated_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -updated_at.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "email_thread_id": 1,
    "email_ids": [
     1
    ],
    "draft_ids": [
     1
    ],
    "incoming": true,
    "outgoing": true,
    "read": true,
    "label": "string",
    "starred": true,
    "archived": true,
    "spam": true,
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "subject": "string",
    "participants": [
     {
      "name": "string",
      "email": "user@example.com"
     }
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
inbox_threads = apis.gmail.show_inbox_threads(access_token=gmail_access_token, query='checklist OR get-together')
print(inbox_threads)
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    inbox_threads = apis.gmail.show_inbox_threads(access_token=gmail_access_token, query='checklist OR get-together')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 401:
{"message":"You are either not authorized to access this gmail API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
inbox_threads = apis.gmail.show_inbox_threads(access_token=token_str, query='checklist OR get-together')
print(inbox_threads)
```

```
[
 {
  "email_thread_id": 47826,
  "email_ids": [
   20874,
   20875,
   20876,
   20877
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": true,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-14T09:43:21",
  "updated_at": "2023-05-14T09:43:21",
  "subject": "Get-together Invitation",
  "participants": [
   {
    "name": "Isaac Miller",
    "email": "ismill@gmail.com"
   },
   {
    "name": "Mason Smith",
    "email": "masmith@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "David Martinez",
    "email": "dav.mart@gmail.com"
   },
   {
    "name": "Brandon Weber",
    "email": "brandon-webe@gmail.com"
   },
   {
    "name": "Angela Riddle",
    "email": "angriddle@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 47823,
  "email_ids": [
   20868,
   20869,
   20870,
   20871
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T16:17:35",
  "updated_at": "2023-05-17T16:17:35",
  "subject": "Get-together Invitee",
  "participants": [
   {
    "name": "Brian Ritter",
    "email": "br_ritt@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 47821,
  "email_ids": [
   20867
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T08:57:00",
  "updated_at": "2023-05-17T08:57:00",
  "subject": "Get-together Shopping List",
  "participants": [
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Brian Ritter",
    "email": "br_ritt@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 8080,
  "email_ids": [
   2492
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": true,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2022-10-21T10:52:10",
  "updated_at": "2022-10-21T10:52:10",
  "subject": "Office Space Renovation Updates",
  "participants": [
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 13600,
  "email_ids": [
   4245
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": true,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-04-21T10:53:35",
  "updated_at": "2023-04-21T10:53:35",
  "subject": "Office Space Renovation Updates",
  "participants": [
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 }
]
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
email_content = apis.gmail.show_email(access_token=token_str, email_id=20867)
print(email_content)
```

```
{
 "email_id": 20867,
 "subject": "Get-together Shopping List",
 "body": "Attached shopping list. Can you please buy them on amazon and have it delivered to our home.",
 "response_to_email_id": null,
 "created_at": "2023-05-17T08:57:00",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8483,
   "file_name": "get-together-shopping-list.txt"
  }
 ]
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "search_users",
  "description": "Search Gmail users by name or email address."
 },
 {
  "name": "show_inbox_threads",
  "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_outbox_threads",
  "description": "Show or search email threads you have sent. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_archived_threads",
  "description": "Show or search email threads you have archived. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_spam_threads",
  "description": "Show or search email threads that have been marked as spam. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_category_sizes",
  "description": "Show the number of email threads in each category of inbox, outbox, archived, spam, and the number of unscheduled and scheduled email drafts."
 },
 {
  "name": "show_thread",
  "description": "Show detailed information about a given email thread, including emails and drafts within it."
 },
 {
  "name": "delete_thread",
  "description": "Delete an email thread."
 },
 {
  "name": "show_email",
  "description": "Show detailed information about a given email."
 },
 {
  "name": "label_thread",
  "description": "Label an email thread."
 },
 {
  "name": "unlabel_thread",
  "description": "Remove label from an email thread."
 },
 {
  "name": "mark_thread_read",
  "description": "Mark an email thread as read."
 },
 {
  "name": "mark_thread_unread",
  "description": "Mark an email thread as unread."
 },
 {
  "name": "mark_thread_archived",
  "description": "Mark an email thread as archived."
 },
 {
  "name": "mark_thread_unarchived",
  "description": "Mark an email thread as unarchived."
 },
 {
  "name": "mark_thread_spam",
  "description": "Mark an email thread as spam."
 },
 {
  "name": "mark_thread_not_spam",
  "description": "Mark an email thread as not spam."
 },
 {
  "name": "mark_thread_starred",
  "description": "Mark an email thread as starred."
 },
 {
  "name": "mark_thread_unstarred",
  "description": "Mark an email thread as unstarred."
 },
 {
  "name": "delete_email_in_thread",
  "description": "Delete an email in a thread."
 },
 {
  "name": "send_email",
  "description": "Send a new email to one or more recipients."
 },
 {
  "name": "reply_to_email",
  "description": "Reply to an existing email in a thread."
 },
 {
  "name": "forward_email_from_thread",
  "description": "Forward an email from an email thread to one or more recipients."
 },
 {
  "name": "forward_email_thread",
  "description": "Forward entire email thread to one or more recipients."
 },
 {
  "name": "show_drafts",
  "description": "Show a list of user drafts."
 },
 {
  "name": "create_draft",
  "description": "Create a new draft."
 },
 {
  "name": "show_draft",
  "description": "Show detailed draft information."
 },
 {
  "name": "delete_draft",
  "description": "Delete draft information."
 },
 {
  "name": "update_draft",
  "description": "Update draft information."
 },
 {
  "name": "send_email_from_draft",
  "description": "Send a new email from a draft right away."
 },
 {
  "name": "download_attachment",
  "description": "Download a file attachment."
 },
 {
  "name": "upload_attachments_to_draft",
  "description": "Upload attachments to a draft."
 },
 {
  "name": "remove_attachment_from_draft",
  "description": "Delete an attachment from a draft."
 }
]
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_app_descriptions())
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
email_content = apis.gmail.show_email(access_token=token_str, email_id=20867)
print(email_content)
```

```
[
 {
  "name": "api_docs",
  "description": "An app to search and explore API documentation."
 },
 {
  "name": "supervisor",
  "description": "An app to access supervisor's personal information, account credentials, addresses, payment cards, and manage the assigned task."
 },
 {
  "name": "amazon",
  "description": "An online shopping app to buy products and manage orders, returns, etc."
 },
 {
  "name": "phone",
  "description": "An app to find and manage contact information for friends, family members, etc., send and receive messages, and manage alarms."
 },
 {
  "name": "file_system",
  "description": "A file system app to create and manage files and folders."
 },
 {
  "name": "spotify",
  "description": "A music streaming app to stream songs and manage song, album and playlist libraries."
 },
 {
  "name": "venmo",
  "description": "A social payment app to send, receive and request money to and from others."
 },
 {
  "name": "gmail",
  "description": "An email app to draft, send, receive, and manage emails."
 },
 {
  "name": "splitwise",
  "description": "A bill splitting app to track and split expenses with people."
 },
 {
  "name": "simple_note",
  "description": "A note-taking app to create and manage notes"
 },
 {
  "name": "todoist",
  "description": "A task management app to manage todo lists and collaborate on them with others."
 }
]
{
 "email_id": 20867,
 "subject": "Get-together Shopping List",
 "body": "Attached shopping list. Can you please buy them on amazon and have it delivered to our home.",
 "response_to_email_id": null,
 "created_at": "2023-05-17T08:57:00",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8483,
   "file_name": "get-together-shopping-list.txt"
  }
 ]
}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
email_content = apis.gmail.show_email(access_token=token_str, email_id=20867)
print(email_content.get('body', email_content.get('text', str(email_content))))
```

```
Attached shopping list. Can you please buy them on amazon and have it delivered to our home.
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
email_content = apis.gmail.show_email(access_token=token_str, email_id=20867)
print(list(email_content.keys()))
print(email_content)
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
```

```
[
 "email_id",
 "subject",
 "body",
 "response_to_email_id",
 "created_at",
 "sender",
 "recipients",
 "attachments"
]
{
 "email_id": 20867,
 "subject": "Get-together Shopping List",
 "body": "Attached shopping list. Can you please buy them on amazon and have it delivered to our home.",
 "response_to_email_id": null,
 "created_at": "2023-05-17T08:57:00",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8483,
   "file_name": "get-together-shopping-list.txt"
  }
 ]
}
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "search_users",
  "description": "Search Gmail users by name or email address."
 },
 {
  "name": "show_inbox_threads",
  "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_outbox_threads",
  "description": "Show or search email threads you have sent. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_archived_threads",
  "description": "Show or search email threads you have archived. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_spam_threads",
  "description": "Show or search email threads that have been marked as spam. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_category_sizes",
  "description": "Show the number of email threads in each category of inbox, outbox, archived, spam, and the number of unscheduled and scheduled email drafts."
 },
 {
  "name": "show_thread",
  "description": "Show detailed information about a given email thread, including emails and drafts within it."
 },
 {
  "name": "delete_thread",
  "description": "Delete an email thread."
 },
 {
  "name": "show_email",
  "description": "Show detailed information about a given email."
 },
 {
  "name": "label_thread",
  "description": "Label an email thread."
 },
 {
  "name": "unlabel_thread",
  "description": "Remove label from an email thread."
 },
 {
  "name": "mark_thread_read",
  "description": "Mark an email thread as read."
 },
 {
  "name": "mark_thread_unread",
  "description": "Mark an email thread as unread."
 },
 {
  "name": "mark_thread_archived",
  "description": "Mark an email thread as archived."
 },
 {
  "name": "mark_thread_unarchived",
  "description": "Mark an email thread as unarchived."
 },
 {
  "name": "mark_thread_spam",
  "description": "Mark an email thread as spam."
 },
 {
  "name": "mark_thread_not_spam",
  "description": "Mark an email thread as not spam."
 },
 {
  "name": "mark_thread_starred",
  "description": "Mark an email thread as starred."
 },
 {
  "name": "mark_thread_unstarred",
  "description": "Mark an email thread as unstarred."
 },
 {
  "name": "delete_email_in_thread",
  "description": "Delete an email in a thread."
 },
 {
  "name": "send_email",
  "description": "Send a new email to one or more recipients."
 },
 {
  "name": "reply_to_email",
  "description": "Reply to an existing email in a thread."
 },
 {
  "name": "forward_email_from_thread",
  "description": "Forward an email from an email thread to one or more recipients."
 },
 {
  "name": "forward_email_thread",
  "description": "Forward entire email thread to one or more recipients."
 },
 {
  "name": "show_drafts",
  "description": "Show a list of user drafts."
 },
 {
  "name": "create_draft",
  "description": "Create a new draft."
 },
 {
  "name": "show_draft",
  "description": "Show detailed draft information."
 },
 {
  "name": "delete_draft",
  "description": "Delete draft information."
 },
 {
  "name": "update_draft",
  "description": "Update draft information."
 },
 {
  "name": "send_email_from_draft",
  "description": "Send a new email from a draft right away."
 },
 {
  "name": "download_attachment",
  "description": "Download a file attachment."
 },
 {
  "name": "upload_attachments_to_draft",
  "description": "Upload attachments to a draft."
 },
 {
  "name": "remove_attachment_from_draft",
  "description": "Delete an attachment from a draft."
 }
]
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
print([x['name'] for x in apis.api_docs.show_api_descriptions(app_name='gmail')])
```

```
[
 "show_account",
 "signup",
 "delete_account",
 "update_account_name",
 "login",
 "logout",
 "send_password_reset_code",
 "reset_password",
 "show_profile",
 "search_users",
 "show_inbox_threads",
 "show_outbox_threads",
 "show_archived_threads",
 "show_spam_threads",
 "show_category_sizes",
 "show_thread",
 "delete_thread",
 "show_email",
 "label_thread",
 "unlabel_thread",
 "mark_thread_read",
 "mark_thread_unread",
 "mark_thread_archived",
 "mark_thread_unarchived",
 "mark_thread_spam",
 "mark_thread_not_spam",
 "mark_thread_starred",
 "mark_thread_unstarred",
 "delete_email_in_thread",
 "send_email",
 "reply_to_email",
 "forward_email_from_thread",
 "forward_email_thread",
 "show_drafts",
 "create_draft",
 "show_draft",
 "delete_draft",
 "update_draft",
 "send_email_from_draft",
 "download_attachment",
 "upload_attachments_to_draft",
 "remove_attachment_from_draft"
]
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
email_content = apis.gmail.show_email(access_token=token_str, email_id=20867)
print(email_content['body'])
print(email_content.get('attachments', 'NO ATTACHMENTS KEY'))
print(list(email_content.keys()))
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='download_attachment'))
```

```
Attached shopping list. Can you please buy them on amazon and have it delivered to our home.
[{"id": 8483, "file_name": "get-together-shopping-list.txt"}]
[
 "email_id",
 "subject",
 "body",
 "response_to_email_id",
 "created_at",
 "sender",
 "recipients",
 "attachments"
]
{
 "app_name": "gmail",
 "api_name": "download_attachment",
 "path": "/attachments/{attachment_id}",
 "method": "GET",
 "description": "Download a file attachment.",
 "parameters": [
  {
   "name": "attachment_id",
   "type": "integer",
   "required": true,
   "description": "The ID of the attachment to download.",
   "default": null,
   "constraints": []
  },
  {
   "name": "file_system_access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from file_system app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from gmail app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "download_to_file_path",
   "type": "string",
   "required": false,
   "description": "The file path to download the attachment to in file system app. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'. If not passed, it will be saved in your ~/downloads directory.",
   "default": null,
   "constraints": []
  },
  {
   "name": "overwrite",
   "type": "boolean",
   "required": false,
   "description": "Whether to overwrite the file if it already exists.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "file_path": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='login'))
fs_token = apis.file_system.login(username='pa_ritter@gmail.com', password='{R0sv}t')['access_token']
print(fs_token)
```

```
{
 "app_name": "file_system",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWxlX3N5c3RlbStwYV9yaXR0ZXJAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyMDI1fQ.jeaf7O1d_aLNKftudCgqLdfAD2Hn5WcdmJ1iovx2yuA
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
fs_token = apis.file_system.login(username='pa_ritter@gmail.com', password='{R0sv}t')['access_token']
print(apis.file_system.list_files(access_token=fs_token))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.file_system.list_files(access_token=fs_token))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: No API named 'list_files' found in the file_system app.
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='file_system'))
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
fs_token = apis.file_system.login(username='pa_ritter@gmail.com', password='{R0sv}t')['access_token']
result = apis.gmail.download_attachment(access_token=token_str, attachment_id=8483, file_system_access_token=fs_token)
print(result)
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_directory",
  "description": "Show a list of files and/or sub-directories, optionally recursively, in a directory."
 },
 {
  "name": "create_directory",
  "description": "Create a directory if it does not exist, optionally recursively."
 },
 {
  "name": "delete_directory",
  "description": "Delete a directory with its sub-directories and files."
 },
 {
  "name": "directory_exists",
  "description": "Check if a directory exists."
 },
 {
  "name": "show_file",
  "description": "Show a file's content and other details, if it exists."
 },
 {
  "name": "create_file",
  "description": "Create a new file with the given content."
 },
 {
  "name": "delete_file",
  "description": "Delete a file."
 },
 {
  "name": "update_file",
  "description": "Update a file's content."
 },
 {
  "name": "file_exists",
  "description": "Check if a file exists."
 },
 {
  "name": "copy_file",
  "description": "Copy a file to another location."
 },
 {
  "name": "move_file",
  "description": "Move a file to another location."
 },
 {
  "name": "copy_directory",
  "description": "Copy a directory to another location."
 },
 {
  "name": "move_directory",
  "description": "Move a directory to another location."
 },
 {
  "name": "compress_directory",
  "description": "Compress a directory."
 },
 {
  "name": "decompress_file",
  "description": "Decompress a compressed file."
 }
]
{
 "message": "Attachment downloaded in file_system app.",
 "file_path": "/home/patricia/downloads/get-together-shopping-list.txt"
}
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='download_attachment'))
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
result = apis.gmail.download_attachment(access_token=token_str, attachment_id=8483)
print(result)
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    result = apis.gmail.download_attachment(access_token=token_str, attachment_id=8483)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Validation error. Reason: \nfile_system_access_token: field required"}
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
fs_token = apis.file_system.login(username='pa_ritter@gmail.com', password='{R0sv}t')['access_token']
result = apis.gmail.download_attachment(access_token=token_str, attachment_id=8483, file_system_access_token=fs_token)
print(result)
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    result = apis.gmail.download_attachment(access_token=token_str, attachment_id=8483, file_system_access_token=fs_token)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"A file already exists at the given file_path in your account. Set overwrite to True to overwrite it."}
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
emails = apis.gmail.list_emails(access_token=token_str)
print(emails)
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    emails = apis.gmail.list_emails(access_token=token_str)
             ^^^^^^^^^^^^^^^^^^^^^^
Exception: No API named 'list_emails' found in the gmail app.
```


### Environment Interaction 24
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "search_users",
  "description": "Search Gmail users by name or email address."
 },
 {
  "name": "show_inbox_threads",
  "description": "Show or search email threads you have received. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_outbox_threads",
  "description": "Show or search email threads you have sent. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_archived_threads",
  "description": "Show or search email threads you have archived. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_spam_threads",
  "description": "Show or search email threads that have been marked as spam. This will not show detailed information about emails within the thread."
 },
 {
  "name": "show_category_sizes",
  "description": "Show the number of email threads in each category of inbox, outbox, archived, spam, and the number of unscheduled and scheduled email drafts."
 },
 {
  "name": "show_thread",
  "description": "Show detailed information about a given email thread, including emails and drafts within it."
 },
 {
  "name": "delete_thread",
  "description": "Delete an email thread."
 },
 {
  "name": "show_email",
  "description": "Show detailed information about a given email."
 },
 {
  "name": "label_thread",
  "description": "Label an email thread."
 },
 {
  "name": "unlabel_thread",
  "description": "Remove label from an email thread."
 },
 {
  "name": "mark_thread_read",
  "description": "Mark an email thread as read."
 },
 {
  "name": "mark_thread_unread",
  "description": "Mark an email thread as unread."
 },
 {
  "name": "mark_thread_archived",
  "description": "Mark an email thread as archived."
 },
 {
  "name": "mark_thread_unarchived",
  "description": "Mark an email thread as unarchived."
 },
 {
  "name": "mark_thread_spam",
  "description": "Mark an email thread as spam."
 },
 {
  "name": "mark_thread_not_spam",
  "description": "Mark an email thread as not spam."
 },
 {
  "name": "mark_thread_starred",
  "description": "Mark an email thread as starred."
 },
 {
  "name": "mark_thread_unstarred",
  "description": "Mark an email thread as unstarred."
 },
 {
  "name": "delete_email_in_thread",
  "description": "Delete an email in a thread."
 },
 {
  "name": "send_email",
  "description": "Send a new email to one or more recipients."
 },
 {
  "name": "reply_to_email",
  "description": "Reply to an existing email in a thread."
 },
 {
  "name": "forward_email_from_thread",
  "description": "Forward an email from an email thread to one or more recipients."
 },
 {
  "name": "forward_email_thread",
  "description": "Forward entire email thread to one or more recipients."
 },
 {
  "name": "show_drafts",
  "description": "Show a list of user drafts."
 },
 {
  "name": "create_draft",
  "description": "Create a new draft."
 },
 {
  "name": "show_draft",
  "description": "Show detailed draft information."
 },
 {
  "name": "delete_draft",
  "description": "Delete draft information."
 },
 {
  "name": "update_draft",
  "description": "Update draft information."
 },
 {
  "name": "send_email_from_draft",
  "description": "Send a new email from a draft right away."
 },
 {
  "name": "download_attachment",
  "description": "Download a file attachment."
 },
 {
  "name": "upload_attachments_to_draft",
  "description": "Upload attachments to a draft."
 },
 {
  "name": "remove_attachment_from_draft",
  "description": "Delete an attachment from a draft."
 }
]
```


### Environment Interaction 25
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='search_emails'))
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
emails = apis.gmail.search_emails(access_token=token_str, query='checklist OR shopping')
print(emails)
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.api_docs.show_api_doc(app_name='gmail', api_name='search_emails'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name search_emails found for the gmail app. Check the api and app name again."}
```


### Environment Interaction 26
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_account'))
docs = apis.api_docs.show_api_descriptions(app_name='gmail')
[print(d['name']) for d in docs]
```

```
{
 "app_name": "gmail",
 "api_name": "show_account",
 "path": "/account",
 "method": "GET",
 "description": "Show your account information. Unlike show_profile, this includes private information.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from gmail app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "first_name": "string",
   "last_name": "string",
   "email": "user@example.com",
   "registered_at": "2019-01-01T00:00:00",
   "last_logged_in": "2019-01-01T00:00:00"
  },
  "failure": {
   "message": "string"
  }
 }
}
show_account
signup
delete_account
update_account_name
login
logout
send_password_reset_code
reset_password
show_profile
search_users
show_inbox_threads
show_outbox_threads
show_archived_threads
show_spam_threads
show_category_sizes
show_thread
delete_thread
show_email
label_thread
unlabel_thread
mark_thread_read
mark_thread_unread
mark_thread_archived
mark_thread_unarchived
mark_thread_spam
mark_thread_not_spam
mark_thread_starred
mark_thread_unstarred
delete_email_in_thread
send_email
reply_to_email
forward_email_from_thread
forward_email_thread
show_drafts
create_draft
show_draft
delete_draft
update_draft
send_email_from_draft
download_attachment
upload_attachments_to_draft
remove_attachment_from_draft
```


### Environment Interaction 27
----------------------------------------------------------------------------
```python
result = apis.api_docs.show_api_descriptions(app_name='gmail')
all_names = [d['name'] for d in result]
print(all_names)
```

```
[
 "show_account",
 "signup",
 "delete_account",
 "update_account_name",
 "login",
 "logout",
 "send_password_reset_code",
 "reset_password",
 "show_profile",
 "search_users",
 "show_inbox_threads",
 "show_outbox_threads",
 "show_archived_threads",
 "show_spam_threads",
 "show_category_sizes",
 "show_thread",
 "delete_thread",
 "show_email",
 "label_thread",
 "unlabel_thread",
 "mark_thread_read",
 "mark_thread_unread",
 "mark_thread_archived",
 "mark_thread_unarchived",
 "mark_thread_spam",
 "mark_thread_not_spam",
 "mark_thread_starred",
 "mark_thread_unstarred",
 "delete_email_in_thread",
 "send_email",
 "reply_to_email",
 "forward_email_from_thread",
 "forward_email_thread",
 "show_drafts",
 "create_draft",
 "show_draft",
 "delete_draft",
 "update_draft",
 "send_email_from_draft",
 "download_attachment",
 "upload_attachments_to_draft",
 "remove_attachment_from_draft"
]
```


### Environment Interaction 28
----------------------------------------------------------------------------
```python
token_result = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')
print(token_result)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtwYV9yaXR0ZXJAZ21haWwuY29tIiwiZXhwIjoxNjg0NDEyNDg2fQ.LRMFMJvPbAMPr-APiFWpvPX9SO86XHxP2L9LMGoEWcw",
 "token_type": "Bearer"
}
```


### Environment Interaction 29
----------------------------------------------------------------------------
```python
result = apis.api_docs.show_api_descriptions(app_name='gmail')
for d in result:
    print(d['name'], d.get('description','')[:50])
```

```
show_account Show your account information. Unlike show_profile
signup Sign up to create account.
delete_account Delete your account.
update_account_name Update your first or last name in the account prof
login Login to your account.
logout Logout from your account.
send_password_reset_code Send password reset code to your email address.
reset_password Reset your password using the password reset code 
show_profile Show public profile information of a user.
search_users Search Gmail users by name or email address.
show_inbox_threads Show or search email threads you have received. Th
show_outbox_threads Show or search email threads you have sent. This w
show_archived_threads Show or search email threads you have archived. Th
show_spam_threads Show or search email threads that have been marked
show_category_sizes Show the number of email threads in each category 
show_thread Show detailed information about a given email thre
delete_thread Delete an email thread.
show_email Show detailed information about a given email.
label_thread Label an email thread.
unlabel_thread Remove label from an email thread.
mark_thread_read Mark an email thread as read.
mark_thread_unread Mark an email thread as unread.
mark_thread_archived Mark an email thread as archived.
mark_thread_unarchived Mark an email thread as unarchived.
mark_thread_spam Mark an email thread as spam.
mark_thread_not_spam Mark an email thread as not spam.
mark_thread_starred Mark an email thread as starred.
mark_thread_unstarred Mark an email thread as unstarred.
delete_email_in_thread Delete an email in a thread.
send_email Send a new email to one or more recipients.
reply_to_email Reply to an existing email in a thread.
forward_email_from_thread Forward an email from an email thread to one or mo
forward_email_thread Forward entire email thread to one or more recipie
show_drafts Show a list of user drafts.
create_draft Create a new draft.
show_draft Show detailed draft information.
delete_draft Delete draft information.
update_draft Update draft information.
send_email_from_draft Send a new email from a draft right away.
download_attachment Download a file attachment.
upload_attachments_to_draft Upload attachments to a draft.
remove_attachment_from_draft Delete an attachment from a draft.
```


### Environment Interaction 30
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
threads = apis.gmail.show_inbox_threads(access_token=token_str)
print(threads)
```

```
[
 {
  "email_thread_id": 47825,
  "email_ids": [
   20872,
   20873
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T18:34:25",
  "updated_at": "2023-05-17T18:34:25",
  "subject": "Running Late for Dinner",
  "participants": [
   {
    "name": "Brian Ritter",
    "email": "br_ritt@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 7447,
  "email_ids": [
   2282
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T18:08:08",
  "updated_at": "2023-05-17T18:08:08",
  "subject": "Monthly Sales Update",
  "participants": [
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 47823,
  "email_ids": [
   20868,
   20869,
   20870,
   20871
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T16:17:35",
  "updated_at": "2023-05-17T16:17:35",
  "subject": "Get-together Invitee",
  "participants": [
   {
    "name": "Brian Ritter",
    "email": "br_ritt@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 3518,
  "email_ids": [
   1078
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T12:55:33",
  "updated_at": "2023-05-17T12:55:33",
  "subject": "IT Helpdesk Satisfaction Survey",
  "participants": [
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 7414,
  "email_ids": [
   2273
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T12:08:45",
  "updated_at": "2023-05-17T12:08:45",
  "subject": "Reminder: Expense Report Submission",
  "participants": [
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 }
]
```


### Environment Interaction 31
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
email_content = apis.gmail.show_email(access_token=token_str, email_id=2282)
print(email_content)
```

```
{
 "email_id": 2282,
 "subject": "Monthly Sales Update",
 "body": "Hello team,\n\nPlease find attached the sales update for this month. Let's discuss the highlights in our upcoming team meeting.\n\nBest,\nEric",
 "response_to_email_id": null,
 "created_at": "2023-05-17T18:08:08",
 "sender": {
  "name": "Eric Bailey",
  "email": "eric.bailey@gmail.com"
 },
 "recipients": [
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 224,
   "file_name": "monthly_sales_report.pdf"
  }
 ]
}
```


### Environment Interaction 32
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
threads = apis.gmail.show_inbox_threads(access_token=token_str)
[print(t) for t in threads]
```

```
{
 "email_thread_id": 47825,
 "email_ids": [
  20872,
  20873
 ],
 "draft_ids": [],
 "incoming": true,
 "outgoing": true,
 "read": false,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T18:34:25",
 "updated_at": "2023-05-17T18:34:25",
 "subject": "Running Late for Dinner",
 "participants": [
  {
   "name": "Brian Ritter",
   "email": "br_ritt@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ]
}
{
 "email_thread_id": 7447,
 "email_ids": [
  2282
 ],
 "draft_ids": [],
 "incoming": true,
 "outgoing": false,
 "read": false,
 "label": null,
 "starred": true,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T18:08:08",
 "updated_at": "2023-05-17T18:08:08",
 "subject": "Monthly Sales Update",
 "participants": [
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  },
  {
   "name": "Eric Bailey",
   "email": "eric.bailey@gmail.com"
  }
 ]
}
{
 "email_thread_id": 47823,
 "email_ids": [
  20868,
  20869,
  20870,
  20871
 ],
 "draft_ids": [],
 "incoming": true,
 "outgoing": true,
 "read": false,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T16:17:35",
 "updated_at": "2023-05-17T16:17:35",
 "subject": "Get-together Invitee",
 "participants": [
  {
   "name": "Brian Ritter",
   "email": "br_ritt@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ]
}
{
 "email_thread_id": 3518,
 "email_ids": [
  1078
 ],
 "draft_ids": [],
 "incoming": true,
 "outgoing": false,
 "read": false,
 "label": null,
 "starred": true,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T12:55:33",
 "updated_at": "2023-05-17T12:55:33",
 "subject": "IT Helpdesk Satisfaction Survey",
 "participants": [
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  },
  {
   "name": "Eric Bailey",
   "email": "eric.bailey@gmail.com"
  }
 ]
}
{
 "email_thread_id": 7414,
 "email_ids": [
  2273
 ],
 "draft_ids": [],
 "incoming": true,
 "outgoing": false,
 "read": false,
 "label": null,
 "starred": true,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T12:08:45",
 "updated_at": "2023-05-17T12:08:45",
 "subject": "Reminder: Expense Report Submission",
 "participants": [
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  },
  {
   "name": "Eric Bailey",
   "email": "eric.bailey@gmail.com"
  }
 ]
}
```


### Environment Interaction 33
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
print(apis.gmail.show_email(access_token=token_str, email_id=20872))
print(apis.gmail.show_email(access_token=token_str, email_id=20873))
```

```
{
 "email_id": 20872,
 "subject": "Running Late for Dinner",
 "body": "... please don't wait for me today.",
 "response_to_email_id": null,
 "created_at": "2023-05-17T18:34:25",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 20873,
 "subject": "Re: Running Late for Dinner",
 "body": "Cool",
 "response_to_email_id": 20872,
 "created_at": "2023-05-17T18:39:08",
 "sender": {
  "name": "Patricia Ritter",
  "email": "pa_ritter@gmail.com"
 },
 "recipients": [
  {
   "name": "Brian Ritter",
   "email": "br_ritt@gmail.com"
  }
 ],
 "attachments": []
}
```


### Environment Interaction 34
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
threads = apis.gmail.show_inbox_threads(access_token=token_str)
all_ids = [eid for t in threads for eid in t.get('email_ids', [])]
print('All email IDs:', all_ids)
[print(apis.gmail.show_email(access_token=token_str, email_id=eid)) for eid in all_ids]
```

```
All email IDs: [20872, 20873, 2282, 20868, 20869, 20870, 20871, 1078, 2273]
{
 "email_id": 20872,
 "subject": "Running Late for Dinner",
 "body": "... please don't wait for me today.",
 "response_to_email_id": null,
 "created_at": "2023-05-17T18:34:25",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 20873,
 "subject": "Re: Running Late for Dinner",
 "body": "Cool",
 "response_to_email_id": 20872,
 "created_at": "2023-05-17T18:39:08",
 "sender": {
  "name": "Patricia Ritter",
  "email": "pa_ritter@gmail.com"
 },
 "recipients": [
  {
   "name": "Brian Ritter",
   "email": "br_ritt@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 2282,
 "subject": "Monthly Sales Update",
 "body": "Hello team,\n\nPlease find attached the sales update for this month. Let's discuss the highlights in our upcoming team meeting.\n\nBest,\nEric",
 "response_to_email_id": null,
 "created_at": "2023-05-17T18:08:08",
 "sender": {
  "name": "Eric Bailey",
  "email": "eric.bailey@gmail.com"
 },
 "recipients": [
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 224,
   "file_name": "monthly_sales_report.pdf"
  }
 ]
}
{
 "email_id": 20868,
 "subject": "Get-together Invitee",
 "body": "Have you invited all of your {natural_join(invitee_relations)}?",
 "response_to_email_id": null,
 "created_at": "2023-05-17T16:17:35",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 20869,
 "subject": "Re: Get-together Invitee",
 "body": "Yes, waiting on a couple of RSVPs, otherwise done. How about you?",
 "response_to_email_id": 20868,
 "created_at": "2023-05-17T17:03:04",
 "sender": {
  "name": "Patricia Ritter",
  "email": "pa_ritter@gmail.com"
 },
 "recipients": [
  {
   "name": "Brian Ritter",
   "email": "br_ritt@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 20870,
 "subject": "Re: Re: Get-together Invitee",
 "body": "I am done too. I am preparing the shopping list now.",
 "response_to_email_id": 20869,
 "created_at": "2023-05-17T17:47:27",
 "sender": {
  "name": "Brian Ritter",
  "email": "br_ritt@gmail.com"
 },
 "recipients": [
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 20871,
 "subject": "Re: Re: Re: Get-together Invitee",
 "body": "Sounds good!",
 "response_to_email_id": 20870,
 "created_at": "2023-05-17T18:13:12",
 "sender": {
  "name": "Patricia Ritter",
  "email": "pa_ritter@gmail.com"
 },
 "recipients": [
  {
   "name": "Brian Ritter",
   "email": "br_ritt@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 1078,
 "subject": "IT Helpdesk Satisfaction Survey",
 "body": "Dear team,\n\nWe would like to gather your feedback on our IT helpdesk services. Please take a few minutes to complete the attached survey and share your thoughts. Your input will help us improve our support and provide better service to our clients. https://forms.google.com/jfewpflqwer .\n\nThank you,\nEric\n",
 "response_to_email_id": null,
 "created_at": "2023-05-17T12:55:33",
 "sender": {
  "name": "Eric Bailey",
  "email": "eric.bailey@gmail.com"
 },
 "recipients": [
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": []
}
{
 "email_id": 2273,
 "subject": "Reminder: Expense Report Submission",
 "body": "Dear team,\n\nA friendly reminder to submit your expense reports for the recent business trip by end of today. Please ensure that all receipts are attached and expenses are properly categorized. Let's keep our financial records accurate and up to date.\n\nRegards,\nEric",
 "response_to_email_id": null,
 "created_at": "2023-05-17T12:08:45",
 "sender": {
  "name": "Eric Bailey",
  "email": "eric.bailey@gmail.com"
 },
 "recipients": [
  {
   "name": "Nicholas Weber",
   "email": "nicholas.weber@gmail.com"
  },
  {
   "name": "Chris Mccoy",
   "email": "chris.mcco@gmail.com"
  },
  {
   "name": "Susan Burton",
   "email": "susanmiller@gmail.com"
  },
  {
   "name": "Chelsea Burch",
   "email": "chelsea-burch@gmail.com"
  },
  {
   "name": "Valerie Blackburn",
   "email": "va-blac@gmail.com"
  },
  {
   "name": "Kyle Moore",
   "email": "kyl_moor@gmail.com"
  },
  {
   "name": "Andrew Brown",
   "email": "andrew_brow@gmail.com"
  },
  {
   "name": "Patricia Ritter",
   "email": "pa_ritter@gmail.com"
  }
 ],
 "attachments": []
}
```


### Environment Interaction 35
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
for eid in [20868, 20869, 20870, 20871, 1078, 2273]:
    e = apis.gmail.show_email(access_token=token_str, email_id=eid)
    print('ID:', eid, 'Subject:', e.get('subject'), 'From:', e.get('sender',{}).get('email'))
    print('Body:', e.get('body','')[:1000])
    print('Attachments:', e.get('attachments'))
    print('---')
```

```
ID: 20868 Subject: Get-together Invitee From: br_ritt@gmail.com
Body: Have you invited all of your {natural_join(invitee_relations)}?
Attachments: []
---
ID: 20869 Subject: Re: Get-together Invitee From: pa_ritter@gmail.com
Body: Yes, waiting on a couple of RSVPs, otherwise done. How about you?
Attachments: []
---
ID: 20870 Subject: Re: Re: Get-together Invitee From: br_ritt@gmail.com
Body: I am done too. I am preparing the shopping list now.
Attachments: []
---
ID: 20871 Subject: Re: Re: Re: Get-together Invitee From: pa_ritter@gmail.com
Body: Sounds good!
Attachments: []
---
ID: 1078 Subject: IT Helpdesk Satisfaction Survey From: eric.bailey@gmail.com
Body: Dear team,

We would like to gather your feedback on our IT helpdesk services. Please take a few minutes to complete the attached survey and share your thoughts. Your input will help us improve our support and provide better service to our clients. https://forms.google.com/jfewpflqwer .

Thank you,
Eric

Attachments: []
---
ID: 2273 Subject: Reminder: Expense Report Submission From: eric.bailey@gmail.com
Body: Dear team,

A friendly reminder to submit your expense reports for the recent business trip by end of today. Please ensure that all receipts are attached and expenses are properly categorized. Let's keep our financial records accurate and up to date.

Regards,
Eric
Attachments: []
---
```


### Environment Interaction 36
----------------------------------------------------------------------------
```python
token_str = apis.gmail.login(username='pa_ritter@gmail.com', password='}v0#GvJ')['access_token']
threads = apis.gmail.show_inbox_threads(access_token=token_str, page=2)
print(threads)
```

```
[
 {
  "email_thread_id": 47825,
  "email_ids": [
   20872,
   20873
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T18:34:25",
  "updated_at": "2023-05-17T18:34:25",
  "subject": "Running Late for Dinner",
  "participants": [
   {
    "name": "Brian Ritter",
    "email": "br_ritt@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 7447,
  "email_ids": [
   2282
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T18:08:08",
  "updated_at": "2023-05-17T18:08:08",
  "subject": "Monthly Sales Update",
  "participants": [
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 47823,
  "email_ids": [
   20868,
   20869,
   20870,
   20871
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T16:17:35",
  "updated_at": "2023-05-17T16:17:35",
  "subject": "Get-together Invitee",
  "participants": [
   {
    "name": "Brian Ritter",
    "email": "br_ritt@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 3518,
  "email_ids": [
   1078
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T12:55:33",
  "updated_at": "2023-05-17T12:55:33",
  "subject": "IT Helpdesk Satisfaction Survey",
  "participants": [
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 7414,
  "email_ids": [
   2273
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": true,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T12:08:45",
  "updated_at": "2023-05-17T12:08:45",
  "subject": "Reminder: Expense Report Submission",
  "participants": [
   {
    "name": "Nicholas Weber",
    "email": "nicholas.weber@gmail.com"
   },
   {
    "name": "Chris Mccoy",
    "email": "chris.mcco@gmail.com"
   },
   {
    "name": "Susan Burton",
    "email": "susanmiller@gmail.com"
   },
   {
    "name": "Chelsea Burch",
    "email": "chelsea-burch@gmail.com"
   },
   {
    "name": "Valerie Blackburn",
    "email": "va-blac@gmail.com"
   },
   {
    "name": "Kyle Moore",
    "email": "kyl_moor@gmail.com"
   },
   {
    "name": "Andrew Brown",
    "email": "andrew_brow@gmail.com"
   },
   {
    "name": "Patricia Ritter",
    "email": "pa_ritter@gmail.com"
   },
   {
    "name": "Eric Bailey",
    "email": "eric.bailey@gmail.com"
   }
  ]
 }
]
```

