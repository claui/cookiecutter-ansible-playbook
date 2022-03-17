# {{ cookiecutter.project_title }}

This repository contains a `{{ cookiecutter.first_playbook_name }}` playbook.


## Setting up {{ cookiecutter.project_title }}

Clone this repository.

Make sure you have the following packages installed:

- Ansible
- sshpass
- 1Password CLI (optional but recommended)
- op-vault-client (optional but recommended; not available on Windows)

To install those packages on macOS, run:

```
brew reinstall \
  1password-cli \
  ansible \
  claui/public/sshpass \
  claui/public/op-vault-client
```


## Using {{ cookiecutter.project_title }}

1. `cd` to the directory where this README is.

2. In 1Password, look up the password under the item name _{{ cookiecutter.ansible_vault_itemname_in_1password }}_.

3. Run one of the command lines in the _Command lines_ section. For every command line, append the options ` -i inventory --ask-vault-password` directly after the executable name `ansible` or `ansible-playbook`.


## Advanced: 1Password integration

If you add 1Password integration, you don’t have to enter the Ansible vault password manually all the time.

### Configuring 1Password CLI

One-time steps to configure 1Password CLI:

1. Make sure the 1Password CLI is installed and configured for the `{{ cookiecutter.onepassword_account_shortname }}` 1Password account.

2. Make sure you have the `op-vault-client` script installed.
If you can’t install the package, here’s a copy of the script:

    ```bash
    #!/bin/bash
    set -eu -o pipefail

    if [ "${SKIP_VAULT_PASSWORD:-0}" -ne '0' ]; then
      printf '\0'
      exit 0
    fi

    if [ "$(op --version | cut -d . -f 1)" -le '1' ]; then
      set -- op get item
    else
      set -- op item get
    fi

    exec "$@" --vault=iic4muvgtwosr67kogwh4q7t2a \
      owerpe2tcbemjou3wyauz3bd5y --fields password
    ```

3. Create a file `.ansible.cfg` in your home directory if it’s not already there.

4. In `.ansible.cfg`, add a line that says `[defaults]` if that line isn’t already present.

5. Add the following two lines to the `[defaults]` section:

    ```
    vault_encrypt_identity = {{ cookiecutter.ansible_vault_id }}
    vault_identity_list = {{ cookiecutter.ansible_vault_id }}@/path/to/op-vault-client
    ```

5. Replace the fragment `/path/to/op-vault-client` with the actual path to the `op-vault-client` tool.

For maximum convenience, consider setting up a default inventory directory. That way, you’ll be able to use all the examples in the _Command lines_ section without having to provide any additional options. For more details, see _Configuring a default inventory._

### Signing in to 1Password CLI

To set up a 1Password CLI session:

1. If you’re not signed in to 1Password CLI, run `eval $(op signin --account {{ cookiecutter.onepassword_account_shortname }})` on the command line.

2. Run one of the command lines in the _Command lines_ section. Make sure to insert the option `-i inventory` after the executable name `ansible` or `ansible-playbook`.

Notes:

- You no longer need to provide `--ask-vault-password` on the command line if you’re using the 1Password integration.


## Advanced: Configuring a default inventory

Configuring a default inventory means you no longer have to provide the `-i inventory` option at the command line.

One-time steps to configure a default inventory:

1. Create a file `.ansible.cfg` in your home directory if it’s not already there.

2. In `.ansible.cfg`, add a line that says `[defaults]` if that line isn’t already present.

3. Add the following line to the `[defaults]` section:
  `inventory = path/to/{{ cookiecutter.project_slug }}/inventory`

4. Replace the fragment `path/to/{{ cookiecutter.project_slug }}` with the actual path to the directory where this README file is. The path can be either absolute or relative to your home directory.

Note: If you set up both the 1Password integration and a default inventory, you’ll be able to run all the examples in the _Command lines_ section as-is.


## Advanced: Visual Studio Code integration

To use the VS Code tasks included in this repository, first configure 1Password CLI integration.

To set up a 1Password CLI session in Visual Studio Code:

1. Sign in to 1Password CLI using the special command line:
  `op signin --raw --account {{ cookiecutter.onepassword_account_shortname }}`
  This will print a token to your terminal.

2. Copy the token to your clipboard.

3. Open the `{{ cookiecutter.project_slug }}` directory in a new VS Code window.

4. In VS Code, invoke _Tasks: Run Task._

5. Select a task to run and press Enter.

6. If VS Code asks you for the `OP_SESSION_{{ cookiecutter.onepassword_account_shortname }}` token, paste the token from your clipboard.


## Command lines

### Check whether the hosts are online

```bash
ansible {{ cookiecutter.first_host_groupname }} -m ping
```

### Run the {{ cookiecutter.first_playbook_name }} playbook

```bash
ansible-playbook {{ cookiecutter.first_playbook_name }}.yml
```


## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
