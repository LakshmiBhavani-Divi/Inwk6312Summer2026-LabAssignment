from jinja2 import Environment, FileSystemLoader

# ✅ This line was missing (VERY IMPORTANT)
ENV = Environment(loader=FileSystemLoader('.'))

# Load template
template = ENV.get_template("template-task3.j2")

# Create sample data
interface = {
    "description": "Server Port",
    "vlan": 10
}

# Render template
print(template.render(interface=interface))
