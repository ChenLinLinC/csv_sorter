import csv
from .sort_2d import sort_2d_array


def sort_csv_file(input_path: str, output_path: str):
    """
    读取 CSV 文件，按 Value 列排序，并将结果写入新文件。
    保留原表头与格式。

    :param input_path:  输入 CSV 文件路径
    :param output_path: 输出 CSV 文件路径
    """
    # 读取
    data = []
    with open(input_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # ["Name", "Value"]
        for row in reader:
            data.append([row[0], int(row[1])])

    # 排序
    sorted_data = sort_2d_array(data)

    # 写入
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(sorted_data)

    print(f"排序完成！结果已保存至 {output_path}")


def main():
    """命令行入口（可用于 pyproject.toml 的 scripts）"""
    import sys
    if len(sys.argv) != 3:
        print("用法: csv_sorter <输入文件> <输出文件>")
        sys.exit(1)
    sort_csv_file(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()