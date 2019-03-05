from gym.envs.registration import register

register(
    id='flappybird-v0',
    entry_point='flappybird_env.envs:FlappyBirdEnv',
)
