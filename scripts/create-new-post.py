#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os
import shlex
import subprocess
import re

from jinja2 import Environment, FileSystemLoader

# Define a list of predefined categories
PREDEFINED_CATEGORIES = [
    'Development',
    'Editors',
    'Networking',
    'Security',
    'Sysadmin',
]

def sanitize_title(title):
    # Replace spaces and underscores with dashes
    sanitized_title = re.sub(r'[ _]', '-', title)
    # Check for invalid characters
    if not re.match(r'^[a-zA-Z0-9-]+$', sanitized_title):
        print("Error: Title contains invalid characters. Only letters, numbers, spaces, and underscores are allowed.")
        exit(1)

def get_git_root():
    try:
        git_root_cmd = 'git rev-parse --show-toplevel'
        git_root_args = shlex.split(git_root_cmd)
        git_root = subprocess.check_output(git_root_args, encoding='utf-8').strip()
        return git_root
    except subprocess.CalledProcessError:
        print("Error: Not in a git repository.")
        exit(1)
    return sanitized_title



def render_template(git_root, title, date, tags, category, author, language, content):
    template_path = os.path.join(git_root, 'templates', 'posts')
    environment = Environment(loader=FileSystemLoader(template_path))
    template = environment.get_template("post_template.rst")
    content = template.render(
        title=title,
        date=date.strftime('%b %d, %Y'),
        tags=tags,
        category=category,
        author=author,
        language=language,
        content=content
    )
    return content


def select_category():
    print("Choose a category:")
    for i, category in enumerate(PREDEFINED_CATEGORIES):
        print(f"{i + 1}. {category}")
    choice = input("Enter the number corresponding to your choice: ")
    try:
        index = int(choice) - 1
        if index < 0 or index >= len(PREDEFINED_CATEGORIES):
            raise ValueError
        return PREDEFINED_CATEGORIES[index]
    except ValueError:
        print("Invalid choice. Please enter a valid number.")
        return select_category()

def main():
    git_root = get_git_root()
    tags = "new post, updateme"
    author = "Marcin Prączko"
    language = "eg"
    content = ".. Place your content here and replace this text."

    title = input("Enter title: ")
    category = select_category()
    date = datetime.datetime.now()

    ctx = render_template(
        git_root=git_root,
        title=title,
        date=date,
        tags=tags,
        category=category,
        author=author,
        language=language,
        content=content
    )

    # Debug: print the content of the rendered template
    print("-----BEGIN TEMPLATE CONTENT-----")
    print(ctx)
    print("-----END TEMPLATE CONTENT-----")

    sanitized_title = sanitize_title(title)
    post_filename = os.path.join(git_root, 'website', 'source', 'posts', f'{sanitized_title}.rst')

    print()
    print(f"Rendered template saved as: {post_filename}")
    if not os.path.exists(post_filename):
        with open(post_filename, mode="w", encoding="utf-8") as message:
            message.write(ctx)
    else:
        print(f"WARNING: File exist: {post_filename}")
        print(f"WARNING: Please rename the file or remove the existing file.")

if __name__ == "__main__":
    main()
