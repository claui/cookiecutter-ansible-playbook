# cookiecutter-ansible-playbook

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for a simple Ansible playbook.


## Using cookiecutter-ansible-playbook

### Basic usage

To run the template generator, make sure you have a working
Cookiecutter installation. Then run:

```
cookiecutter gh:claui/cookiecutter-ansible-playbook
```

### Alternative usage

If you use `cookiecutter-ansible-playbook` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```
abbreviations:
    ansible: https://github.com/claui/cookiecutter-ansible-playbook.git
```

Then, to generate a project, run:

```
cookiecutter ansible
```


## License

Copyright (c) 2021 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are just there for the template user’s
convenience so they can choose a license for their own content.
Those licenses may not apply to this project. The only license
that applies to this project is the Apache License.
