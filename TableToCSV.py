import pandas as pd
import os

# Read the HTML table into a Pandas DataFrame

tablenames = {
    '0': 'ig_by_owner',
    '1': 'ot_by_origin_unique',
    '2': 'ot_by_origin',
    '3': 'join_aig',
    '4': 'ig_bidding_urls',
    '5': 'arapi_sources_reporting_origins"',
    '6': 'arapi_triggers_reporting_origins',
    '7': 'arapi_orphaned_reporting_origins',
    '8': 'browsing_topics',
    '9': 'browsing_topics_with_skipObservation',
    '10': 'shared_storage',
    '11': 'ig_by_owner_by_origin',
    '12': 'join_aig_single',
    '13': 'browsing_topics_single',
    '14': 'browsing_topics_skip_single',
    '15': 'shared_storage_single',
    '16': 'fencedframes',
    '17': 'iframes_with_topics',
    '18': 'topics_xhr_headers_groups',
    '19': 'topics_xhr_headers_single',
    '20': 'run_ad_auction',
    '21': 'run_ad_auction_single',
}

# Loop through all the table in the df
def save_tables(df, filename):
    for i in range(len(df)):
        print(filename, f"Table {i} - {tablenames[str(i)]}")
        df[i].to_csv(f"{filename}_{tablenames[str(i)]}.csv", index=False)

# Read the HTML table into a Pandas DataFrame

# Get the list of HTML files in the directory
html_files = [file for file in os.listdir('/Users/hgombos/Downloads/PersonalPSandbox/HTML') if file.endswith('.htm')]

# Loop through each HTML file and read it into a Pandas DataFrame
for file in html_files:
    df = pd.read_html(os.path.join('/Users/hgombos/Downloads/PersonalPSandbox/HTML', file))
    save_tables(df, file)

#df = pd.read_html("two.log.htm")
#save_tables(df)
