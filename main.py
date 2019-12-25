import yaml

from resolver import get_domains
from result_parser import resolve_ips, augment_results
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--config", "-c", help="Config file's path", default="config/config.yml")
parser.add_argument("--output", "-o", help="Output file's path", default="final_result.txt")
parser.add_argument("--url", '-u', help="Source url")

args = parser.parse_args()

# sebulan max 100 request -> request != jumlah domain
with open(args.config) as f:
    cfg = yaml.safe_load(f.read())
API_KEY = cfg['API_KEY']

if args.url:
    url = args.url

    domains = get_domains(url, API_KEY)
    res = resolve_ips(domains)
    lines = augment_results(res)

    with open('final_result.txt', 'w') as f:
        for line in lines:
            f.write(line)
else:
    print('please insert target url first!')