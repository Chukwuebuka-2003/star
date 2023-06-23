import instaloader

def get_instagram_stats(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        # Access the profile information
        followers = profile.followers
        following = profile.followees
        posts = profile.mediacount

        # Do something with the statistics
        print("Followers:", followers)
        print("Following:", following)
        print("Posts:", posts)

    except instaloader.exceptions.ProfileNotExistsException:
        print("The specified username does not exist.")

def main():
    username = input("Enter Instagram username: ")
    get_instagram_stats(username)

if __name__ == "__main__":
    main()
