import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime, timedelta


rclpy.init()
class BirthdayCountdown(Node):
    def __init__(self):
        super().__init__("birthday_countdown")
        self.pub = self.create_publisher(String, "birthday_countdown", 10)

        # 誕生日の設定: 年、月、日、時、分、秒
        self.birthday = datetime(
            month=1, 
            day=2, 
            year=datetime.now().year,
            hour=23,
            minute=35,
            second=0
        )
        self.create_timer(1.0, self.cb)

    def cb(self):
        now = datetime.now()
        current_year_birthday = self.birthday.replace(year=now.year)

        if current_year_birthday < now:
            # If the birthday this year has passed, calculate for the next year
            next_birthday = self.birthday.replace(year=now.year + 1)
        else:
            next_birthday = current_year_birthday

        time_left = next_birthday - now
        seconds_left = int(time_left.total_seconds())

        # Format the message as a string
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if seconds_left > 0:
            message = f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds."
        else:
            message = "Happy Birthday!"

        # Publish the message
        msg = String()
        msg.data = message
        self.pub.publish(msg)

def main():
    node = BirthdayCountdown()
    rclpy.spin(node)

