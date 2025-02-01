"""
script to automate updation of changelog as I add features.
"""

import subprocess
import datetime

CHANGELOG_FILE = "CHANGELOG.md"
CHECK_INTERVAL = "weekly"

INTERVALS = {
    "daily": "1 day ago",
    "weekly": "1 week ago",
    "monthly": "1 month ago",
}


def get_latest_commits(since=None):
    """
    Get the latest commits in the repository
    since the specified time.
    """
    since = since or INTERVALS.get(CHECK_INTERVAL, "1 week ago")

    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--pretty=format:%h %s",
                "--since={since}",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print("Error fetching commits: ", {e})
        return []


def format_commit_entries(commits):
    """
    Format the commit entries for the changelog.
    """
    return "\n".join([f"- {commit}" for commit in commits])


def update_changelog(commits):
    """
    Update the changelog.md file with the latest commits.
    Updates happen weekly, scheduled with task manager.
    """

    if not commits:
        print("No new commits to add to changelog.")
        return

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    formatted_commits = format_commit_entries(commits)

    try:
        with open(CHANGELOG_FILE, "a", encoding="utf-8") as changelog_file:
            changelog_file.write(f"\n## {current_date}\n")
            changelog_file.write(commits)
            changelog_file.write(formatted_commits + "\n")

            print(f"Changelog updated with {len(commits)} new commits.")
    except OSError as e:
        print(f"Error updating changelog: {e}")


if __name__ == "__main__":
    latest_commits = get_latest_commits()
    update_changelog(latest_commits)
