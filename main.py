"""Write the invented word and its definition to /output/entry.txt.

Gate: UTF-8 text, 1-140 characters, not only whitespace.
"""

import os

LINE = "Notifright (n.): the dread that the notification you just cleared was the one important message of your life."

if len(LINE) > 140 or not LINE.strip():
    raise SystemExit(f"line must be 1-140 characters, got {len(LINE)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"wrote /output/entry.txt: {len(LINE)} characters")
