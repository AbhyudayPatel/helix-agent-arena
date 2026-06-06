
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
 "instruction": "Reset my Spotify queue with all of its recommended songs, shuffle it, and play it.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "WH=L{FS"
 },
 {
  "account_name": "file_system",
  "password": "hOodwkS"
 },
 {
  "account_name": "gmail",
  "password": "x&xcoCg"
 },
 {
  "account_name": "phone",
  "password": "2I1#6ld"
 },
 {
  "account_name": "simple_note",
  "password": "aVfy)Rr"
 },
 {
  "account_name": "splitwise",
  "password": "KqI[fbx"
 },
 {
  "account_name": "spotify",
  "password": "+=)+0kx"
 },
 {
  "account_name": "todoist",
  "password": "o1Dv3KT"
 },
 {
  "account_name": "venmo",
  "password": "{{YH7SV"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Glen",
 "last_name": "Moore",
 "email": "gl.moore@gmail.com",
 "phone_number": "8346699249",
 "birthday": "1987-11-10",
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


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Login to Spotify
result = apis.spotify.login(username='gl.moore@gmail.com', password='+=)+0kx')
print(result)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2dsLm1vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.1-auY1iwWfor4_lD-JwFuaGPDvlyBbJk_gvylHLc1LE",
 "token_type": "Bearer"
}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2dsLm1vb3JlQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjA5OH0.1-auY1iwWfor4_lD-JwFuaGPDvlyBbJk_gvylHLc1LE"

# Search for recommendation-related APIs
print(apis.api_docs.search_api_docs(query='recommendations spotify'))
```

```
[
 {
  "app_name": "spotify",
  "api_name": "show_recommendations",
  "path": "/recommendations",
  "method": "GET",
  "description": "Get personalized song recommendations for the user.",
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
  "api_name": "delete_account",
  "path": "/account",
  "method": "DELETE",
  "description": "Delete your account.",
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
 },
 {
  "app_name": "spotify",
  "api_name": "logout",
  "path": "/auth/logout",
  "method": "POST",
  "description": "Logout from your account.",
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
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Discover queue and playback related APIs
print(apis.api_docs.search_api_docs(query='queue spotify'))
print('---')
print(apis.api_docs.search_api_docs(query='shuffle play spotify'))
```

```
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
---
[
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
  "api_name": "delete_account",
  "path": "/account",
  "method": "DELETE",
  "description": "Delete your account.",
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


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Step 1: Get all recommended songs (paginate)
all_recs = []
page_index = 0
page_limit = 20
while True:
    page = apis.spotify.show_recommendations(access_token=access_token, page_index=page_index, page_limit=page_limit)
    print(f"Page {page_index}: got {len(page)} songs")
    all_recs.extend(page)
    if len(page) < page_limit:
        break
    page_index += 1

print(f"Total recommended songs: {len(all_recs)}")
for s in all_recs:
    print(s['song_id'], s['title'])
```

```
Page 0: got 20 songs
Page 1: got 3 songs
Total recommended songs: 23
28 Invisible Lines
50 Lonely Skies
60 The Haunting Echo of Goodbye
63 Journey Through the Unknown
70 Serenade of the Forgotten Stars
76 Whispers of the Heart
82 Lost in the Twilight of Hope
86 Shattered
100 Fragile Bonds
106 The Irony of a Perfect Moment
135 In the Silence of Your Absence
153 Love's Aftermath
170 The Silence that Speaks Volumes
189 Sinking Ship
190 Final Goodbye
212 A Labyrinth of Empty Streets
220 The Threads of a Frayed Bond
228 The Last Waltz of a Broken Heart
265 Secrets of the Heart
270 Tangled Web
280 The Tragedy of Living Without
286 Golden Lies
295 City of Fallen Angels
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Step 2: Clear the current queue
clear_result = apis.spotify.clear_song_queue(access_token=access_token)
print("Clear queue:", clear_result)

# Step 3: Find the add_song_to_queue API doc
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='add_song_to_queue'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 6, in <module>
    print(apis.api_docs.show_api_doc(app_name='spotify', api_name='add_song_to_queue'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name add_song_to_queue found for the spotify app. Check the api and app name again."}
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='add song queue spotify'))
```

```
[
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
  "api_name": "add_song_to_playlist",
  "path": "/playlists/{playlist_id}/songs/{song_id}",
  "method": "POST",
  "description": "Add a song to a playlist.",
  "parameters": [
   {
    "name": "playlist_id",
    "type": "integer",
    "required": true,
    "description": "The playlist id to add the song to.",
    "default": null,
    "constraints": []
   },
   {
    "name": "song_id",
    "type": "integer",
    "required": true,
    "description": "The song id to add.",
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
]
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Step 2: Clear the current queue
clear_result = apis.spotify.clear_song_queue(access_token=access_token)
print("Clear queue:", clear_result)

# Step 3: Add all recommended songs to the queue
for song in all_recs:
    result = apis.spotify.add_to_queue(access_token=access_token, song_id=song['song_id'])
    print(f"Added song {song['song_id']} ({song['title']}): {result}")

print(f"\nAdded {len(all_recs)} songs to queue.")
```

```
Clear queue: {'message': 'Cleared the song queue.'}
Added song 28 (Invisible Lines): {'message': 'Song added to the queue.'}
Added song 50 (Lonely Skies): {'message': 'Song added to the queue.'}
Added song 60 (The Haunting Echo of Goodbye): {'message': 'Song added to the queue.'}
Added song 63 (Journey Through the Unknown): {'message': 'Song added to the queue.'}
Added song 70 (Serenade of the Forgotten Stars): {'message': 'Song added to the queue.'}
Added song 76 (Whispers of the Heart): {'message': 'Song added to the queue.'}
Added song 82 (Lost in the Twilight of Hope): {'message': 'Song added to the queue.'}
Added song 86 (Shattered): {'message': 'Song added to the queue.'}
Added song 100 (Fragile Bonds): {'message': 'Song added to the queue.'}
Added song 106 (The Irony of a Perfect Moment): {'message': 'Song added to the queue.'}
Added song 135 (In the Silence of Your Absence): {'message': 'Song added to the queue.'}
Added song 153 (Love's Aftermath): {'message': 'Song added to the queue.'}
Added song 170 (The Silence that Speaks Volumes): {'message': 'Song added to the queue.'}
Added song 189 (Sinking Ship): {'message': 'Song added to the queue.'}
Added song 190 (Final Goodbye): {'message': 'Song added to the queue.'}
Added song 212 (A Labyrinth of Empty Streets): {'message': 'Song added to the queue.'}
Added song 220 (The Threads of a Frayed Bond): {'message': 'Song added to the queue.'}
Added song 228 (The Last Waltz of a Broken Heart): {'message': 'Song added to the queue.'}
Added song 265 (Secrets of the Heart): {'message': 'Song added to the queue.'}
Added song 270 (Tangled Web): {'message': 'Song added to the queue.'}
Added song 280 (The Tragedy of Living Without): {'message': 'Song added to the queue.'}
Added song 286 (Golden Lies): {'message': 'Song added to the queue.'}
Added song 295 (City of Fallen Angels): {'message': 'Song added to the queue.'}

Added 23 songs to queue.
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Step 4: Shuffle the queue
shuffle_result = apis.spotify.shuffle_song_queue(access_token=access_token)
print("Shuffle:", shuffle_result)

# Step 5: Find and use the play API
print(apis.api_docs.search_api_docs(query='play music player spotify'))
```

```
Shuffle: {'message': 'Shuffled the music player queue.'}
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


### Environment Interaction 12
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='resume start playback spotify'))
```

```
[
 {
  "app_name": "spotify",
  "api_name": "delete_account",
  "path": "/account",
  "method": "DELETE",
  "description": "Delete your account.",
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
 },
 {
  "app_name": "spotify",
  "api_name": "logout",
  "path": "/auth/logout",
  "method": "POST",
  "description": "Logout from your account.",
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
 }
]
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Get all spotify API descriptions - need to see the full list
descs = apis.api_docs.show_api_descriptions(app_name='spotify')
for d in descs:
    print(d['name'], '-', d['description'])
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


### Environment Interaction 14
----------------------------------------------------------------------------
```python
for d in descs:
    print(d['name'], '-', d['description'])
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


### Environment Interaction 15
----------------------------------------------------------------------------
```python
for i, d in enumerate(descs):
    print(i, d['name'], '-', d['description'])
```

```
0 show_account - Show your account information. Unlike show_profile, this includes private information.
1 signup - Sign up to create account.
2 delete_account - Delete your account.
3 update_account_name - Update your first or last name in the account profile.
4 login - Login to your account.
5 logout - Logout from your account.
6 send_verification_code - Send account verification code to your email address.
7 verify_account - Verify your account using the verification code sent to your email address.
8 send_password_reset_code - Send password reset code to your email address.
9 reset_password - Reset your password using the password reset code sent to your email address.
10 show_profile - Show public profile information of a user.
11 show_genres - Show the list of all music genres.
12 search_songs - Search for songs with a query.
13 show_song - Get details of a specific song.
14 show_song_privates - Show information about the song that is private to the user.
15 like_song - Like a song.
16 unlike_song - Unlike a song.
17 show_liked_songs - Get a list of songs you have liked.
18 search_albums - Search for albums with a query.
19 show_album - Get details of a specific album.
20 show_album_privates - Show information about the album that is private to the user.
21 like_album - Like a album.
22 unlike_album - Unlike a album.
23 show_liked_albums - Get a list of albums you have liked.
24 show_playlist_library - Get a list of playlists in the user's playlist library.
25 search_playlists - Search for playlists with a query. It will search over all public playlists and your own private playlists.
26 create_playlist - Create a new playlist.
27 show_playlist - Get detailed information about a specific playlist. You can view your own playlists or others' playlists if they are public.
28 delete_playlist - Delete a playlist.
29 update_playlist - Update a playlist title or privacy.
30 show_playlist_privates - Show information about the playlist that is private to the user.
31 like_playlist - Like a playlist.
32 unlike_playlist - Unlike a playlist.
33 show_liked_playlists - Get a list of playlists you have liked.
34 search_artists - Search for artists with a query.
35 show_artist - Get details of a specific artist.
36 show_artist_following - Show if the user is following the artist.
37 show_song_library - Get a list of songs in the user's song library.
38 add_song_to_library - Add a song to the user's song library.
39 remove_song_from_library - Remove a song from the user's song library.
40 show_album_library - Get a list of albums in the user's album library.
41 add_album_to_library - Add an album to the user's album library.
42 remove_album_from_library - Remove an album from the user's album library.
43 add_song_to_playlist - Add a song to a playlist.
44 remove_song_from_playlist - Remove a song from a playlist.
45 show_downloaded_songs - Get a list of downloaded songs.
46 download_song - Download a song.
47 remove_downloaded_song - Remove a song from downloads.
48 show_following_artists - Get a list of artists the user is following.
49 follow_artist - Follow an artist.
50 unfollow_artist - Unfollow an artist.
51 show_song_reviews - Get a list of reviews for a song.
52 review_song - Rate or review a song.
53 show_song_review - Show a song review.
54 delete_song_review - Delete a song review.
55 update_song_review - Update a song review.
56 show_album_reviews - Get a list of reviews for an album.
57 review_album - Rate or review an album.
58 show_album_review - Show an album review.
59 delete_album_review - Delete an album review.
60 update_album_review - Update an album review.
61 show_playlist_reviews - Show a list of reviews for your playlist or others' public playlist.
62 review_playlist - Rate or review a playlist.
63 show_playlist_review - Show a playlist review.
64 delete_playlist_review - Delete a playlist review.
65 update_playlist_review - Update a playlist review.
66 show_payment_cards - Get a list of users payment cards.
67 add_payment_card - Add a new payment card.
68 show_payment_card - Get details of a payment card.
69 delete_payment_card - Delete payment card information.
70 update_payment_card - Update payment card information.
71 show_current_song - Show details of the current song on the queue.
72 play_music - Play music based on various criteria. You can pass, at most, any one of queue_position, song_id, album_id or playlist_id. If one of song_id, album_id or playlist_id is passed, that song, album or playlist will be added to the queue and played. Otherwise, the queue will remain unchanged. If queue_position is passed, the song at that position in the queue will be played. If none is passed, the current song in the queue will be played.
73 pause_music - Pause the currently playing song.
74 previous_song - Go to the previous song in the song queue.
75 next_song - Go to the next song in the song queue.
76 move_song_in_queue - Move a song in the queue to a new position.
77 seek_song - Seek the current song to the given number of seconds.
78 loop_song - Set whether to loop the current song.
79 shuffle_song_queue - Shuffle songs in the music player queue.
80 show_song_queue - Get the music player song queue. Songs are played in the order of the queue in a cycle.
81 add_to_queue - Add a song, album or playlist to the music player song queue.
82 clear_song_queue - Clear the music player song queue.
83 remove_song_from_queue - Remove a song at the given position from the music player song queue.
84 show_volume - Get the volume level of the music player.
85 set_volume - Set the volume level of the music player.
86 show_recommendations - Get personalized song recommendations for the user.
87 show_premium_plans - Show information about premium plans available.
88 show_premium_subscriptions - Show your premium subscription history.
89 subscribe_premium - Subscribe to premium membership.
90 download_premium_subscription_receipt - Download the receipt for a premium subscription.
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
print([d['name'] for d in descs])
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


### Environment Interaction 17
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='play_music'))
```

```
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
}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# Step 5: Play from position 0 (start of the shuffled queue)
play_result = apis.spotify.play_music(access_token=access_token, queue_position=0)
print("Play:", play_result)

# Verify: show current queue state
queue = apis.spotify.show_song_queue(access_token=access_token)
print(f"\nQueue has {len(queue)} songs")
for s in queue:
    print(f"  pos={s['position']} is_current={s['is_current']} is_playing={s['is_playing']} - {s['title']}")
```

```
Play: {'message': 'Song (In the Silence of Your Absence) is now playing.', 'song_id': 135}

Queue has 23 songs
  pos=0 is_current=True is_playing=True - In the Silence of Your Absence
  pos=1 is_current=False is_playing=False - The Irony of a Perfect Moment
  pos=2 is_current=False is_playing=False - Golden Lies
  pos=3 is_current=False is_playing=False - The Tragedy of Living Without
  pos=4 is_current=False is_playing=False - Lost in the Twilight of Hope
  pos=5 is_current=False is_playing=False - Tangled Web
  pos=6 is_current=False is_playing=False - The Haunting Echo of Goodbye
  pos=7 is_current=False is_playing=False - A Labyrinth of Empty Streets
  pos=8 is_current=False is_playing=False - Invisible Lines
  pos=9 is_current=False is_playing=False - Serenade of the Forgotten Stars
  pos=10 is_current=False is_playing=False - Shattered
  pos=11 is_current=False is_playing=False - Secrets of the Heart
  pos=12 is_current=False is_playing=False - The Last Waltz of a Broken Heart
  pos=13 is_current=False is_playing=False - Lonely Skies
  pos=14 is_current=False is_playing=False - Fragile Bonds
  pos=15 is_current=False is_playing=False - Journey Through the Unknown
  pos=16 is_current=False is_playing=False - The Threads of a Frayed Bond
  pos=17 is_current=False is_playing=False - Sinking Ship
  pos=18 is_current=False is_playing=False - Love's Aftermath
  pos=19 is_current=False is_playing=False - The Silence that Speaks Volumes
  pos=20 is_current=False is_playing=False - Whispers of the Heart
  pos=21 is_current=False is_playing=False - City of Fallen Angels
  pos=22 is_current=False is_playing=False - Final Goodbye
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task(status="success")
```

```
Execution successful.
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
# Re-read the task
print(apis.supervisor.show_active_task())

# Verify queue state
queue = apis.spotify.show_song_queue(access_token=access_token)
print(f"\nQueue has {len(queue)} songs (expected 23 recommended songs)")

# Check all recommended song IDs are in the queue
rec_ids = set(s['song_id'] for s in all_recs)
queue_ids = set(s['song_id'] for s in queue)
print(f"Recommended IDs: {sorted(rec_ids)}")
print(f"Queue IDs: {sorted(queue_ids)}")
print(f"All recommended songs in queue: {rec_ids == queue_ids}")

# Check playback is active
playing = [s for s in queue if s['is_playing']]
current = [s for s in queue if s['is_current']]
print(f"\nCurrently playing: {playing}")
print(f"Current song: {current}")

# Check shuffle happened (order differs from original recommendation order)
original_order = [s['song_id'] for s in all_recs]
queue_order = [s['song_id'] for s in sorted(queue, key=lambda x: x['position'])]
print(f"\nOriginal order: {original_order}")
print(f"Queue order:    {queue_order}")
print(f"Shuffled (order differs): {original_order != queue_order}")
```

```
{
 "instruction": "Reset my Spotify queue with all of its recommended songs, shuffle it, and play it.",
 "status": "success",
 "answer": null
}

Queue has 23 songs (expected 23 recommended songs)
Recommended IDs: [28, 50, 60, 63, 70, 76, 82, 86, 100, 106, 135, 153, 170, 189, 190, 212, 220, 228, 265, 270, 280, 286, 295]
Queue IDs: [28, 50, 60, 63, 70, 76, 82, 86, 100, 106, 135, 153, 170, 189, 190, 212, 220, 228, 265, 270, 280, 286, 295]
All recommended songs in queue: True

Currently playing: [{'song_id': 135, 'title': 'In the Silence of Your Absence', 'album_id': None, 'duration': 208, 'artists': [{'id': 9, 'name': 'Zoey James'}], 'position': 0, 'is_playing': True, 'is_current': True}]
Current song: [{'song_id': 135, 'title': 'In the Silence of Your Absence', 'album_id': None, 'duration': 208, 'artists': [{'id': 9, 'name': 'Zoey James'}], 'position': 0, 'is_playing': True, 'is_current': True}]

Original order: [28, 50, 60, 63, 70, 76, 82, 86, 100, 106, 135, 153, 170, 189, 190, 212, 220, 228, 265, 270, 280, 286, 295]
Queue order:    [135, 106, 286, 280, 82, 270, 60, 212, 28, 70, 86, 265, 228, 50, 100, 63, 220, 189, 153, 170, 76, 295, 190]
Shuffled (order differs): True
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task(status="success")
```

```
Execution successful.
```

