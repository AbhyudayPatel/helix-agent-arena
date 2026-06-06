
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
 "instruction": "Remove all the songs that I have not liked from my Spotify queue, and then start the player.",
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
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_queue'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_liked_songs'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_queue'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_queue found for the spotify app. Check the api and app name again."}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
print(apis.api_docs.search_api_docs(query='queue spotify'))
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
[
 {
  "app_name": "spotify",
  "api_name": "clear_song_queue",
  "path": "/music_player/song_queue",
  "method": "DELETE",
  "description": "Clear the music player song queue.",
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
  "api_name": "shuffle_song_queue",
  "path": "/music_player/shuffle",
  "method": "POST",
  "description": "Shuffle songs in the music player queue.",
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
  "api_name": "show_song_queue",
  "path": "/music_player/song_queue",
  "method": "GET",
  "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle.",
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
     "position": 1,
     "is_playing": true,
     "is_current": true
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "move_song_in_queue",
  "path": "/music_player/move_song",
  "method": "POST",
  "description": "Move a song in the queue to a new position.",
  "parameters": [
   {
    "name": "current_position",
    "type": "integer",
    "required": true,
    "description": "The current position of the song in the queue.",
    "default": null,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "new_position",
    "type": "integer",
    "required": true,
    "description": "The new position of the song in the queue.",
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
  "api_name": "add_to_queue",
  "path": "/music_player/song_queue",
  "method": "POST",
  "description": "Add a song, album or playlist to the music player song queue.",
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
    "name": "song_id",
    "type": "integer",
    "required": false,
    "description": "ID of the song to add to queue.",
    "default": null,
    "constraints": []
   },
   {
    "name": "album_id",
    "type": "integer",
    "required": false,
    "description": "ID of the album to add to queue.",
    "default": null,
    "constraints": []
   },
   {
    "name": "playlist_id",
    "type": "integer",
    "required": false,
    "description": "ID of the playlist to add to queue.",
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
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_song_queue'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_liked_songs'))
print(apis.api_docs.search_api_docs(query='remove song from queue spotify'))
print(apis.api_docs.search_api_docs(query='start player spotify'))
```

```
{
 "app_name": "spotify",
 "api_name": "show_song_queue",
 "path": "/music_player/song_queue",
 "method": "GET",
 "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle.",
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
    "position": 1,
    "is_playing": true,
    "is_current": true
   }
  ],
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
  "api_name": "remove_song_from_queue",
  "path": "/music_player/song_queue/{position}",
  "method": "DELETE",
  "description": "Remove a song at the given position from the music player song queue.",
  "parameters": [
   {
    "name": "position",
    "type": "integer",
    "required": true,
    "description": "The 0-indexed position of the song in the queue.",
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
  "api_name": "remove_song_from_playlist",
  "path": "/playlists/{playlist_id}/songs/{song_id}",
  "method": "DELETE",
  "description": "Remove a song from a playlist.",
  "parameters": [
   {
    "name": "playlist_id",
    "type": "integer",
    "required": true,
    "description": "The playlist id to remove the song from.",
    "default": null,
    "constraints": []
   },
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to remove.",
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
  "api_name": "remove_downloaded_song",
  "path": "/downloaded_songs/{song_id}",
  "method": "DELETE",
  "description": "Remove a song from downloads.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to remove from downloads.",
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
  "api_name": "remove_song_from_library",
  "path": "/library/songs/{song_id}",
  "method": "DELETE",
  "description": "Remove a song from the user's song library.",
  "parameters": [
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to remove.",
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
  "api_name": "clear_song_queue",
  "path": "/music_player/song_queue",
  "method": "DELETE",
  "description": "Clear the music player song queue.",
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
 }
]
[
 {
  "app_name": "spotify",
  "api_name": "clear_song_queue",
  "path": "/music_player/song_queue",
  "method": "DELETE",
  "description": "Clear the music player song queue.",
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
  "api_name": "shuffle_song_queue",
  "path": "/music_player/shuffle",
  "method": "POST",
  "description": "Shuffle songs in the music player queue.",
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
  "api_name": "show_volume",
  "path": "/music_player/volume",
  "method": "GET",
  "description": "Get the volume level of the music player.",
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
    "volume": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "set_volume",
  "path": "/music_player/volume",
  "method": "POST",
  "description": "Set the volume level of the music player.",
  "parameters": [
   {
    "name": "volume",
    "type": "integer",
    "required": true,
    "description": "Volume level to set.",
    "default": null,
    "constraints": [
     "value >= 0.0, <= 10.0"
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
  "api_name": "add_to_queue",
  "path": "/music_player/song_queue",
  "method": "POST",
  "description": "Add a song, album or playlist to the music player song queue.",
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
    "name": "song_id",
    "type": "integer",
    "required": false,
    "description": "ID of the song to add to queue.",
    "default": null,
    "constraints": []
   },
   {
    "name": "album_id",
    "type": "integer",
    "required": false,
    "description": "ID of the album to add to queue.",
    "default": null,
    "constraints": []
   },
   {
    "name": "playlist_id",
    "type": "integer",
    "required": false,
    "description": "ID of the playlist to add to queue.",
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
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='remove_song_from_queue'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='start_player'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name='start_player'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name start_player found for the spotify app. Check the api and app name again."}
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='remove_song_from_queue'))
print(apis.api_docs.search_api_docs(query='play resume start music player'))
```

```
{
 "app_name": "spotify",
 "api_name": "remove_song_from_queue",
 "path": "/music_player/song_queue/{position}",
 "method": "DELETE",
 "description": "Remove a song at the given position from the music player song queue.",
 "parameters": [
  {
   "name": "position",
   "type": "integer",
   "required": true,
   "description": "The 0-indexed position of the song in the queue.",
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
[
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
  "api_name": "show_song_queue",
  "path": "/music_player/song_queue",
  "method": "GET",
  "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle.",
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
     "position": 1,
     "is_playing": true,
     "is_current": true
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "clear_song_queue",
  "path": "/music_player/song_queue",
  "method": "DELETE",
  "description": "Clear the music player song queue.",
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
  "api_name": "shuffle_song_queue",
  "path": "/music_player/shuffle",
  "method": "POST",
  "description": "Shuffle songs in the music player queue.",
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
  "api_name": "show_volume",
  "path": "/music_player/volume",
  "method": "GET",
  "description": "Get the volume level of the music player.",
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
    "volume": 1
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Login
resp = apis.spotify.login(username='erikabail@gmail.com', password='XZ!zW*T')
print(resp)
token = resp['access_token']

# Get queue
queue = apis.spotify.show_song_queue(access_token=token)
print(f"Queue ({len(queue)} songs):")
for s in queue:
    print(f"  pos={s['position']} id={s['song_id']} title={s['title']}")

# Get all liked songs (paginate)
liked_songs = []
page = 0
while True:
    page_data = apis.spotify.show_liked_songs(access_token=token, page_index=page, page_limit=20)
    liked_songs.extend(page_data)
    if len(page_data) < 20:
        break
    page += 1
print(f"\nTotal liked songs: {len(liked_songs)}")
liked_ids = {s['song_id'] for s in liked_songs}
print(f"Liked song IDs: {liked_ids}")
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2VyaWthYmFpbEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.X7Zn7xfsNMdRM2qvFzHIXvEvX4jyPhJ1jkHJK4Cptig",
 "token_type": "Bearer"
}
Queue (24 songs):
  pos=0 id=49 title=Whispers of the Enchanted Forest
  pos=1 id=195 title=Rhapsody of the Ocean's Embrace
  pos=2 id=43 title=Whispers of Destiny
  pos=3 id=164 title=Waiting for the Morning Light
  pos=4 id=295 title=City of Fallen Angels
  pos=5 id=60 title=The Haunting Echo of Goodbye
  pos=6 id=242 title=Cracks in the Facade of Love
  pos=7 id=97 title=Holding Onto Threads of Hope
  pos=8 id=1 title=Painting Shadows on the Wall
  pos=9 id=176 title=Echoes of Silence
  pos=10 id=15 title=In the Depths of Despair
  pos=11 id=136 title=Finding Solace in the Abyss
  pos=12 id=84 title=Wilted Petals
  pos=13 id=5 title=Chasing the Ghosts of Yesterday
  pos=14 id=16 title=Yearning for a Glimpse of Heaven
  pos=15 id=283 title=Bitter Haze
  pos=16 id=206 title=Escaping the Chains of Fate
  pos=17 id=232 title=The Road Less Traveled By
  pos=18 id=104 title=Nostalgia's Hold
  pos=19 id=65 title=Eternal Solitude
  pos=20 id=45 title=Eclipsed
  pos=21 id=102 title=Autumn's Lament
  pos=22 id=214 title=The Sweet Pain of Reminiscence
  pos=23 id=272 title=Torn Apart

Total liked songs: 12
Liked song IDs: {1, 5, 102, 295, 104, 136, 206, 15, 176, 214, 283, 60}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Search for the play/start API
print(apis.api_docs.search_api_docs(query='play music start'))
```

```
[
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
  "api_name": "play_music",
  "path": "/music_player/play",
  "method": "POST",
  "description": "Play music based on various criteria. You can pass, at most, any one of queue_position, song_id, album_id or playlist_id. If one of song_id, album_id or playlist_id is passed, that song, album or playlist will be added to the queue and played. Otherwise, the queue will remain unchanged. If queue_position is passed, the song at that position in the queue will be played. If none is passed, the current song in the queue will be played.",
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
    "name": "song_id",
    "type": "integer",
    "required": false,
    "description": "ID of the song to play.",
    "default": null,
    "constraints": []
   },
   {
    "name": "album_id",
    "type": "integer",
    "required": false,
    "description": "ID of the album to play.",
    "default": null,
    "constraints": []
   },
   {
    "name": "playlist_id",
    "type": "integer",
    "required": false,
    "description": "ID of the playlist to play.",
    "default": null,
    "constraints": []
   },
   {
    "name": "queue_position",
    "type": "integer",
    "required": false,
    "description": "Position of the song in the queue to play.",
    "default": null,
    "constraints": [
     "value >= 0.0"
    ]
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
  "api_name": "show_song_queue",
  "path": "/music_player/song_queue",
  "method": "GET",
  "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle.",
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
     "position": 1,
     "is_playing": true,
     "is_current": true
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "show_genres",
  "path": "/genres",
  "method": "GET",
  "description": "Show the list of all music genres.",
  "parameters": [],
  "response_schemas": {
   "success": [
    "string"
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "clear_song_queue",
  "path": "/music_player/song_queue",
  "method": "DELETE",
  "description": "Clear the music player song queue.",
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
 }
]
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Already have token, queue, and liked_ids from previous run
# token = 'eyJ...'
# queue = list of 24 songs
# liked_ids = {1, 5, 102, 295, 104, 136, 206, 15, 176, 214, 283, 60}

# Identify non-liked songs in queue
non_liked = [s for s in queue if s['song_id'] not in liked_ids]
print(f"Non-liked songs to remove ({len(non_liked)}):")
for s in non_liked:
    print(f"  pos={s['position']} id={s['song_id']} title={s['title']}")

# Sort by position DESCENDING to avoid index shifting
non_liked_sorted = sorted(non_liked, key=lambda s: s['position'], reverse=True)

# Remove each non-liked song from queue
for s in non_liked_sorted:
    result = apis.spotify.remove_song_from_queue(access_token=token, position=s['position'])
    print(f"Removed pos={s['position']} id={s['song_id']} title={s['title']}: {result}")

# Verify queue after removal
queue_after = apis.spotify.show_song_queue(access_token=token)
print(f"\nQueue after removal ({len(queue_after)} songs):")
for s in queue_after:
    print(f"  pos={s['position']} id={s['song_id']} title={s['title']} liked={s['song_id'] in liked_ids}")

# Start the player
play_result = apis.spotify.play_music(access_token=token)
print(f"\nPlay result: {play_result}")
```

```
Non-liked songs to remove (12):
  pos=0 id=49 title=Whispers of the Enchanted Forest
  pos=1 id=195 title=Rhapsody of the Ocean's Embrace
  pos=2 id=43 title=Whispers of Destiny
  pos=3 id=164 title=Waiting for the Morning Light
  pos=6 id=242 title=Cracks in the Facade of Love
  pos=7 id=97 title=Holding Onto Threads of Hope
  pos=12 id=84 title=Wilted Petals
  pos=14 id=16 title=Yearning for a Glimpse of Heaven
  pos=17 id=232 title=The Road Less Traveled By
  pos=19 id=65 title=Eternal Solitude
  pos=20 id=45 title=Eclipsed
  pos=23 id=272 title=Torn Apart
Removed pos=23 id=272 title=Torn Apart: {'message': 'Removed song at position 23 from the song queue.'}
Removed pos=20 id=45 title=Eclipsed: {'message': 'Removed song at position 20 from the song queue.'}
Removed pos=19 id=65 title=Eternal Solitude: {'message': 'Removed song at position 19 from the song queue.'}
Removed pos=17 id=232 title=The Road Less Traveled By: {'message': 'Removed song at position 17 from the song queue.'}
Removed pos=14 id=16 title=Yearning for a Glimpse of Heaven: {'message': 'Removed song at position 14 from the song queue.'}
Removed pos=12 id=84 title=Wilted Petals: {'message': 'Removed song at position 12 from the song queue.'}
Removed pos=7 id=97 title=Holding Onto Threads of Hope: {'message': 'Removed song at position 7 from the song queue.'}
Removed pos=6 id=242 title=Cracks in the Facade of Love: {'message': 'Removed song at position 6 from the song queue.'}
Removed pos=3 id=164 title=Waiting for the Morning Light: {'message': 'Removed song at position 3 from the song queue.'}
Removed pos=2 id=43 title=Whispers of Destiny: {'message': 'Removed song at position 2 from the song queue.'}
Removed pos=1 id=195 title=Rhapsody of the Ocean's Embrace: {'message': 'Removed song at position 1 from the song queue.'}
Removed pos=0 id=49 title=Whispers of the Enchanted Forest: {'message': 'Removed song at position 0 from the song queue.'}

Queue after removal (12 songs):
  pos=0 id=295 title=City of Fallen Angels liked=True
  pos=1 id=60 title=The Haunting Echo of Goodbye liked=True
  pos=2 id=1 title=Painting Shadows on the Wall liked=True
  pos=3 id=176 title=Echoes of Silence liked=True
  pos=4 id=15 title=In the Depths of Despair liked=True
  pos=5 id=136 title=Finding Solace in the Abyss liked=True
  pos=6 id=5 title=Chasing the Ghosts of Yesterday liked=True
  pos=7 id=283 title=Bitter Haze liked=True
  pos=8 id=206 title=Escaping the Chains of Fate liked=True
  pos=9 id=104 title=Nostalgia's Hold liked=True
  pos=10 id=102 title=Autumn's Lament liked=True
  pos=11 id=214 title=The Sweet Pain of Reminiscence liked=True

Play result: {'message': 'Song (City of Fallen Angels) is now playing.', 'song_id': 295}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Re-check queue and play result
queue_final = apis.spotify.show_song_queue(access_token=token)
print(f"Final queue ({len(queue_final)} songs):")
for s in queue_final:
    print(f"  pos={s['position']} id={s['song_id']} title={s['title']} liked={s['song_id'] in liked_ids}")

# Start the player (call play_music with no optional args)
play_result = apis.spotify.play_music(access_token=token)
print(f"\nPlay result: {play_result}")
```

```
Final queue (12 songs):
  pos=0 id=295 title=City of Fallen Angels liked=True
  pos=1 id=60 title=The Haunting Echo of Goodbye liked=True
  pos=2 id=1 title=Painting Shadows on the Wall liked=True
  pos=3 id=176 title=Echoes of Silence liked=True
  pos=4 id=15 title=In the Depths of Despair liked=True
  pos=5 id=136 title=Finding Solace in the Abyss liked=True
  pos=6 id=5 title=Chasing the Ghosts of Yesterday liked=True
  pos=7 id=283 title=Bitter Haze liked=True
  pos=8 id=206 title=Escaping the Chains of Fate liked=True
  pos=9 id=104 title=Nostalgia's Hold liked=True
  pos=10 id=102 title=Autumn's Lament liked=True
  pos=11 id=214 title=The Sweet Pain of Reminiscence liked=True

Play result: {'message': 'Song (City of Fallen Angels) is now playing.', 'song_id': 295}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Verify: all songs in queue are liked, and player is running
print("Verification:")
print(f"Queue size: {len(queue_final)} (was 24, removed 12 non-liked)")
all_liked = all(s['song_id'] in liked_ids for s in queue_final)
print(f"All remaining songs are liked: {all_liked}")
print(f"Player started: {play_result}")

# Complete the task
apis.supervisor.complete_task(status="success")
```

```
Verification:
Queue size: 12 (was 24, removed 12 non-liked)
All remaining songs are liked: True
Player started: {'message': 'Song (City of Fallen Angels) is now playing.', 'song_id': 295}
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Re-read the task
print(apis.supervisor.show_active_task())

# Re-query the queue to confirm state
queue_check = apis.spotify.show_song_queue(access_token=token)
print(f"\nCurrent queue ({len(queue_check)} songs):")
for s in queue_check:
    in_liked = s['song_id'] in liked_ids
    print(f"  pos={s['position']} id={s['song_id']} title={s['title']} liked={in_liked}")

all_liked_check = all(s['song_id'] in liked_ids for s in queue_check)
any_non_liked = any(s['song_id'] not in liked_ids for s in queue_check)
print(f"\nAll songs in queue are liked: {all_liked_check}")
print(f"Any non-liked songs remain: {any_non_liked}")
print(f"Player was started: {play_result}")
```

```
{
 "instruction": "Remove all the songs that I have not liked from my Spotify queue, and then start the player.",
 "status": "success",
 "answer": null
}

Current queue (12 songs):
  pos=0 id=295 title=City of Fallen Angels liked=True
  pos=1 id=60 title=The Haunting Echo of Goodbye liked=True
  pos=2 id=1 title=Painting Shadows on the Wall liked=True
  pos=3 id=176 title=Echoes of Silence liked=True
  pos=4 id=15 title=In the Depths of Despair liked=True
  pos=5 id=136 title=Finding Solace in the Abyss liked=True
  pos=6 id=5 title=Chasing the Ghosts of Yesterday liked=True
  pos=7 id=283 title=Bitter Haze liked=True
  pos=8 id=206 title=Escaping the Chains of Fate liked=True
  pos=9 id=104 title=Nostalgia's Hold liked=True
  pos=10 id=102 title=Autumn's Lament liked=True
  pos=11 id=214 title=The Sweet Pain of Reminiscence liked=True

All songs in queue are liked: True
Any non-liked songs remain: False
Player was started: {'message': 'Song (City of Fallen Angels) is now playing.', 'song_id': 295}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
print("Task already marked as success. All requirements verified:")
print("1. Logged into Spotify")
print("2. Fetched queue (24 songs)")
print("3. Fetched liked songs (12 songs)")
print("4. Identified 12 non-liked songs in queue")
print("5. Removed all 12 non-liked songs (from highest to lowest position)")
print("6. Queue now has 12 songs, all liked")
print("7. Player started - City of Fallen Angels is now playing")
print("Task status: success")
```

```
Task already marked as success. All requirements verified:
1. Logged into Spotify
2. Fetched queue (24 songs)
3. Fetched liked songs (12 songs)
4. Identified 12 non-liked songs in queue
5. Removed all 12 non-liked songs (from highest to lowest position)
6. Queue now has 12 songs, all liked
7. Player started - City of Fallen Angels is now playing
Task status: success
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
result = apis.supervisor.complete_task(status="success")
print(result)
```

```
{"message": "Marked the active task complete."}
```

