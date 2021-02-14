import csv
import json
import re
import sys


DISCORD_URL = 'https://cdn.discordapp.com/emojis/%s.png'
DISCORD_EPOCH = 1420070400000


def snowflake_to_ts(snowflake):
    return ((int(snowflake) >> 22) + DISCORD_EPOCH) / 1000


def custom_emoji_transform(text):
    return re.sub(
        r'<\w?:(\w+):(\d+)>',
        lambda m: '<:' + m[1] + ':' + (DISCORD_URL % m[2]) + '>',
        text
    )


for fpath in sys.argv[1:]:
    writer = csv.writer(sys.stdout)
    with open(fpath, encoding='utf8') as f:
        for l in f:
            data = json.loads(l)
            if data['type'] != 'message':
                continue
            msg = data['data']
            text = custom_emoji_transform(msg['__clean_content'])
            ts = snowflake_to_ts(msg['id'])
            writer.writerow((ts, text))
            for react in msg.get('reactions', []):
                emoji = react['emoji']
                if emoji.get('id'):
                    emoji = '<:' + emoji['name'] + ':' + (DISCORD_URL % emoji['id']) + '>'
                else:
                    emoji = emoji['name']
                writer.writerow((ts, f'(reaction) {emoji}'))
