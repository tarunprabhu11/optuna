import optuna
from optuna.samplers import TPESampler


def test_hyperopt_parameters():
    # type: () -> None

    sampler = TPESampler(**TPESampler.hyperopt_parameters())
    study = optuna.create_study(sampler=sampler)
    study.optimize(lambda t: t.suggest_uniform('x', 10, 20), n_trials=50)
