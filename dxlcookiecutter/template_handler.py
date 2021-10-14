from jinja2 import Environment, PackageLoader

# use this jinja2 environment to load and fill templates from ./templates/
# Note: these are meta-templates. The start/end strings below are filled to create
# the templates that go into the actual cookiecutter. The metatemplates in
# ./templates/ can contain standard jinja start/end strings ("{{", etc.) that
# are untouched by the processing of the metatemplates and will end up in the
# final cookiecutter template.
metatemplater = Environment(loader=PackageLoader("dxlcookiecutter"),
                            variable_start_string="!{",
                            variable_end_string="}!",
                            block_start_string="<%",
                            block_end_string="%>")
