import time
import datetime

# Path of hosts file. Update based on your operating system.
hosts_path = r"C:\WINDOWS\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# List of sites to block. Update to your preferences.
block_list = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.reddit.com",
    "reddit.com",
    "www.twitter.com",
    "twitter.com",
    "www.amazon.com",
    "amazon.com",
    "www.instagram.com",
    "instagram.com",
    "www.netflix.com",
    "netflix.com"]

while True:

    now = datetime.datetime.now()

    # Time frame when sites are blocked. Update to your preferences.
    start_time = now.replace(
        hour = 9,
        minute = 0,
        second = 0,
        microsecond = 0)

    stop_time = now.replace(
        hour = 17,
        minute = 0,
        second = 0,
        microsecond = 0)

    # Work hours
    if ((start_time < now) and (now < stop_time)):

        with open(hosts_path, "r+") as file:
            content = file.read()

            # Add blocked sites to hosts file
            for website in block_list:
                if (website in content):
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    # Leisure hours
    else:

        with open(hosts_path, "r+") as file:
            content = file.readlines()

            file.seek(0)

            # Re-write hosts file without blocked sites
            for line in content:
                if (not any(website in line for website in block_list)):
                    file.write(line)

            file.truncate()

    # How often time is checked (seconds). Update to your preferences.
    time.sleep(10)