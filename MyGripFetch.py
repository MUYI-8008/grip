import os
from gym import utils
from gym.envs.robotics import arm_gripper_env

# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join('grip', 'arm_desktop_A1.xml')

class ArmGripEnv(arm_gripper_env.ArmGripperEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'object0:joint': [0.65, 0.1, 0.3, 1., 0., 0., 0.],
        }
        arm_gripper_env.ArmGripperEnv.__init__(
            self, MODEL_XML_PATH, has_object=False, block_gripper=True, n_substeps=20,
            gripper_extra_height=0.2,target_in_the_air=True,target_offset=0.0,
            obj_range=0.1,target_range=0.1, distance_threshold=0.05,
            initial_qpos=initial_qpos,reward_type=reward_type)
        utils.EzPickle.__init__(self)