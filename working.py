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
        url_start = line.find("(", end + 1)
        url_end = line.find(")", url_start + 1)
        if url_end == -1:
            break
        url = line[url_start+1:url_end]
        text = line[start+1:end]
        line = line[:start] + f'<a href="{url}">{text}</a>' + line[url_end+1:]
        start += len(f'<a href="{url}">{text}</a>')  # Move past the newly inserted <a> tag
    return line