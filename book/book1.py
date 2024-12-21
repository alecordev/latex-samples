import os
import jinja2


def load_template(template_name):
    cwd = os.getcwd()
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(cwd),
        block_start_string="\BLOCK{",
        block_end_string="}",
        variable_start_string="\VAR{",
        variable_end_string="}",
        comment_start_string="\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
    )
    template = env.get_template(template_name)
    return template


def render_template(template_name, context):
    template = load_template(template_name)
    return template.render(context)


def save(content, filename):
    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    template_name = "book1_template.tex"
    context = {
        "book_title": "The Art of Python",
        "author_name": "John Doe",
        "publisher_name": "Tech Publishers",
        "chapters": [
            {"title": "Introduction", "content": "Welcome to the world of Python."},
            {
                "title": "Advanced Topics",
                "content": "Explore advanced Python features.",
            },
        ],
    }

    output = render_template(template_name, context)
    print(output)
    save(output, "book1.tex")
