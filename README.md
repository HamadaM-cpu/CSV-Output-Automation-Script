# CSV Output Automation Script

このスクリプトは、CSVファイルからデータを読み込み、各行の内容をもとに個別のCSVファイルを自動生成するツールです。

## **概要**
- 入力CSVファイル（氏名、日付、金額、備考など）を行ごとに分割し、各行を個別のCSVファイルとして出力します。
- 出力ファイルは `output` フォルダに `output_001.csv`, `output_002.csv` などの形式で保存されます。

## **動作環境**
- Python 3.x
- 必要なライブラリ:
  - pandas

## **インストール手順**

### 1. 必要なライブラリをインストール
プロジェクトを使用するためには、以下のライブラリが必要です。以下のコマンドでインストールできます。

```bash
pip install pandas
```

### 2. 設定ファイルの確認

config.jsonファイルを開き、パスが正しいことを確認してください。

```json
{
    "csv_path": "input_data.csv",
    "output_folder": "output"
}
```

・csv_path: 入力CSVファイルのパス
・output_folder: 出力先のフォルダパス(無ければ自動生成されます)

### 3. CSVファイルの準備
CSVファイル (input_data.csv) を以下の形式で準備してください（サンプルデータ）:

```CS
ID,氏名,日付,金額,備考
1,田中太郎,2025/6/1,15000,交通費（東京〜調布）
2,佐藤花子,2025/6/2,20000,出張費（名古屋）
```

### 使い方
1.設定を確認
config.json 内のパスが正しいか確認してください。

2.スクリプトを実行
以下のコマンドでスクリプトを実行します：

```bash
python generate_excel.py
```

3.出力結果
スクリプトが正常に実行されると、output フォルダ内に csv ファイルが生成されます。各ファイルは、output_001.csv、output_002.csv といった名前で保存されます。

### サンプルデータ
input_data.csv: 処理するデータが含まれるCSVファイル

### ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細は LICENSE ファイルをご覧ください。
