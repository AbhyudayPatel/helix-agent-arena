
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
 "instruction": "Keep going to the next song on Spotify until you reach a song I have already downloaded.",
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
print(apis.api_docs.show_api_descriptions(app_name='file_system'))
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
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='login'))
print(apis.api_docs.show_api_doc(app_name='file_system', api_name='show_directory'))
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
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
{
 "app_name": "file_system",
 "api_name": "show_directory",
 "path": "/directory",
 "method": "GET",
 "description": "Show a list of files and/or sub-directories, optionally recursively, in a directory.",
 "parameters": [
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from file_system app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "directory_path",
   "type": "string",
   "required": false,
   "description": "Path of the directory. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'.",
   "default": "/",
   "constraints": [
    "length >= 1"
   ]
  },
  {
   "name": "substring",
   "type": "string",
   "required": false,
   "description": "If passed, only files and sub-directories containing the given substring (ignoring case) will be shown.",
   "default": null,
   "constraints": []
  },
  {
   "name": "entry_type",
   "type": "string",
   "required": false,
   "description": "Whether to show all files and sub-directories, only files, or only sub-directories.",
   "default": "all",
   "constraints": [
    "value in ['all', 'files', 'directories']"
   ]
  },
  {
   "name": "recursive",
   "type": "boolean",
   "required": false,
   "description": "Whether to show files recursively.",
   "default": true,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   "string"
  ],
  "failure": {
   "message": "string"
  }
 }
}
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


### Environment Interaction 4
----------------------------------------------------------------------------
```python
# Login to file_system
fs_login = apis.file_system.login(username='carbrown@gmail.com', password='4k9jcny')
print('FS login:', fs_login)

# Login to spotify
sp_login = apis.spotify.login(username='carbrown@gmail.com', password='3a-m^o6')
print('SP login:', sp_login)
```

```
FS login: {'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmaWxlX3N5c3RlbStjYXJicm93bkBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.xJKEGHX16bg9nuz5_q95NYJ9SGTbKDMa_8BnohmmQPs', 'token_type': 'Bearer'}
SP login: {'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K2NhcmJyb3duQGdtYWlsLmNvbSIsImV4cCI6MTY4NDQxMjc0MX0.9d_I8NCxkjjw4tzQbeJq4JFYfr-NRaeA2tiTCvchMvw', 'token_type': 'Bearer'}
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
fs_token = fs_login['access_token']
sp_token = sp_login['access_token']

# Get all files recursively from root
files = apis.file_system.show_directory(access_token=fs_token, directory_path='/', recursive=True, entry_type='files')
print('Files:', files)
```

```
Files: ['/home/carl/backups/laptop.zip', '/home/carl/backups/phone.zip', '/home/carl/bills/electricity/2022-09.pdf', '/home/carl/bills/electricity/2022-10.pdf', '/home/carl/bills/electricity/2022-11.pdf', '/home/carl/bills/electricity/2022-12.pdf', '/home/carl/bills/electricity/2023-01.pdf', '/home/carl/bills/electricity/2023-02.pdf', '/home/carl/bills/electricity/2023-03.pdf', '/home/carl/bills/electricity/2023-04.pdf', '/home/carl/bills/electricity/2023-05.pdf', '/home/carl/bills/internet/2022-09.pdf', '/home/carl/bills/internet/2022-10.pdf', '/home/carl/bills/internet/2022-11.pdf', '/home/carl/bills/internet/2022-12.pdf', '/home/carl/bills/internet/2023-01.pdf', '/home/carl/bills/internet/2023-02.pdf', '/home/carl/bills/internet/2023-03.pdf', '/home/carl/bills/internet/2023-04.pdf', '/home/carl/bills/internet/2023-05.pdf', '/home/carl/bills/phone/2022-09.pdf', '/home/carl/bills/phone/2022-10.pdf', '/home/carl/bills/phone/2022-11.pdf', '/home/carl/bills/phone/2022-12.pdf', '/home/carl/bills/phone/2023-01.pdf', '/home/carl/bills/phone/2023-02.pdf', '/home/carl/bills/phone/2023-03.pdf', '/home/carl/bills/phone/2023-04.pdf', '/home/carl/bills/phone/2023-05.pdf', '/home/carl/documents/financial/bank_statements/2022-12.pdf', '/home/carl/documents/financial/bank_statements/2023-01.pdf', '/home/carl/documents/financial/bank_statements/2023-02.pdf', '/home/carl/documents/financial/bank_statements/2023-03.pdf', '/home/carl/documents/financial/bank_statements/2023-04.pdf', '/home/carl/documents/financial/bank_statements/2023-05.pdf', '/home/carl/documents/financial/taxes/federal/financial_year_2017.pdf', '/home/carl/documents/financial/taxes/federal/financial_year_2018.pdf', '/home/carl/documents/financial/taxes/federal/financial_year_2019.pdf', '/home/carl/documents/financial/taxes/federal/financial_year_2020.pdf', '/home/carl/documents/financial/taxes/federal/financial_year_2021.pdf', '/home/carl/documents/financial/taxes/state/financial_year_2017.pdf', '/home/carl/documents/financial/taxes/state/financial_year_2018.pdf', '/home/carl/documents/financial/taxes/state/financial_year_2019.pdf', '/home/carl/documents/financial/taxes/state/financial_year_2020.pdf', '/home/carl/documents/financial/taxes/state/financial_year_2021.pdf', '/home/carl/documents/personal/identity/birth_certificate.pdf', '/home/carl/documents/personal/identity/driving_license.pdf', '/home/carl/documents/personal/identity/passport.pdf', '/home/carl/documents/personal/identity/ssn.pdf', '/home/carl/documents/work/meetings/2023-apr-04/slides.ppt', '/home/carl/documents/work/meetings/2023-apr-04/video_recording.mp4', '/home/carl/documents/work/meetings/2023-apr-11/slides.ppt', '/home/carl/documents/work/meetings/2023-apr-11/video_recording.mp4', '/home/carl/documents/work/meetings/2023-apr-18/slides.ppt', '/home/carl/documents/work/meetings/2023-apr-18/video_recording.mp4', '/home/carl/documents/work/meetings/2023-apr-25/slides.ppt', '/home/carl/documents/work/meetings/2023-apr-25/video_recording.mp4', '/home/carl/documents/work/meetings/2023-mar-21/slides.ppt', '/home/carl/documents/work/meetings/2023-mar-21/video_recording.mp4', '/home/carl/documents/work/meetings/2023-mar-28/slides.ppt', '/home/carl/documents/work/meetings/2023-mar-28/video_recording.mp4', '/home/carl/documents/work/meetings/2023-may-02/slides.ppt', '/home/carl/documents/work/meetings/2023-may-02/video_recording.mp4', '/home/carl/documents/work/meetings/2023-may-09/slides.ppt', '/home/carl/documents/work/meetings/2023-may-09/video_recording.mp4', '/home/carl/documents/work/professional_headshot.jpeg', '/home/carl/documents/work/resume.pdf', '/home/carl/downloads/DIY_home_decor_inspiration.rar', '/home/carl/downloads/accommodation.jpg', '/home/carl/downloads/art_class_fees.pdf', '/home/carl/downloads/belay_device.pdf', '/home/carl/downloads/bird_feeder.jpg', '/home/carl/downloads/business_cards.pdf', '/home/carl/downloads/candy.pdf', '/home/carl/downloads/car_repair_sibling.pdf', '/home/carl/downloads/charcoal_pencils.pdf', '/home/carl/downloads/childhood_memories.zip', '/home/carl/downloads/client_meeting.pdf', '/home/carl/downloads/coding_interview_prep.docx', '/home/carl/downloads/coding_projects_portfolio.docx', '/home/carl/downloads/conference_tickets.jpg', '/home/carl/downloads/cooking_utensils.jpg', '/home/carl/downloads/corporate_gifts.pdf', '/home/carl/downloads/curtains.jpg', '/home/carl/downloads/dads_new_phone.pdf', '/home/carl/downloads/data_visualization_examples.ppt', '/home/carl/downloads/data_visualization_tutorial.mp4', '/home/carl/downloads/decorations.jpg', '/home/carl/downloads/dinner_party.jpg', '/home/carl/downloads/dinner_party_cousins.jpg', '/home/carl/downloads/dog_food.jpg', '/home/carl/downloads/exhibition_entry_fee.jpg', '/home/carl/downloads/exotic_cuisine_recipe_collection.pdf', '/home/carl/downloads/exotic_recipe_adventures.pdf', '/home/carl/downloads/extra_dice.jpg', '/home/carl/downloads/family_dinner.jpg', '/home/carl/downloads/family_photoshoot.jpg', '/home/carl/downloads/fashion_design_inspiration_gallery.zip', '/home/carl/downloads/fashion_design_sketches.rar', '/home/carl/downloads/gallery_membership.pdf', '/home/carl/downloads/game_expansion_pack.jpg', '/home/carl/downloads/game_night_decorations.pdf', '/home/carl/downloads/hand_warmers.jpg', '/home/carl/downloads/health_and_wellness_podcasts.mp3', '/home/carl/downloads/historical_documentary_series.mp4', '/home/carl/downloads/holiday_candles.pdf', '/home/carl/downloads/holiday_music.pdf', '/home/carl/downloads/home_decor.jpg', '/home/carl/downloads/home_renovation.jpg', '/home/carl/downloads/landscape_painting_tutorial.mp4', '/home/carl/downloads/lighting.pdf', '/home/carl/downloads/magazines.pdf', '/home/carl/downloads/marketing_campaign.pdf', '/home/carl/downloads/marketing_materials.jpg', '/home/carl/downloads/microwave.pdf', '/home/carl/downloads/moms_new_dress.jpg', '/home/carl/downloads/monthly_groceries.jpg', '/home/carl/downloads/monthly_magazine.pdf', '/home/carl/downloads/mystery_novel_ebook.epub', '/home/carl/downloads/nature_documentary_series.mp4', '/home/carl/downloads/new_books.jpg', '/home/carl/downloads/new_glasses_dad.jpg', '/home/carl/downloads/new_laptop.pdf', '/home/carl/downloads/office_lighting.pdf', '/home/carl/downloads/party_hats.jpg', '/home/carl/downloads/party_supplies.jpg', '/home/carl/downloads/pet_toys.jpg', '/home/carl/downloads/presentation_slides.pptx', '/home/carl/downloads/quickdraws.jpg', '/home/carl/downloads/scientific_research_paper.pdf', '/home/carl/downloads/ski_locker.pdf', '/home/carl/downloads/ski_pants.pdf', '/home/carl/downloads/snacks.pdf', '/home/carl/downloads/snacks_for_climbing.pdf', '/home/carl/downloads/sommelier_fee.jpg', '/home/carl/downloads/subscription_service.jpg', '/home/carl/downloads/sun_protection.pdf', '/home/carl/downloads/tablecloth.jpg', '/home/carl/downloads/tea_kettle.pdf', '/home/carl/downloads/team_building_activity.pdf', '/home/carl/downloads/team_photo_session.jpg', '/home/carl/downloads/timers.pdf', '/home/carl/downloads/tool_set.jpg', '/home/carl/downloads/training_board.pdf', '/home/carl/downloads/upbeat_music_playlist.mp3', '/home/carl/downloads/vacation_rental.jpg', '/home/carl/downloads/vacuum_cleaner.pdf', '/home/carl/downloads/virtual_reality_gaming_experience.zip', '/home/carl/downloads/watercolors.jpg', '/home/carl/downloads/world_travel_itinerary.docx', '/home/carl/photographs/vacations/cairo.tar', '/home/carl/photographs/vacations/florence.zip', '/home/carl/photographs/vacations/miami.tar', '/home/carl/photographs/vacations/santorini.tar', '/home/carl/trash/art_inspiration_sketches.zip', '/home/carl/trash/astronomy_101_course_materials.doc', '/home/carl/trash/cooking_tips_and_tricks_videos.zip', '/home/carl/trash/data_analysis_case_studies.xlsx', '/home/carl/trash/fashion_trends_lookbook.zip', '/home/carl/trash/mindfulness_and_stress_relief_workshops.mp3', '/home/carl/trash/world_landmarks_photo_album.zip']
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
# Filter for music files
music_files = [f for f in files if any(f.lower().endswith(ext) for ext in ['.mp3', '.wav', '.flac', '.m4a', '.ogg', '.aac'])]
print('Music files:', music_files)

# Also check for music-related paths
music_related = [f for f in files if 'music' in f.lower() or 'song' in f.lower() or 'audio' in f.lower()]
print('Music related:', music_related)
```

```
Music files: ['/home/carl/downloads/health_and_wellness_podcasts.mp3', '/home/carl/downloads/upbeat_music_playlist.mp3', '/home/carl/trash/mindfulness_and_stress_relief_workshops.mp3']
Music related: ['/home/carl/downloads/holiday_music.pdf', '/home/carl/downloads/upbeat_music_playlist.mp3']
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Show all files in downloads directory
downloads = [f for f in files if '/downloads/' in f.lower()]
print('Downloads:', downloads)

# Check Spotify API descriptions
print(apis.api_docs.show_api_descriptions(app_name='spotify'))
```

```
Downloads: ['/home/carl/downloads/DIY_home_decor_inspiration.rar', '/home/carl/downloads/accommodation.jpg', '/home/carl/downloads/art_class_fees.pdf', '/home/carl/downloads/belay_device.pdf', '/home/carl/downloads/bird_feeder.jpg', '/home/carl/downloads/business_cards.pdf', '/home/carl/downloads/candy.pdf', '/home/carl/downloads/car_repair_sibling.pdf', '/home/carl/downloads/charcoal_pencils.pdf', '/home/carl/downloads/childhood_memories.zip', '/home/carl/downloads/client_meeting.pdf', '/home/carl/downloads/coding_interview_prep.docx', '/home/carl/downloads/coding_projects_portfolio.docx', '/home/carl/downloads/conference_tickets.jpg', '/home/carl/downloads/cooking_utensils.jpg', '/home/carl/downloads/corporate_gifts.pdf', '/home/carl/downloads/curtains.jpg', '/home/carl/downloads/dads_new_phone.pdf', '/home/carl/downloads/data_visualization_examples.ppt', '/home/carl/downloads/data_visualization_tutorial.mp4', '/home/carl/downloads/decorations.jpg', '/home/carl/downloads/dinner_party.jpg', '/home/carl/downloads/dinner_party_cousins.jpg', '/home/carl/downloads/dog_food.jpg', '/home/carl/downloads/exhibition_entry_fee.jpg', '/home/carl/downloads/exotic_cuisine_recipe_collection.pdf', '/home/carl/downloads/exotic_recipe_adventures.pdf', '/home/carl/downloads/extra_dice.jpg', '/home/carl/downloads/family_dinner.jpg', '/home/carl/downloads/family_photoshoot.jpg', '/home/carl/downloads/fashion_design_inspiration_gallery.zip', '/home/carl/downloads/fashion_design_sketches.rar', '/home/carl/downloads/gallery_membership.pdf', '/home/carl/downloads/game_expansion_pack.jpg', '/home/carl/downloads/game_night_decorations.pdf', '/home/carl/downloads/hand_warmers.jpg', '/home/carl/downloads/health_and_wellness_podcasts.mp3', '/home/carl/downloads/historical_documentary_series.mp4', '/home/carl/downloads/holiday_candles.pdf', '/home/carl/downloads/holiday_music.pdf', '/home/carl/downloads/home_decor.jpg', '/home/carl/downloads/home_renovation.jpg', '/home/carl/downloads/landscape_painting_tutorial.mp4', '/home/carl/downloads/lighting.pdf', '/home/carl/downloads/magazines.pdf', '/home/carl/downloads/marketing_campaign.pdf', '/home/carl/downloads/marketing_materials.jpg', '/home/carl/downloads/microwave.pdf', '/home/carl/downloads/moms_new_dress.jpg', '/home/carl/downloads/monthly_groceries.jpg', '/home/carl/downloads/monthly_magazine.pdf', '/home/carl/downloads/mystery_novel_ebook.epub', '/home/carl/downloads/nature_documentary_series.mp4', '/home/carl/downloads/new_books.jpg', '/home/carl/downloads/new_glasses_dad.jpg', '/home/carl/downloads/new_laptop.pdf', '/home/carl/downloads/office_lighting.pdf', '/home/carl/downloads/party_hats.jpg', '/home/carl/downloads/party_supplies.jpg', '/home/carl/downloads/pet_toys.jpg', '/home/carl/downloads/presentation_slides.pptx', '/home/carl/downloads/quickdraws.jpg', '/home/carl/downloads/scientific_research_paper.pdf', '/home/carl/downloads/ski_locker.pdf', '/home/carl/downloads/ski_pants.pdf', '/home/carl/downloads/snacks.pdf', '/home/carl/downloads/snacks_for_climbing.pdf', '/home/carl/downloads/sommelier_fee.jpg', '/home/carl/downloads/subscription_service.jpg', '/home/carl/downloads/sun_protection.pdf', '/home/carl/downloads/tablecloth.jpg', '/home/carl/downloads/tea_kettle.pdf', '/home/carl/downloads/team_building_activity.pdf', '/home/carl/downloads/team_photo_session.jpg', '/home/carl/downloads/timers.pdf', '/home/carl/downloads/tool_set.jpg', '/home/carl/downloads/training_board.pdf', '/home/carl/downloads/upbeat_music_playlist.mp3', '/home/carl/downloads/vacation_rental.jpg', '/home/carl/downloads/vacuum_cleaner.pdf', '/home/carl/downloads/virtual_reality_gaming_experience.zip', '/home/carl/downloads/watercolors.jpg', '/home/carl/downloads/world_travel_itinerary.docx']
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


### Environment Interaction 8
----------------------------------------------------------------------------
```python
# Print all downloads
for f in downloads:
    print(f)
```

```
/home/carl/downloads/DIY_home_decor_inspiration.rar
/home/carl/downloads/accommodation.jpg
/home/carl/downloads/art_class_fees.pdf
/home/carl/downloads/belay_device.pdf
/home/carl/downloads/bird_feeder.jpg
/home/carl/downloads/business_cards.pdf
/home/carl/downloads/candy.pdf
/home/carl/downloads/car_repair_sibling.pdf
/home/carl/downloads/charcoal_pencils.pdf
/home/carl/downloads/childhood_memories.zip
/home/carl/downloads/client_meeting.pdf
/home/carl/downloads/coding_interview_prep.docx
/home/carl/downloads/coding_projects_portfolio.docx
/home/carl/downloads/conference_tickets.jpg
/home/carl/downloads/cooking_utensils.jpg
/home/carl/downloads/corporate_gifts.pdf
/home/carl/downloads/curtains.jpg
/home/carl/downloads/dads_new_phone.pdf
/home/carl/downloads/data_visualization_examples.ppt
/home/carl/downloads/data_visualization_tutorial.mp4
/home/carl/downloads/decorations.jpg
/home/carl/downloads/dinner_party.jpg
/home/carl/downloads/dinner_party_cousins.jpg
/home/carl/downloads/dog_food.jpg
/home/carl/downloads/exhibition_entry_fee.jpg
/home/carl/downloads/exotic_cuisine_recipe_collection.pdf
/home/carl/downloads/exotic_recipe_adventures.pdf
/home/carl/downloads/extra_dice.jpg
/home/carl/downloads/family_dinner.jpg
/home/carl/downloads/family_photoshoot.jpg
/home/carl/downloads/fashion_design_inspiration_gallery.zip
/home/carl/downloads/fashion_design_sketches.rar
/home/carl/downloads/gallery_membership.pdf
/home/carl/downloads/game_expansion_pack.jpg
/home/carl/downloads/game_night_decorations.pdf
/home/carl/downloads/hand_warmers.jpg
/home/carl/downloads/health_and_wellness_podcasts.mp3
/home/carl/downloads/historical_documentary_series.mp4
/home/carl/downloads/holiday_candles.pdf
/home/carl/downloads/holiday_music.pdf
/home/carl/downloads/home_decor.jpg
/home/carl/downloads/home_renovation.jpg
/home/carl/downloads/landscape_painting_tutorial.mp4
/home/carl/downloads/lighting.pdf
/home/carl/downloads/magazines.pdf
/home/carl/downloads/marketing_campaign.pdf
/home/carl/downloads/marketing_materials.jpg
/home/carl/downloads/microwave.pdf
/home/carl/downloads/moms_new_dress.jpg
/home/carl/downloads/monthly_groceries.jpg
/home/carl/downloads/monthly_magazine.pdf
/home/carl/downloads/mystery_novel_ebook.epub
/home/carl/downloads/nature_documentary_series.mp4
/home/carl/downloads/new_books.jpg
/home/carl/downloads/new_glasses_dad.jpg
/home/carl/downloads/new_laptop.pdf
/home/carl/downloads/office_lighting.pdf
/home/carl/downloads/party_hats.jpg
/home/carl/downloads/party_supplies.jpg
/home/carl/downloads/pet_toys.jpg
/home/carl/downloads/presentation_slides.pptx
/home/carl/downloads/quickdraws.jpg
/home/carl/downloads/scientific_research_paper.pdf
/home/carl/downloads/ski_locker.pdf
/home/carl/downloads/ski_pants.pdf
/home/carl/downloads/snacks.pdf
/home/carl/downloads/snacks_for_climbing.pdf
/home/carl/downloads/sommelier_fee.jpg
/home/carl/downloads/subscription_service.jpg
/home/carl/downloads/sun_protection.pdf
/home/carl/downloads/tablecloth.jpg
/home/carl/downloads/tea_kettle.pdf
/home/carl/downloads/team_building_activity.pdf
/home/carl/downloads/team_photo_session.jpg
/home/carl/downloads/timers.pdf
/home/carl/downloads/tool_set.jpg
/home/carl/downloads/training_board.pdf
/home/carl/downloads/upbeat_music_playlist.mp3
/home/carl/downloads/vacation_rental.jpg
/home/carl/downloads/vacuum_cleaner.pdf
/home/carl/downloads/virtual_reality_gaming_experience.zip
/home/carl/downloads/watercolors.jpg
/home/carl/downloads/world_travel_itinerary.docx
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Print remaining downloads
print(downloads[50:])
print()
# All mp3 files across entire filesystem
print('All MP3 files:', [f for f in files if f.endswith('.mp3')])
print()
# Check Spotify API descriptions
print(apis.api_docs.show_api_descriptions(app_name='spotify'))
```

```
[
 "/home/carl/downloads/monthly_magazine.pdf",
 "/home/carl/downloads/mystery_novel_ebook.epub",
 "/home/carl/downloads/nature_documentary_series.mp4",
 "/home/carl/downloads/new_books.jpg",
 "/home/carl/downloads/new_glasses_dad.jpg",
 "/home/carl/downloads/new_laptop.pdf",
 "/home/carl/downloads/office_lighting.pdf",
 "/home/carl/downloads/party_hats.jpg",
 "/home/carl/downloads/party_supplies.jpg",
 "/home/carl/downloads/pet_toys.jpg",
 "/home/carl/downloads/presentation_slides.pptx",
 "/home/carl/downloads/quickdraws.jpg",
 "/home/carl/downloads/scientific_research_paper.pdf",
 "/home/carl/downloads/ski_locker.pdf",
 "/home/carl/downloads/ski_pants.pdf",
 "/home/carl/downloads/snacks.pdf",
 "/home/carl/downloads/snacks_for_climbing.pdf",
 "/home/carl/downloads/sommelier_fee.jpg",
 "/home/carl/downloads/subscription_service.jpg",
 "/home/carl/downloads/sun_protection.pdf",
 "/home/carl/downloads/tablecloth.jpg",
 "/home/carl/downloads/tea_kettle.pdf",
 "/home/carl/downloads/team_building_activity.pdf",
 "/home/carl/downloads/team_photo_session.jpg",
 "/home/carl/downloads/timers.pdf",
 "/home/carl/downloads/tool_set.jpg",
 "/home/carl/downloads/training_board.pdf",
 "/home/carl/downloads/upbeat_music_playlist.mp3",
 "/home/carl/downloads/vacation_rental.jpg",
 "/home/carl/downloads/vacuum_cleaner.pdf",
 "/home/carl/downloads/virtual_reality_gaming_experience.zip",
 "/home/carl/downloads/watercolors.jpg",
 "/home/carl/downloads/world_travel_itinerary.docx"
]

All MP3 files: ['/home/carl/downloads/health_and_wellness_podcasts.mp3', '/home/carl/downloads/upbeat_music_playlist.mp3', '/home/carl/trash/mindfulness_and_stress_relief_workshops.mp3']

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


### Environment Interaction 10
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


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Search for playback-related APIs
print(apis.api_docs.search_api_docs(query='playback current song playing'))
print(apis.api_docs.search_api_docs(query='skip next song'))
print(apis.api_docs.search_api_docs(query='download song'))
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
  "api_name": "previous_song",
  "path": "/music_player/previous_song",
  "method": "POST",
  "description": "Go to the previous song in the song queue.",
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
]
[
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
  "api_name": "show_downloaded_songs",
  "path": "/downloaded_songs",
  "method": "GET",
  "description": "Get a list of downloaded songs.",
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
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "min_downloaded_at",
    "type": "string",
    "required": false,
    "description": "Filter songs by minimum downloaded_at date in YYYY-MM-DD format.",
    "default": "1500-01-01",
    "constraints": []
   },
   {
    "name": "max_downloaded_at",
    "type": "string",
    "required": false,
    "description": "Filter songs by maximum downloaded_at date in YYYY-MM-DD format.",
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
    "description": "The attribute to sort the downloaded songs by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and downloaded_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -downloaded_at.",
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
     "downloaded_at": "2019-01-01T00:00:00"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
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
 },
 {
  "app_name": "todoist",
  "api_name": "download_attachment",
  "path": "/task_comments/{task_comment_id}/attachments/{attachment_file_name}",
  "method": "GET",
  "description": "Download the attachment of a task comment.",
  "parameters": [
   {
    "name": "task_comment_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the comment to download the attachment from.",
    "default": null,
    "constraints": []
   },
   {
    "name": "attachment_file_name",
    "type": "string",
    "required": true,
    "description": "Name of the file attached to the task comment.",
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
    "description": "Access token obtained from todoist app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "download_to_file_path",
    "type": "string",
    "required": false,
    "description": "The file path to download the file attachment to in file system app. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'. If not passed, it will be saved in your ~/downloads directory.",
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
]
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='skip next'))
print(apis.api_docs.search_api_docs(query='downloaded'))
```

```
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
 }
]
[
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
  "api_name": "show_downloaded_songs",
  "path": "/downloaded_songs",
  "method": "GET",
  "description": "Get a list of downloaded songs.",
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
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "min_downloaded_at",
    "type": "string",
    "required": false,
    "description": "Filter songs by minimum downloaded_at date in YYYY-MM-DD format.",
    "default": "1500-01-01",
    "constraints": []
   },
   {
    "name": "max_downloaded_at",
    "type": "string",
    "required": false,
    "description": "Filter songs by maximum downloaded_at date in YYYY-MM-DD format.",
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
    "description": "The attribute to sort the downloaded songs by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at and downloaded_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -downloaded_at.",
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
     "downloaded_at": "2019-01-01T00:00:00"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "todoist",
  "api_name": "download_attachment",
  "path": "/task_comments/{task_comment_id}/attachments/{attachment_file_name}",
  "method": "GET",
  "description": "Download the attachment of a task comment.",
  "parameters": [
   {
    "name": "task_comment_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the comment to download the attachment from.",
    "default": null,
    "constraints": []
   },
   {
    "name": "attachment_file_name",
    "type": "string",
    "required": true,
    "description": "Name of the file attached to the task comment.",
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
    "description": "Access token obtained from todoist app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "download_to_file_path",
    "type": "string",
    "required": false,
    "description": "The file path to download the file attachment to in file system app. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'. If not passed, it will be saved in your ~/downloads directory.",
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
]
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_song_privates'))
```

```
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


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Get current song
current = apis.spotify.show_current_song(access_token=sp_token)
print('Current song:', current)
```

```
Current song: {'song_id': 322, 'title': 'Lost in the Labyrinth of Love', 'album_id': None, 'duration': 281, 'artists': [{'id': 36, 'name': 'Noah Bennett'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# Check if current song is downloaded
privates = apis.spotify.show_song_privates(song_id=322, access_token=sp_token)
print('Current song privates:', privates)

# If not downloaded, skip and check in a loop
max_iterations = 50
iteration = 0

current_song_id = 322
current_title = 'Lost in the Labyrinth of Love'

if privates.get('downloaded'):
    print(f'Current song "{current_title}" is already downloaded!')
else:
    print(f'Song "{current_title}" (id={current_song_id}) is NOT downloaded. Skipping...')
    
    while iteration < max_iterations:
        # Skip to next song
        skip_result = apis.spotify.next_song(access_token=sp_token)
        print(f'Skip result: {skip_result}')
        
        # Get current song
        current = apis.spotify.show_current_song(access_token=sp_token)
        current_song_id = current['song_id']
        current_title = current['title']
        print(f'Now playing: "{current_title}" (id={current_song_id})')
        
        # Check if downloaded
        privates = apis.spotify.show_song_privates(song_id=current_song_id, access_token=sp_token)
        print(f'Downloaded: {privates.get("downloaded")}')
        
        if privates.get('downloaded'):
            print(f'\n=== FOUND DOWNLOADED SONG: "{current_title}" (id={current_song_id}) ===')
            break
        
        iteration += 1
    
    if iteration >= max_iterations:
        print('Reached max iterations without finding a downloaded song.')
```

```
Current song privates: {'liked': False, 'reviewed': False, 'in_song_library': False, 'downloaded': False}
Song "Lost in the Labyrinth of Love" (id=322) is NOT downloaded. Skipping...
Skip result: {'message': 'Moved to the next song in the queue.', 'song_id': 40}
Now playing: "Burning Like a Distant Star" (id=40)
Downloaded: False
Skip result: {'message': 'Moved to the next song in the queue.', 'song_id': 71}
Now playing: "Eternal Fade" (id=71)
Downloaded: False
Skip result: {'message': 'Moved to the next song in the queue.', 'song_id': 50}
Now playing: "Lonely Skies" (id=50)
Downloaded: False
Skip result: {'message': 'Moved to the next song in the queue.', 'song_id': 66}
Now playing: "Phantom Pain" (id=66)
Downloaded: True

=== FOUND DOWNLOADED SONG: "Phantom Pain" (id=66) ===
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# Verify current state
current = apis.spotify.show_current_song(access_token=sp_token)
print('Current song:', current)
privates = apis.spotify.show_song_privates(song_id=current['song_id'], access_token=sp_token)
print('Privates:', privates)
print(f'\nThe downloaded song we stopped at: "{current["title"]}" (id={current["song_id"]})')
```

```
Current song: {'song_id': 66, 'title': 'Phantom Pain', 'album_id': 13, 'duration': 223, 'artists': [{'id': 31, 'name': 'Hazel Winter'}, {'id': 5, 'name': 'Ava Morgan'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Privates: {'liked': False, 'reviewed': False, 'in_song_library': False, 'downloaded': True}

The downloaded song we stopped at: "Phantom Pain" (id=66)
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task(answer="Phantom Pain")
```

```
Execution successful.
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
# Re-read the task
print(apis.supervisor.show_active_task())

# Verify current song state
current = apis.spotify.show_current_song(access_token=sp_token)
print('Current song:', current)
privates = apis.spotify.show_song_privates(song_id=current['song_id'], access_token=sp_token)
print('Privates:', privates)
print(f'Song "{current["title"]}" is downloaded: {privates["downloaded"]}')
```

```
{
 "instruction": "Keep going to the next song on Spotify until you reach a song I have already downloaded.",
 "status": "success",
 "answer": "Phantom Pain"
}
Current song: {'song_id': 66, 'title': 'Phantom Pain', 'album_id': 13, 'duration': 223, 'artists': [{'id': 31, 'name': 'Hazel Winter'}, {'id': 5, 'name': 'Ava Morgan'}], 'played_seconds': 0, 'is_playing': True, 'is_looping': False}
Privates: {'liked': False, 'reviewed': False, 'in_song_library': False, 'downloaded': True}
Song "Phantom Pain" is downloaded: True
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
apis.supervisor.complete_task(answer="Phantom Pain")
```

```
Execution successful.
```

