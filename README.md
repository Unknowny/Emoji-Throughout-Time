# Emoji Throughout Time ![img](https://i.imgur.com/m3uZGO3.png)
Visualization from [this](https://www.reddit.com/r/dataisbeautiful/comments/8icg5x/personal_usage_of_emoji_animated_over_time_oc/) reddit /r/dataisbeautiful post.

![img](https://i.imgur.com/OHhPC1u.gif)

## Disclaimer
This software is not exactly if at all well tested, I hope you can overcome any issues you might encounter.

## Install
Clone or download this repository. Download Twemoji from https://github.com/twitter/twemoji/releases/tag/v2.5.1. Inside the archive find `72x72` subfolder and unpack it as an `emoji` folder into the repository root directory.

Install dependencies using `pip install -r requirements.txt` or manually.

## Run
Specify any required options inside `settings.py` and run `> python ./plot.py`.  
Dataset file is assumed to have the following CSV structure:
```csv
timestamp,text
timestamp,text
...
```
Timestamp is a standard UTC timestamp of when the text was posted / made. Script will search over all records for emoji and custom emoji. Custom emoji must appear in text in the following form:  
`<:emoji-name:optional-filesystem-path-or-url>`  
Custom emoji that don't have a path or url associated must be placed into `custom_emoji` directory as png images.

## Working with discord logs and custom emojis
You can use this https://github.com/hermit-crab/discord-export to export whatever needed. Afterwards you can run the `discord_convert.py` script to convert extracted data into digestible CSV `> python discord_convert.py database.jl > posts.csv`.
- Message reactions are also taken into account unless you disabled their extraction.
