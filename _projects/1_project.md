---
layout: page
title: AGN Feedback in the Cosmic Web
#description: Modeling AGN jets and baryon redistribution using the Three Hundred simulations
img: assets/img/agn_banner.jpg
importance: 1
category: research
#related_publications: true
---

This project explores the impact of active galactic nuclei (AGN) feedback on the structure and distribution of the Warm-Hot Intergalactic Medium (WHIM). AGN feedback—through black hole jets and winds—plays a key role in redistributing baryonic matter across the intergalactic medium. Using cosmological hydrodynamic simulations from the **Three Hundred Project**, we systematically vary the **AGN jet velocity** and **decoupling time** to investigate their effects on gas temperature profiles, baryon mass fractions, and thermal Sunyaev-Zel’dovich (tSZ) signals.

While some studies only explore binary feedback toggles, our approach tests a spectrum of physical feedback models to understand their role in shaping large-scale cosmic structure. We find that higher jet velocities suppress central gas temperatures but increase heating in the outskirts of halos. Our results also demonstrate how feedback changes the morphology of filaments and the thermal history of diffuse gas.

Below, you’ll find mock tSZ maps of three hydrodynamic simulations with varying jet velocities, and a GIF comparing the temperature over time.

---


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
    {% include figure.liquid path="assets/img/agn_feedback.gif" title="AGN Feedback Evolution" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  Simulated evolution of AGN feedback over cosmic time. GIF to be added.
</div>

This project outlines a framework for quantifying filament morphology changes due to feedback and sets up future comparisons with observations from X-ray and SZ surveys. Stay tuned for our forthcoming publication.


Banner image credit: V.Springel, Max-Planck Institut für Astrophysik, Garching bei München

