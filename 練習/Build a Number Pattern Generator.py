import math

def number_pattern(n):
    #引数が整数でないかチェック
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    #引数が1未満（正の整数ではない）かチェック
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # 結果を格納するリスト
    result = []
    
    # forループを使用して1からnまでを処理
    for i in range(1, n + 1):
        result.append(str(i))
    
    # リストをスペースで区切った文字列にして返す
    return " ".join(result)

# 動作確認用のテストコード
if __name__ == "__main__":
    print(f"Test 1-5 (n=4): {number_pattern(4)}")          # 期待値: 1 2 3 4
    print(f"Test 1-5 (n=12): {number_pattern(12)}")         # 期待値: 1 2 3 4 5 6 7 8 9 10 11 12
    print(f"Test 6 (not int): {number_pattern('4')}")        # 期待値: Argument must be an integer value.
    print(f"Test 7 (less than 1): {number_pattern(0)}")      # 期待値: Argument must be an integer greater than 0.
