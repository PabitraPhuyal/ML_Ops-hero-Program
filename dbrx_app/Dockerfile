from python:3.11

workdir /dbrx_app
copy /dbrx_app .

copy /Mlops_live_notebook .
run user -m runner

env port=8080
expose 8080

user runner

cmd['python', '-m','dbrx_app.main:main_app','--host', '0.0.0.0','--port','8080']