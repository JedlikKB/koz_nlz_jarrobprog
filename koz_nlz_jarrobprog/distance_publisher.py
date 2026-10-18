"""Szimulált távolságadatok küldése ROS 2 topicra."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistancePublisher(Node):
    """Előre rögzített távolságok ismétlődő közzététele."""

    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher = self.create_publisher(Float32, '/robot/distance', 10)
        self.distances = [2.5, 1.6, 1.0, 0.6, 0.3, 0.9, 1.8]
        self.index = 0
        self.timer = self.create_timer(1.0, self.publish_distance)
        self.get_logger().info('Távolságszenzor szimuláció elindult.')

    def publish_distance(self):
        distance = self.distances[self.index]
        self.index = (self.index + 1) % len(self.distances)
        message = Float32()
        message.data = float(distance)
        self.publisher.publish(message)
        self.get_logger().info(f'Távolság: {distance:.2f} m')


def main(args=None):
    rclpy.init(args=args)
    node = DistancePublisher()
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
