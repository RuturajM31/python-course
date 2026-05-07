import requests
import pandas as pd
from tabulate import tabulate



def fetch_jobs():
    """
    Fetch jobs from Arbeitnow API
    """

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(url)

    data = response.json()

    jobs_raw = data["data"]

    print("Total jobs:", len(jobs_raw))

    jobs = []

    for job in jobs_raw:

        # -----------------------------------------
        # POSTED DATE (may vary in API response)
        # -----------------------------------------

        posted_date = (
            job.get("created_at") or
            job.get("createdAt") or
            job.get("published_at") or
            "Not Available"
        )

        # -----------------------------------------
        # JOB URL
        # -----------------------------------------

        job_url = job.get("url")

        # Some APIs return only slug → fallback
        if not job_url and job.get("slug"):
            job_url = "https://www.arbeitnow.com/jobs/" + job.get("slug")

        # -----------------------------------------
        # BUILD CLEAN RECORD
        # -----------------------------------------

        jobs.append({
            "Title": job.get("title"),
            "Company": job.get("company_name"),
            "Location": job.get("location"),
            "Remote": job.get("remote"),
            "Posted Date": posted_date,
            "Job URL": job_url
        })

    return jobs


def create_dataframe(jobs):

    df = pd.DataFrame(jobs)

    # Clean duplicates
    df.drop_duplicates(inplace=True)

    # Sort by date if possible (safe fallback)
    if "Posted Date" in df.columns:
        df = df.sort_values(by="Posted Date", ascending=False)

    df.reset_index(drop=True, inplace=True)

    return df


def main():

    jobs = fetch_jobs()

    df = create_dataframe(jobs)

    print("\n==============================")
    print("GERMANY JOBS DATAFRAME")
    print("==============================\n")

    # Show full table nicely
    
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()