from flask import Flask, request, render_template, session, redirect
import json
import numpy as np
import pandas as pd
import redis

# Set up redis client.
r = redis.Redis(host="pandas-dashboard_redis_1", port="6379", password="demo")

app = Flask(__name__)


@app.route("/", methods=("POST", "GET"))
def html_table():

    json_data = r.get("dashboard_data")
    data = json.loads(json_data)
    df = pd.DataFrame(data)
    return render_template(
        "index.html", tables=[df.to_html(classes="data")], titles=df.columns.values
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
