{%- if cookiecutter.frontend_type|lower == "!{frontend_type_str}!" -%}
from yt.loaders import !{load_func}!

def load(filename: str):

    # write code to load data from filename into memory!
    <% for arg in argnames -%>
    !{arg}! = ????????
    <% endfor %>
    # set or delete optional kwargs
    <% for key, value in kwarg_dict.items() -%>
    !{key}! = !{value}!
    <% endfor %>
    # call the stream data loader
    ds = !{load_func}!(
        <% for arg in argnames -%>
        !{arg}!,
        <% endfor -%>
        <% for key in kwarg_dict.keys() -%>
        !{key}! = !{key}!,
        <% endfor %>
    )

    # return the in-memory ds
    return ds
<% if include_docstring -%>
# description of !{load_func}! for convenience:

"""
!{docstring}!
"""
<% endif %>
{%- endif -%}
