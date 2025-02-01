"""
script to automate updation of changelog as I add features.
"""

import subprocess
import datetime

CHANGELOG_FILE = "CHANGELOG.md"
CHECK_INTERVAL = "weekly"


def get_latest_commits(since="1 week ago"):
    """
    Get the latest commits in the repository since the specified time.
    """
    try:
        result = subprocess.run(
            ["git", "log", "--pretty=format:%h %s", f"--since={since}"],
            stdout=subprocess.PIPE,
        )
        return result.stdout.decode("utf-8")
    except Exception as e:
        print(f"Error: {e}")
        return None


def update_changelog(commits):
    """
    Update the changelog.md file with the latest commits.
    """
    if not commits:
        print("No new commits to add to changelog.")
        return

    changelog_path = "changelog.md"
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    with open(changelog_path, "a") as changelog_file:
        changelog_file.write(f"\n## {current_date}\n")
        changelog_file.write(commits)
        changelog_file.write("\n")

    print(f"Changelog updated with {len(commits.splitlines())} new commits.")


if __name__ == "__main__":
    # Get the latest commits from the past week
    latest_commits = get_latest_commits()

    # Update the changelog with the latest commits
    update_changelog(latest_commits)
