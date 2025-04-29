---
layout: page
title: Cosmology with Spectral Sirens
#description: Constraining the Hubble constant using gravitational-wave sources and galaxy clustering
img: assets/img/gw_banner.png
importance: 1
category: research
#related_publications: true
---

This project uses **spectral sirens**—a novel approach combining gravitational-wave standard sirens with galaxy redshift surveys—to constrain cosmological parameters, particularly the **Hubble constant (H₀)**. Unlike traditional methods, spectral sirens don’t require electromagnetic counterparts. Instead, it
exploits intrinsic features in the distribution of binary
black hole (BBH) mass function to extract cosmological
information

Assuming a binary black hole (BBH) mass distribution, we generate samples
of masses and luminosity distances, incorporating redshift-dependent evolution of the population. This allows us to extract cosmological information without relying on electromagnetic counterparts. Our method simultaneously fits for H0 and the evolution of the BBH mass distribution peaks as a function of redshift. We examine how factors such as peak evolution, measurement errors in mass and distance,
and the number of detected events influence the resulting H0 posterior. We demonstrate that, with a sufficiently large sample of detections and realistic observational uncertainties, this approach can achieve percent-level precision on H0. These results highlight the promise of spectral sirens as a complementary probe of cosmic expansion in upcoming gravitational-wave surveys.

Our goal is to recover H0 from features in the BBH
mass distribution. We begin by simulating a catalog
of gravitational wave events (luminosity distances and
redshifted masses) with detector-level noise. This sec-
tion outlines our assumptions, simulation strategy, and
fitting procedure.
We adopt the following assumptions:
1. Events are distributed uniformly in comoving vol-
ume.
2. The BBH source-frame mass distribution follows
a broken power law with two Gaussian peaks.
3. The Gaussian peaks evolve linearly with redshift.
4. The detector-frame mass error scales with the true
detector-frame mass.
5. The luminosity distance error scales with the log-
arithm of the luminosity distance.

These assumptions are made primarily for simplicity. The choice to model the evolution of the Gaussian peaks linearly with redshift reflects the simplest, nontrivial behavior. More complex forms could be incorporated in future work, but linear evolution offers a useful starting point for demonstrating feasibility. Similarly, our modeling of detector-frame mass and luminosity distance errors provides a straightforward and broadly realistic approximation. While real measurement errors may be more complex, these simplifications are unlikely to introduce significant systematic bias in the context of this
proof-of-concept. The assumption of uniformity in comoving volume is also not strictly accurate, as the BBH merger rate following the star formation rate leads to nonuniform distributions (L. Lehoucq et al. 2023). However, our fitting framework is sufficiently flexible and should remain valid under different merger rates.

<div class="row justify-content-center">
  <div class="col-md-6 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/spectralSiren_demo.png" title="Spectral Siren Illustration" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="caption">
  This illustration highlights the idea behind the spectral siren method. As a function of distance, we can track the
  evolution of the binary black hole mass distribution. The evolution of the position of these peaks is a direct tracer of <i>H</i><sub>0</sub>.
</div>


This project builds toward future applications with the Einstein Telescope and Cosmic Explorer. Spectral sirens are an exciting and tenable method for obtaining percent and sub-percent level measurements of H₀.

Banner image credit: Einstein Telescope
