'''
Each of the functions in this file takes a single line of input and transforms the line in some way.
'''

def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.

    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    if line[:2] == '# ':
    #why doesnt this line do anything?
    # answer: stringd are *immutable*; they never change
    # so functions that "seem like they should change the string"
    # actually return a new string with the changes, and leave the original string unchanged
        line = line.replace('# ', '<h1> ') + '</h1>'
    if line[:3] == '## ':
        line = line.replace('## ', '<h2> ') + '</h2>'
    if line[:4] == '### ':
        line = line.replace('### ', '<h3> ') + '</h3>'
    if line[:5] == '#### ':
        line = line.replace('#### ', '<h4> ') + '</h4>'
    if line[:6] == '##### ':
        line = line.replace('##### ', '<h5> ') + '</h5>'
    if line[:7] == '###### ':
        line = line.replace('###### ', '<h6> ') + '</h6>'
    return line


def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    start = 0
    while True:
        start = line.find("*", start)
        if start == -1:
            break
        end = line.find("*", start + 1)
        if end == -1:
            break
        line = line[:start] + "<i>" + line[start+1:end] + "</i>" + line[end+1:]
        start += 3  # Move past the newly inserted <i> tag
    return line


def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    
    start = 0
    while True:
        start = line.find("*", start)
        if start == -1:
            break
        end = line.find("*", start + 1)
        if end == -1:
            break
        line = line[:start] + "<i>" + line[start+1:end] + "</i>" + line[end+1:]
        start += 3  # Move past the newly inserted <i> tag
    return line


def compile_strikethrough(line):
    '''
    Convert "~~strikethrough~~" to "<ins>strikethrough</ins>".

    HINT:
    The strikethrough annotations are very similar to implement as the italic function.
    The difference is that there are two delimiting characters instead of one.
    This will require carefully thinking about the range of your for loop and all of your list indexing.

    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''
    start = 0
    while True:
        start = line.find("~~", start)
        if start == -1:
            break
        end = line.find("~~", start + 2)
        if end == -1:
            break
        line = line[:start] + "<ins>" + line[start+2:end] + "</ins>" + line[end+2:]
        start += 5  # Move past the newly inserted <ins> tag
    return line


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    start = 0
    while True:
        start = line.find("**", start)
        if start == -1:
            break
        end = line.find("**", start + 2)
        if end == -1:
            break
        line = line[:start] + "<b>" + line[start+2:end] + "</b>" + line[end+2:]
        start += 4  # Move past the newly inserted <b> tag
    return line


def compile_bold_underscore(line):
    '''
    Convert "__bold__" to "<b>bold</b>".

    HINT:
    This function is similar to the strikethrough function.

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    start = 0
    while True:
        start = line.find("__", start)
        if start == -1:
            break
        end = line.find("__", start + 2)
        if end == -1:
            break
        line = line[:start] + "<b>" + line[start+2:end] + "</b>" + line[end+2:]
        start += 4  # Move past the newly inserted <b> tag
    return line


def compile_code_inline(line):
    '''
    Add <code> tags.

    HINT:
    This function is like the italics functions because inline code uses only a single character as a delimiter.
    It is more complex, however, because inline code blocks can contain valid HTML inside of them,
    but we do not want that HTML to get rendered as HTML.
    Therefore, we must convert the `<` and `>` signs into `&lt;` and `&gt;` respectively.

    >>> compile_code_inline('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code_inline('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code_inline('`1+2`')
    '<code>1+2</code>'
    >>> compile_code_inline('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code_inline('this example has a math formula in the  code: `1 + 2 < 4`')
    'this example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('this example has a <b>math formula</b> in the  code: `1 + 2 < 4`')
    'this example has a <b>math formula</b> in the  code: <code>1 + 2 &lt; 4</code>'
    >>> compile_code_inline('```')
    '```'
    >>> compile_code_inline('```python3')
    '```python3'
    '''
    if "```" in line:
        return line

    start = 0
    while True:
        start = line.find("`", start)
        if start == -1:
            break

        end = line.find("`", start + 1)
        if end == -1:
            break

        content = line[start+1:end]
        content = content.replace("<", "&lt;")
        content = content.replace(">", "&gt;")

        replacement = f"<code>{content}</code>"

        line = line[:start] + replacement + line[end+1:]

        # Move past the inserted replacement
        start += len(replacement)

    return line


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''
    start = 0
    while True:
        start = line.find("[", start)
        if start == -1:
            break

        end = line.find("]", start + 1)
        if end == -1:
            break

        # Require '(' immediately after ']'
        if end + 1 >= len(line) or line[end + 1] != "(":
            start = end + 1
            continue

        url_start = end + 1
        url_end = line.find(")", url_start + 1)
        if url_end == -1:
            break

        text = line[start+1:end]
        url = line[url_start+1:url_end]

        replacement = f'<a href="{url}">{text}</a>'
        line = line[:start] + replacement + line[url_end+1:]
        start += len(replacement)

    return line


def compile_images(line):
    '''
    Add <img> tags.

    HINT:
    Images are formatted in markdown almost exactly the same as links,
    except that images have a leading `!`.
    So your code here should be based off of the <a> tag code.

    >>> compile_images('[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)'
    >>> compile_images('![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '<img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    >>> compile_images('This is an image of Mike Izbicki: ![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    'This is an image of Mike Izbicki: <img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    '''
    start = 0
    while True:
        start = line.find("![", start)
        if start == -1:
            break
        end = line.find("]", start + 1)
        if end == -1:
            break
        url_start = line.find("(", end + 1)
        if url_start == -1:
            break
        url_end = line.find(")", url_start + 1)
        if url_end == -1:
            break
        # Extract the image alt text and URL
        alt_text = line[start+2:end]
        url = line[url_start+1:url_end]
        # Replace the markdown image with HTML img tag
        line = line[:start] + f'<img src="{url}" alt="{alt_text}" />' + line[url_end+1:]
    return line
