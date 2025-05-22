# make.py

"""
Uses `json-schema-for-humans` to generate a set of HTML/Markdown files in 
`doc/html` and `doc/md` respectively.
"""

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

from pathlib import Path
import os
import sys


def main(template_name):
    config = GenerationConfiguration(
        description_is_markdown=True,
        show_breadcrumbs=False,
        link_to_reused_ref=False,
        template_name=template_name,
        footer_show_time=False,
    )

    if template_name in {"js", "js_offline", "flat"}:
        extension = "html"
    else:
        extension = "md"

    for dir_path, _, file_names in Path("schemas").walk():
        dest_dir_path = Path("doc", extension, *dir_path.parts[1:])
        os.makedirs(dest_dir_path, exist_ok=True)
        for file_name in file_names:
            file_path = Path(dir_path, file_name)
            generate_from_filename(file_path, dest_dir_path, config=config)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        template_name = sys.argv[1]
    else:
        template_name = "js"
    main(template_name=template_name)