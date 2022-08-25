TITLE CA1 Pyr model
: NMODL implementation of CA1 PYR model
: Implemented by: Shailesh Appukuttan (CNRS), August 2022
: 
: Original work: 
: Ferguson KA, Huh CY, Amilhon B, Williams S, Skinner FK (2014)
: Simple, biologically-constrained CA1 pyramidal cell models 
: using an intact, whole hippocampus context . 
: F1000Research 2015, 3:104 (https://doi.org/10.12688/f1000research.3894.2) 

NEURON {
    POINT_PROCESS Pyr
    RANGE v_init, vr, vt, c, vpeak, Cm, a, b, d, khigh, klow, Ishift, Iinj, Iext, stim_start, stim_stop, k
}

UNITS {
    (mV) = (millivolt)
    (pA) = (picoamp)
    (nS) = (nanosiemens)
}

INITIAL {
    vm = v_init
    um = 0
}

PARAMETER {
    : Default values correspond to strongly adapting model
    v_init = -65 (mV)
    vr = -61.8 (mV)
    vt = -57.0 (mV)
    c = -65.8 (mV)
    vpeak = 22.6 (mV)
    Cm = 115  (pF)
    a = 0.0012 (1/ms)
    b = 3 (nS)
    d = 10 (pA)
    khigh = 3.3  (nS/mV)
    klow = 0.1 (nS/mV)

    Ishift = 0 (pA)
    Iinj = 100 (pA)
    stim_start = 0.0 (ms)
    stim_stop = 1000.0 (ms)
}

ASSIGNED {
    k (nS/mV)
    Iext (nA)
}

STATE {
    vm (mV)
    um (pA)
}

BREAKPOINT {
    if (vm > vpeak) {
        vm = c
        um = um + d
    }

    if (vm<vt) {
        k = klow
    } else {
        k = khigh
    }

    if ((t >= stim_start) && (t <stim_stop)) {
        Iext = Iinj
    } else {
        Iext = 0
    }

    SOLVE states METHOD derivimplicit
}

DERIVATIVE states {
    um' = a*(b*(vm-vr)-um)
    vm' = (k*(vm-vr)*(vm-vt)+Ishift+Iext -um)/Cm
}