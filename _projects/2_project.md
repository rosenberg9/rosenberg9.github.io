---
layout: page
title: Cosmology with Spectral Sirens
#description: Constraining the Hubble constant using gravitational-wave sources and galaxy clustering
img: assets/img/gw_banner.png
importance: 1
category: research
#related_publications: true
---

This project uses **spectral sirens** to constrain cosmological parameters, particularly the **Hubble constant (H₀)**. Unlike traditional methods, spectral sirens don’t require electromagnetic counterparts. Instead, it exploits intrinsic features in the distribution of binary
black hole (BBH) mass function to extract cosmological
information

Assuming a binary black hole (BBH) mass distribution, we generate samples
of masses and luminosity distances, incorporating redshift-dependent evolution of the population. Our method simultaneously fits for H0 and the evolution of the BBH mass distribution peaks as a function of redshift. We examine how factors such as peak evolution, measurement errors in mass and distance,
and the number of detected events influence the resulting H0 posterior. We demonstrate that, with a sufficiently large sample of detections and realistic observational uncertainties, this approach can achieve percent-level precision on H0. These results highlight the promise of spectral sirens as a complementary probe of cosmic expansion in upcoming gravitational-wave surveys.

<div class="row justify-content-center">
  <div class="col-md-6 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/spectralSiren_demo.png" title="Spectral Siren Illustration" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  This illustration highlights the idea behind the spectral siren method. As a function of distance, we can track the evolution of the binary black hole mass distribution. The evolution of the position of these peaks is a direct tracer of <i>H</i><sub>0</sub>.
</div>

This project builds toward future applications with the Einstein Telescope and Cosmic Explorer. Spectral sirens are an exciting and tenable method for obtaining percent and sub-percent level measurements of H₀.

Banner image credit: Einstein Telescope
