from jinja2 import Template

lst = [{'price': 15}, {'price': 24}]

strr = "Mаксимальная стоимость: {{ l  | max(attribute='price') }}"
tm = Template(strr)
tm_render = tm.render(l=lst)

print(tm_render)