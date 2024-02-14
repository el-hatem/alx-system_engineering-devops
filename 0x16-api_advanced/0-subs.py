import requests

def number_of_subscribers(subreddit):
    # Reddit API URL to get information about the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid potential issues
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the number of subscribers
            data = response.json()
            subscribers_count = data["data"]["subscribers"]
            return subscribers_count
        else:
            # If the subreddit is invalid or another issue occurred, return 0
            return 0
    except Exception as e:
        # Handle any exceptions that might occur during the request
        print(f"Error: {e}")
        return 0

# If this script is run directly, read the subreddit from command line arguments
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        print(subscribers_count)
