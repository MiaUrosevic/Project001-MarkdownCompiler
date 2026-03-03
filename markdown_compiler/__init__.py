"""
This file contains functions that work on entire documents at a time
(and not line-by-line).
"""

import re

from markdown_compiler.util.line_functions import (
    compile_headers,
    compile_strikethrough,
    compile_bold_stars,
    compile_bold_underscore,
    compile_italic_star,
    compile_italic_underscore,
    compile_code_inline,
    compile_images,
    compile_links,
)


def compile_lines(text):
    r'''
    Apply all markdown transformations to the input text.

    NOTE:
    This function calls all of the functions you created above to convert the full markdown file into HTML.
    This function also handles multiline markdown like <p> tags and <pre> tags;
    because these are multiline commands, they cannot work with the line-by-line style of commands above.

    NOTE:
    The doctests are divided into two sets.
    The first set of doctests below show how this function adds <p> tags and calls the functions above.
    Once you implement the functions above correctly,
    then this first set of doctests will pass.

    NOTE:
    For your assignment, the most important thing to take away from these test cases is how multiline tests can be formatted.

    >>> compile_lines('This is a **bold** _italic_ `code` test.\nAnd *another line*!\n')
    '<p>\nThis is a <b>bold</b> <i>italic</i> <code>code</code> test.\nAnd <i>another line</i>!\n</p>'

    >>> compile_lines("""
    ... This is a **bold** _italic_ `code` test.
    ... And *another line*!
    ... """)
    '\n<p>\nThis is a <b>bold</b> <i>italic</i> <code>code</code> test.\nAnd <i>another line</i>!\n</p>'

    >>> print(compile_lines("""
    ... This is a **bold** _italic_ `code` test.
    ... And *another line*!
    ... """))
    <BLANKLINE>
    <p>
    This is a <b>bold</b> <i>italic</i> <code>code</code> test.
    And <i>another line</i>!
    </p>

    >>> print(compile_lines("""
    ... *paragraph1*
    ...
    ... **paragraph2**
    ...
    ... `paragraph3`
    ... """))
    <BLANKLINE>
    <p>
    <i>paragraph1</i>
    </p>
    <p>
    <b>paragraph2</b>
    </p>
    <p>
    <code>paragraph3</code>
    </p>

    NOTE:
    This second set of test cases tests multiline code blocks.

    >>> print(compile_lines("""
    ... ```
    ... x = 1*2 + 3*4
    ... ```
    ... """))
    <BLANKLINE>
    <pre>
    x = 1*2 + 3*4
    </pre>
    <BLANKLINE>

    >>> print(compile_lines("""
    ... Consider the following code block:
    ... ```
    ... x = 1*2 + 3*4
    ... ```
    ... """))
    <BLANKLINE>
    <p>
    Consider the following code block:
    <pre>
    x = 1*2 + 3*4
    </pre>
    </p>

    >>> print(compile_lines("""
    ... Consider the following code block:
    ... ```
    ... x = 1*2 + 3*4
    ... print('x=', x)
    ... ```
    ... And here's another code block:
    ... ```
    ... print(this_is_a_variable)
    ... ```
    ... """))
    <BLANKLINE>
    <p>
    Consider the following code block:
    <pre>
    x = 1*2 + 3*4
    print('x=', x)
    </pre>
    And here's another code block:
    <pre>
    print(this_is_a_variable)
    </pre>
    </p>

    >>> print(compile_lines("""
    ... ```
    ... for i in range(10):
    ...     print('i=',i)
    ... ```
    ... """))
    <BLANKLINE>
    <pre>
    for i in range(10):
        print('i=',i)
    </pre>
    <BLANKLINE>
    '''
    lines = text.split("\n")

    out = []
    in_paragraph = False
    in_code_block = False

    for raw in lines:
        stripped = raw.strip()

        if stripped == "```":
            if not in_code_block:
                in_code_block = True
                out.append("<pre>")
            else:
                in_code_block = False
                out.append("</pre>")
            continue

        if in_code_block:
            out.append(raw.rstrip("\n"))
            continue

        if stripped == "":
            if in_paragraph:
                out.append("</p>")
                in_paragraph = False
            else:
                out.append("")
            continue

        if stripped.startswith("#"):
            if in_paragraph:
                out.append("</p>")
                in_paragraph = False

            line = compile_headers(stripped)
            out.append(line)
            continue

        if not in_paragraph:
            in_paragraph = True
            out.append("<p>")

        line = stripped
        line = compile_headers(line)
        line = compile_strikethrough(line)
        line = compile_bold_stars(line)
        line = compile_bold_underscore(line)
        line = compile_italic_star(line)
        line = compile_italic_underscore(line)
        line = compile_code_inline(line)
        line = compile_images(line)
        line = compile_links(line)
        out.append(line)

    if in_code_block:
        out.append("</pre>")

    if in_paragraph:
        out.append("</p>")

    return "\n".join(out)


def markdown_to_html(markdown, add_css):
    '''
    Convert the input markdown into valid HTML,
    optionally adding CSS formatting.

    >>> assert(markdown_to_html('this *is* a _test_', False))
    >>> assert(markdown_to_html('this *is* a _test_', True))
    '''
    html = """
<html>
<head>
    <style>
    ins { text-decoration: line-through; }
    </style>
"""
    if add_css:
        html += """
<link rel="stylesheet" href="https://izbicki.me/css/code.css" />
<link rel="stylesheet" href="https://izbicki.me/css/default.css" />
"""
    html += """
</head>
<body>
"""
    html += compile_lines(markdown)
    html += """
</body>
</html>
"""
    return html


def minify(html):
    r'''
    Remove redundant whitespace (spaces and newlines) from the input HTML,
    and convert all whitespace characters into spaces.

    >>> minify('       ')
    ''
    >>> minify('   a    ')
    'a'
    >>> minify('   a    b        c    ')
    'a b c'
    >>> minify('a b c')
    'a b c'
    >>> minify('a\nb\nc')
    'a b c'
    >>> minify('a \nb\n c')
    'a b c'
    >>> minify('a\n\n\n\n\n\n\n\n\n\n\n\n\n\nb\n\n\n\n\n\n\n\n\n\n')
    'a b'
    '''
    return re.sub(r"\s+", " ", html).strip()


def convert_file(input_file, add_css):
    '''
    Convert the input markdown file into an HTML file.
    If the input filename is `README.md`,
    then the output filename will be `README.html`.
    '''
    if input_file[-3:] != ".md":
        raise ValueError("input_file does not end in .md")

    with open(input_file, "r") as f:
        markdown = f.read()

    html = markdown_to_html(markdown, add_css)
    html = minify(html)

    with open(input_file[:-2] + "html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
