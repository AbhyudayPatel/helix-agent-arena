
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
 "instruction": "I get monthly cable bill via email on the 1st of every month for the previous month's usage. I pay for it but its total cost is to be shared equally with my roommates and me. In our Splitwise group, create an expense for each month with a note \"cable bill [MM-YY]\" and the associated total cost (including my share). The MM-YY refers to the month and year the bill usage is for. Do it only for bills for this year's cable usage.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "oIhoOb9"
 },
 {
  "account_name": "file_system",
  "password": "4k9jcny"
 },
 {
  "account_name": "gmail",
  "password": "#x}}5n5"
 },
 {
  "account_name": "phone",
  "password": "X53y6aW"
 },
 {
  "account_name": "simple_note",
  "password": "eizVxAh"
 },
 {
  "account_name": "splitwise",
  "password": "F{Q8_pw"
 },
 {
  "account_name": "spotify",
  "password": "3a-m^o6"
 },
 {
  "account_name": "todoist",
  "password": "+&R$o4K"
 },
 {
  "account_name": "venmo",
  "password": "rl2A-Xl"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Carl",
 "last_name": "Brown",
 "email": "carbrown@gmail.com",
 "phone_number": "7934818191",
 "birthday": "1982-11-12",
 "sex": "male"
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
print(apis.api_docs.show_api_doc(app_name='gmail', api_name='search_emails'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.api_docs.show_api_doc(app_name='gmail', api_name='search_emails'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name search_emails found for the gmail app. Check the api and app name again."}
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(app_name='gmail', query='email'))
print(apis.api_docs.show_api_descriptions(app_name='gmail'))
```

```
[
 {
  "app_name": "gmail",
  "api_name": "forward_email_from_thread",
  "path": "/email_threads/{email_thread_id}/emails/{email_id}/forward",
  "method": "POST",
  "description": "Forward an email from an email thread to one or more recipients.",
  "parameters": [
   {
    "name": "email_thread_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email thread to forward.",
    "default": null,
    "constraints": []
   },
   {
    "name": "email_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email to forward.",
    "default": null,
    "constraints": []
   },
   {
    "name": "email_addresses",
    "type": "list[string]",
    "required": true,
    "description": "List of recipient email addresses.",
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
    "name": "draft_not_send",
    "type": "boolean",
    "required": false,
    "description": "If true, the email will be saved as a draft instead of being sent. This way it can be edited before sending.",
    "default": false,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "sent_email_thread_id": 1,
    "sent_email_id": 1,
    "draft_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "show_email",
  "path": "/emails/{email_id}",
  "method": "GET",
  "description": "Show detailed information about a given email.",
  "parameters": [
   {
    "name": "email_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email to show.",
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
    "email_id": 1,
    "subject": "string",
    "body": "string",
    "response_to_email_id": 1,
    "created_at": "2019-01-01T00:00:00",
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
  "api_name": "delete_email_in_thread",
  "path": "/email_threads/{email_thread_id}/emails/{email_id}",
  "method": "DELETE",
  "description": "Delete an email in a thread.",
  "parameters": [
   {
    "name": "email_thread_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email thread to delete an email from.",
    "default": null,
    "constraints": []
   },
   {
    "name": "email_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email to delete.",
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
  "api_name": "send_email",
  "path": "/emails",
  "method": "POST",
  "description": "Send a new email to one or more recipients.",
  "parameters": [
   {
    "name": "email_addresses",
    "type": "list[string]",
    "required": true,
    "description": "List of recipient email addresses.",
    "default": null,
    "constraints": []
   },
   {
    "name": "subject",
    "type": "string",
    "required": true,
    "description": "The subject of the email.",
    "default": null,
    "constraints": []
   },
   {
    "name": "body",
    "type": "string",
    "required": true,
    "description": "The body of the email.",
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
    "name": "attachment_file_paths",
    "type": "list[string]",
    "required": false,
    "description": "List of absolute file paths (starting with /) from the file_system app to attach to the email.",
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
    "sent_email_thread_id": 1,
    "sent_email_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "gmail",
  "api_name": "reply_to_email",
  "path": "/email_threads/{email_thread_id}/emails/{email_id}/reply",
  "method": "POST",
  "description": "Reply to an existing email in a thread.",
  "parameters": [
   {
    "name": "email_thread_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email thread to reply to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "email_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the email to reply to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "body",
    "type": "string",
    "required": true,
    "description": "The body of the reply email.",
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
    "description": "List of recipient email addresses. If passed, it'll reply to all recipients in the list, otherwise, to the sender.",
    "default": null,
    "constraints": []
   },
   {
    "name": "attachment_file_paths",
    "type": "list[string]",
    "required": false,
    "description": "List of absolute file paths (starting with /) from the file_system app to attach to the email.",
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
    "sent_email_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
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


### Environment Interaction 4
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(app_name='gmail', query='fetch'))
print(apis.api_docs.search_api_docs(app_name='gmail', query='search'))
print(apis.api_docs.search_api_docs(app_name='gmail', query='list'))
```

```
[
 {
  "app_name": "api_docs",
  "api_name": "show_app_descriptions",
  "path": "/app_descriptions",
  "method": "GET",
  "description": "Show descriptions for all apps available.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_descriptions",
  "path": "/api_descriptions",
  "method": "GET",
  "description": "Show descriptions for all APIs available for a given app.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name to return API descriptions for.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_doc",
  "path": "/api_doc",
  "method": "GET",
  "description": "Show detailed API doc.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name for the API.",
    "default": null,
    "constraints": []
   },
   {
    "name": "api_name",
    "type": "string",
    "required": true,
    "description": "Name of the API.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "app_name": "string",
    "api_name": "string",
    "path": "string",
    "method": "string",
    "description": "string",
    "parameters": [
     {
      "name": "string",
      "type": "string",
      "required": true,
      "description": "string",
      "default": null,
      "constraints": [
       "string"
      ]
     }
    ],
    "response_schemas": {
     "success": [
      {}
     ],
     "failure": [
      {}
     ]
    }
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "search_api_docs",
  "path": "/api_docs",
  "method": "GET",
  "description": "Search for relevant API docs.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
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
   }
  ],
  "response_schemas": {
   "success": [
    {
     "app_name": "string",
     "api_name": "string",
     "path": "string",
     "method": "string",
     "description": "string",
     "parameters": [
      {
       "name": "string",
       "type": "string",
       "required": true,
       "description": "string",
       "default": null,
       "constraints": [
        "string"
       ]
      }
     ],
     "response_schemas": {
      "success": [
       {}
      ],
      "failure": [
       {}
      ]
     }
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "supervisor",
  "api_name": "show_active_task",
  "path": "/active_task",
  "method": "GET",
  "description": "Show the currently active task assigned to you by the supervisor.",
  "parameters": [],
  "response_schemas": {
   "success": {
    "instruction": "string",
    "status": "string",
    "answer": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
[
 {
  "app_name": "todoist",
  "api_name": "search_labels",
  "path": "/labels",
  "method": "GET",
  "description": "Search your or task labels.",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from todoist app login.",
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
    "name": "task_id",
    "type": "integer",
    "required": false,
    "description": "The ID of the task to filter by.",
    "default": null,
    "constraints": []
   },
   {
    "name": "color",
    "type": "string",
    "required": false,
    "description": "The color of the label to filter by.",
    "default": null,
    "constraints": [
     "value in ['charcoal', 'red', 'blue', 'green', 'orange', 'yellow']"
    ]
   },
   {
    "name": "task_attached",
    "type": "boolean",
    "required": false,
    "description": "If true, and task_id is passed, labels attached to the task will be returned. If false, and task_id is passed, your labels that are not already attached to the task will be returned. It will be ignored if task_id is not passed.",
    "default": true,
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
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "color": "charcoal",
     "label_id": 1,
     "creator": {
      "name": "string",
      "email": "user@example.com"
     }
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "search_sellers",
  "path": "/sellers",
  "method": "GET",
  "description": "Search for sellers with a query.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
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
   }
  ],
  "response_schemas": {
   "success": [
    {
     "seller_id": 1,
     "name": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "search_songs",
  "path": "/songs",
  "method": "GET",
  "description": "Search for songs with a query.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "artist_id",
    "type": "integer",
    "required": false,
    "description": "The artist id to filter the search results by.",
    "default": null,
    "constraints": []
   },
   {
    "name": "album_id",
    "type": "integer",
    "required": false,
    "description": "The album id to filter the search results by.",
    "default": null,
    "constraints": []
   },
   {
    "name": "genre",
    "type": "string",
    "required": false,
    "description": "The genre to filter the albums by.",
    "default": null,
    "constraints": []
   },
   {
    "name": "min_release_date",
    "type": "string",
    "required": false,
    "description": "The minimum release date for search results in YYYY-MM-DD format.",
    "default": "1500-01-01",
    "constraints": []
   },
   {
    "name": "max_release_date",
    "type": "string",
    "required": false,
    "description": "The maximum release date for search results in YYYY-MM-DD format.",
    "default": "3000-01-01",
    "constraints": []
   },
   {
    "name": "min_duration",
    "type": "integer",
    "required": false,
    "description": "The minimum duration in seconds for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "max_duration",
    "type": "integer",
    "required": false,
    "description": "The maximum duration in seconds for search results.",
    "default": 9223372036854775807,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "min_rating",
    "type": "number",
    "required": false,
    "description": "The minimum rating for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0, <= 5.0"
    ]
   },
   {
    "name": "max_rating",
    "type": "number",
    "required": false,
    "description": "The maximum rating for search results.",
    "default": 5,
    "constraints": [
     "value >= 0.0, <= 5.0"
    ]
   },
   {
    "name": "min_like_count",
    "type": "integer",
    "required": false,
    "description": "The minimum like count for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "max_like_count",
    "type": "integer",
    "required": false,
    "description": "The maximum like count for search results.",
    "default": 9223372036854775807,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "min_play_count",
    "type": "integer",
    "required": false,
    "description": "The minimum play count for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "max_play_count",
    "type": "integer",
    "required": false,
    "description": "The maximum play count for search results.",
    "default": 9223372036854775807,
    "constraints": [
     "value >= 0.0"
    ]
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
    "description": "The attribute to sort the songs by prefixed with +/- to reflect ascending/descending. Valid attributes: rating, like_count and play_count. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "song_id": 1,
     "title": "string",
     "album_id": 1,
     "album_title": "string",
     "duration": 1,
     "artists": [
      {
       "id": 1,
       "name": "string"
      }
     ],
     "release_date": "2019-01-01T00:00:00",
     "genre": "string",
     "play_count": 0.0,
     "rating": 0.0,
     "like_count": 1,
     "review_count": 1,
     "shareable_link": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "search_albums",
  "path": "/albums",
  "method": "GET",
  "description": "Search for albums with a query.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "min_rating",
    "type": "number",
    "required": false,
    "description": "The minimum rating for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0, <= 5.0"
    ]
   },
   {
    "name": "max_rating",
    "type": "number",
    "required": false,
    "description": "The maximum rating for search results.",
    "default": 5,
    "constraints": [
     "value >= 0.0, <= 5.0"
    ]
   },
   {
    "name": "min_release_date",
    "type": "string",
    "required": false,
    "description": "The minimum release date for search results in YYYY-MM-DD format.",
    "default": "1500-01-01",
    "constraints": []
   },
   {
    "name": "max_release_date",
    "type": "string",
    "required": false,
    "description": "The maximum release date for search results in YYYY-MM-DD format.",
    "default": "3000-01-01",
    "constraints": []
   },
   {
    "name": "min_like_count",
    "type": "integer",
    "required": false,
    "description": "The minimum like count for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "max_like_count",
    "type": "integer",
    "required": false,
    "description": "The maximum like count for search results.",
    "default": 9223372036854775807,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "genre",
    "type": "string",
    "required": false,
    "description": "The genre to filter the albums by.",
    "default": null,
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
    "description": "The attribute to sort the albums by prefixed with +/- to reflect ascending/descending. Valid attributes: rating and release_date. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "album_id": 1,
     "title": "string",
     "genre": "string",
     "artists": [
      {
       "id": 1,
       "name": "string"
      }
     ],
     "rating": 0.0,
     "like_count": 1,
     "review_count": 1,
     "release_date": "2019-01-01T00:00:00",
     "song_ids": [
      1
     ]
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "search_artists",
  "path": "/artists",
  "method": "GET",
  "description": "Search for artists with a query.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "genre",
    "type": "string",
    "required": false,
    "description": "The genre to filter the artists by.",
    "default": null,
    "constraints": []
   },
   {
    "name": "min_follower_count",
    "type": "integer",
    "required": false,
    "description": "The minimum number of followers for search results.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "max_follower_count",
    "type": "integer",
    "required": false,
    "description": "The maximum number of followers for search results.",
    "default": 9223372036854775807,
    "constraints": [
     "value >= 0.0"
    ]
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
    "description": "The attribute to sort the artists by prefixed with +/- to reflect ascending/descending. Valid attributes: follower_count. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "artist_id": 1,
     "name": "string",
     "genre": "string",
     "follower_count": 1,
     "created_at": "2019-01-01T00:00:00"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 }
]
[
 {
  "app_name": "amazon",
  "api_name": "clear_wish_list",
  "path": "/wish_list",
  "method": "DELETE",
  "description": "Clear wish list.",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
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
  "app_name": "amazon",
  "api_name": "show_wish_list",
  "path": "/wish_list",
  "method": "GET",
  "description": "Get list of products in your wishlist.",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "product_id": 1,
     "product_name": "string",
     "quantity": 1.0,
     "price": 0.0
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "delete_product_from_wish_list",
  "path": "/wish_list/{product_id}",
  "method": "DELETE",
  "description": "Remove product from the user wish list.",
  "parameters": [
   {
    "name": "product_id",
    "type": "integer",
    "required": true,
    "description": "ID of the product to be deleted from the wish list.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
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
  "app_name": "amazon",
  "api_name": "update_product_quantity_in_wish_list",
  "path": "/wish_lists/{product_id}",
  "method": "PATCH",
  "description": "Update product quantity in the user wish_list.",
  "parameters": [
   {
    "name": "product_id",
    "type": "integer",
    "required": true,
    "description": "ID of the product being updated in the wish list.",
    "default": null,
    "constraints": []
   },
   {
    "name": "quantity",
    "type": "integer",
    "required": true,
    "description": "The new quantity of the product to be updated in the wish list.",
    "default": null,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
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
  "app_name": "amazon",
  "api_name": "add_product_to_wish_list",
  "path": "/wish_list/{product_id}",
  "method": "POST",
  "description": "Add product by id and quantities to your wish list.",
  "parameters": [
   {
    "name": "product_id",
    "type": "integer",
    "required": true,
    "description": "ID of the product to be added to the wish list.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "quantity",
    "type": "integer",
    "required": false,
    "description": "The quantity of the product to be added to the wish list.",
    "default": 1,
    "constraints": [
     "value >= 1.0"
    ]
   },
   {
    "name": "clear_wish_list_first",
    "type": "boolean",
    "required": false,
    "description": "If true, the wish list will be cleared before adding the product to the wish list.",
    "default": false,
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
]
```


### Environment Interaction 5
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


### Environment Interaction 6
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


### Environment Interaction 7
----------------------------------------------------------------------------
```python
gmail_password = [x['password'] for x in apis.supervisor.show_account_passwords() if x['account_name'] == 'gmail'][0]
gmail_email = apis.supervisor.show_profile()['email']
response = apis.gmail.login(username=gmail_email, password=gmail_password)
print(response)
access_token = response['access_token']
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtjYXJicm93bkBnbWFpbC5jb20iLCJleHAiOjE2ODk2ODI0OTh9.Z3ojsBN5_Q4H4baXgCxEaj6vNNHfr5_M_MlgdH1Saz8",
 "token_type": "Bearer"
}
```


### Environment Interaction 8
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


### Environment Interaction 9
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtjYXJicm93bkBnbWFpbC5jb20iLCJleHAiOjE2ODk2ODI0OTh9.Z3ojsBN5_Q4H4baXgCxEaj6vNNHfr5_M_MlgdH1Saz8"
query = "subject:Cable Bill"
response = apis.gmail.show_inbox_threads(access_token=access_token, query=query)
print(response)
```

```
[
 {
  "email_thread_id": 47823,
  "email_ids": [
   20868
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-07-01T10:49:29",
  "updated_at": "2023-07-01T10:49:29",
  "subject": "Internet Bill for June 2023",
  "participants": [
   {
    "name": "Carl Brown",
    "email": "carbrown@gmail.com"
   },
   {
    "name": "Netboost Notifications",
    "email": "notifications@netboost.com"
   }
  ]
 },
 {
  "email_thread_id": 47825,
  "email_ids": [
   20869
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-07-01T10:49:29",
  "updated_at": "2023-07-01T10:49:29",
  "subject": "Cable Bill for June 2023",
  "participants": [
   {
    "name": "Carl Brown",
    "email": "carbrown@gmail.com"
   },
   {
    "name": "Thundercable Notifications",
    "email": "notifications@thundercable.com"
   }
  ]
 },
 {
  "email_thread_id": 47829,
  "email_ids": [
   20871
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-06-01T14:42:52",
  "updated_at": "2023-06-01T14:42:52",
  "subject": "Internet Bill for May 2023",
  "participants": [
   {
    "name": "Carl Brown",
    "email": "carbrown@gmail.com"
   },
   {
    "name": "Netboost Notifications",
    "email": "notifications@netboost.com"
   }
  ]
 },
 {
  "email_thread_id": 47831,
  "email_ids": [
   20872
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-06-01T14:42:52",
  "updated_at": "2023-06-01T14:42:52",
  "subject": "Cable Bill for May 2023",
  "participants": [
   {
    "name": "Carl Brown",
    "email": "carbrown@gmail.com"
   },
   {
    "name": "Thundercable Notifications",
    "email": "notifications@thundercable.com"
   }
  ]
 },
 {
  "email_thread_id": 47835,
  "email_ids": [
   20874
  ],
  "draft_ids": [],
  "incoming": true,
  "outgoing": false,
  "read": false,
  "label": null,
  "starred": false,
  "archived": false,
  "spam": false,
  "created_at": "2023-05-01T17:11:09",
  "updated_at": "2023-05-01T17:11:09",
  "subject": "Internet Bill for April 2023",
  "participants": [
   {
    "name": "Carl Brown",
    "email": "carbrown@gmail.com"
   },
   {
    "name": "Netboost Notifications",
    "email": "notifications@netboost.com"
   }
  ]
 }
]
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtjYXJicm93bkBnbWFpbC5jb20iLCJleHAiOjE2ODk2ODI0OTh9.Z3ojsBN5_Q4H4baXgCxEaj6vNNHfr5_M_MlgdH1Saz8"
email_ids = [20868, 20869, 20871, 20872, 20874]
for email_id in email_ids:
    response = apis.gmail.show_email(access_token=access_token, email_id=email_id)
    print(response)
```

```
{
 "email_id": 20868,
 "subject": "Internet Bill for June 2023",
 "body": "Please find attached the internet bill for June 2023.",
 "response_to_email_id": null,
 "created_at": "2023-07-01T10:49:29",
 "sender": {
  "name": "Netboost Notifications",
  "email": "notifications@netboost.com"
 },
 "recipients": [
  {
   "name": "Carl Brown",
   "email": "carbrown@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8484,
   "file_name": "2023-06.txt"
  }
 ]
}
{
 "email_id": 20869,
 "subject": "Cable Bill for June 2023",
 "body": "Please find attached the cable bill for June 2023.",
 "response_to_email_id": null,
 "created_at": "2023-07-01T10:49:29",
 "sender": {
  "name": "Thundercable Notifications",
  "email": "notifications@thundercable.com"
 },
 "recipients": [
  {
   "name": "Carl Brown",
   "email": "carbrown@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8485,
   "file_name": "2023-06.txt"
  }
 ]
}
{
 "email_id": 20871,
 "subject": "Internet Bill for May 2023",
 "body": "Please find attached the internet bill for May 2023.",
 "response_to_email_id": null,
 "created_at": "2023-06-01T14:42:52",
 "sender": {
  "name": "Netboost Notifications",
  "email": "notifications@netboost.com"
 },
 "recipients": [
  {
   "name": "Carl Brown",
   "email": "carbrown@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8487,
   "file_name": "2023-05.txt"
  }
 ]
}
{
 "email_id": 20872,
 "subject": "Cable Bill for May 2023",
 "body": "Please find attached the cable bill for May 2023.",
 "response_to_email_id": null,
 "created_at": "2023-06-01T14:42:52",
 "sender": {
  "name": "Thundercable Notifications",
  "email": "notifications@thundercable.com"
 },
 "recipients": [
  {
   "name": "Carl Brown",
   "email": "carbrown@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8488,
   "file_name": "2023-05.txt"
  }
 ]
}
{
 "email_id": 20874,
 "subject": "Internet Bill for April 2023",
 "body": "Please find attached the internet bill for April 2023.",
 "response_to_email_id": null,
 "created_at": "2023-05-01T17:11:09",
 "sender": {
  "name": "Netboost Notifications",
  "email": "notifications@netboost.com"
 },
 "recipients": [
  {
   "name": "Carl Brown",
   "email": "carbrown@gmail.com"
  }
 ],
 "attachments": [
  {
   "id": 8490,
   "file_name": "2023-04.txt"
  }
 ]
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
import re

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbWFpbCtjYXJicm93bkBnbWFpbC5jb20iLCJleHAiOjE2ODk2ODI0OTh9.Z3ojsBN5_Q4H4baXgCxEaj6vNNHfr5_M_MlgdH1Saz8"
email_ids = [20868, 20869, 20871, 20872, 20874]
bills = []
for email_id in email_ids:
    response = apis.gmail.show_email(access_token=access_token, email_id=email_id)
    subject = response['subject']
    body = response['body']
    match = re.search(r'\d{4}-\d{2}', subject)
    if match:
        usage_month = match.group()[-2:] + '-' + match.group()[:4][-2:]
    else:
        usage_month = None
    match = re.search(r'\$\d{1,3}(,\d{3})*(\.\d+)?', body)
    if match:
        total_cost = float(match.group().replace('$', '').replace(',', ''))
    else:
        total_cost = None
    if usage_month and total_cost:
        bills.append({'usage_month': usage_month, 'total_cost': total_cost})
print(bills)
```

```
[]
```

