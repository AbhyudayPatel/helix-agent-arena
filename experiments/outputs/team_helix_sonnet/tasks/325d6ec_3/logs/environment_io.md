
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
 "instruction": "Keep going to the next song on Spotify until you reach a song I have already liked.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "$F!HiVT"
 },
 {
  "account_name": "file_system",
  "password": "XPsql9G"
 },
 {
  "account_name": "gmail",
  "password": "sK_Fo7s"
 },
 {
  "account_name": "phone",
  "password": "v9l1MDm"
 },
 {
  "account_name": "simple_note",
  "password": "rw9UclF"
 },
 {
  "account_name": "splitwise",
  "password": "l8n-_zZ"
 },
 {
  "account_name": "spotify",
  "password": "=oskMku"
 },
 {
  "account_name": "todoist",
  "password": "%VH3es3"
 },
 {
  "account_name": "venmo",
  "password": "wDjC^}F"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Anthony",
 "last_name": "Harrison",
 "email": "an-harrison@gmail.com",
 "phone_number": "2466064078",
 "birthday": "1990-06-09",
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
print(apis.api_docs.show_api_descriptions(app_name='spotify'))
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
  "name": "show_genres",
  "description": "Show the list of all music genres."
 },
 {
  "name": "search_songs",
  "description": "Search for songs with a query."
 },
 {
  "name": "show_song",
  "description": "Get details of a specific song."
 },
 {
  "name": "show_song_privates",
  "description": "Show information about the song that is private to the user."
 },
 {
  "name": "like_song",
  "description": "Like a song."
 },
 {
  "name": "unlike_song",
  "description": "Unlike a song."
 },
 {
  "name": "show_liked_songs",
  "description": "Get a list of songs you have liked."
 },
 {
  "name": "search_albums",
  "description": "Search for albums with a query."
 },
 {
  "name": "show_album",
  "description": "Get details of a specific album."
 },
 {
  "name": "show_album_privates",
  "description": "Show information about the album that is private to the user."
 },
 {
  "name": "like_album",
  "description": "Like a album."
 },
 {
  "name": "unlike_album",
  "description": "Unlike a album."
 },
 {
  "name": "show_liked_albums",
  "description": "Get a list of albums you have liked."
 },
 {
  "name": "show_playlist_library",
  "description": "Get a list of playlists in the user's playlist library."
 },
 {
  "name": "search_playlists",
  "description": "Search for playlists with a query. It will search over all public playlists and your own private playlists."
 },
 {
  "name": "create_playlist",
  "description": "Create a new playlist."
 },
 {
  "name": "show_playlist",
  "description": "Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public."
 },
 {
  "name": "delete_playlist",
  "description": "Delete a playlist."
 },
 {
  "name": "update_playlist",
  "description": "Update a playlist title or privacy."
 },
 {
  "name": "show_playlist_privates",
  "description": "Show information about the playlist that is private to the user."
 },
 {
  "name": "like_playlist",
  "description": "Like a playlist."
 },
 {
  "name": "unlike_playlist",
  "description": "Unlike a playlist."
 },
 {
  "name": "show_liked_playlists",
  "description": "Get a list of playlists you have liked."
 },
 {
  "name": "search_artists",
  "description": "Search for artists with a query."
 },
 {
  "name": "show_artist",
  "description": "Get details of a specific artist."
 },
 {
  "name": "show_artist_following",
  "description": "Show if the user is following the artist."
 },
 {
  "name": "show_song_library",
  "description": "Get a list of songs in the user's song library."
 },
 {
  "name": "add_song_to_library",
  "description": "Add a song to the user's song library."
 },
 {
  "name": "remove_song_from_library",
  "description": "Remove a song from the user's song library."
 },
 {
  "name": "show_album_library",
  "description": "Get a list of albums in the user's album library."
 },
 {
  "name": "add_album_to_library",
  "description": "Add an album to the user's album library."
 },
 {
  "name": "remove_album_from_library",
  "description": "Remove an album from the user's album library."
 },
 {
  "name": "add_song_to_playlist",
  "description": "Add a song to a playlist."
 },
 {
  "name": "remove_song_from_playlist",
  "description": "Remove a song from a playlist."
 },
 {
  "name": "show_downloaded_songs",
  "description": "Get a list of downloaded songs."
 },
 {
  "name": "download_song",
  "description": "Download a song."
 },
 {
  "name": "remove_downloaded_song",
  "description": "Remove a song from downloads."
 },
 {
  "name": "show_following_artists",
  "description": "Get a list of artists the user is following."
 },
 {
  "name": "follow_artist",
  "description": "Follow an artist."
 },
 {
  "name": "unfollow_artist",
  "description": "Unfollow an artist."
 },
 {
  "name": "show_song_reviews",
  "description": "Get a list of reviews for a song."
 },
 {
  "name": "review_song",
  "description": "Rate or review a song."
 },
 {
  "name": "show_song_review",
  "description": "Show a song review."
 },
 {
  "name": "delete_song_review",
  "description": "Delete a song review."
 },
 {
  "name": "update_song_review",
  "description": "Update a song review."
 },
 {
  "name": "show_album_reviews",
  "description": "Get a list of reviews for an album."
 },
 {
  "name": "review_album",
  "description": "Rate or review an album."
 },
 {
  "name": "show_album_review",
  "description": "Show an album review."
 },
 {
  "name": "delete_album_review",
  "description": "Delete an album review."
 },
 {
  "name": "update_album_review",
  "description": "Update an album review."
 },
 {
  "name": "show_playlist_reviews",
  "description": "Show a list of reviews for your playlist or others' public playlist."
 },
 {
  "name": "review_playlist",
  "description": "Rate or review a playlist."
 },
 {
  "name": "show_playlist_review",
  "description": "Show a playlist review."
 },
 {
  "name": "delete_playlist_review",
  "description": "Delete a playlist review."
 },
 {
  "name": "update_playlist_review",
  "description": "Update a playlist review."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of users payment cards."
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
  "name": "show_current_song",
  "description": "Show details of the current song on the queue."
 },
 {
  "name": "play_music",
  "description": "Play music based on various criteria. You can pass, at most, any one of queue_position, song_id, album_id or playlist_id. If one of song_id, album_id or playlist_id is passed, that song, album or playlist will be added to the queue and played. Otherwise, the queue will remain unchanged. If queue_position is passed, the song at that position in the queue will be played. If none is passed, the current song in the queue will be played."
 },
 {
  "name": "pause_music",
  "description": "Pause the currently playing song."
 },
 {
  "name": "previous_song",
  "description": "Go to the previous song in the song queue."
 },
 {
  "name": "next_song",
  "description": "Go to the next song in the song queue."
 },
 {
  "name": "move_song_in_queue",
  "description": "Move a song in the queue to a new position."
 },
 {
  "name": "seek_song",
  "description": "Seek the current song to the given number of seconds."
 },
 {
  "name": "loop_song",
  "description": "Set whether to loop the current song."
 },
 {
  "name": "shuffle_song_queue",
  "description": "Shuffle songs in the music player queue."
 },
 {
  "name": "show_song_queue",
  "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle."
 },
 {
  "name": "add_to_queue",
  "description": "Add a song, album or playlist to the music player song queue."
 },
 {
  "name": "clear_song_queue",
  "description": "Clear the music player song queue."
 },
 {
  "name": "remove_song_from_queue",
  "description": "Remove a song at the given position from the music player song queue."
 },
 {
  "name": "show_volume",
  "description": "Get the volume level of the music player."
 },
 {
  "name": "set_volume",
  "description": "Set the volume level of the music player."
 },
 {
  "name": "show_recommendations",
  "description": "Get personalized song recommendations for the user."
 },
 {
  "name": "show_premium_plans",
  "description": "Show information about premium plans available."
 },
 {
  "name": "show_premium_subscriptions",
  "description": "Show your premium subscription history."
 },
 {
  "name": "subscribe_premium",
  "description": "Subscribe to premium membership."
 },
 {
  "name": "download_premium_subscription_receipt",
  "description": "Download the receipt for a premium subscription."
 }
]
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_liked_songs'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_playback_state'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='skip_to_next_song'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_playback_state'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_playback_state found for the spotify app. Check the api and app name again."}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_liked_songs'))
# Search for playback-related APIs
print(apis.api_docs.search_api_docs(query='playback current song spotify'))
print(apis.api_docs.search_api_docs(query='skip next song spotify'))
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
{
 "app_name": "spotify",
 "api_name": "show_liked_songs",
 "path": "/liked_songs",
 "method": "GET",
 "description": "Get a list of songs you have liked.",
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
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the liked songs by prefixed with +/- to reflect ascending/descending. Valid attributes: liked_at, play_count and title.",
   "default": "-liked_at",
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
    "liked_at": "2019-01-01T00:00:00"
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
[
 {
  "app_name": "spotify",
  "api_name": "show_current_song",
  "path": "/music_player/current_song",
  "method": "GET",
  "description": "Show details of the current song on the queue.",
  "parameters": [
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
    "played_seconds": 1,
    "is_playing": true
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "loop_song",
  "path": "/music_player/loop",
  "method": "POST",
  "description": "Set whether to loop the current song.",
  "parameters": [
   {
    "name": "loop",
    "type": "boolean",
    "required": true,
    "description": "Whether to loop the current song.",
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "pause_music",
  "path": "/music_player/pause",
  "method": "POST",
  "description": "Pause the currently playing song.",
  "parameters": [
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "seek_song",
  "path": "/music_player/seek",
  "method": "POST",
  "description": "Seek the current song to the given number of seconds.",
  "parameters": [
   {
    "name": "seek_seconds",
    "type": "integer",
    "required": true,
    "description": "The number of seconds to seek.",
    "default": null,
    "constraints": [
     "value >= 0.0"
    ]
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "like_song",
  "path": "/songs/{song_id}/like",
  "method": "POST",
  "description": "Like a song.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to like.",
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
[
 {
  "app_name": "spotify",
  "api_name": "next_song",
  "path": "/music_player/next_song",
  "method": "POST",
  "description": "Go to the next song in the song queue.",
  "parameters": [
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
    "message": "string",
    "song_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "like_song",
  "path": "/songs/{song_id}/like",
  "method": "POST",
  "description": "Like a song.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to like.",
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "unlike_song",
  "path": "/songs/{song_id}/like",
  "method": "DELETE",
  "description": "Unlike a song.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to unlike.",
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "download_song",
  "path": "/downloaded_songs/{song_id}",
  "method": "POST",
  "description": "Download a song.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to download.",
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
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "review_song",
  "path": "/songs/{song_id}/reviews",
  "method": "POST",
  "description": "Rate or review a song.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "ID of the song to review.",
    "default": null,
    "constraints": []
   },
   {
    "name": "rating",
    "type": "integer",
    "required": true,
    "description": "Song rating for this review.",
    "default": null,
    "constraints": [
     "value >= 1.0, <= 5.0"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from spotify app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "title",
    "type": "string",
    "required": false,
    "description": "Title of the review.",
    "default": "",
    "constraints": []
   },
   {
    "name": "text",
    "type": "string",
    "required": false,
    "description": "Text content of the review.",
    "default": "",
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "song_review_id": 1
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
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_current_song'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='skip_to_next_song'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name='skip_to_next_song'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name skip_to_next_song found for the spotify app. Check the api and app name again."}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
result = apis.api_docs.show_api_descriptions(app_name='spotify')
for api in result:
    print(api['name'], '-', api['description'])
```

```
show_account - Show your account information. Unlike show_profile, this includes private information.
signup - Sign up to create account.
delete_account - Delete your account.
update_account_name - Update your first or last name in the account profile.
login - Login to your account.
logout - Logout from your account.
send_verification_code - Send account verification code to your email address.
verify_account - Verify your account using the verification code sent to your email address.
send_password_reset_code - Send password reset code to your email address.
reset_password - Reset your password using the password reset code sent to your email address.
show_profile - Show public profile information of a user.
show_genres - Show the list of all music genres.
search_songs - Search for songs with a query.
show_song - Get details of a specific song.
show_song_privates - Show information about the song that is private to the user.
like_song - Like a song.
unlike_song - Unlike a song.
show_liked_songs - Get a list of songs you have liked.
search_albums - Search for albums with a query.
show_album - Get details of a specific album.
show_album_privates - Show information about the album that is private to the user.
like_album - Like a album.
unlike_album - Unlike a album.
show_liked_albums - Get a list of albums you have liked.
show_playlist_library - Get a list of playlists in the user's playlist library.
search_playlists - Search for playlists with a query. It will search over all public playlists and your own private playlists.
create_playlist - Create a new playlist.
show_playlist - Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public.
delete_playlist - Delete a playlist.
update_playlist - Update a playlist title or privacy.
show_playlist_privates - Show information about the playlist that is private to the user.
like_playlist - Like a playlist.
unlike_playlist - Unlike a playlist.
show_liked_playlists - Get a list of playlists you have liked.
search_artists - Search for artists with a query.
show_artist - Get details of a specific artist.
show_artist_following - Show if the user is following the artist.
show_song_library - Get a list of songs in the user's song library.
add_song_to_library - Add a song to the user's song library.
remove_song_from_library - Remove a song from the user's song library.
show_album_library - Get a list of albums in the user's album library.
add_album_to_library - Add an album to the user's album library.
remove_album_from_library - Remove an album from the user's album library.
add_song_to_playlist - Add a song to a playlist.
remove_song_from_playlist - Remove a song from a playlist.
show_downloaded_songs - Get a list of downloaded songs.
download_song - Download a song.
remove_downloaded_song - Remove a song from downloads.
show_following_artists - Get a list of artists the user is following.
follow_artist - Follow an artist.
unfollow_artist - Unfollow an artist.
show_song_reviews - Get a list of reviews for a song.
review_song - Rate or review a song.
show_song_review - Show a song review.
delete_song_review - Delete a song review.
update_song_review - Update a song review.
show_album_reviews - Get a list of reviews for an album.
review_album - Rate or review an album.
show_album_review - Show an album review.
delete_album_review - Delete an album review.
update_album_review - Update an album review.
show_playlist_reviews - Show a list of reviews for your playlist or others' public playlist.
review_playlist - Rate or review a playlist.
show_playlist_review - Show a playlist review.
delete_playlist_review - Delete a playlist review.
update_playlist_review - Update a playlist review.
show_payment_cards - Get a list of users payment cards.
add_payment_card - Add a new payment card.
show_payment_card - Get details of a payment card.
delete_payment_card - Delete payment card information.
update_payment_card - Update payment card information.
show_current_song - Show details of the current song on the queue.
play_music - Play music based on various criteria. You can pass, at most, any one of queue_position, song_id, album_id or playlist_id. If one of song_id, album_id or playlist_id is passed, that song, album or playlist will be added to the queue and played. Otherwise, the queue will remain unchanged. If queue_position is passed, the song at that position in the queue will be played. If none is passed, the current song in the queue will be played.
pause_music - Pause the currently playing song.
previous_song - Go to the previous song in the song queue.
next_song - Go to the next song in the song queue.
move_song_in_queue - Move a song in the queue to a new position.
seek_song - Seek the current song to the given number of seconds.
loop_song - Set whether to loop the current song.
shuffle_song_queue - Shuffle songs in the music player queue.
show_song_queue - Get the music player song queue. Songs are played in the order of the queue in a cycle.
add_to_queue - Add a song, album or playlist to the music player song queue.
clear_song_queue - Clear the music player song queue.
remove_song_from_queue - Remove a song at the given position from the music player song queue.
show_volume - Get the volume level of the music player.
set_volume - Set the volume level of the music player.
show_recommendations - Get personalized song recommendations for the user.
show_premium_plans - Show information about premium plans available.
show_premium_subscriptions - Show your premium subscription history.
subscribe_premium - Subscribe to premium membership.
download_premium_subscription_receipt - Download the receipt for a premium subscription.
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
result = apis.api_docs.show_api_descriptions(app_name='spotify')
print([api['name'] for api in result])
```

```
[
 "show_account",
 "signup",
 "delete_account",
 "update_account_name",
 "login",
 "logout",
 "send_verification_code",
 "verify_account",
 "send_password_reset_code",
 "reset_password",
 "show_profile",
 "show_genres",
 "search_songs",
 "show_song",
 "show_song_privates",
 "like_song",
 "unlike_song",
 "show_liked_songs",
 "search_albums",
 "show_album",
 "show_album_privates",
 "like_album",
 "unlike_album",
 "show_liked_albums",
 "show_playlist_library",
 "search_playlists",
 "create_playlist",
 "show_playlist",
 "delete_playlist",
 "update_playlist",
 "show_playlist_privates",
 "like_playlist",
 "unlike_playlist",
 "show_liked_playlists",
 "search_artists",
 "show_artist",
 "show_artist_following",
 "show_song_library",
 "add_song_to_library",
 "remove_song_from_library",
 "show_album_library",
 "add_album_to_library",
 "remove_album_from_library",
 "add_song_to_playlist",
 "remove_song_from_playlist",
 "show_downloaded_songs",
 "download_song",
 "remove_downloaded_song",
 "show_following_artists",
 "follow_artist",
 "unfollow_artist",
 "show_song_reviews",
 "review_song",
 "show_song_review",
 "delete_song_review",
 "update_song_review",
 "show_album_reviews",
 "review_album",
 "show_album_review",
 "delete_album_review",
 "update_album_review",
 "show_playlist_reviews",
 "review_playlist",
 "show_playlist_review",
 "delete_playlist_review",
 "update_playlist_review",
 "show_payment_cards",
 "add_payment_card",
 "show_payment_card",
 "delete_payment_card",
 "update_payment_card",
 "show_current_song",
 "play_music",
 "pause_music",
 "previous_song",
 "next_song",
 "move_song_in_queue",
 "seek_song",
 "loop_song",
 "shuffle_song_queue",
 "show_song_queue",
 "add_to_queue",
 "clear_song_queue",
 "remove_song_from_queue",
 "show_volume",
 "set_volume",
 "show_recommendations",
 "show_premium_plans",
 "show_premium_subscriptions",
 "subscribe_premium",
 "download_premium_subscription_receipt"
]
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_current_song'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='next_song'))
```

```
{
 "app_name": "spotify",
 "api_name": "show_current_song",
 "path": "/music_player/current_song",
 "method": "GET",
 "description": "Show details of the current song on the queue.",
 "parameters": [
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
   "played_seconds": 1,
   "is_playing": true
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "spotify",
 "api_name": "next_song",
 "path": "/music_player/next_song",
 "method": "POST",
 "description": "Go to the next song in the song queue.",
 "parameters": [
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
   "message": "string",
   "song_id": 1
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
# Login to Spotify
login_resp = apis.spotify.login(username='an-harrison@gmail.com', password='=oskMku')
token = login_resp['access_token']
print('Logged in, token:', token[:20], '...')

# Fetch ALL liked songs (paginate)
liked_songs = []
page_index = 0
page_limit = 20
while True:
    page = apis.spotify.show_liked_songs(access_token=token, page_index=page_index, page_limit=page_limit)
    liked_songs.extend(page)
    print(f'Page {page_index}: got {len(page)} songs')
    if len(page) < page_limit:
        break
    page_index += 1

liked_ids = set(s['song_id'] for s in liked_songs)
print(f'Total liked songs: {len(liked_ids)}')

# Check current song
current = apis.spotify.show_current_song(access_token=token)
print(f'Current song: {current["song_id"]} - {current["title"]}')
```

```
Logged in, token: eyJhbGciOiJIUzI1NiIs ...
Page 0: got 13 songs
Total liked songs: 13
Current song: 36 - A Whisper in the Midnight Air
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
print('Sample liked song:', liked_songs[0])
print('Current song id:', current['song_id'], 'in liked_ids:', current['song_id'] in liked_ids)

# Loop: skip to next song until we hit a liked one
max_iterations = 100
for i in range(max_iterations):
    if current['song_id'] in liked_ids:
        print(f'Found liked song after {i} skips: {current["song_id"]} - {current["title"]}')
        break
    print(f'Skipping song {current["song_id"]} - {current["title"]}')
    apis.spotify.next_song(access_token=token)
    current = apis.spotify.show_current_song(access_token=token)
else:
    print('Did not find a liked song in 100 skips')
```

```
Sample liked song: {'song_id': 94, 'title': 'Bridges Burned and Rivers Crossed', 'album_id': None, 'duration': 250, 'artists': [{'id': 3, 'name': 'Jasper Skye'}], 'liked_at': '2023-05-18T12:00:00'}
Current song id: 36 in liked_ids: False
Skipping song 36 - A Whisper in the Midnight Air
Skipping song 56 - Distant Love
Skipping song 167 - The Tragic Beauty of Love
Skipping song 323 - Innocent Lies
Found liked song after 4 skips: 94 - Bridges Burned and Rivers Crossed
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Verify current song is the liked one
current = apis.spotify.show_current_song(access_token=token)
print(f'Current song: {current["song_id"]} - {current["title"]}')
print(f'Is liked: {current["song_id"] in liked_ids}')

# Complete the task
apis.supervisor.complete_task(status="success")
```

```
Current song: 94 - Bridges Burned and Rivers Crossed
Is liked: True
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Re-read the task
print(apis.supervisor.show_active_task())

# Verify current state
current = apis.spotify.show_current_song(access_token=token)
print(f'Current song: {current["song_id"]} - {current["title"]}')
print(f'Is liked: {current["song_id"] in liked_ids}')
print(f'Total liked songs: {len(liked_ids)}')
```

```
{
 "instruction": "Keep going to the next song on Spotify until you reach a song I have already liked.",
 "status": "success",
 "answer": null
}
Current song: 94 - Bridges Burned and Rivers Crossed
Is liked: True
Total liked songs: 13
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
result = apis.supervisor.complete_task(status="success")
print(result)
```

```
{"message": "Marked the active task complete."}
```

