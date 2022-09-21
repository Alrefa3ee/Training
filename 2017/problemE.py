import typing as t

stages = [100, 110, 250, 160, 130, 200]
min_stage = min(stages)

def check_stage(stage: int, stages: t.List[int], counter: int = 0):
    stages.sort()
    available_stages = [i for i in stages if i-stage <= 60]
    if not available_stages:
        return counter
    stage = max(available_stages)
    counter += 1
    [stages.remove(i) for i in available_stages]
    return check_stage(stage, stages, counter)

print(check_stage(min_stage, stages))
