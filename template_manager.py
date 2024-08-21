# template_manager.py

from jinja2 import FileSystemLoader, Environment


class TemplateManager:
    def __init__(self, template_path):
        self.template_path = template_path
        self.env = Environment(loader=FileSystemLoader(self.template_path))

    def render_template(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)
