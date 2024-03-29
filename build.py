"""probably wouldnt need this if GH wasnt static sites"""

import yaml
from pprint import pprint

tr = "<tr>"
BR = lambda: "<br>"

nonone = lambda x: not x in ["None", None]
a = lambda href, text: f'<a href="{href}"> {text} </a>' if nonone(href) else text
p = lambda text: f"<p> {text} </p>" if nonone(text) else ""
em = lambda text: f"<em>{text}</em>"

def item(
    title=None,
    authors=None,
    venue=None,
    links=None,
    desc=None,
    name=None,
    project=None,
    arxiv=None,
    media=None,
):
    """
    builds an html research item
    """

    tr = [f'<tr onmouseout="{media}_stop()" onmouseover="{media}_start()">', "</tr>"]
    left = demo(media)
    right = textbox(
        venue=venue, authors=authors, title=title, project=project, arxiv=arxiv, desc=desc
    )

    return "\n".join([tr[0], left, right, tr[1]])


def textbox(*, venue, authors, title, project, arxiv, desc):
    """docstring"""

    td = '<td style="padding:20px;width:75%;vertical-align:middle">'

    title = f'<span class="title">{title}</span>'
    title = a(**{"href": None, "text": em(title)})

    for auth in authors:
        if 'Hyatt' in auth['text']:
            auth['text'] = em(auth['text'])

    authors = "\n".join([a(**i) for i in authors])

    venue = f"{em(venue[0])}, {venue[1]}"

    project = a(**{"href": project, "text": "project page"})
    arxiv = a(**{"href": arxiv, "text": "arxiv"})
    pages = '\n'.join([project,' // ', arxiv])

    desc = p(desc)

    return "\n".join([td, title, BR(), authors, BR(), venue, BR(), pages, desc, "</td>"])


def demo(media):
    """builds demo str"""

    a = '<td class="demo">'
    b = '<div class="one">'
    c = f'<div class="two" id="{media}_image">'
    d = f'<img src="img/{media}_after.jpg" >'
    e = "</div>"
    f = f'<img src="img/{media}_before.jpg" >'
    g = e
    h = script(media)
    i = "</td>"

    return "\n".join([a, b, c, d, e, f, g, h, i])


def script(elem):
    """toggles opacity of element"""

    a = '<script>'
    b = (
        f"function {elem}_start() "
        '{ document.getElementById("'
        f'{elem}_image").style.opacity = "1"; '
        "}"
    )
    c = (
        f"function {elem}_stop() "
        '{ document.getElementById("'
        f'{elem}_image").style.opacity = "0"; '
        "}"
    )
    d = f"{elem}_stop()"
    e = "</script>"

    return "\n".join([a, b, c, d, e])


# print(demo("yee"))


def build():
    """docstring"""

    with open("pub.yaml", "r") as file:
        data = yaml.safe_load(file)

    # pprint(data[0])

    site = [item(**d) for d in data]

    with open("build.html", "w") as file:
        file.write("\n".join(site))

    print("done")


build()
