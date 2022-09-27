"""probably wouldnt need this if GH wasnt static sites"""

import yaml
from pprint import pprint

tr = "<tr>"
BR = lambda: "<br>"

a = lambda href, text: f"<a href={href}> {text} </a>"
p = lambda text: f"<p> {text} </p>"


def item(title=None, authors=None, venue=None, links=None, desc=None, name=None, project=None, arxiv=None, media=None):
    """builds an html research item"""

    tr = [f'<tr onmouseout="{media}_stop()" onmouseover="{media}_start()">', "</tr>"]
    left = demo(media)
    right = textbox(venue=venue, authors=authors, title=title, project=project, arxiv=arxiv, desc=desc)

    return "\n".join([tr[0], left, right, tr[1]])


def textbox(*, venue, authors, title, project, arxiv, desc):
    """docstring"""

    td = '<td style="padding:20px;width:75%;vertical-align:middle">'

    title = f'<span class="title">{title}</span>'
    title = a(**{"href": "/", "text": title})

    authors = "\n".join([a(**i) for i in authors])
    venue = f"<em>{venue[0]}</em>, {venue[1]}"

    project = a(**{"href": "/", "text": "project page"})
    arxiv = a(**{"href": "/", "text": "arxiv"})

    desc = p(desc)

    return "\n".join([td, title, BR(), authors, BR(), venue, BR(), project, arxiv, desc, "</td>"])


# print(
    # textbox(
        # authors=[{"text": "Matt Hyatt", "href": "/"}],
        # venue=["ACM", 2022],
        # title="PRIME",
        # project="none yet",
        # arxiv="coming soon",
        # desc="descriprion",
    # )
# )


def demo(media):
    """builds demo str"""

    a = '<td class="demo">'
    b = '<div class="one">'
    c = f'<div class="two" id="{media}">'
    d = f'<img src="img/{media}_after.jpg" ></div>'
    e = f'<img src="img/{media}_before.jpg" >'
    f = "</div>"
    g = script(media)
    h = f

    return "\n".join([a, b, c, d, e, f, g, h])


def script(elem):
    """toggles opacity of element"""

    a = '<script type="text/javascript">'
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

    with open('pub.yaml','r') as file:
        data = yaml.load(file)

    pprint(data[0])

    site = [item(**d) for d in data]
    
    with open('build.html','w') as file:
        file.write('\n'.join(site))


build()

"""
<tr onmouseout="malle_stop()" onmouseover="malle_start()">

    demo
        script
    demo
    
    textbox

</tr>
"""