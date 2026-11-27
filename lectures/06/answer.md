# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query':3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url':'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'search_phrase':'Versioning Amazon S3 bucket overview','topics':['general']})
- 気づき・疑問：エージェント本体を変更しなくても、設定ファイルにMCPサーバーを追加することで、利用できるツールが増えることを確認できた。また「３レベル」と全角で入力したときは検索できなかったが、半角に代えたら検索できた。検索語の表記の違いが検索結果に影響することに気がついた。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 
- やったこと：app/mcp_server.pyの31行目に
server.tool()(tools.get_lecture_summary)を追加した。git statusで変更したファイルが１ファイルのみであることを確認した。
- 結果：ツール一覧にglossary_get_lecture_summaryが追加された。「第２回では何を学びますか？」と質問したところ、glossary_get_lecture_summary({'lecture':2})が呼び出され第２回の講義内容を取得できた。テストは21件中20件成功、1件失敗だった。追加したコードを無効にして該当テストを再実行したが、同じエラーが発生した。
- 気づき・疑問：
エージェント側の設定やコードを変更せず、サーバー側に１行追加するだけで、新しいツールを利用できることを確認。また、テストでエラーが発生した際には、変更前後を比較することで、今回の変更が原因かどうか切り分けられることを学んだ。