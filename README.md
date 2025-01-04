## 誕生日のカウントダウン


![test](https://github.com/ken222d/birthday/actions/workflows/test.yml/badge.svg)
![](https://img.shields.io/github/license/ken222d/birthday)


## リポジトリの説明
このリポジトリには, ROS 2を使用して誕生日までのカウントダウンを行うことができます.  
* ノード: countdown_talker
  * 予定までの残りの日数と時間(メッセージ)をパブリッシュするノードです. 
* トピック: countdown_topic 
  * countdown_publisherから送信されたメッセージを別のノードに送るパイプの役割をします.
* メッセージ: 
  * 誕生日まで残り: {days} 日, {hours} 時間, {minutes} 分, {seconds} 秒. 
  * 誕生日おめでとう!

## 使い方
ROS 2をインストールしていない方は, インストールをしてください. 

端末で以下のコマンドを実行します. 
```
$ ros2 run birthday countdown
```
実行後は何も表示しません. 
別の端末で以下のコマンドを実行します. 
```
$ ros2 topic echo /birthday_countdown
```
実行後, 誕生日までのカウントダウンが始まります. 
```
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 20 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 19 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 18 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 17 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 16 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 15 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 14 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 13 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 12 秒.'
---
data: '誕生日まで残り: 363 日, 5 時間, 18 分, 11 秒.'
```
誕生日の日になったら, 
```
data: 誕生日おめでとう!
---
```
と表示され, 再度カウントダウンが始まります. 
countdown.pyファイル内の18~26行目にある誕生日の設定の部分を友達や家族, 大切な人の誕生日に設定してください. 
また, 時間と分, 秒まで設定できるので予定の日時を入れて使うことも可能です. 

## 使用ソフトウェア
- Ubuntu
- ROS 2 (Humble)
- Python
  - テスト済みバージョン: 3.7 ~ 3.10

## テスト環境
- Ubuntu 22.04.5 LTS
- ROS 2 (Humble)

## 参考資料
- [Pythonで日付操作を完全マスター！！](https://qiita.com/papi_tokei/items/43b1d15a6694f576486c)
- [Pythonのdivmodで割り算の商と余りを同時に取得 - nkmk note](https://note.nkmk.me/python-divmod-quotient-remainder/)

## ライセンスと著作権
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます. 
- このパッケージのコードの一部は, 下記のスライド（CC-BY-SA 4.0 by ryuichi ueda）のものを, 本人の許可を得て自身の著作としたものです. 
 - https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024
- © 2024 Kenta Ishizeki
