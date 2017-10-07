#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gym
from gym import utils, spaces
import logging

logger = logging.getLogger(__name__)


class blokusEnv(gym.Env):

    def __init__(self):
        self.action_space = spaces.Discrete
        self.observation_space = []
        pass

    def _reset(self):
        obs = []

        return obs
        pass



    def _step(self, action):
        obs = []
        is_finished = False
        step_reward = []
        info = {}

        # eval action space


        #eval observation space


        return obs, step_reward, is_finished, info
        pass

    def _render(self, mode='human', close=False):
        pass

    def _close(self):
        pass

    def _seed(self):
        pass


    pass