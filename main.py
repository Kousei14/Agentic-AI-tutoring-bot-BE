from tutorbot.assets.problems.problems import (get_calculus_problem,
                                               get_lin_alg_problem,
                                               get_physics_problem,
                                               get_chemistry_problem, 
                                               get_finance_problems)

def run_test(prompt: str):

    from tutorbot.app.logic.generate_illustration import IllustrationGeneratorAgent
    from tutorbot.app import settings

    illustration_generator = IllustrationGeneratorAgent(
            model = settings.ILLUSTRATION_GENERATOR_MODEL
        )

    generated_illustration = illustration_generator.generate(
        prompt = prompt, 
        number_of_outputs = 1,
        aspect_ratio = "16:9"
    )

    print(generated_illustration)

def run(quality: str = "-pql",
        version: str = "v1.0",
        problem_prompt: str = ""):

    from manim.__main__ import main
    import os

    if version == "v2.0":
        scene_file = "generated_scene_v2"
    elif version == "v1.0":
        scene_file = "generated_scene"

    os.environ['PROBLEM_PROMPT'] = problem_prompt

    main([
            quality,
            "--flush_cache",
            f"tutorbot/app/logic/{scene_file}.py",
            "AnimationScene"
        ])

if __name__ == "__main__":

    calc_prompt = get_calculus_problem(index = 12)
    physics_prompt = get_physics_problem(index = -1)
    lin_alg_prompt = get_lin_alg_problem(index = 0)
    chem_prompt = get_chemistry_problem(index = 1)
    finance_prompt = get_finance_problems(index = 0)

    run(quality = "-pqh", version = "v2.0", problem_prompt = calc_prompt)
    # run_test(prompt = "a corgi in a space suit.")