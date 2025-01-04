#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build  # ビルド
source $dir/.bashrc  # セットアップ

# ros2 run をバックグラウンドで実行
timeout 12 ros2 run birthday countdown &
#ROS2_PID=$!  # バックグラウンドプロセスのPIDを取得

# ノードが立ち上がるまで少し待機
sleep 3  # 1秒では不十分な場合があるので、3秒程度待つ

# トピックを10秒間監視してログに出力
timeout 10 ros2 topic echo /birthday_countdown > /tmp/birthday.log

# 結果をフィルタリング
grep 'Time until next birthday:' /tmp/birthday.log

# ノードをSIGINTで終了
#kill -SIGINT $ROS2_PID
#wait $ROS2_PID  # プロセスの終了を待つ

