# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16


class KvadratPub(Node):

    def __init__(self):
        super().__init__('kvadrat_pub')

        self.publisher_ = self.create_publisher(Int16, 'kvadrat_broja', 10)
        self.kvadrat = 0
        self.subscription = self.create_subscription(
            Int16,
            'broj',
            self.listener_callback,
            10)
        self.subscription


    def listener_callback(self, msg):
        msg1 = Int16()
        self.kvadrat = msg.data**2
        msg1.data = self.kvadrat
        self.publisher_.publish(msg1)
        
    
def main(args=None):
    rclpy.init(args=args)

    kvadrat_pub = KvadratPub()

    rclpy.spin(kvadrat_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    kvadrat_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()