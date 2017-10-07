#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import tensorflow as tf
#
# import gym

import socket

# env = gym.make('CartPole-v0')
# env.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample()) # take a random action
#
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))


team_id = 1234
team_name = "2333"
server_ip = "127.0.0.1"
server_port = 5001

def process(recv_msg):

    pass


def __main__():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((server_ip, server_port))

    reg_msg = "{\"msg_name\":\"registration\",\"msg_data\":{\"team_id\":%d,\"team_name\":\"%s\"}}" % (team_id,team_name)

    # print(reg_msg)

    s.send(reg_msg)


    while(1):
        recv_msg = s.recv(1024)
        process(recv_msg)

        pass


    s.close()
    # print("game end")

    pass


__main__()


