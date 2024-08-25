from src.loaders.container import Container
from src.loaders import index
import importlib

loader = Container()

print('### Loading the Repos')
for adapter in index.adapters:
    loader.register(
        adapter["name"],
        adapter["path"]
    )   
print('### Loading the Services')
for service in index.services:
    loader.register(
        service["name"],
        service["path"]
    )

print("### Loading the Controllers")
for controller in index.controllers:
    loader.register(
        controller["name"],
        controller["path"]
    )


