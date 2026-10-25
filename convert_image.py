import base64
from pathlib import Path

image_path = Path("static/profile.jpg")
html_path = Path("templates/index.html")

if not image_path.exists():
    print("ERROR: static/profile.jpg file nahi mili!")
else:
    image_data = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    image_tag = (
        f'<img src="data:image/jpeg;base64,{image_data}" '
        'alt="Dewansh Pandey" class="profile-photo">'
    )

    html = html_path.read_text(encoding="utf-8")

    import re
    pattern = r'<img\b[^>]*class=["\'][^"\']*profile-photo[^"\']*["\'][^>]*>'

    updated_html, count = re.subn(
        pattern, lambda match: image_tag, html, count=1, flags=re.IGNORECASE
    )

    if count:
        html_path.write_text(updated_html, encoding="utf-8")
        print("Profile image HTML mein embed ho gayi!")
    else:
        print("index.html mein profile-photo class wala img tag nahi mila.")
        print("HTML ko manually update karna hoga.")