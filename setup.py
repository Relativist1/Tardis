import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == "__main__":
    setup(name="Tardis",

          version = "0.1",
          author = "Saurabh",
          author_email = "sbhkmr1999@gmail.com",
          description = "Triangular Distribution Plotting for MCMC Sampling Analysis",
          license = "GPLv3",
          keywords = "plotting MCMC",
          url = "https://github.com/Relativist1/Tardis",
          packages = ["tardis"],
          long_description=read('README.md'),
          install_requires=["matplotlib",
                            "numpy",
                            "seaborn",
                            "future"]
         )

