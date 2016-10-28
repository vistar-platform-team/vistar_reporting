# About

This script will pull a report based on the parameters defined in `options.json`

The results will get dumped as a csv in `results.csv`

### But Eric, why would I go through all the trouble when I have the dashboard?

I'm glad you asked.

The dashboard doesn't let you group by multiple date intervals (e.g. pull a report grouped by day of week AND by hour). This script lets you do anything your heart desires.

# Required Modules

In order to run this report, you will need to have the **requests** module installed on your computer. If you already have **pip** installed, skip to step 2.

### 1. Install pip

Run this in your terminal:
`$ sudo easy_install pip`

You will be prompted to enter a password. Use whatever password you use to unlock your computer
### 2. Install dependencies

Run this in your terminal from the project directory
`$ sudo pip install -r requirements.txt`

# Running the Report

Once you have the required modules, you can pull reports as much you damn well please. To run this script, clone this repo and then cd into the vistar-reporting directory.

### Configuring the Report Parameters

In order to customize the report, you edit the `options.json` file. Here, you can set parameters such as environment, account + password (e.g. intersection@vistarmedia.com), reporting filters, and more. Once you are happy with the options, save `options.json` and run the script from your terminal.

Run:

`$ python get_reporting.py options.json`

If there are no errors, you can open results.csv in excel to review the data.

**Note:** the resulting csv can be very large. If it contains more than 1 million rows, it will be truncated (rows get deleted) when you try to open it in excel. For very large pulls, you will want to pull the report multiple times (e.g. report per week).

# Date Conversion
If you are pulling "date" as a column, you will need to convert it from a unix timestamp to a human readable date.

You can do tha with this formula in excel:

=(((**CELL W DATE**/60)/60)/24)+DATE(1970,1,1)
