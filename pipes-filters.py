from body import get_body
from doctype import get_doctype_tag
from html_tag import get_html
from head import get_head
from full_text import get_full_text_html
from studies_list import get_studies_list
from info_list import get_info_list

text_html = get_full_text_html(
    get_doctype_tag(),
    get_html(get_body(get_info_list(get_studies_list())), get_head())
)

f = open("index.html", "a")
f.write(text_html)
f.close()
