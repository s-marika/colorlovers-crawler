# colorlovers-crawler

[COLOURLovers](https://www.colourlovers.com/)に掲載されているカラーパレット群をcsvに集約するためのクローラです．

> 現在，colourloversにseleniumからアクセスすると高頻度でアクセスブロックされます．1ページ分だけをクロールすることはできますが，2ページ目以降のアクセスブロックは回避できませんでした．  
ここでは開発時のコードを公開しています．

## install

### リポジトリをクローン

```bash
git clone git@github.com:s-marika/colorlovers-crawler.git
```

### Python3のインストール

Python3.7以上をインストールする([参考](https://www.python.jp/install/windows/install.html))

### 必要なライブラリのインストール

```bash
pip install requests beautifulsoup4 selenium
```

## usage

クロールするページ数を変数`page_num`に指定

以下を実行

```bash
python3 request_lovers.py
```

## output

2つのファイルが出力されます

* color palettes ... パレットに含まれる5色の組み合わせ
* palette evaluation ... パレットに対する人気度やViewなどの値

これらのファイルの値は行ごとに対応しています．

|   出力されるもの   | パスを指定する変数      | 変数のデフォルト値          |
| :----------------: | :---------------------- | :-------------------------- |
|   color palettes   | result_data_colors_path | ./result_color_palletes.csv |
| palette evaluation | result_data_eval_path   | ./result_color_eval.csv     |

## 開発環境

* Windows10 Home
* Python3.7
