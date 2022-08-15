# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/distributed.multiprocess.ipynb.

# %% auto 0
__all__ = ['MultiprocessBackend']

# %% ../nbs/distributed.multiprocess.ipynb 4
from typing import Any

from ..core import StatsForecast
from .core import ParallelBackend

# %% ../nbs/distributed.multiprocess.ipynb 5
class MultiprocessBackend(ParallelBackend):
    def __init__(self, n_jobs: int) -> None:
        self.n_jobs = n_jobs
        super().__init__()

    def forecast(self, df, models, freq, **kwargs: Any) -> Any:
        model = StatsForecast(df=df, models=models, freq=freq, n_jobs=self.n_jobs)
        return model.forecast(**kwargs)

    def cross_validation(self, df, models, freq, **kwargs: Any) -> Any:
        model = StatsForecast(df=df, models=models, freq=freq, n_jobs=self.n_jobs)
        return model.cross_validation(**kwargs)