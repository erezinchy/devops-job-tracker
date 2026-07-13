import pandas as pd
import os
from datetime import datetime
import io
from config import (
    CSV_URL, LOCAL_FILE, TARGET_LOCATIONS, MUST_CONTAIN,
    EXCLUDE_LEVELS, EXCLUDE_KEYWORDS, EXCLUDE_COMPANIES, EXCLUDE_URL_KEYWORDS
)


def passes_exclusions(df):
    """Returns a boolean mask of rows that do NOT match any exclusion rule.
    Shared by both the remote filtering step and the local purge step,
    so the two stay in sync automatically."""
    level_ok = ~df['level'].str.contains('|'.join(EXCLUDE_LEVELS), case=False, na=False)
    title_ok = ~df['title'].str.contains('|'.join(EXCLUDE_KEYWORDS), case=False, na=False)
    company_ok = ~df['company'].str.contains('|'.join(EXCLUDE_COMPANIES), case=False, na=False)
    url_ok = ~df['url'].str.contains('|'.join(EXCLUDE_URL_KEYWORDS), case=False, na=False)
    return level_ok & title_ok & company_ok & url_ok


def update_job_tracker():
    try:
        # 1. Fetch and clean remote data
        df_remote = pd.read_csv(CSV_URL)

        for col in ['title', 'company', 'city', 'level', 'url']:
            if col in df_remote.columns:
                df_remote[col] = df_remote[col].astype(str).str.strip()

        # 2. Build filters for incoming data
        location_mask = df_remote['city'].isin(TARGET_LOCATIONS)
        title_include_mask = df_remote['title'].str.contains('|'.join(MUST_CONTAIN), case=False, na=False)

        final_mask = location_mask & title_include_mask & passes_exclusions(df_remote)

        new_matches = df_remote[final_mask].copy()
        new_matches['date_found'] = datetime.now().strftime("%Y-%m-%d %H:%M")

        purged_count = 0

        # 3. Load and PURGE existing local file
        if os.path.exists(LOCAL_FILE):
            with open(LOCAL_FILE, 'r', encoding='utf-8-sig', errors='replace') as f:
                content = f.read()
                if content.strip():
                    df_local = pd.read_csv(io.StringIO(content))
                else:
                    df_local = pd.DataFrame()

            if not df_local.empty:
                # Clean local strings to match properly
                for col in ['title', 'company', 'level', 'url']:
                    if col in df_local.columns:
                        df_local[col] = df_local[col].astype(str).str.strip()

                initial_local_count = len(df_local)

                # Apply the identical exclusion logic directly to your local file data
                df_local = df_local[passes_exclusions(df_local)]
                purged_count = initial_local_count - len(df_local)

                # Process new records
                existing_urls = df_local['url'].tolist()
                really_new_jobs = new_matches[~new_matches['url'].isin(existing_urls)]
                combined_df = pd.concat([df_local, really_new_jobs], ignore_index=True)
                added_count = len(really_new_jobs)
            else:
                combined_df = new_matches
                added_count = len(new_matches)
        else:
            combined_df = new_matches
            added_count = len(new_matches)

        # 4. Save
        combined_df.to_csv(LOCAL_FILE, index=False, encoding='utf-8-sig')

        print(f"--- Sync Report ---")
        if purged_count > 0:
            print(
                f"🔥 Retroactive Clean: Removed {purged_count} existing positions from your CSV matching updated exclusion lists.")
        print(f"Added: {added_count} new positions.")
        print(f"Total in CSV: {len(combined_df)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    update_job_tracker()
