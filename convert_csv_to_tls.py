import pandas as pd
import sys

def convert_csv_to_tls(csv_filename, output_filename, port):
    # 使用pandas读取CSV文件
    df = pd.read_csv(csv_filename, encoding='utf-8')
    # 选取第一列的所有行
    ips = df.iloc[:, 0]
    # 为每个IP地址添加端口号
    ips_with_port = [f"{ip}:{port}" for ip in ips]
    # 将IP地址写入文件，每个IP地址一行
    with open(output_filename, 'w', encoding='utf-8') as f:
        for ip in ips_with_port:
            f.write(ip + '\n')

# 假设csv_filename为 'result.csv'
csv_filename = 'result.csv'
output_filename = 'notls.txt' if len(sys.argv) > 1 and sys.argv[1] == 'notls' else 'TLS.txt'
port = 80 if len(sys.argv) > 1 and sys.argv[1] == 'notls' else 443
convert_csv_to_tls(csv_filename, output_filename, port)