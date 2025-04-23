---
layout: page
title: AGN Feedback in the Cosmic Web
description: Modeling AGN jets and baryon redistribution using the Three Hundred simulations
img: assets/img/agn_banner.jpg
importance: 1
category: work
#related_publications: true
---

This project explores the impact of active galactic nuclei (AGN) feedback on the structure and distribution of the Warm-Hot Intergalactic Medium (WHIM). AGN feedback—through black hole jets and winds—plays a key role in redistributing baryonic matter across the intergalactic medium. Using cosmological hydrodynamic simulations from the **Three Hundred Project**, we systematically vary the **AGN jet velocity** and **decoupling time** to investigate their effects on gas temperature profiles, baryon mass fractions, and thermal Sunyaev-Zel’dovich (tSZ) signals.

While some studies only explore binary feedback toggles, our approach tests a spectrum of physical feedback models to understand their role in shaping large-scale cosmic structure. We find that higher jet velocities suppress central gas temperatures but increase heating in the outskirts of halos. Our results also demonstrate how feedback changes the morphology of filaments and the thermal history of diffuse gas.

Below, you’ll find selected figures from the analysis, including tSZ maps, temperature profiles, halo gas fraction comparisons, and a GIF comparing the temperature over time.

---

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/agn_jet_vs_profile.png" title="Gas Temperature Profiles" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  The plots above show the mean temperature profile for the 25 most massive halos at redshift 1. Centering at each
  halo, the mean temperature is averaged over spherical shells out to radius R200. The left plot shows the temperature profiles
  for three different jet velocity runs, whereas the right plot shows the profiles for varying decoupling times.
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/tsz_maps.png" title="Thermal SZ Signal Maps" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Above are mock tSZ maps at redshift 0 for three different simulations. Each has a radius of 12 Mpc. From left to
  right, the three plots show the Compton-y parameter projected onto the z-axis for three different runs where the maximum jet
  velocity is set to 0, 7,000, and 35,000 km/s. We see the central cluster is less affected by these changes, with more pronounced
  effects along the cosmic filaments.
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/mass_fraction.png" title="WHIM Mass Fraction Across Runs" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Separating hot gas (T > 10⁷K) and cold gas (T < 10⁷K), we can track their evolution as a function of redshift.
  The gas mass fraction is defined as M<sub>gas</sub>/M<sub>Tot</sub> inside a radius of R200. The plot above averages the gas mass
  fraction for the 25 most massive halos in each snapshot as a function of redshift. The three different lines correspond to varying
  maximum jet velocities.
</div>

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/agn_feedback.gif" title="AGN Feedback Evolution" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Simulated evolution of AGN feedback over cosmic time. GIF to be added.
</div>

This project outlines a framework for quantifying filament morphology changes due to feedback and sets up future comparisons with observations from X-ray and SZ surveys. Stay tuned for our forthcoming publication.


Banner image credit: V.Springel, Max-Planck Institut für Astrophysik, Garching bei München

