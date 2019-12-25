import socket


def resolve_ips(urls: list):
    res = []
    for url in urls:
        ip = socket.gethostbyname(url)
        dat = {
            'IP':   ip,
            'Domain': url
        }
        res.append(dat)
    return res

def augment_results(data: dict):
    res = []
    for dat in data:
        if len(dat['IP']) > 1:
            row = '%s\t%s\n'%(dat['IP'], dat['Domain'])
            res.append(row)
            res.append(row.upper())
            if 'www.' not in dat['Domain']:
                row_www = '%s\twww.%s\n'%(dat['IP'], dat['Domain'])
                res.append(row_www)
                res.append(row_www.upper())
            else:
                row_www = '%s\t%s\n'%(dat['IP'], dat['Domain'].replace('www.', ''))
                res.append(row_www)
                res.append(row_www.upper())
    return res

if __name__ == "__main__":
    import csv  
    with open('ip_result/ip-result-1.csv', 'r') as data:
        dats = csv.DictReader(data)
        print(augment_results(dats))
            