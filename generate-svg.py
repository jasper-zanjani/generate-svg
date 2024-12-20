#!/usr/bin/env python3
import argparse
from jinja2 import Environment, FileSystemLoader
import tomllib
import json
from datetime import datetime

tokens = ['eth', 'uni', 'aave', 'eigen', 'op', 'arb', 'zk', 'pol']

def get_config():
    with open('conf.toml', 'rb') as f:
        return tomllib.load(f)

def generate_chart(data):
    environment = Environment(loader=FileSystemLoader('templates'))
    template = environment.get_template('chart.svg.j2')
    filename = 'output.svg'
    output = template.render(tokens=data)

    with open (filename, 'w') as f:
        f.write(output)

def get_data(datafile="data.json"):
    with open(datafile, 'r') as f:
        data = json.load(f)
    # Getting only ether data for now
    data = data['eth']
    first_price = data[0]['price']
    return [ (datetime.strptime(i['date'], '%Y-%m-%d'), i['price']/first_price) for i in data ]

def get_curve(data, ticker_class):
    
    # Magnification of changes
    zoom = 2

    # Height of SVG file
    height = 100

    # Find minimum price
    bottom = min(i[1] for i in data])


    # 100% is close to top of window
    return f"<g class=\"{ticker}\"><path d=\"\" /></g>"
    


if __name__ == '__main__':
    # Process command-line arguments (possibly not needed)
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-t', '--ticker', choices=tokens, action="append")
    # show_tickers = parser.parse_args().ticker

    # TODO: pass filename provided from command-line
    data = get_data()
    curve = get_curve(data, 'eth')

    # Pass a data object containing only data needed for template rendering
    config = get_config()
    # data = [ config[i] for i in config if i in show_tickers ]

    generate_chart(chart_data)
    # pass

