開発中のファイルです。

# Lambda Function: S3 Backup
## 概要
このLambda関数は、指定した時間に実行され、S3バケット間でバックアップを移動します。  
移動元のS3バケットからファイルを取得し、日付ごとのフォルダに保存します。

## 使用方法
1. AWS Lambdaコンソールにログインします。
2. ファンクションの作成を選択し、新しいLambda関数を作成します。
3. lambda_function.pyのコードをLambda関数のコードエディタに貼り付けます。
4. ハンドラをlambda_function.lambda_handlerに設定します。
5. Lambda関数のトリガーを設定し、定期的なトリガーを選択します。バックアップを移動したい時間を指定してください。
6. 移動元のS3バケット名と移動先のS3バケット名を、Lambda関数の環境変数として設定します。
7. Lambda関数を保存してデプロイし、トリガーをテストします。

## Lambda関数の構成
### トリガー
Lambda関数は、定期的なトリガーによって実行されます。トリガーは、指定した時間に関数を自動的に呼び出します。

### 環境変数
SOURCE_BUCKET: 移動元のS3バケット名。  
TARGET_BUCKET: 移動先のS3バケット名。

### 注意事項
Lambda関数のIAMロールには、S3バケットへのアクセス権限が必要です。  
Lambda関数の実行権限には、移動元のS3バケットからオブジェクトを読み取り、移動先のS3バケットにオブジェクトを書き込む権限が必要です。  
Lambda関数がトリガーされる時間帯を慎重に選択してください。ピークタイムにバックアップを移動すると、S3バケットの容量やLambda関数のスロットルが発生する可能性があります。  
