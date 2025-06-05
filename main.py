import os
import pandas as pd
import json

# 設定ファイルの読み込み（config.json）
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 設定情報の取得
csv_path = config["csv_path"]
output_folder = config["output_folder"]

# 出力フォルダが存在しない場合は作成
os.makedirs(output_folder, exist_ok=True)

# CSVデータの読み込み
df = pd.read_csv(csv_path)

# 各行ごとに別々のCSVファイルを出力
for index, row in df.iterrows():
    # 出力用のデータフレームを作成（1行だけ）
    output_df = pd.DataFrame([row])

    # ファイル名の作成
    out_csv = os.path.join(output_folder, f"output_{index + 1:03d}.csv")

    # CSVファイルを保存（インデックスは不要なのでindex=False）
    output_df.to_csv(out_csv, index=False, encoding="utf-8-sig")

    print(f"Saved {out_csv}")

print("完了！CSVファイルが出力フォルダに保存されました。")
