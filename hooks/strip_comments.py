"""Drop HTML comments from pages before they render.

Each page starts with a comment listing the live configs it was written from. Those are
notes for staff editing the wiki; they stay in the Markdown but not in the published HTML.
"""
import re

COMMENT = re.compile(r"<!--.*?-->\s*", re.DOTALL)


def on_page_markdown(markdown, **kwargs):
    return COMMENT.sub("", markdown)
