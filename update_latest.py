import json
import cloudscraper

PRIMARY = "https://www.mylotto.co.nz/api/results/v1/results/powerball/latest"

def fetch_latest():
    scraper = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "windows", "mobile": False}
    )
    r = scraper.get(PRIMARY, timeout=15)

    if r.status_code == 200 and r.headers.get("Content-Type", "").startswith("application/json"):
        return r.json()

    raise Exception("Blocked by Cloudflare or invalid response")

def main():
    try:
        data = fetch_latest()

        with open("latest.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Updated latest.json successfully")

    except Exception as e:
        print("Failed to update:", e)

if __name__ == "__main__":
    main()
