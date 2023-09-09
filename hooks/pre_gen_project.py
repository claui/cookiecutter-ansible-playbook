# pylint: disable=docstring-first-line-empty
"""
{%
    set version_tuple_dict = {
        "Ansible 2.5 or higher": (2, 5),
        "Ansible 2.10 or higher": (2, 10),
    }
%}
{{
    cookiecutter.update({
        "ansible_version_tuple_min_required":
            version_tuple_dict[cookiecutter.ansible_version],
    })
}}
"""
