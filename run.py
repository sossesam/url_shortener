#!/bin/env python3
from urlApp import create_app
import requests
app = create_app()
if __name__ == "__main__":
    app.run()
    