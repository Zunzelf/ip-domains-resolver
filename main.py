import yaml

from resolver import get_domains
from result_parser import resolve_ips, augment_results

# sebulan max 100 request -> request != jumlah domain
with open('config/config.yml') as f:
    cfg = yaml.safe_load(f.read())
API_KEY = cfg['API_KEY']
url = 'your-link.com'

domains = get_domains(url, API_KEY)
res = resolve_ips(domains)
lines = augment_results(res)

with open('final_result.txt', 'w') as f:
    for line in lines:
        f.write(line)