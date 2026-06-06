
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
 "instruction": "Delete all my Gmail drafts that have empty subject or body.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "!#i62}T"
 },
 {
  "account_name": "file_system",
  "password": "0rE1V#a"
 },
 {
  "account_name": "gmail",
  "password": "u%TW7ah"
 },
 {
  "account_name": "phone",
  "password": "4_%505T"
 },
 {
  "account_name": "simple_note",
  "password": "Q=srh$w"
 },
 {
  "account_name": "splitwise",
  "password": "]aOK-3Z"
 },
 {
  "account_name": "spotify",
  "password": "aHOM-+d"
 },
 {
  "account_name": "todoist",
  "password": "ffqROlZ"
 },
 {
  "account_name": "venmo",
  "password": "B)]&d{u"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Katie",
 "last_name": "Simpson",
 "email": "kat_simp@gmail.com",
 "phone_number": "6727300099",
 "birthday": "1965-01-15",
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
print(apis.api_docs.show_api_descriptions('gmail'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.api_docs.show_api_descriptions('gmail'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: _wrap_api_request.<locals>._api_request() takes 0 positional arguments but 1 was given
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions())
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.api_docs.show_api_descriptions())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Validation error. Reason: \napp_name: field required"}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_app_descriptions()); print(apis.api_docs.show_api_descriptions(app_name='gmail'))
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


### Environment Interaction 5
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


### Environment Interaction 6
----------------------------------------------------------------------------
```python
gmail_password = [p for p in apis.supervisor.show_account_passwords() if p['account_name'] == 'gmail'][0]['password']
print(apis.gmail.login(username='kat_simp@gmail.com', password=gmail_password))
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI",
 "token_type": "Bearer"
}
```


### Environment Interaction 7
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


### Environment Interaction 8
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='draft'))
```

```
[
 {
  "app_name": "gmail",
  "api_name": "delete_draft",
  "path": "/drafts/{draft_id}",
  "method": "DELETE",
  "description": "Delete draft information.",
  "parameters": [
   {
    "name": "draft_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the draft to delete.",
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
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "update_draft",
  "path": "/drafts/{draft_id}",
  "method": "PATCH",
  "description": "Update draft information.",
  "parameters": [
   {
    "name": "draft_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the draft to update.",
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
    "name": "email_addresses",
    "type": "list[string]",
    "required": false,
    "description": "List of recipient email addresses.",
    "default": null,
    "constraints": []
   },
   {
    "name": "subject",
    "type": "string",
    "required": false,
    "description": "The updated subject of the draft.",
    "default": null,
    "constraints": []
   },
   {
    "name": "body",
    "type": "string",
    "required": false,
    "description": "The updated body of the draft.",
    "default": null,
    "constraints": []
   },
   {
    "name": "belongs_to_email_thread_id",
    "type": "integer",
    "required": false,
    "description": "The updated ID of the email thread that the draft should belong to. Must be passed if it's a reply to an email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "response_to_email_id",
    "type": "integer",
    "required": false,
    "description": "The updated ID of the email in the thread that the draft is a response to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "scheduled_send_at",
    "type": "string",
    "required": false,
    "description": "The updated time at which the draft should be sent in YYYY-MM-DD|HH:MM:SS format.To remove the scheduled delivery, pass 'None' string, as leaving it empty or null is for when you don't want to update it.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "create_draft",
  "path": "/drafts",
  "method": "POST",
  "description": "Create a new draft.",
  "parameters": [
   {
    "name": "recipient_email_addresses",
    "type": "list[string]",
    "required": true,
    "description": "List of recipient email addresses.",
    "default": null,
    "constraints": []
   },
   {
    "name": "body",
    "type": "string",
    "required": true,
    "description": "The body of the draft.",
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
    "name": "subject",
    "type": "string",
    "required": false,
    "description": "The subject of the draft. Must be None if it's a reply to an email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "belongs_to_email_thread_id",
    "type": "integer",
    "required": false,
    "description": "The ID of the email thread that the draft should belong to. Must be passed if it's a reply to or forward of an email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "response_to_email_id",
    "type": "integer",
    "required": false,
    "description": "The ID of the email in the thread that the draft should responds to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "attachment_file_paths",
    "type": "list[string]",
    "required": false,
    "description": "List of absolute file paths (starting with /) from the file_system app to attach to the draft.",
    "default": null,
    "constraints": []
   },
   {
    "name": "scheduled_send_at",
    "type": "string",
    "required": false,
    "description": "If set, the draft will be sent at the specified future time in YYYY-MM-DD|HH:MM:SS format. Otherwise, it will not be sent until you manually send it.",
    "default": null,
    "constraints": []
   },
   {
    "name": "file_system_access_token",
    "type": "string",
    "required": false,
    "description": "Access token obtained from file_system app login. Only needed for attachments.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "draft_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "show_draft",
  "path": "/drafts/{draft_id}",
  "method": "GET",
  "description": "Show detailed draft information.",
  "parameters": [
   {
    "name": "draft_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the draft to show.",
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
   }
  ],
  "response_schemas": {
   "success": {
    "draft_id": 1,
    "subject": "string",
    "body": "string",
    "belongs_to_email_thread_id": 1,
    "response_to_email_id": 1,
    "scheduled_send_at": "2019-01-01T00:00:00",
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "recipients": [
     {
      "name": "string",
      "email": "user@example.com"
     }
    ],
    "attachments": [
     {
      "id": 1,
      "file_name": "string"
     }
    ]
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "show_drafts",
  "path": "/drafts",
  "method": "GET",
  "description": "Show a list of user drafts.",
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
    "name": "recipient_email",
    "type": "string",
    "required": false,
    "description": "Filter emails by recipient email address.",
    "default": null,
    "constraints": [
     "value is email address"
    ]
   },
   {
    "name": "attachment",
    "type": "boolean",
    "required": false,
    "description": "Filter drafts by attachment status.",
    "default": null,
    "constraints": []
   },
   {
    "name": "scheduled",
    "type": "boolean",
    "required": false,
    "description": "Filter drafts by whether they are scheduled to be sent in the future.",
    "default": null,
    "constraints": []
   },
   {
    "name": "belongs_to_email_thread_id",
    "type": "integer",
    "required": false,
    "description": "Filter drafts by email thread ID that the draft belongs to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "response_to_email_id",
    "type": "integer",
    "required": false,
    "description": "Filter drafts by email ID that the draft responds to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "min_created_at",
    "type": "string",
    "required": false,
    "description": "Filter drafts by minimum created_at date in YYYY-MM-DD format.",
    "default": "1500-01-01",
    "constraints": []
   },
   {
    "name": "max_created_at",
    "type": "string",
    "required": false,
    "description": "Filter drafts by maximum created_at date in YYYY-MM-DD format.",
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
    "description": "The attribute to sort the drafts by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and updated_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -updated_at.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "draft_id": 1,
     "subject": "string",
     "body": "string",
     "belongs_to_email_thread_id": 1,
     "response_to_email_id": 1,
     "scheduled_send_at": "2019-01-01T00:00:00",
     "created_at": "2019-01-01T00:00:00",
     "updated_at": "2019-01-01T00:00:00",
     "recipients": [
      {
       "name": "string",
       "email": "user@example.com"
      }
     ],
     "attachments": [
      {
       "id": 1,
       "file_name": "string"
      }
     ]
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_category_sizes'))
```

```
{
 "app_name": "gmail",
 "api_name": "show_category_sizes",
 "path": "/category_sizes",
 "method": "GET",
 "description": "Show the number of email threads in each category of inbox, outbox, archived, spam, and the number of unscheduled and scheduled email drafts.",
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
   "inbox": 1,
   "outbox": 1,
   "archived": 1,
   "spam": 1,
   "unscheduled_drafts": 1,
   "scheduled_drafts": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
print(apis.gmail.show_category_sizes(access_token=access_token))
```

```
{
 "inbox": 228,
 "outbox": 95,
 "archived": 4,
 "spam": 16,
 "unscheduled_drafts": 17,
 "scheduled_drafts": 0
}
```


### Environment Interaction 11
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


### Environment Interaction 12
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_thread'))
```

```
{
 "app_name": "gmail",
 "api_name": "show_thread",
 "path": "/email_threads/{email_thread_id}",
 "method": "GET",
 "description": "Show detailed information about a given email thread, including emails and drafts within it.",
 "parameters": [
  {
   "name": "email_thread_id",
   "type": "integer",
   "required": true,
   "description": "The ID of the email thread to show.",
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
  }
 ],
 "response_schemas": {
  "success": {
   "email_thread_id": 1,
   "incoming": true,
   "outgoing": true,
   "read": true,
   "label": "string",
   "starred": true,
   "archived": true,
   "spam": true,
   "created_at": "2019-01-01T00:00:00",
   "updated_at": "2019-01-01T00:00:00",
   "emails": [
    {
     "email_id": 1,
     "subject": "string",
     "sender": {
      "name": "string",
      "email": "user@example.com"
     },
     "recipients": [
      {
       "name": "string",
       "email": "user@example.com"
      }
     ],
     "body": "string",
     "attachments": [
      {
       "id": 1,
       "file_name": "string"
      }
     ],
     "created_at": "2019-01-01T00:00:00"
    }
   ],
   "drafts": [
    {
     "draft_id": 1,
     "response_to_email_id": 1,
     "subject": "string",
     "recipients": [
      {
       "name": "string",
       "email": "user@example.com"
      }
     ],
     "body": "string",
     "attachments": [
      {
       "id": 1,
       "file_name": "string"
      }
     ],
     "scheduled_send_at": "2019-01-01T00:00:00",
     "created_at": "2019-01-01T00:00:00",
     "updated_at": "2019-01-01T00:00:00"
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
print(apis.gmail.show_inbox_threads(access_token=access_token))
```

```
[
 {
  "email_thread_id": 7018,
  "email_ids": [
   2145,
   2146,
   2147
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": true,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-18T08:55:05",
  "updated_at": "2023-05-18T08:55:05",
  "subject": "Conference Attendance Approval",
  "participants": [
   {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 33911,
  "email_ids": [
   13912
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T17:21:32",
  "updated_at": "2023-05-17T17:21:32",
  "subject": "Amazon Delivery Update for Order #1785",
  "participants": [
   {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   },
   {
    "name": "Amazon Notifications",
    "email": "notifications@amazon.com"
   }
  ]
 },
 {
  "email_thread_id": 33913,
  "email_ids": [
   13913
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-17T11:42:20",
  "updated_at": "2023-05-17T11:42:20",
  "subject": "Amazon Return Confirmation and Label",
  "participants": [
   {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   },
   {
    "name": "Amazon Notifications",
    "email": "notifications@amazon.com"
   }
  ]
 },
 {
  "email_thread_id": 9442,
  "email_ids": [
   2922,
   2923
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": true,
  "read": true,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-16T13:52:06",
  "updated_at": "2023-05-16T13:52:06",
  "subject": "Reminder: Team Lunch Tomorrow",
  "participants": [
   {
    "name": "Mason Smith",
    "email": "masmith@gmail.com"
   },
   {
    "name": "Ronald Harrison",
    "email": "ron.harrison@gmail.com"
   },
   {
    "name": "Isaac Miller",
    "email": "ismill@gmail.com"
   },
   {
    "name": "Miranda Weber",
    "email": "mir-powe@gmail.com"
   },
   {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   {
    "name": "Adrian Burton",
    "email": "adrian_burt@gmail.com"
   },
   {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   },
   {
    "name": "Bradley Ball",
    "email": "bradley_ball@gmail.com"
   }
  ]
 },
 {
  "email_thread_id": 33915,
  "email_ids": [
   13914
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-16T12:21:29",
  "updated_at": "2023-05-16T12:21:29",
  "subject": "Amazon Return Confirmation and Label",
  "participants": [
   {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   },
   {
    "name": "Amazon Notifications",
    "email": "notifications@amazon.com"
   }
  ]
 }
]
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
threads = apis.gmail.show_inbox_threads(access_token=access_token)
for thread in threads:
    print(apis.gmail.show_thread(email_thread_id=thread['email_thread_id'], access_token=access_token))
```

```
{
 "email_thread_id": 7018,
 "incoming": true,
 "outgoing": true,
 "read": true,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-18T08:55:05",
 "updated_at": "2023-05-18T08:55:05",
 "emails": [
  {
   "email_id": 2145,
   "subject": "Conference Attendance Approval",
   "sender": {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   "recipients": [
    {
     "name": "Katie Simpson",
     "email": "kat_simp@gmail.com"
    }
   ],
   "body": "Hi Katie,\n\nI'm interested in attending a conference scheduled for next week. The event aligns well with our current projects and I believe it will provide valuable insights. Kindly let me know if I can proceed with registration.\n\nThanks,\nJeremy",
   "attachments": [],
   "created_at": "2023-05-18T08:55:05"
  },
  {
   "email_id": 2146,
   "subject": "Re: Conference Attendance Approval",
   "sender": {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   },
   "recipients": [
    {
     "name": "Jeremy Calhoun",
     "email": "jer.calhoun@gmail.com"
    }
   ],
   "body": "Sure thing. Go ahead!",
   "attachments": [],
   "created_at": "2023-05-18T09:20:29"
  },
  {
   "email_id": 2147,
   "subject": "Re: Re: Conference Attendance Approval",
   "sender": {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   "recipients": [
    {
     "name": "Katie Simpson",
     "email": "kat_simp@gmail.com"
    }
   ],
   "body": "Awesome, thank you!",
   "attachments": [],
   "created_at": "2023-05-18T09:20:43"
  }
 ],
 "drafts": []
}
{
 "email_thread_id": 33911,
 "incoming": true,
 "outgoing": false,
 "read": false,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T17:21:32",
 "updated_at": "2023-05-17T17:21:32",
 "emails": [
  {
   "email_id": 13912,
   "subject": "Amazon Delivery Update for Order #1785",
   "sender": {
    "name": "Amazon Notifications",
    "email": "notifications@amazon.com"
   },
   "recipients": [
    {
     "name": "Katie Simpson",
     "email": "kat_simp@gmail.com"
    }
   ],
   "body": "\nHi Katie Simpson,\n\nKala KA-15S Mahogany Soprano Ukulele from your order #1785 has been delivered.\n\nBest,\nAmazon Team\n",
   "attachments": [],
   "created_at": "2023-05-17T17:21:32"
  }
 ],
 "drafts": []
}
{
 "email_thread_id": 33913,
 "incoming": true,
 "outgoing": false,
 "read": false,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-17T11:42:20",
 "updated_at": "2023-05-17T11:42:20",
 "emails": [
  {
   "email_id": 13913,
   "subject": "Amazon Return Confirmation and Label",
   "sender": {
    "name": "Amazon Notifications",
    "email": "notifications@amazon.com"
   },
   "recipients": [
    {
     "name": "Katie Simpson",
     "email": "kat_simp@gmail.com"
    }
   ],
   "body": "\nHello Katie Simpson,\n\nThis is a confirmation that your return request for the following has been initiated.\n\n-> 1 quantity of Rachael Ray Yum-o! Nonstick Baking Sheet from order #1785\n\nPlease find the return label attached herewith. You must print it and attach it to the package.\nThe package must be dropped off at the nearest FedEx location.\nWe will refund you the amount of the returned product(s) in your gift card balance.\n\nBest,\nAmazon Team\n",
   "attachments": [
    {
     "id": 5040,
     "file_name": "return_1785_484_1.txt"
    }
   ],
   "created_at": "2023-05-17T11:42:20"
  }
 ],
 "drafts": []
}
{
 "email_thread_id": 9442,
 "incoming": true,
 "outgoing": true,
 "read": true,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-16T13:52:06",
 "updated_at": "2023-05-16T13:52:06",
 "emails": [
  {
   "email_id": 2922,
   "subject": "Reminder: Team Lunch Tomorrow",
   "sender": {
    "name": "Katie Simpson",
    "email": "kat_simp@gmail.com"
   },
   "recipients": [
    {
     "name": "Mason Smith",
     "email": "masmith@gmail.com"
    },
    {
     "name": "Bradley Ball",
     "email": "bradley_ball@gmail.com"
    },
    {
     "name": "Ronald Harrison",
     "email": "ron.harrison@gmail.com"
    },
    {
     "name": "Isaac Miller",
     "email": "ismill@gmail.com"
    },
    {
     "name": "Miranda Weber",
     "email": "mir-powe@gmail.com"
    },
    {
     "name": "Jeremy Calhoun",
     "email": "jer.calhoun@gmail.com"
    },
    {
     "name": "Adrian Burton",
     "email": "adrian_burt@gmail.com"
    }
   ],
   "body": "Hello team,\n\nJust a friendly reminder that we have a team lunch planned for tomorrow at Orchid Oasis Eatery at 12:30 PM. It's a great opportunity to relax and catch up in an informal setting. Looking forward to seeing you all there!\n\nCheers,\nKatie",
   "attachments": [],
   "created_at": "2023-05-16T13:52:06"
  },
  {
   "email_id": 2923,
   "subject": "Re: Reminder: Team Lunch Tomorrow",
   "sender": {
    "name": "Bradley Ball",
    "email": "bradley_ball@gmail.com"
   },
   "recipients": [
    {
     "name": "Mason Smith",
     "email": "masmith@gmail.com"
    },
    {
     "name": "Katie Simpson",
     "email": "kat_simp@gmail.com"
    },
    {
     "name": "Ronald Harrison",
     "email": "ron.harrison@gmail.com"
    },
    {
     "name": "Isaac Miller",
     "email": "ismill@gmail.com"
    },
    {
     "name": "Miranda Weber",
     "email": "mir-powe@gmail.com"
    },
    {
     "name": "Jeremy Calhoun",
     "email": "jer.calhoun@gmail.com"
    },
    {
     "name": "Adrian Burton",
     "email": "adrian_burt@gmail.com"
    }
   ],
   "body": "Thanks for the reminder! Looking forward to it.\n\nRegards,\nBradley",
   "attachments": [],
   "created_at": "2023-05-16T14:19:52"
  }
 ],
 "drafts": []
}
{
 "email_thread_id": 33915,
 "incoming": true,
 "outgoing": false,
 "read": false,
 "label": null,
 "starred": false,
 "archived": false,
 "spam": false,
 "created_at": "2023-05-16T12:21:29",
 "updated_at": "2023-05-16T12:21:29",
 "emails": [
  {
   "email_id": 13914,
   "subject": "Amazon Return Confirmation and Label",
   "sender": {
    "name": "Amazon Notifications",
    "email": "notifications@amazon.com"
   },
   "recipients": [
    {
     "name": "Katie Simpson",
     "email": "kat_simp@gmail.com"
    }
   ],
   "body": "\nHello Katie Simpson,\n\nThis is a confirmation that your return request for the following has been initiated.\n\n-> 2 quantity of Kala KA-15S Mahogany Soprano Ukulele from order #1785\n\nPlease find the return label attached herewith. You must print it and attach it to the package.\nThe package must be dropped off at the nearest USPS location.\nWe will refund you the amount of the returned product(s) in your gift card balance.\n\nBest,\nAmazon Team\n",
   "attachments": [
    {
     "id": 5041,
     "file_name": "return_1785_314_2.txt"
    }
   ],
   "created_at": "2023-05-16T12:21:29"
  }
 ],
 "drafts": []
}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
threads = apis.gmail.show_inbox_threads(access_token=access_token)
drafts_to_delete = []
for thread in threads:
    thread_details = apis.gmail.show_thread(email_thread_id=thread['email_thread_id'], access_token=access_token)
    if 'drafts' in thread_details and thread_details['drafts']:
        for draft in thread_details['drafts']:
            if not draft['subject'] or not draft['body']:
                drafts_to_delete.append(draft['draft_id'])
print(drafts_to_delete)
```

```
[]
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
categories = ['inbox', 'outbox', 'archived', 'spam']
drafts_to_delete = []
for category in categories:
    threads = apis.gmail.show_inbox_threads(access_token=access_token, label=category)
    for thread in threads:
        thread_details = apis.gmail.show_thread(email_thread_id=thread['email_thread_id'], access_token=access_token)
        if 'drafts' in thread_details and thread_details['drafts']:
            for draft in thread_details['drafts']:
                if not draft['subject'] or not draft['body']:
                    drafts_to_delete.append(draft['draft_id'])
print(drafts_to_delete)
```

```
[]
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
print(apis.gmail.show_category_sizes(access_token=access_token))
```

```
{
 "inbox": 228,
 "outbox": 95,
 "archived": 4,
 "spam": 16,
 "unscheduled_drafts": 17,
 "scheduled_drafts": 0
}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='draft'))
```

```
[
 {
  "app_name": "gmail",
  "api_name": "delete_draft",
  "path": "/drafts/{draft_id}",
  "method": "DELETE",
  "description": "Delete draft information.",
  "parameters": [
   {
    "name": "draft_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the draft to delete.",
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
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "update_draft",
  "path": "/drafts/{draft_id}",
  "method": "PATCH",
  "description": "Update draft information.",
  "parameters": [
   {
    "name": "draft_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the draft to update.",
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
    "name": "email_addresses",
    "type": "list[string]",
    "required": false,
    "description": "List of recipient email addresses.",
    "default": null,
    "constraints": []
   },
   {
    "name": "subject",
    "type": "string",
    "required": false,
    "description": "The updated subject of the draft.",
    "default": null,
    "constraints": []
   },
   {
    "name": "body",
    "type": "string",
    "required": false,
    "description": "The updated body of the draft.",
    "default": null,
    "constraints": []
   },
   {
    "name": "belongs_to_email_thread_id",
    "type": "integer",
    "required": false,
    "description": "The updated ID of the email thread that the draft should belong to. Must be passed if it's a reply to an email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "response_to_email_id",
    "type": "integer",
    "required": false,
    "description": "The updated ID of the email in the thread that the draft is a response to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "scheduled_send_at",
    "type": "string",
    "required": false,
    "description": "The updated time at which the draft should be sent in YYYY-MM-DD|HH:MM:SS format.To remove the scheduled delivery, pass 'None' string, as leaving it empty or null is for when you don't want to update it.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "create_draft",
  "path": "/drafts",
  "method": "POST",
  "description": "Create a new draft.",
  "parameters": [
   {
    "name": "recipient_email_addresses",
    "type": "list[string]",
    "required": true,
    "description": "List of recipient email addresses.",
    "default": null,
    "constraints": []
   },
   {
    "name": "body",
    "type": "string",
    "required": true,
    "description": "The body of the draft.",
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
    "name": "subject",
    "type": "string",
    "required": false,
    "description": "The subject of the draft. Must be None if it's a reply to an email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "belongs_to_email_thread_id",
    "type": "integer",
    "required": false,
    "description": "The ID of the email thread that the draft should belong to. Must be passed if it's a reply to or forward of an email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "response_to_email_id",
    "type": "integer",
    "required": false,
    "description": "The ID of the email in the thread that the draft should responds to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "attachment_file_paths",
    "type": "list[string]",
    "required": false,
    "description": "List of absolute file paths (starting with /) from the file_system app to attach to the draft.",
    "default": null,
    "constraints": []
   },
   {
    "name": "scheduled_send_at",
    "type": "string",
    "required": false,
    "description": "If set, the draft will be sent at the specified future time in YYYY-MM-DD|HH:MM:SS format. Otherwise, it will not be sent until you manually send it.",
    "default": null,
    "constraints": []
   },
   {
    "name": "file_system_access_token",
    "type": "string",
    "required": false,
    "description": "Access token obtained from file_system app login. Only needed for attachments.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "draft_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "show_draft",
  "path": "/drafts/{draft_id}",
  "method": "GET",
  "description": "Show detailed draft information.",
  "parameters": [
   {
    "name": "draft_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the draft to show.",
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
   }
  ],
  "response_schemas": {
   "success": {
    "draft_id": 1,
    "subject": "string",
    "body": "string",
    "belongs_to_email_thread_id": 1,
    "response_to_email_id": 1,
    "scheduled_send_at": "2019-01-01T00:00:00",
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "recipients": [
     {
      "name": "string",
      "email": "user@example.com"
     }
    ],
    "attachments": [
     {
      "id": 1,
      "file_name": "string"
     }
    ]
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "show_drafts",
  "path": "/drafts",
  "method": "GET",
  "description": "Show a list of user drafts.",
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
    "name": "recipient_email",
    "type": "string",
    "required": false,
    "description": "Filter emails by recipient email address.",
    "default": null,
    "constraints": [
     "value is email address"
    ]
   },
   {
    "name": "attachment",
    "type": "boolean",
    "required": false,
    "description": "Filter drafts by attachment status.",
    "default": null,
    "constraints": []
   },
   {
    "name": "scheduled",
    "type": "boolean",
    "required": false,
    "description": "Filter drafts by whether they are scheduled to be sent in the future.",
    "default": null,
    "constraints": []
   },
   {
    "name": "belongs_to_email_thread_id",
    "type": "integer",
    "required": false,
    "description": "Filter drafts by email thread ID that the draft belongs to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "response_to_email_id",
    "type": "integer",
    "required": false,
    "description": "Filter drafts by email ID that the draft responds to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "min_created_at",
    "type": "string",
    "required": false,
    "description": "Filter drafts by minimum created_at date in YYYY-MM-DD format.",
    "default": "1500-01-01",
    "constraints": []
   },
   {
    "name": "max_created_at",
    "type": "string",
    "required": false,
    "description": "Filter drafts by maximum created_at date in YYYY-MM-DD format.",
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
    "description": "The attribute to sort the drafts by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and updated_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -updated_at.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "draft_id": 1,
     "subject": "string",
     "body": "string",
     "belongs_to_email_thread_id": 1,
     "response_to_email_id": 1,
     "scheduled_send_at": "2019-01-01T00:00:00",
     "created_at": "2019-01-01T00:00:00",
     "updated_at": "2019-01-01T00:00:00",
     "recipients": [
      {
       "name": "string",
       "email": "user@example.com"
      }
     ],
     "attachments": [
      {
       "id": 1,
       "file_name": "string"
      }
     ]
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='show_drafts'))
```

```
{
 "app_name": "gmail",
 "api_name": "show_drafts",
 "path": "/drafts",
 "method": "GET",
 "description": "Show a list of user drafts.",
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
   "name": "recipient_email",
   "type": "string",
   "required": false,
   "description": "Filter emails by recipient email address.",
   "default": null,
   "constraints": [
    "value is email address"
   ]
  },
  {
   "name": "attachment",
   "type": "boolean",
   "required": false,
   "description": "Filter drafts by attachment status.",
   "default": null,
   "constraints": []
  },
  {
   "name": "scheduled",
   "type": "boolean",
   "required": false,
   "description": "Filter drafts by whether they are scheduled to be sent in the future.",
   "default": null,
   "constraints": []
  },
  {
   "name": "belongs_to_email_thread_id",
   "type": "integer",
   "required": false,
   "description": "Filter drafts by email thread ID that the draft belongs to.",
   "default": null,
   "constraints": []
  },
  {
   "name": "response_to_email_id",
   "type": "integer",
   "required": false,
   "description": "Filter drafts by email ID that the draft responds to.",
   "default": null,
   "constraints": []
  },
  {
   "name": "min_created_at",
   "type": "string",
   "required": false,
   "description": "Filter drafts by minimum created_at date in YYYY-MM-DD format.",
   "default": "1500-01-01",
   "constraints": []
  },
  {
   "name": "max_created_at",
   "type": "string",
   "required": false,
   "description": "Filter drafts by maximum created_at date in YYYY-MM-DD format.",
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
   "description": "The attribute to sort the drafts by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and updated_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -updated_at.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "draft_id": 1,
    "subject": "string",
    "body": "string",
    "belongs_to_email_thread_id": 1,
    "response_to_email_id": 1,
    "scheduled_send_at": "2019-01-01T00:00:00",
    "created_at": "2019-01-01T00:00:00",
    "updated_at": "2019-01-01T00:00:00",
    "recipients": [
     {
      "name": "string",
      "email": "user@example.com"
     }
    ],
    "attachments": [
     {
      "id": 1,
      "file_name": "string"
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


### Environment Interaction 20
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
drafts = []
page_index = 0
page_limit = 100
while True:
    response = apis.gmail.show_drafts(access_token=access_token, page_index=page_index, page_limit=page_limit)
    drafts.extend(response)
    if len(response) < page_limit:
        break
    page_index += 1
drafts_to_delete = [draft['draft_id'] for draft in drafts if not draft['subject'] or not draft['body']]
print(drafts_to_delete)
```

```
Execution failed. Traceback:
  File "<python-input>", line 6, in <module>
    response = apis.gmail.show_drafts(access_token=access_token, page_index=page_index, page_limit=page_limit)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"Validation error. Reason: \npage_limit: ensure this value is less than or equal to 20"}
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
drafts = []
page_index = 0
page_limit = 20
while True:
    response = apis.gmail.show_drafts(access_token=access_token, page_index=page_index, page_limit=page_limit)
    drafts.extend(response)
    if len(response) < page_limit:
        break
    page_index += 1
drafts_to_delete = [draft['draft_id'] for draft in drafts if not draft['subject'] or not draft['body']]
print(drafts_to_delete)
```

```
[27, 85, 209, 84, 24, 476, 52, 293]
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='delete_draft'))
```

```
{
 "app_name": "gmail",
 "api_name": "delete_draft",
 "path": "/drafts/{draft_id}",
 "method": "DELETE",
 "description": "Delete draft information.",
 "parameters": [
  {
   "name": "draft_id",
   "type": "integer",
   "required": true,
   "description": "The ID of the draft to delete.",
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
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
response = apis.gmail.show_drafts(access_token=access_token)
print(type(response))
print(response)
```

```
<class 'list'>
[
 {
  "draft_id": 479,
  "subject": "Performance Review Schedules",
  "body": "Hello Adrian,\n\nYour performance review is scheduled for next week. Please prepare any materials or feedback you'd like to discuss.\n\nThanks,\nKatie",
  "belongs_to_email_thread_id": null,
  "response_to_email_id": null,
  "scheduled_send_at": null,
  "created_at": "2023-05-17T18:36:03",
  "updated_at": "2023-05-17T18:36:03",
  "recipients": [
   {
    "name": "Adrian Burton",
    "email": "adrian_burt@gmail.com"
   }
  ],
  "attachments": []
 },
 {
  "draft_id": 25,
  "subject": "Updated Office Security Protocols",
  "body": "Dear team,\n\nPlease review the updated security protocols for our office. It's important that everyone is aware and compliant. Safety first!\n\nCheers,\nKatie",
  "belongs_to_email_thread_id": null,
  "response_to_email_id": null,
  "scheduled_send_at": null,
  "created_at": "2023-05-15T13:30:25",
  "updated_at": "2023-05-15T13:30:25",
  "recipients": [
   {
    "name": "Bradley Ball",
    "email": "bradley_ball@gmail.com"
   },
   {
    "name": "Ronald Harrison",
    "email": "ron.harrison@gmail.com"
   },
   {
    "name": "Isaac Miller",
    "email": "ismill@gmail.com"
   },
   {
    "name": "Miranda Weber",
    "email": "mir-powe@gmail.com"
   },
   {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   {
    "name": "Mason Smith",
    "email": "masmith@gmail.com"
   },
   {
    "name": "Adrian Burton",
    "email": "adrian_burt@gmail.com"
   }
  ],
  "attachments": []
 },
 {
  "draft_id": 27,
  "subject": "Upcoming Project Deadlines",
  "body": "",
  "belongs_to_email_thread_id": null,
  "response_to_email_id": null,
  "scheduled_send_at": null,
  "created_at": "2023-05-11T08:36:31",
  "updated_at": "2023-05-11T08:36:31",
  "recipients": [
   {
    "name": "Bradley Ball",
    "email": "bradley_ball@gmail.com"
   },
   {
    "name": "Ronald Harrison",
    "email": "ron.harrison@gmail.com"
   },
   {
    "name": "Isaac Miller",
    "email": "ismill@gmail.com"
   },
   {
    "name": "Miranda Weber",
    "email": "mir-powe@gmail.com"
   },
   {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   {
    "name": "Mason Smith",
    "email": "masmith@gmail.com"
   },
   {
    "name": "Adrian Burton",
    "email": "adrian_burt@gmail.com"
   }
  ],
  "attachments": []
 },
 {
  "draft_id": 26,
  "subject": "Internship Program Applications Open",
  "body": "Hello team,\n\nOur internship program applications are now open! If you know any students or recent graduates who would be interested in joining our team, please share the attached flyer with them. We appreciate your help in spreading the word.\n\nBest regards,\nKatie\n",
  "belongs_to_email_thread_id": null,
  "response_to_email_id": null,
  "scheduled_send_at": null,
  "created_at": "2023-05-10T15:51:40",
  "updated_at": "2023-05-10T15:51:40",
  "recipients": [
   {
    "name": "Bradley Ball",
    "email": "bradley_ball@gmail.com"
   },
   {
    "name": "Ronald Harrison",
    "email": "ron.harrison@gmail.com"
   },
   {
    "name": "Isaac Miller",
    "email": "ismill@gmail.com"
   },
   {
    "name": "Miranda Weber",
    "email": "mir-powe@gmail.com"
   },
   {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   {
    "name": "Mason Smith",
    "email": "masmith@gmail.com"
   },
   {
    "name": "Adrian Burton",
    "email": "adrian_burt@gmail.com"
   }
  ],
  "attachments": []
 },
 {
  "draft_id": 85,
  "subject": "",
  "body": "",
  "belongs_to_email_thread_id": null,
  "response_to_email_id": null,
  "scheduled_send_at": null,
  "created_at": "2023-05-09T15:26:10",
  "updated_at": "2023-05-09T15:26:10",
  "recipients": [
   {
    "name": "Isaac Miller",
    "email": "ismill@gmail.com"
   },
   {
    "name": "Bradley Ball",
    "email": "bradley_ball@gmail.com"
   },
   {
    "name": "Ronald Harrison",
    "email": "ron.harrison@gmail.com"
   },
   {
    "name": "Miranda Weber",
    "email": "mir-powe@gmail.com"
   },
   {
    "name": "Jeremy Calhoun",
    "email": "jer.calhoun@gmail.com"
   },
   {
    "name": "Mason Smith",
    "email": "masmith@gmail.com"
   },
   {
    "name": "Adrian Burton",
    "email": "adrian_burt@gmail.com"
   }
  ],
  "attachments": []
 }
]
```


### Environment Interaction 24
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
for draft_id in [27, 85, 209, 84, 24, 476, 52, 293]:
    result = apis.gmail.delete_draft(access_token=access_token, draft_id=draft_id)
    print(draft_id, result)
```

```
27 {'message': 'Draft deleted.'}
85 {'message': 'Draft deleted.'}
209 {'message': 'Draft deleted.'}
84 {'message': 'Draft deleted.'}
24 {'message': 'Draft deleted.'}
476 {'message': 'Draft deleted.'}
52 {'message': 'Draft deleted.'}
293 {'message': 'Draft deleted.'}
```


### Environment Interaction 25
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


### Environment Interaction 26
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_app_descriptions())
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
```


### Environment Interaction 27
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtrYXRfc2ltcEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.ChdP7jyPQYnkUJXZBywOBrJmq36axbD0MMgSYdFGSGI"
response = apis.gmail.show_drafts(access_token=access_token)
remaining = [d for d in response if not d['subject'] or not d['body']]
print('Remaining empty drafts:', remaining)
if not remaining:
    apis.supervisor.complete_task(status="success")
```

```
Remaining empty drafts: []
```


### Environment Interaction 28
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='supervisor', api_name='complete_task'))
```

```
{
 "app_name": "supervisor",
 "api_name": "complete_task",
 "path": "/message",
 "method": "POST",
 "description": "Mark the currently active task as complete with the given answer.",
 "parameters": [
  {
   "name": "answer",
   "type": "number | integer | string",
   "required": false,
   "description": "The answer to the task instruction. Pass it if and only if the task requests an answer, e.g., 'How many songs are in the Spotify queue?'. The answer must be concise, such as a number, a yes/no, or a specific entity, name, etc, e.g., '10' in this case. If the task is not a question, e.g., 'Start my Spotify music player.', the answer must be left to the default value, i.e., None.",
   "default": null,
   "constraints": []
  },
  {
   "name": "status",
   "type": "string",
   "required": false,
   "description": "Mark the task complete.",
   "default": "success",
   "constraints": [
    "value in ['success', 'fail']"
   ]
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```

