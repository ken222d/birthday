# SPDX-FileCopyrightText: 2025 Kenta ishizeki<a.w.g.d0201@icloud.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime, timedelta


rclpy.init()


class BirthdayCountdown(Node):
    def __init__(self):
        super().__init__("countdown_talker")
        self.pub = self.create_publisher(String, "countdown_topic", 10)

        # 誕生日の設定: 年、月、日、時、分、秒
        self.birthday = datetime(
            month=1, 
            day=5, 
            year=datetime.now().year,
            hour=20,
            minute=30,
            second=0
        )
        self.create_timer(1.0, self.cb)

    def cb(self):
        now = datetime.now()
        current_year_birthday = self.birthday.replace(year=now.year)

        if current_year_birthday < now:
            next_birthday = self.birthday.replace(year=now.year + 1)
        else:
            next_birthday = current_year_birthday

        time_left = next_birthday - now
        seconds_left = int(time_left.total_seconds())

        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600) #時間を求める
        minutes, seconds = divmod(remainder, 60) #分と秒を求める

        if seconds_left > 0:
            message = f"誕生日まで残り: {days} 日, {hours} 時間, {minutes} 分, {seconds} 秒."
        else:
            message = "誕生日おめでとう!"

        msg = String()
        msg.data = message
        self.pub.publish(msg)


def main():
    node = BirthdayCountdown()
    rclpy.spin(node)

