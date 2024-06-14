# to install the pip

pip install poetry

# to crate fastapi project run command

```
1: poetry new hello-fastapi --name todos

```
here hello-fastapi is project Name and
todos is folder name where we want to do development just like app folder in next js

# to add package
poetry add fastapi
poetry add sqlmodel

# write script in pyproject.toml file
[tool.poetry.scripts]
dev= "todos.main:start"

# to start the server
poetry run dev 
