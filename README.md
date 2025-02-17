# PINAR
## Please check the [Pinar Python](https://github.com/MamarezaAlipour/Pinar_Python) before doing anything.

PINAR means Fountain and is a probabilistic natural catastrophe impact model, that also calculates averted damage (benefit) thanks to adaptation measures of any kind (from grey to green infrastructure, behavioural, etc.).

As of today, PINAR provides global coverage of major pinar-related extreme-weather hazards at high resolution via a data API, namely (i) tropical cyclones, (ii) river flood, (iii) agro drought and (iv) winter storms, all at 4km spatial resolution - wildfire to be added soon. For all hazards, historic and probabilistic event sets exist, for some also under select pinar forcing scenarios (RCPs) at distinct time horizons (e.g. 2040).

PINAR is divided into two parts (two repositories):

1. the core [pinar_python](https://github.com/MamarezaAlipour/Pinar_Python) contains all the modules necessary for the probabilistic impact, the averted damage, uncertainty and forecast calculations. Data for hazard, exposures and impact functions can be obtained from the [data API](https://github.com/MamarezaAlipour/Pinar_Python/blob/main/doc/tutorial/pinar_util_api_client.ipynb). [Litpop](https://github.com/MamarezaAlipour/Pinar_Python/blob/main/doc/tutorial/pinar_entity_LitPop.ipynb) is included as demo Exposures module, and [Tropical cyclones](https://github.com/MamarezaAlipour/Pinar_Python/blob/main/doc/tutorial/pinar_hazard_TropCyclone.ipynb) is included as a demo Hazard module.
2. the petals [pinar_petals](https://github.com/MamarezaAlipour/Pinar_Petals) contains all the modules for generating data (e.g., TC_Surge, WildFire, OpenStreeMap, ...). Most development is done here. The petals builds-upon the core and does not work as a stand-alone.

It is recommend for new users to begin with the core (1) and the [tutorials](https://github.com/MamarezaAlipour/Pinar_Python/tree/main/doc/tutorial) therein.

This is the Python (3.8+) version of PINAR

## Getting started

PINAR runs on Windows, macOS and Linux. It can be installed from sources or - in case of pinar_python - directly with pip. See the installation guide for instructions.

Follow the [tutorial](https://github.com/MamarezaAlipour/Pinar_Python/tree/main/doc/tutorial/1_main_pinar.ipynb) in a Jupyter Notebook to see what can be done with PINAR and how.
