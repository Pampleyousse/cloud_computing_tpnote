#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from main_serverless import ServerlessStack
from main_server import ServerStack


#class MyStack(TerraformStack):
#    def __init__(self, scope: Construct, id: str):
#        super().__init__(scope, id)

#        ServerlessStack(self, "Serverless")

#        ServerStack(self, "Server")


app = App()

ServerlessStack(app, "Serverless")
ServerStack(app, "Server")
#MyStack(app, "ter")

app.synth()
