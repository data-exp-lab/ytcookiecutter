from jinja2 import Environment, PackageLoader

metatemplater = Environment(loader=PackageLoader("dxlcookiecutter"),
                            variable_start_string="!{",
                            variable_end_string="}!",
                            block_start_string="<%",
                            block_end_string = "%>"
                           )
