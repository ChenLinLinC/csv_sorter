import csv
import random
import string


def generate_csv(filepath: str, num_rows: int = 300, max_value: int = 1000):
    """
    生成随机的 CSV 文件，包含 Name 和 Value 两列。

    :param filepath: 输出文件路径
    :param num_rows: 数据行数（不含表头）
    :param max_value: Value 的最大值（不含）
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