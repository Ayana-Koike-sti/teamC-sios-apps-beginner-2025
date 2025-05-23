# 商品情報の登録
items = [
    {'name': 'りんご', 'price': 100, 'stock': 10},
    {'name': 'バナナ', 'price': 80, 'stock': 20},
    {'name': 'みかん', 'price': 50, 'stock': 15},
    {'name': 'お肉', 'price': 500, 'stock': 5},
    {'name': '牛乳', 'price': 300, 'stock': 25},
    {'name': '魚', 'price': 400, 'stock': 30}
]

def process_payment(total):
    """
    お支払い処理を行う関数
    :param total: 合計金額
    """
    print(f"合計金額: {total}円")
    while True:
        try:
            payment = int(input("お支払い金額を入力してください: "))
            if payment < total:
                print("金額が不足しています。再度入力してください。")
            else:
                change = payment - total
                if change == 0:
                    print("お釣りなし")
                else:
                    print(f"お釣り: {change}円")
                    calculate_change(change)
                break
        except ValueError:
            print("無効な入力です。数字を入力してください。")

def calculate_change(change):
    """
    お釣りを最少の貨幣枚数で計算する関数
    :param change: お釣りの金額
    """
    denominations = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]  # 日本の貨幣単位
    result = {}
    for denom in denominations:
        count = change // denom
        if count > 0:
            result[denom] = count
            change %= denom

    print("お釣りの内訳:")
    for denom, count in result.items():
        print(f"{denom}円: {count}枚")

if __name__ == '__main__':
    print('お会計システム作成')

     # サンプル合計金額
    total_amount = 1500  # 仮の合計金額
    process_payment(total_amount)
