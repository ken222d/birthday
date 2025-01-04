#!/bin/bash
# SPDX-FileCopyrightText: 2024 Kenta ishizeki<a.w.g.d0201@icloud.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 14 ros2 run birthday countdown &

sleep 3

timeout 11 ros2 topic echo /countdown_topic > /tmp/birthday.log

grep '誕生日まで残り:' /tmp/birthday.log

