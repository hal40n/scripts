# VM上に保存されているバックアップデータを、別のVMにコピーして保存するためのスクリプト

# やりたいこと：圧縮された2023年までのバックアップデータをVM間で移動して保存したい
# 1. 圧縮したファイルをコピーして別のディレクトリに保存する
# 2. 圧縮したファイルを解凍する

import time
import os.path
import shutil
import zipfile

print('------------------------------------------------------------')
print()

# 計測開始
print('Job Start!')
print('Start Time:', time.strftime('%Y/%m/%d %H:%M:%S'))
start_time = time.time()

print()
print('------------------------------------------------------------')

# 事前準備
# 圧縮したいファイルとコピー先のパスを定義する
# 保存先ディレクトリに保存されているファイル名の一覧を取得する
# 取得したファイル名の一覧から「2024」とついたファイルとZipファイルではないものを取り除く＝保存対象

# 本番環境用
# zip_file_path = 'F:/Data/JNX/Storage/' # 生データ保存場所
# copy_dir_path = '' # コピー先のディレクトリパス
# テスト環境用
zip_file_path = '' # 生データ保存場所
copy_dir_path = '' # コピー先のディレクトリパス

# コピー対象(2024年までかつZipファイルではないもの)を指定する
exclude_dirs = []

for dir_name in os.listdir(zip_file_path):
    file_path = os.path.join(zip_file_path, dir_name)
    if os.path.isfile(file_path) and file_path.endswith('.zip'):
        year_str = dir_name[-8:-4]
        if year_str != '2024':
            exclude_dirs.append(dir_name)
    else:
        print(f"Ignoring non-zip file: {file_path}")

############################################################################################################
print()
print('------------------------------------------------------------')

print('Zip File Lists')
for dir in exclude_dirs:
    print(dir)

print('------------------------------------------------------------')
print()
############################################################################################################

print()
print('Copy Start!')
print()

# 1. 取得した一覧をコピーして別のディレクトリに保存する
for root, dirs, files in os.walk(zip_file_path):
    for file in files:
        source_path = os.path.join(root, file)
        relative_path = os.path.relpath(source_path, zip_file_path)
        destination_path = os.path.join(copy_dir_path, relative_path)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copyfile(source_path, destination_path)

print()
print('Copy is OK!')
print()

# 2. 圧縮したファイルを解凍する
print()
print('Unzip Start!')
print()

copy_dir_abs_path = os.path.abspath(copy_dir_path)
for dir in exclude_dirs:
    output_path = os.path.join(copy_dir_abs_path, dir.split('.zip')[0])
    dir_path = os.path.join(copy_dir_abs_path, dir)
    with zipfile.ZipFile(dir_path, 'r') as zf:
        zf.extractall(output_path)
        zf.close()

print()
print('Unzip is OK!')
print()

print('------------------------------------------------------------')
print()

# 計測終了
end_time = time.time()
execution_time = end_time - start_time
print("Script execution time: {:.2f} seconds".format(execution_time))
print('End Time:', time.strftime('%Y/%m/%d %H:%M:%S'))
print('Good job!')

print()
print('------------------------------------------------------------')