
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
 "instruction": "Remove all the songs that I have liked from my Spotify queue, and then start the player.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "Kv8O=+h"
 },
 {
  "account_name": "file_system",
  "password": "PpLu_dZ"
 },
 {
  "account_name": "gmail",
  "password": "%Czv-5s"
 },
 {
  "account_name": "phone",
  "password": "QG77Xz8"
 },
 {
  "account_name": "simple_note",
  "password": "3qCC2+8"
 },
 {
  "account_name": "splitwise",
  "password": "Z#{O$AI"
 },
 {
  "account_name": "spotify",
  "password": "TsivP)G"
 },
 {
  "account_name": "todoist",
  "password": "&M=jE1u"
 },
 {
  "account_name": "venmo",
  "password": "f$paRge"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Matthew",
 "last_name": "Blackburn",
 "email": "matthew.blac@gmail.com",
 "phone_number": "4886643554",
 "birthday": "1982-12-15",
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
# Get full list
import json
docs = apis.api_docs.show_api_descriptions(app_name='spotify')
for d in docs:
    print(d['name'], '-', d['description'])
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


### Environment Interaction 4
----------------------------------------------------------------------------
```python
docs = apis.api_docs.show_api_descriptions(app_name='spotify')
for d in docs:
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


### Environment Interaction 5
----------------------------------------------------------------------------
```python
docs = apis.api_docs.show_api_descriptions(app_name='spotify')
# Print all names
names = [d['name'] for d in docs]
print(names)
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


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='login'))
print('---')
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_liked_songs'))
print('---')
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='show_song_queue'))
print('---')
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='remove_song_from_queue'))
print('---')
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='play_music'))
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
---
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
---
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
---
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
---
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


### Environment Interaction 7
----------------------------------------------------------------------------
```python
# Login to Spotify
resp = apis.spotify.login(username='matthew.blac@gmail.com', password='TsivP)G')
print(resp)
```

```
{
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K21hdHRoZXcuYmxhY0BnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.1CWbU1EGrApamnSF06oN46u6Z7T3fP6l_o104s3HM7A",
 "token_type": "Bearer"
}
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzcG90aWZ5K21hdHRoZXcuYmxhY0BnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.1CWbU1EGrApamnSF06oN46u6Z7T3fP6l_o104s3HM7A"

# Fetch the song queue
queue = apis.spotify.show_song_queue(access_token=access_token)
print(queue)
```

```
[
 {
  "song_id": 268,
  "title": "Empty Pages",
  "album_id": null,
  "duration": 293,
  "artists": [
   {
    "id": 28,
    "name": "Evelyn Rose"
   }
  ],
  "position": 0,
  "is_playing": false,
  "is_current": true
 },
 {
  "song_id": 290,
  "title": "Whispers in the Wind",
  "album_id": null,
  "duration": 253,
  "artists": [
   {
    "id": 31,
    "name": "Hazel Winter"
   }
  ],
  "position": 1,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 153,
  "title": "Love's Aftermath",
  "album_id": null,
  "duration": 265,
  "artists": [
   {
    "id": 12,
    "name": "Mia Sullivan"
   }
  ],
  "position": 2,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 134,
  "title": "Lost in a Sea of Echoes",
  "album_id": null,
  "duration": 224,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "position": 3,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 158,
  "title": "Siren's Call",
  "album_id": null,
  "duration": 200,
  "artists": [
   {
    "id": 13,
    "name": "Luna Starlight"
   }
  ],
  "position": 4,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 132,
  "title": "Shadow Dance",
  "album_id": null,
  "duration": 210,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "position": 5,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 139,
  "title": "Momentary Bliss",
  "album_id": null,
  "duration": 236,
  "artists": [
   {
    "id": 10,
    "name": "Zoe Mitchell"
   }
  ],
  "position": 6,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 178,
  "title": "Sorrow's Silent Symphony",
  "album_id": null,
  "duration": 287,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "position": 7,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 180,
  "title": "The Intricacies of a Broken Heart",
  "album_id": null,
  "duration": 244,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   }
  ],
  "position": 8,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 121,
  "title": "Astral Serenity",
  "album_id": null,
  "duration": 200,
  "artists": [
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "position": 9,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 130,
  "title": "Longing for Another Chance",
  "album_id": null,
  "duration": 274,
  "artists": [
   {
    "id": 8,
    "name": "Aria Sterling"
   }
  ],
  "position": 10,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 76,
  "title": "Whispers of the Heart",
  "album_id": 16,
  "duration": 270,
  "artists": [
   {
    "id": 34,
    "name": "Lily Moon"
   },
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "position": 11,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 111,
  "title": "Lonesome Road",
  "album_id": null,
  "duration": 277,
  "artists": [
   {
    "id": 6,
    "name": "Seraphina Dawn"
   }
  ],
  "position": 12,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 82,
  "title": "Lost in the Twilight of Hope",
  "album_id": 18,
  "duration": 193,
  "artists": [
   {
    "id": 33,
    "name": "Felix Blackwood"
   }
  ],
  "position": 13,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 251,
  "title": "Trapped in the Snare of Love",
  "album_id": null,
  "duration": 268,
  "artists": [
   {
    "id": 26,
    "name": "Isabella Cruz"
   }
  ],
  "position": 14,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 58,
  "title": "Cursed Love",
  "album_id": 12,
  "duration": 214,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "position": 15,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 157,
  "title": "Chasing the Elusive Horizon",
  "album_id": null,
  "duration": 201,
  "artists": [
   {
    "id": 13,
    "name": "Luna Starlight"
   }
  ],
  "position": 16,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 219,
  "title": "Strangers Again",
  "album_id": null,
  "duration": 292,
  "artists": [
   {
    "id": 21,
    "name": "Oceanic Odyssey"
   }
  ],
  "position": 17,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 71,
  "title": "Eternal Fade",
  "album_id": 15,
  "duration": 267,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   },
   {
    "id": 7,
    "name": "Orion Steele"
   }
  ],
  "position": 18,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 265,
  "title": "Secrets of the Heart",
  "album_id": null,
  "duration": 183,
  "artists": [
   {
    "id": 27,
    "name": "Carter Knight"
   }
  ],
  "position": 19,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 60,
  "title": "The Haunting Echo of Goodbye",
  "album_id": 12,
  "duration": 224,
  "artists": [
   {
    "id": 9,
    "name": "Zoey James"
   }
  ],
  "position": 20,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 14,
  "title": "Memories Etched in Melancholy",
  "album_id": 3,
  "duration": 196,
  "artists": [
   {
    "id": 16,
    "name": "Apollo Serenade"
   },
   {
    "id": 2,
    "name": "Phoenix Rivers"
   }
  ],
  "position": 21,
  "is_playing": false,
  "is_current": false
 },
 {
  "song_id": 275,
  "title": "In the Arms of Solitude",
  "album_id": null,
  "duration": 187,
  "artists": [
   {
    "id": 29,
    "name": "Lucas Diaz"
   }
  ],
  "position": 22,
  "is_playing": false,
  "is_current": false
 }
]
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
# Store queue songs
queue_songs = queue  # already fetched
queue_ids = {s['song_id'] for s in queue_songs}
print(f"Queue has {len(queue_songs)} songs: {[s['song_id'] for s in queue_songs]}")

# Fetch ALL liked songs (paginate)
liked_songs = []
page_index = 0
page_limit = 20
while True:
    page = apis.spotify.show_liked_songs(access_token=access_token, page_index=page_index, page_limit=page_limit)
    if not page:
        break
    liked_songs.extend(page)
    if len(page) < page_limit:
        break
    page_index += 1

liked_ids = {s['song_id'] for s in liked_songs}
print(f"Total liked songs: {len(liked_songs)}")
print(f"Liked song IDs: {liked_ids}")
```

```
Queue has 23 songs: [268, 290, 153, 134, 158, 132, 139, 178, 180, 121, 130, 76, 111, 82, 251, 58, 157, 219, 71, 265, 60, 14, 275]
Total liked songs: 11
Liked song IDs: {130, 132, 134, 265, 268, 251, 82, 275, 58, 219, 60}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
# Find queued songs that are liked
to_remove = [s for s in queue_songs if s['song_id'] in liked_ids]
print(f"Songs to remove ({len(to_remove)}):")
for s in to_remove:
    print(f"  song_id={s['song_id']}, title={s['title']}, position={s['position']}")

# Check remove API signature
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='remove_song_from_queue'))
```

```
Songs to remove (11):
  song_id=268, title=Empty Pages, position=0
  song_id=134, title=Lost in a Sea of Echoes, position=3
  song_id=132, title=Shadow Dance, position=5
  song_id=130, title=Longing for Another Chance, position=10
  song_id=82, title=Lost in the Twilight of Hope, position=13
  song_id=251, title=Trapped in the Snare of Love, position=14
  song_id=58, title=Cursed Love, position=15
  song_id=219, title=Strangers Again, position=17
  song_id=265, title=Secrets of the Heart, position=19
  song_id=60, title=The Haunting Echo of Goodbye, position=20
  song_id=275, title=In the Arms of Solitude, position=22
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
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
# Sort by position descending so removing higher positions first doesn't affect lower positions
to_remove_sorted = sorted(to_remove, key=lambda s: s['position'], reverse=True)
print("Removing in order (highest position first):")
for s in to_remove_sorted:
    print(f"  Removing song_id={s['song_id']}, title={s['title']}, position={s['position']}")
    result = apis.spotify.remove_song_from_queue(access_token=access_token, position=s['position'])
    print(f"    Result: {result}")
```

```
Removing in order (highest position first):
  Removing song_id=275, title=In the Arms of Solitude, position=22
    Result: {'message': 'Removed song at position 22 from the song queue.'}
  Removing song_id=60, title=The Haunting Echo of Goodbye, position=20
    Result: {'message': 'Removed song at position 20 from the song queue.'}
  Removing song_id=265, title=Secrets of the Heart, position=19
    Result: {'message': 'Removed song at position 19 from the song queue.'}
  Removing song_id=219, title=Strangers Again, position=17
    Result: {'message': 'Removed song at position 17 from the song queue.'}
  Removing song_id=58, title=Cursed Love, position=15
    Result: {'message': 'Removed song at position 15 from the song queue.'}
  Removing song_id=251, title=Trapped in the Snare of Love, position=14
    Result: {'message': 'Removed song at position 14 from the song queue.'}
  Removing song_id=82, title=Lost in the Twilight of Hope, position=13
    Result: {'message': 'Removed song at position 13 from the song queue.'}
  Removing song_id=130, title=Longing for Another Chance, position=10
    Result: {'message': 'Removed song at position 10 from the song queue.'}
  Removing song_id=132, title=Shadow Dance, position=5
    Result: {'message': 'Removed song at position 5 from the song queue.'}
  Removing song_id=134, title=Lost in a Sea of Echoes, position=3
    Result: {'message': 'Removed song at position 3 from the song queue.'}
  Removing song_id=268, title=Empty Pages, position=0
    Result: {'message': 'Removed song at position 0 from the song queue.'}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
# Verify the queue - check no liked songs remain
new_queue = apis.spotify.show_song_queue(access_token=access_token)
new_queue_ids = {s['song_id'] for s in new_queue}
remaining_liked = new_queue_ids & liked_ids
print(f"New queue size: {len(new_queue)}")
print(f"New queue song IDs: {[s['song_id'] for s in new_queue]}")
print(f"Liked songs still in queue: {remaining_liked}")

# Now start the player
print(apis.api_docs.show_api_doc(app_name='spotify', api_name='play_music'))
```

```
New queue size: 12
New queue song IDs: [290, 153, 158, 139, 178, 180, 121, 76, 111, 157, 71, 14]
Liked songs still in queue: set()
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


### Environment Interaction 13
----------------------------------------------------------------------------
```python
# Start the player - play current song in queue (no extra params = play current)
result = apis.spotify.play_music(access_token=access_token)
print(result)
```

```
{"message": "Song (Whispers in the Wind) is now playing.", "song_id": 290}
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
# Final verification
print("=== VERIFICATION ===")
print(f"Removed {len(to_remove)} liked songs from queue")
print(f"Remaining queue size: {len(new_queue)} (none are liked songs)")
print(f"Player started: Song 'Whispers in the Wind' (song_id=290) is now playing")

# Complete the task
apis.supervisor.complete_task(status="success")
```

```
=== VERIFICATION ===
Removed 11 liked songs from queue
Remaining queue size: 12 (none are liked songs)
Player started: Song 'Whispers in the Wind' (song_id=290) is now playing
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
# 1. Re-read the exact task
print("=== ACTIVE TASK ===")
print(apis.supervisor.show_active_task())

# 2. Re-query current queue state
current_queue = apis.spotify.show_song_queue(access_token=access_token)
current_queue_ids = {s['song_id'] for s in current_queue}
print(f"\n=== CURRENT QUEUE ({len(current_queue)} songs) ===")
for s in current_queue:
    print(f"  song_id={s['song_id']}, title={s['title']}, is_current={s.get('is_current')}, is_playing={s.get('is_playing')}")

# 3. Check no liked songs remain in queue
still_liked_in_queue = current_queue_ids & liked_ids
print(f"\nLiked songs still in queue: {still_liked_in_queue}")

# 4. Check player is running
current_song = apis.spotify.show_current_song(access_token=access_token)
print(f"\n=== CURRENT SONG ===")
print(current_song)
```

```
=== ACTIVE TASK ===
{
 "instruction": "Remove all the songs that I have liked from my Spotify queue, and then start the player.",
 "status": "success",
 "answer": null
}

=== CURRENT QUEUE (12 songs) ===
  song_id=290, title=Whispers in the Wind, is_current=True, is_playing=True
  song_id=153, title=Love's Aftermath, is_current=False, is_playing=False
  song_id=158, title=Siren's Call, is_current=False, is_playing=False
  song_id=139, title=Momentary Bliss, is_current=False, is_playing=False
  song_id=178, title=Sorrow's Silent Symphony, is_current=False, is_playing=False
  song_id=180, title=The Intricacies of a Broken Heart, is_current=False, is_playing=False
  song_id=121, title=Astral Serenity, is_current=False, is_playing=False
  song_id=76, title=Whispers of the Heart, is_current=False, is_playing=False
  song_id=111, title=Lonesome Road, is_current=False, is_playing=False
  song_id=157, title=Chasing the Elusive Horizon, is_current=False, is_playing=False
  song_id=71, title=Eternal Fade, is_current=False, is_playing=False
  song_id=14, title=Memories Etched in Melancholy, is_current=False, is_playing=False

Liked songs still in queue: set()

=== CURRENT SONG ===
{
 "song_id": 290,
 "title": "Whispers in the Wind",
 "album_id": null,
 "duration": 253,
 "artists": [
  {
   "id": 31,
   "name": "Hazel Winter"
  }
 ],
 "played_seconds": 0,
 "is_playing": true,
 "is_looping": false
}
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
# All checks pass - confirm task completion
apis.supervisor.complete_task(status="success")
```

```
Execution successful.
```

