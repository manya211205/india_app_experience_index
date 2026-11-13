
"""
Google Play Review Scraper
Project: India App Experience Index

Collects recent English and Hindi reviews for apps
listed in data/apps.csv.

Output:
data/raw/google_play_reviews.csv
"""

import csv
import time
from pathlib import Path
from datetime import datetime, timedelta, timezone

from google_play_scraper import Sort, reviews


# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

# Find the main project folder automatically.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

APPS_FILE = PROJECT_ROOT / "data" / "apps.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "raw" / "google_play_reviews.csv"


# --------------------------------------------------
# 2. COLLECTION SETTINGS
# --------------------------------------------------

COUNTRY = "in"

# First version: English and Hindi reviews.
LANGUAGES = ["en", "hi"]

# Collect up to 500 reviews per language per app.
MAX_REVIEWS_PER_LANGUAGE = 500

# Only keep reviews from the last 365 days.
DAYS_TO_COLLECT = 365

# Fetch reviews in batches of 100.
BATCH_SIZE = 100

# Wait between requests to avoid sending requests too quickly.
REQUEST_DELAY_SECONDS = 1


# --------------------------------------------------
# 3. DATE FILTER
# --------------------------------------------------

CUTOFF_DATE = datetime.now(timezone.utc) - timedelta(
    days=DAYS_TO_COLLECT
)


def is_within_date_range(review_date):
    """Return True if a review is from the last 365 days."""

    if review_date is None:
        return False

    # Make sure the date has a timezone.
    if review_date.tzinfo is None:
        review_date = review_date.replace(tzinfo=timezone.utc)

    return review_date >= CUTOFF_DATE


# --------------------------------------------------
# 4. READ THE APP REGISTRY
# --------------------------------------------------

def load_apps():
    """Read the list of apps from data/apps.csv."""

    with open(APPS_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        apps = list(reader)

    # Only collect reviews for apps marked verified.
    verified_apps = [
        app for app in apps
        if app["package_status"].strip().lower() == "verified"
    ]

    print(f"Total apps in registry: {len(apps)}")
    print(f"Verified apps to process: {len(verified_apps)}")

    return verified_apps


# --------------------------------------------------
# 5. COLLECT REVIEWS FOR ONE APP AND LANGUAGE
# --------------------------------------------------

def collect_app_reviews(app, language):
    """Collect recent reviews for one app in one language."""

    package_name = app["package_name"]

    collected = []
    continuation_token = None
    stop_collection = False

    print(
        f"\nCollecting {language} reviews for {app['app_name']}..."
    )

    while len(collected) < MAX_REVIEWS_PER_LANGUAGE:

        try:
            result, continuation_token = reviews(
                package_name,
                lang=language,
                country=COUNTRY,
                sort=Sort.NEWEST,
                count=BATCH_SIZE,
                continuation_token=continuation_token
            )

        except Exception as error:
            print(
                f"Error for {app['app_name']} ({language}): {error}"
            )
            break

        # Stop if Google Play returns no more reviews.
        if not result:
            break

        for review in result:

            review_date = review.get("at")

            # Reviews are sorted newest first.
            # Once we reach older reviews, we can stop.
            if review_date is None:
                continue

            if review_date.tzinfo is None:
                review_date = review_date.replace(
                    tzinfo=timezone.utc
                )

            if not is_within_date_range(review_date):
                stop_collection = True
                break

            review_id = review.get("reviewId")

            if not review_id:
                continue

            collected.append({
                "app_id": app["app_id"],
                "app_name": app["app_name"],
                "category": app["category"],
                "package_name": package_name,
                "review_id": review_id,
                "review_text": review.get("content", ""),
                "rating": review.get("score"),
                "thumbs_up": review.get("thumbsUpCount", 0),
                "review_date": review_date.isoformat(),
                "language_collected": language
            })

            if len(collected) >= MAX_REVIEWS_PER_LANGUAGE:
                break

        print(
            f"  Reviews collected in {language}: {len(collected)}"
        )

        if stop_collection or continuation_token is None:
            break

        time.sleep(REQUEST_DELAY_SECONDS)

    return collected


# --------------------------------------------------
# 6. COLLECT REVIEWS FOR ALL VERIFIED APPS
# --------------------------------------------------

def main():

    apps = load_apps()

    all_reviews = []

    for index, app in enumerate(apps, start=1):

        print(
            f"\n========== APP {index}/{len(apps)}: "
            f"{app['app_name']} =========="
        )

        for language in LANGUAGES:

            app_reviews = collect_app_reviews(
                app,
                language
            )

            all_reviews.extend(app_reviews)

    # Remove duplicate reviews using app ID + review ID.
    unique_reviews = {}

    for review in all_reviews:
        key = (review["app_id"], review["review_id"])
        unique_reviews[key] = review

    final_reviews = list(unique_reviews.values())


    # --------------------------------------------------
    # 7. SAVE REVIEWS TO CSV
    # --------------------------------------------------

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "app_id",
        "app_name",
        "category",
        "package_name",
        "review_id",
        "review_text",
        "rating",
        "thumbs_up",
        "review_date",
        "language_collected"
    ]

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(final_reviews)


    # --------------------------------------------------
    # 8. PRINT COLLECTION SUMMARY
    # --------------------------------------------------

    print("\n========== COLLECTION COMPLETE ==========")

    print(f"Total unique reviews: {len(final_reviews)}")

    print(f"Output file: {OUTPUT_FILE}")

    print("\nReviews collected per app:")

    for app in apps:

        count = sum(
            1 for review in final_reviews
            if review["app_id"] == app["app_id"]
        )

        print(f"{app['app_name']}: {count}")


if __name__ == "__main__":
    main()
