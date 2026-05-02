import pandas as pd


def sort_2d_array(arr):
    """
    对任意长度的二维数组，按第二列的值从小到大排序（pandas 实现）。

    参数:
        arr : list of list, 例如 [['ABC', 523], ['XYZ', 10], ...]
    返回:
        排序后的新数组（list of list）
    """
    if not arr:
        return []
    df = pd.DataFrame(arr, columns=['col1', 'col2'])
    df_sorted = df.sort_values(by='col2')
    return [[row[0], int(row[1])] for row in df_sorted.values]