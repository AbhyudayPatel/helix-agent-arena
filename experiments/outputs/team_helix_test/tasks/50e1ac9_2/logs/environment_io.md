
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
 "instruction": "Give me a comma-separated list of top 6 most played edm song titles from across my Spotify song, album and playlist libraries.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "j7A61ld"
 },
 {
  "account_name": "file_system",
  "password": "p**UPfc"
 },
 {
  "account_name": "gmail",
  "password": "M-)NZ+2"
 },
 {
  "account_name": "phone",
  "password": ")w-S21u"
 },
 {
  "account_name": "simple_note",
  "password": "M2&R$kY"
 },
 {
  "account_name": "splitwise",
  "password": "--cz&%1"
 },
 {
  "account_name": "spotify",
  "password": "XZ!zW*T"
 },
 {
  "account_name": "todoist",
  "password": "3WI5xYn"
 },
 {
  "account_name": "venmo",
  "password": "Ez$26gJ"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Erika",
 "last_name": "Blackburn",
 "email": "erikabail@gmail.com",
 "phone_number": "4226809725",
 "birthday": "1989-06-24",
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
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
```

```
{
 "app_name": "spotify",
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


### Environment Interaction 3
----------------------------------------------------------------------------
```python
login = apis.spotify.login(username='erikabail@gmail.com', password='XZ!zW*T')
print(login)
token = login['access_token']
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2VyaWthYmFpbEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.X7Zn7xfsNMdRM2qvFzHIXvEvX4jyPhJ1jkHJK4Cptig",
 "token_type": "Bearer"
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
[
 {
  "name": "show_album_library",
  "description": "Get a list of all albums in the user's album library."
 },
 {
  "name": "show_playlist_library",
  "description": "Get a list of all playlists in the user's playlist library."
 },
 {
  "name": "show_song_library",
  "description": "Show a list of all songs in the user's song library."
 },
 {
  "name": "search_song",
  "description": "Search for songs based on various criteria.",
 },
 {
  "name": "show_song",
  "description": "Get the metadata of a specific song.",
 },
 {
  "name": "show_album",
  "description": "Get the metadata of a specific album.",
 },
 {
  "name": "show_playlist",
  "description": "Get the metadata of a specific playlist.",
 },
 {
  "name": "show_song_privates",
  "description": "Show a list of private details of all songs in the user's song library.",
 },
 {
  "name": "show_song_play_count",
  "description": "Get the play count for a specific song.",
 },
 {
  "name": "show_album_library",
  "description": "Get a list of all albums in the user's album library."
 },
 {
  "name": "show_playlist_library",
  "description": "Get a list of all playlists in the user's playlist library."
 },
 {
  "name": "show_song_library",
  "description": "Show a list of all songs in the user's song library."
 },
 {
  "name": "search_song",
  "description": "Search for songs based on various criteria.",
 },
 {
  "name": "show_song",
  "description": "Get the metadata of a specific song.",
 }
]
```

```
Execution successful.
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
for api in ['show_song_library','show_album_library','show_playlist_library','show_song','show_album','show_playlist','show_song_play_count']:
    print('='*20, api)
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name=api))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name=api))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_song_play_count found for the spotify app. Check the api and app name again."}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
for api in ['show_song_library','show_album_library','show_playlist_library','show_song','show_album','show_playlist','show_song_privates']:
    print('='*20, api)
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name=api))
```

```
==================== show_song_library
{
 "app_name": "spotify",
 "api_name": "show_song_library",
 "path": "/library/songs",
 "method": "GET",
 "description": "Get a list of songs in the user's song library.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
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
    "added_at": "2019-01-01T00:00:00"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
==================== show_album_library
{
 "app_name": "spotify",
 "api_name": "show_album_library",
 "path": "/library/albums",
 "method": "GET",
 "description": "Get a list of albums in the user's album library.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
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
    ],
    "added_at": "2019-01-01T00:00:00"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
==================== show_playlist_library
{
 "app_name": "spotify",
 "api_name": "show_playlist_library",
 "path": "/library/playlists",
 "method": "GET",
 "description": "Get a list of playlists in the user's playlist library.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "is_public",
   "type": "boolean",
   "required": false,
   "description": "Whether to show public playlists or private playlists.",
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
  }
 ],
 "response_schemas": {
  "success": [
   {
    "playlist_id": 1,
    "title": "string",
    "is_public": true,
    "rating": 0.0,
    "like_count": 1,
    "review_count": 1,
    "owner": {
     "name": "string",
     "email": "user@example.com"
    },
    "created_at": "2019-01-01T00:00:00",
    "song_ids": [
     1
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
==================== show_song
{
 "app_name": "spotify",
 "api_name": "show_song",
 "path": "/songs/{song_id}",
 "method": "GET",
 "description": "Get details of a specific song.",
 "parameters": [
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to retrieve.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
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
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_album
{
 "app_name": "spotify",
 "api_name": "show_album",
 "path": "/albums/{album_id}",
 "method": "GET",
 "description": "Get details of a specific album.",
 "parameters": [
  {
   "name": "album_id",
   "type": "integer",
   "required": true,
   "description": "The album id to retrieve.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
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
   "shareable_link": "string",
   "songs": [
    {
     "id": 1,
     "title": "string",
     "artist_ids": [
      1
     ]
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_playlist
{
 "app_name": "spotify",
 "api_name": "show_playlist",
 "path": "/playlists/{playlist_id}",
 "method": "GET",
 "description": "Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public.",
 "parameters": [
  {
   "name": "playlist_id",
   "type": "integer",
   "required": true,
   "description": "The playlist id to retrieve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "playlist_id": 1,
   "title": "string",
   "is_public": true,
   "rating": 0.0,
   "like_count": 1,
   "review_count": 1,
   "owner": {
    "name": "string",
    "email": "user@example.com"
   },
   "created_at": "2019-01-01T00:00:00",
   "shareable_link": "string",
   "songs": [
    {
     "id": 1,
     "title": "string",
     "artist_ids": [
      1
     ]
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_song_privates
{
 "app_name": "spotify",
 "api_name": "show_song_privates",
 "path": "/songs/{song_id}/privates",
 "method": "GET",
 "description": "Show information about the song that is private to the user.",
 "parameters": [
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to retrieve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "liked": true,
   "reviewed": true,
   "in_song_library": true,
   "downloaded": true
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
for api in ['show_song','show_album','show_playlist','show_song_privates','show_playlist_library']:
    print('='*20, api)
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name=api))
```

```
==================== show_song
{
 "app_name": "spotify",
 "api_name": "show_song",
 "path": "/songs/{song_id}",
 "method": "GET",
 "description": "Get details of a specific song.",
 "parameters": [
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to retrieve.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
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
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_album
{
 "app_name": "spotify",
 "api_name": "show_album",
 "path": "/albums/{album_id}",
 "method": "GET",
 "description": "Get details of a specific album.",
 "parameters": [
  {
   "name": "album_id",
   "type": "integer",
   "required": true,
   "description": "The album id to retrieve.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
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
   "shareable_link": "string",
   "songs": [
    {
     "id": 1,
     "title": "string",
     "artist_ids": [
      1
     ]
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_playlist
{
 "app_name": "spotify",
 "api_name": "show_playlist",
 "path": "/playlists/{playlist_id}",
 "method": "GET",
 "description": "Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public.",
 "parameters": [
  {
   "name": "playlist_id",
   "type": "integer",
   "required": true,
   "description": "The playlist id to retrieve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "playlist_id": 1,
   "title": "string",
   "is_public": true,
   "rating": 0.0,
   "like_count": 1,
   "review_count": 1,
   "owner": {
    "name": "string",
    "email": "user@example.com"
   },
   "created_at": "2019-01-01T00:00:00",
   "shareable_link": "string",
   "songs": [
    {
     "id": 1,
     "title": "string",
     "artist_ids": [
      1
     ]
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_song_privates
{
 "app_name": "spotify",
 "api_name": "show_song_privates",
 "path": "/songs/{song_id}/privates",
 "method": "GET",
 "description": "Show information about the song that is private to the user.",
 "parameters": [
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to retrieve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "liked": true,
   "reviewed": true,
   "in_song_library": true,
   "downloaded": true
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_playlist_library
{
 "app_name": "spotify",
 "api_name": "show_playlist_library",
 "path": "/library/playlists",
 "method": "GET",
 "description": "Get a list of playlists in the user's playlist library.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "is_public",
   "type": "boolean",
   "required": false,
   "description": "Whether to show public playlists or private playlists.",
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
  }
 ],
 "response_schemas": {
  "success": [
   {
    "playlist_id": 1,
    "title": "string",
    "is_public": true,
    "rating": 0.0,
    "like_count": 1,
    "review_count": 1,
    "owner": {
     "name": "string",
     "email": "user@example.com"
    },
    "created_at": "2019-01-01T00:00:00",
    "song_ids": [
     1
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
for api in ['show_playlist','show_song_privates']:
    print('='*20, api)
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name=api))
```

```
==================== show_playlist
{
 "app_name": "spotify",
 "api_name": "show_playlist",
 "path": "/playlists/{playlist_id}",
 "method": "GET",
 "description": "Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public.",
 "parameters": [
  {
   "name": "playlist_id",
   "type": "integer",
   "required": true,
   "description": "The playlist id to retrieve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "playlist_id": 1,
   "title": "string",
   "is_public": true,
   "rating": 0.0,
   "like_count": 1,
   "review_count": 1,
   "owner": {
    "name": "string",
    "email": "user@example.com"
   },
   "created_at": "2019-01-01T00:00:00",
   "shareable_link": "string",
   "songs": [
    {
     "id": 1,
     "title": "string",
     "artist_ids": [
      1
     ]
    }
   ]
  },
  "failure": {
   "message": "string"
  }
 }
}
==================== show_song_privates
{
 "app_name": "spotify",
 "api_name": "show_song_privates",
 "path": "/songs/{song_id}/privates",
 "method": "GET",
 "description": "Show information about the song that is private to the user.",
 "parameters": [
  {
   "name": "song_id",
   "type": "integer",
   "required": true,
   "description": "The song id to retrieve.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from spotify app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "liked": true,
   "reviewed": true,
   "in_song_library": true,
   "downloaded": true
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
def fetch_all(fn, **kw):
    out=[]; pi=0
    while True:
        page=fn(page_index=pi, page_limit=20, **kw)
        out.extend(page)
        if len(page)<20: break
        pi+=1
    return out

songs = fetch_all(apis.spotify.show_song_library, access_token=token)
albums = fetch_all(apis.spotify.show_album_library, access_token=token)
playlists = fetch_all(apis.spotify.show_playlist_library, access_token=token)
print(len(songs), len(albums), len(playlists))
```

```
20 4 7
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
print('songs page0 len check via direct call:')
p1 = apis.spotify.show_song_library(access_token=token, page_index=1, page_limit=20)
print(len(p1))
print(len(songs), len(albums), len(playlists))
```

```
songs page0 len check via direct call:
0
20 4 7
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
print("total unique song ids:", len(song_ids))
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print("total unique song ids:", len(song_ids))
                                        ^^^^^^^^
NameError: name 'song_ids' is not defined
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
token = apis.spotify.login(username='erikabail@gmail.com', password='XZ!zW*T')['access_token']

def fetch_all(fn, **kw):
    out=[]; pi=0
    while True:
        page=fn(page_index=pi, page_limit=20, **kw)
        out.extend(page)
        if len(page)<20: break
        pi+=1
    return out

songs = fetch_all(apis.spotify.show_song_library, access_token=token)
albums = fetch_all(apis.spotify.show_album_library, access_token=token)
playlists = fetch_all(apis.spotify.show_playlist_library, access_token=token)

song_ids = set(s['song_id'] for s in songs)
for a in albums:
    full = apis.spotify.show_album(album_id=a['album_id'])
    for s in full['songs']:
        song_ids.add(s['id'])
for p in playlists:
    full = apis.spotify.show_playlist(playlist_id=p['playlist_id'], access_token=token)
    for s in full['songs']:
        song_ids.add(s['id'])

print(len(songs), len(albums), len(playlists), "unique:", len(song_ids))
```

```
20 4 7 unique: 79
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
details = {}
for sid in song_ids:
    d = apis.spotify.show_song(song_id=sid)
    details[sid] = d

edm = [d for d in details.values() if str(d.get('genre','')).strip().lower()=='edm']
print("edm count:", len(edm))
for d in edm:
    print(d['song_id'], d['play_count'], repr(d['title']), d['genre'])
```

```
edm count: 15
1 638 'Painting Shadows on the Wall' EDM
54 845 'Heartstrings Symphony' EDM
55 437 'Tangled Lies' EDM
56 334 'Distant Love' EDM
57 421 'Silver Lining' EDM
64 468 'Caught in a Web of Lies' EDM
96 382 'In the Chambers of My Mind' EDM
100 549 'Fragile Bonds' EDM
107 466 'Quiet Despair' EDM
111 658 'Lonesome Road' EDM
112 356 'Silent Tears' EDM
116 565 'Paper Planes' EDM
253 548 'In the Wake of Unspoken Promises' EDM
293 786 'Dancing in a Field of Thorns' EDM
294 910 'Eternal Reverie' EDM
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
top6 = sorted(edm, key=lambda d: d['play_count'], reverse=True)[:6]
for d in top6:
    print(d['play_count'], d['title'])
answer = ', '.join(d['title'] for d in top6)
print("ANSWER:", answer)
```

```
910 Eternal Reverie
845 Heartstrings Symphony
786 Dancing in a Field of Thorns
658 Lonesome Road
638 Painting Shadows on the Wall
565 Paper Planes
ANSWER: Eternal Reverie, Heartstrings Symphony, Dancing in a Field of Thorns, Lonesome Road, Painting Shadows on the Wall, Paper Planes
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
print(apis.supervisor.complete_task(answer="Eternal Reverie, Heartstrings Symphony, Dancing in a Field of Thorns, Lonesome Road, Painting Shadows on the Wall, Paper Planes"))
```

```
{"message": "Marked the active task complete."}
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
print(apis.supervisor.show_active_task())
print(apis.supervisor.complete_task(answer="Eternal Reverie, Heartstrings Symphony, Dancing in a Field of Thorns, Lonesome Road, Painting Shadows on the Wall, Paper Planes"))
```

```
{
 "instruction": "Give me a comma-separated list of top 6 most played edm song titles from across my Spotify song, album and playlist libraries.",
 "status": "success",
 "answer": "Eternal Reverie, Heartstrings Symphony, Dancing in a Field of Thorns, Lonesome Road, Painting Shadows on the Wall, Paper Planes"
}
{"message": "Marked the active task complete."}
```

