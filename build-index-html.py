import pathlib
import hashlib
import html
from urllib.parse import quote

TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="pypi:repository-version" content="1.0">
    <title>Links for sudachipy</title>
  </head>
</html>
<body>
  <h1>Links for sudachipy</h1>
  {links}
</body>
</html>
"""

DOWNLOAD_BASE_URL_TEMPLATE = "https://github.com/opencollector/SudachiPy/releases/download/{release}/{file}#sha256={digest}"
LINK_TEMPLATE = """<a href="{url}">{name}</a>"""

RELEASES = {
    "v0.6.0": "0.6.0",
}

print(
    TEMPLATE.format(
        links="\n  ".join(
            LINK_TEMPLATE.format(
                url=html.escape(
                    DOWNLOAD_BASE_URL_TEMPLATE.format(
                        release=quote(release),
                        file=quote(f.name),
                        digest=quote(hashlib.sha256(f.read_bytes()).hexdigest()),
                    ),
                ),
                name=html.escape(f.name),
            )
            for release, f in (
                ([k for k, v in RELEASES.items() if v in f.name][0], f)
                for f in sorted(pathlib.Path(__file__).parent.glob("*.whl"))
            )
        )
    )
)
