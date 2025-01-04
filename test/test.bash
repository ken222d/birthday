#!/bin/bash
# SPDX-FileCopyrightText: 2024 Kenta ishizeki<a.w.g.d0201@icloud.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build  # ビルド
source $dir/.bashrc  # セットアップ

# ros2 run をバックグラウンドで実行
timeout 14 ros2 run birthday countdown &

# ノードが立ち上がるまで少し待機
sleep 3

# トピックを10秒間監視してログに出力
timeout 11 ros2 topic echo /birthday_countdown > /tmp/birthday.log

# 結果をフィルタリング
grep '誕生日まで残り:' /tmp/birthday.log

# ノードをSIGINTで終了
#kill -SIGINT $ROS2_PID
#wait $ROS2_PID  # プロセスの終了を待つ

