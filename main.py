import instaloader
import time

L = instaloader.Instaloader()
L.load_session_from_file("") #it will help you load saved sessions

#logging in
USERNAME = "" #enter your password
PASSWORD = "" #enter your username
L.login(USERNAME, PASSWORD)

# Set username of the target Instagram profile
profile_name = "" #username of the profile


# Load Profile
profile = instaloader.Profile.from_username(L.context, profile_name)

# Iterate through posts with delay
for post in profile.get_posts():
    if post.is_video and post.video_view_count and post.video_view_count >= 1_000_000:
        print(f"Downloading {post.shortcode} with {post.video_view_count} views...")
        L.download_post(post, target=profile.username)
        time.sleep(20)  # Wait 10 seconds between downloads - facebook will not allow too many requests
