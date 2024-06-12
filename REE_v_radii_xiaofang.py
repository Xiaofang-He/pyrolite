"""
REE Radii Plots
============================
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pyrolite.plot import pyroplot

from pyrolite.geochem.ind import REE
from pyrolite.geochem.norm import all_reference_compositions, get_reference_composition

# Ensure that Arial is available and set it as the default font for plots
plt.rcParams['font.family'] = 'Arial'

# sphinx_gallery_thumbnail_number = 3

########################################################################################
# Here we generate some example data, using the
# :func:`~pyrolite.util.synthetic.example_spider_data` function (based on EMORB,
# here normalised to Primitive Mantle);
#
file_path = 'D:\124.xlsx'
# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, engine='openpyxl')
# Print the DataFrame to see the content
print(df)


########################################################################################
chondrite = get_reference_composition("Chondrite_PON")
########################################################################################
# To use the compositions with a specific set of units, you can change them with
# :func:`~pyrolite.geochem.norm.Composition.set_units`:
#
CI = chondrite.set_units("ppm")

#########################################################################################
# The :func:`~pyrolite.geochem.pyrochem.normalize_to` method can be used to normalise DataFrames to a given reference (e.g. for spiderplots):
# for name, ref in list(all_reference_compositions().items())[::2]:

df_norm = df.set_index('Analysis').pyrochem.normalize_to(CI, units="ppm")
#df_norm = df.pyrochem.normalize_to(CI, units="ppm")
#for index, row in df_norm.iterrows():
ax = df_norm.pyroplot.REE(alpha=0.5, color="k", unity_line=True,label=df_norm.index)
ax.set_ylabel("X/X$_{C1-Chondrite}$")

# Iterate over each row and plot
#for index, row in df_norm.iterrows():
#    ax.plot(row.index, row.values, label=index, alpha=0.05, color="k")
#box = ax.get_position()
#ax.legend()
legend = ax.legend(title='Analysis', loc='center left', bbox_to_anchor=(0.9, 0.7),fontsize='small')
plt.show()


########################################################################################
# Where data is specified, the default plot is a line-based spiderplot:
ax = df_norm.pyroplot.REE(color="0.5", figsize=(8, 4))
#plt.legend(title='Sample')
ax.set_ylabel("X/X$_{C1-Chondrite}$")
plt.show()

########################################################################################
# This behaviour can be modified (see spiderplot docs) to provide e.g. filled ranges:
#
df_norm.pyroplot.REE(mode="fill", color="0.5", alpha=0.5, figsize=(8, 4))
plt.show()
########################################################################################
# The plotting axis can be specified to use exisiting axes:
#
fig, ax = plt.subplots(1, 2, sharey=True, figsize=(12, 4))

df_norm.pyroplot.REE(ax=ax[0])
# we can also change the index of the second axes
another_df = pd.read_excel(file_path, engine='openpyxl')(noise_level=0.2, size=20)  # some 'nosier' data
another_df.pd.read_excel(file_path, engine='openpyxl').pyroplot.REE(ax=ax[1], color="k", index="radii")

plt.tight_layout()
plt.show()
########################################################################################
# If you're just after a plotting template, you can use
# :func:`~pyrolite.plot.spider.REE_v_radii` to get a formatted axis which can be used
# for subsequent plotting:

from pyrolite.plot.spider import REE_v_radii

ax = REE_v_radii(index="radii")  # radii mode will put ionic radii on the x axis
plt.show()

########################################################################################
# .. seealso::
#
#   Examples:
#    `Ionic Radii <../geochem/ionic_radii.html>`__,
#    `Spider Diagrams <spider.html>`__,
#    `lambdas: Parameterising REE Profiles <../geochem/lambdas.html>`__
#
#   Functions:
#     :func:`~pyrolite.geochem.ind.get_ionic_radii`,
#     :func:`pyrolite.plot.pyroplot.REE`,
#     :func:`pyrolite.plot.pyroplot.spider`,
#     :func:`~pyrolite.geochem.pyrochem.lambda_lnREE`
