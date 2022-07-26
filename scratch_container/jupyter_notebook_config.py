c.NotebookApp.ip = '*'
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8080
c.NotebookApp.terminado_settings = {'shell_command': ['/bin/bash']}
c.NotebookApp.allow_origin_pat = (
'(^https://8080-dot-[0-9]+-dot-devshell\.appspot\.com$)|'
'(^https://colab\.research\.google\.com$)|'
'((https?://)?[0-9a-z]+-dot-(?:us|asia|europe|northamerica|southamerica)-?[0-9a-z]+\.notebooks\.googleusercontent.com)')
c.NotebookApp.allow_remote_access = True
c.NotebookApp.disable_check_xsrf = False
