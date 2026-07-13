# DevOps Job Tracker

A lightweight Python script to fetch, filter, and track relevant job postings. This project helps you stay organized by cleaning up raw job data from public sources and maintaining a curated list of opportunities that match your specific criteria.

## Acknowledgments

Data aggregation is powered by [mluggy/techmap](https://github.com/mluggy/techmap). Thank you for maintaining the source list!

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**

   This project requires pandas to process the job data.

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your filters:**

   Open `config.py` and customize your preferences:

   - `TARGET_LOCATIONS`: Update the list of cities you are interested in.
   - `MUST_CONTAIN`: Keywords for job titles you are targeting.
   - `EXCLUDE_...`: Easily filter out levels, specific companies, or irrelevant keywords.

4. **Run the script:**

   ```bash
   python main.py
   ```

## Usage

The script will fetch the latest data, apply your filters, and save the results to the file defined in `config.py` (default: `my_devops_jobs.csv`).

It automatically handles existing files, keeping your list up-to-date with new jobs while removing any positions that no longer meet your updated criteria.

> **Note:** If you have `my_devops_jobs.csv` open in Excel (or another spreadsheet app), close it before rerunning the script. The file gets locked while open, and the script will fail to save its updates.

## License

Feel free to use and modify this script for your own job search.
