def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    # 探索範囲の左端と右端
    left = 0
    right = len(sorted_array) - 1

    # 探索対象が存在しない場合のフラグ
    none_flag = 0

    while not none_flag:
        # 中間のインデックス
        middle = int((left + right) / 2)
        
        if left == middle:
            none_flag = 1
        if sorted_array[right] == target_number:
            return right
        elif sorted_array[middle] == target_number:
            return middle
        elif sorted_array[middle] < target_number:
            left = middle
        elif sorted_array[middle] > target_number:
            right = middle

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()