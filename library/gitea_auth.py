"""

## LDAP
```bash
gitea admin auth add-ldap
    --name
    --security-protocol LDAPS
    --host
    --port
    --bind-dn
    --bind-password
    --user-search-base <ie: “DC=company,DC=int”
    --user-filter
    --admin-filter
    --username-attribute
```
root@instance:/# su gitea -c "/usr/bin/gitea --config /etc/gitea/gitea.ini --work-path /var/lib/gitea admin auth add-ldap --help"
NAME:
   Gitea admin auth add-ldap - Add new LDAP (via Bind DN) authentication source

USAGE:
   Gitea admin auth add-ldap [command options] [arguments...]

OPTIONS:
   --name value                      Authentication name.
   --not-active                      Deactivate the authentication source.
   --active                          Activate the authentication source.
   --security-protocol value         Security protocol name.
   --skip-tls-verify                 Disable TLS verification.
   --host value                      The address where the LDAP server can be reached.
   --port value                      The port to use when connecting to the LDAP server. (default: 0)
   --user-search-base value          The LDAP base at which user accounts will be searched for.
   --user-filter value               An LDAP filter declaring how to find the user record that is attempting to authenticate.
   --admin-filter value              An LDAP filter specifying if a user should be given administrator privileges.
   --restricted-filter value         An LDAP filter specifying if a user should be given restricted status.
   --allow-deactivate-all            Allow empty search results to deactivate all users.
   --username-attribute value        The attribute of the user’s LDAP record containing the user name.
   --firstname-attribute value       The attribute of the user’s LDAP record containing the user’s first name.
   --surname-attribute value         The attribute of the user’s LDAP record containing the user’s surname.
   --email-attribute value           The attribute of the user’s LDAP record containing the user’s email address.
   --public-ssh-key-attribute value  The attribute of the user’s LDAP record containing the user’s public ssh key.
   --skip-local-2fa                  Set to true to skip local 2fa for users authenticated by this source
   --avatar-attribute value          The attribute of the user’s LDAP record containing the user’s avatar.
   --bind-dn value                   The DN to bind to the LDAP server with when searching for the user.
   --bind-password value             The password for the Bind DN, if any.
   --attributes-in-bind              Fetch attributes in bind DN context.
   --synchronize-users               Enable user synchronization.
   --disable-synchronize-users       Disable user synchronization.
   --page-size value                 Search page size. (default: 0)
   --custom-path value, -C value     Custom path file path (default: "/usr/bin/custom")
   --config value, -c value          Custom configuration file path (default: "/usr/bin/custom/conf/app.ini")
   --version, -v                     print the version
   --work-path value, -w value       Set the gitea working path (default: "/usr/bin")


DEFAULT CONFIGURATION:
     CustomPath:  /usr/bin/custom
     CustomConf:  /etc/gitea/gitea.ini
     AppPath:     /usr/bin/gitea
     AppWorkPath: /var/lib/gitea


"""
