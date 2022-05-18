def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 0 or len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # 先頭の位置
    left = 0

    # 末端の位置
    right = len(array) - 1

    # 先頭/末端からの探索で交換する値が見つかった場合のフラグ
    left_flag = right_flag = 0

    while left < right:
        # 先頭からの探索
        if not left_flag:
            if array[left] >= pivot:
                left_flag = 1
            else:
                left += 1
        # 末端からの探索
        if not right_flag:
            if array[right] < pivot:
                right_flag = 1
            else:
                right -= 1
        # 交換する2つの値が見つかった場合
        if left_flag and right_flag:
            work = array[left]
            array[left] = array[right]
            array[right] = work
            left += 1
            right -= 1
            left_flag = 0
            right_flag = 0
    
    # 基準値以上のグループ、基準値未満のグループ再帰処理
    if array[left] <= pivot:
        return sort(array[0:left+1]) + sort(array[left+1:len(array)])
    else:
        return sort(array[0:left]) + sort(array[left:len(array)])

if __name__ == '__main__':
    main()