import re


def main():
    filename = "sample.md"
    with open(filename) as f:
        md_lines = iter(f.readlines())
    
    html_lines = ["<html>", "<head></head>", "<body>"]

    while True:
        try:
            line = next(md_lines)

            # bold
            line = re.sub(r"\*\*(.*?)\*\*", lambda x: f"<strong>{x.group(1)}</strong>", line)

            # italic
            line = re.sub(r"\*(.*?)\*", lambda x: f"<em>{x.group(1)}</em>", line)

            # link
            line = re.sub(
                r"\[(.*?)\]\((https?://[\w/:%#\$&\?\(\)~\.=\+\-]+)\)",
                lambda x: f'<a href="{x.group(2)}">{x.group(1)}</a>',
                line
            )

            # h1
            h1_match = re.search(r"^#\s+(.*?)$", line)
            if h1_match:
                t = h1_match.group(1)
                html_lines.append(f"<h1>{t}</h1>")
                continue

            # h2
            h2_match = re.search(r"^##\s+(.*?)$", line)
            if h2_match:
                t = h2_match.group(1)
                html_lines.append(f"<h2>{t}</h2>")
                continue

            # list
            list_pettern = r"^-\s+(.*?)$"
            list_match = re.search(list_pettern, line)
            if list_match:
                html_lines.append("<ul>")
                try:
                    while list_match is not None:
                        html_lines.append(f"<li>{list_match.group(1)}</li>")
                        list_match = re.search(list_pettern, next(md_lines))
                finally:
                    html_lines.append("</ul>")
                    continue

            html_lines.append(line)

        except StopIteration:
            break
    
    html_lines.extend(("</body>", "</html>"))
    html = "\n".join(html_lines)
    print(html)
    with open("sample.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
