import csv
import random
import string
import argparse
import sys

def generate_csv(filepath: str, num_rows: int = 300, max_value: int = 1000):
    """
    生成随机的 CSV 文件，包含 Name 和 Value 两列。
    """
    header = ["Name", "Value"]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for _ in range(num_rows):
            name = ''.join(random.choices(string.ascii_uppercase, k=3))
            value = random.randint(0, max_value - 1)
            writer.writerow([name, value])
    print(f"已生成 {num_rows} 行数据到 {filepath}")

def main():
    parser = argparse.ArgumentParser(
        description="生成随机的 CSV 文件（Name, Value）"
    )
    parser.add_argument("filepath", help="输出 CSV 文件的路径")
    parser.add_argument("--num-rows", type=int, default=300,
                        help="数据行数（不含表头），默认 300")
    parser.add_argument("--max-value", type=int, default=1000,
                        help="Value 列的最大整数值（不含），默认 1000")
    args = parser.parse_args()
    generate_csv(args.filepath, args.num_rows, args.max_value)

if __name__ == "__main__":
    main()