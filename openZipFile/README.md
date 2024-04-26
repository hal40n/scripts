# バックアップデータのコピーと解凍スクリプト
このスクリプトは、指定されたディレクトリからバックアップデータのZipファイルをコピーし、それらを解凍するためのものです。  
バックアップデータは、下4桁が西暦（ex. AAA20XX.zip）になっている必要があります。本スクリプトでは、2024年までのデータのみが処理されます。

## 使用方法
1. Python 3.6以降がインストールされていることを確認してください。
2. スクリプトを実行する前に`zip_file_path`および`copy_dir_path`変数を適切な値に設定してください。
3. スクリプトを実行します。

```bash
python openZip.py
```

スクリプトを実行すると、指定されたディレクトリからバックアップデータがコピーされ、コピー先のディレクトリに解凍されます。  

## 注意事項
- バックアップデータのファイル名は、~20XX.zipの形式に従う必要があります。
- コピー元のディレクトリには、バックアップデータのZipファイル以外のファイルが存在していても構いませんが、処理されません。
- スクリプト実行後、コピー先のディレクトリに解凍されたバックアップデータが保存されます。

## 参考ドキュメント
参考にしたドキュメント等です。
- zipfile --- ZIP アーカイブの処理
    - [https://docs.python.org/ja/3/library/zipfile.html]
- Python で Zip ファイルを抽出する方法と、zip格納時の階層を無視してすべて同じフォルダに解凍する方法
    - [https://note.nkmk.me/python-string-line-break/]
- 【Python】ちがう階層にある、すべてのzipファイルを解凍したい！
    - [https://zenn.dev/namiki_i/articles/c3aa64420e937f]
- pythonでzipファイルを解凍する
    - [https://qiita.com/Tasuku-Q/items/202696c661d337beb400]
- PythonでZIPファイルを圧縮・解凍するzipfile
    - [https://note.nkmk.me/python-zipfile/]




