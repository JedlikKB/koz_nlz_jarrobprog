"""ROS 2 távolságértékek értékelése biztonsági állapotként."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class SafetyMonitor(Node):
    """Távolság fogadása és STOP/SLOW/CLEAR állapot küldése."""

    def __init__(self):
        super().__init__('safety_monitor')
        self.subscription = self.create_subscription(
            Float32, '/robot/distance', self.on_distance, 10
        )
        self.publisher = self.create_publisher(
            String, '/robot/safety_status', 10
        )
        self.get_logger().info('Biztonsági monitor elindult.')

    def on_distance(self, message):
        distance = message.data
        if distance < 0:
            self.get_logger().warning('Hibás, negatív távolságérték.')
            return
        if distance < 0.5:
            status = 'STOP - akadály túl közel'
        elif distance < 1.2:
            status = 'SLOW - akadály közel'
        else:
            status = 'CLEAR - szabad út'

        output = String()
        output.data = status
        self.publisher.publish(output)
        self.get_logger().info(f'{distance:.2f} m -> {status}')


def main(args=None):
    rclpy.init(args=args)
    node = SafetyMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
